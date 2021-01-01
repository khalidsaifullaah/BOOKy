import django_filters
from .views import Book

class BookFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    authors = django_filters.CharFilter(field_name='authors', lookup_expr='icontains')
    #price_lower_than = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    #price_greater_than = django_filters.NumberFilter(field_name='price', lookup_expr='gt')

    class Meta:
        model = Book
        fields = ['genre']