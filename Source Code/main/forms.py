from django import forms
from .models import Book

class BookUploadForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'cover', 'no_of_pages', 'price', 'authors', 'publications', 'synopsis', ]