from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from authentication.models import CustomUser
from author.models import Author
from .forms import BookForm


def book_list_view(request):
    books = Book.objects.all()
    title_query = request.GET.get('title')
    author_query = request.GET.get('author')

    if title_query:
        books = books.filter(name__icontains=title_query)
    if author_query:
        books = books.filter(authors__name__icontains=author_query)

    return render(request, 'book/book_list.html', {
        'books': books,
        'title_query': title_query,
        'author_query': author_query,
    })


def book_detail_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/book_detail.html', {'book': book})


def books_by_user_view(request, user_id):
    if not request.user.is_authenticated or request.user.role != 1:
        return render(request, '403.html')

    user = get_object_or_404(CustomUser, id=user_id)
    books = Book.objects.filter(taken_by=user)
    return render(request, 'book/books_by_user.html', {
        'books': books,
        'user': user
    })


def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()

            author_name = form.cleaned_data.get('author_name')
            author_surname = form.cleaned_data.get('author_surname')

            if author_name and author_surname:
                author, _ = Author.objects.get_or_create(
                    name=author_name.strip(),
                    surname=author_surname.strip()
                )
                book.authors.add(author)

            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'book/add_book.html', {'form': form})
