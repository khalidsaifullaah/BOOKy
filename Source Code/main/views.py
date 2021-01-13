from .models import Book
from django.views import generic
from .forms import BookUploadForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django_filters.views import FilterView
from .filters import BookFilter


class HomePage(FilterView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'main/home.html'
    filterset_class = BookFilter # ADD YOUR filterset class
    paginate_by = 6


class BookUploadView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'main/upload_book.html'
    fields = ['title', 'no_of_pages', 'price', 'authors', 'publications', 'genre', 'synopsis', 'cover']
    
    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'main/book_detail.html'


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    template_name = 'main/upload_book.html'
    fields = ['title', 'no_of_pages', 'price', 'authors', 'publications', 'synopsis', 'cover']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Book = self.get_object()
        if self.request.user == Book.uploader:
            return True
        return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'main/book_confirm_delete.html'
    success_url = '/'
    def test_func(self):
        Book = self.get_object()
        if self.request.user == Book.uploader:
            return True
        return False


#class SearchResultsView(ListView):
#    model = Book
#    template_name = 'main/search_results.html'
#
#    def get_queryset(self):
#        query = self.request.GET.get('query')
#        object_list = Book.objects.filter(title__icontains=query)
#        return object_list
#
#    def get_context_data(self, **kwargs):
#        # Call the base implementation first to get a context
#        context = super(SearchResultsView, self).get_context_data(**kwargs)
#        # Add in additional context
#        context['query'] = self.request.GET.get('query')
#        return context
