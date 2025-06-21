from django import forms
from .models import Book
from author.models import Author

class BookForm(forms.ModelForm):
    author_name = forms.CharField(required=False, max_length=100)
    author_surname = forms.CharField(required=False, max_length=100)

    class Meta:
        model = Book
        fields = ['name', 'description', 'count']