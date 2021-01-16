import django_filters
from .views import Book
from django.forms.widgets import TextInput

class BookFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(field_name='title', label='', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Title contains'}))
    authors = django_filters.CharFilter(field_name='authors', label='', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Authors contain'}))

    class Meta:
        model = Book
        fields = ['genre']