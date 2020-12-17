from django import forms
from .models import Book

class BookUploadForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'no_of_pages', 'price', 'authors', 'publications', 'synopsis', 'cover']