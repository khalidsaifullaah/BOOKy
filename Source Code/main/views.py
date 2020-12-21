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


class HomePage(generic.ListView):
    model = Book
    template_name = 'main/home.html'
    context_object_name = 'books'
    paginate_by = 6


# @login_required
# def uploadBook(request):

#     if request.method == 'POST':
#         #print('aaa', request.POST)
#         form = BookUploadForm(request.POST)
#         if form.is_valid():
#             book = form.save(commit=False)
#             book.uploader = request.user
#             book.save()
#             messages.success(request, 'Book uploaded successfully!')
#             return redirect('home')
#         else:
#             print('vugi', form)

#     form = BookUploadForm()
#     return render(request, 'main/upload_book.html', {'form': form})

class BookUploadView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'main/upload_book.html'
    fields = ['title', 'no_of_pages', 'price', 'authors', 'publications', 'synopsis', 'cover']
    
    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)


class BookDetailView(DetailView):
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