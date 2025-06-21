from django.shortcuts import render, redirect, get_object_or_404
from author.models import Author
from book.models import Book
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm

@login_required
def author_list_view(request):
    if request.user.role != 1:
        return render(request, '403.html')

    authors = Author.objects.all()
    return render(request, 'author/author_list.html', {'authors': authors})


@login_required
def add_author_view(request):
    if request.user.role != 1:
        return render(request, '403.html')

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()

    return render(request, 'author/add_author.html', {'form': form})


@login_required
def delete_author_view(request, author_id):
    if request.user.role != 1:
        return render(request, '403.html')

    author = get_object_or_404(Author, id=author_id)
    if not Book.objects.filter(authors=author).exists():
        author.delete()
    return redirect('author_list')