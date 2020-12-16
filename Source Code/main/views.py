from .models import Book
from django.views import generic
from .forms import BookUploadForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



class HomePage(generic.ListView):
    model = Book
    template_name = 'main/base.html'
    context_object_name = 'books'
    paginate_by = 2


@login_required
def uploadBook(request):

    if request.method == 'POST':
        #print('aaa', request.POST)
        form = BookUploadForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploader = request.user
            book.save()
            messages.success(request, 'Book uploaded successfully!')
            return redirect('home')
        else:
            print('vugi', form)

    form = BookUploadForm()
    return render(request, 'main/upload_book.html', {'form': form})