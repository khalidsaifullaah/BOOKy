import django_filters
from .views import Book
from django.forms.widgets import TextInput

class BookFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(field_name='title', label='', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Title contains'}))
    authors = django_filters.CharFilter(field_name='authors', label='', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Authors contain'}))
    #price_lower_than = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    #price_greater_than = django_filters.NumberFilter(field_name='price', lookup_expr='gt')

    class Meta:
        model = Book
        fields = ['genre']