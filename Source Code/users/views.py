from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (UserRegisterForm,
                    UserUpdateForm,
                    ProfileUpdateForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Book
from django.views import generic
from users.models import Profile
from django.contrib.auth.models import User




def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
                'form' : form,
                'title' : 'Register'
              }
    return render(request,'users/register.html',context)



@login_required
def profile(request):

    books = Book.objects.filter(uploader=request.user)

    # Rating calculation
    if request.user.profile.total_seller_ratings > 0:
        seller_rating = round(request.user.profile.seller_rating/request.user.profile.total_seller_ratings)
    else:
        seller_rating = 0
    if request.user.profile.total_buyer_ratings > 0:
        buyer_rating = round(request.user.profile.buyer_rating/request.user.profile.total_buyer_ratings)
    else:
        buyer_rating = 0
    
    context = {
                'books': books,
                'seller_rating': seller_rating,
                'buyer_rating': buyer_rating
              }
    return render(request,'users/profile.html',context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
                'u_form': u_form,
                'p_form': p_form,
              }
    return render(request,'users/edit_profile.html',context)
    

# class UserDetailView(LoginRequiredMixin, generic.DetailView):
#     model = Profile
#     template_name = 'users/user_detail_view.html'

#     def books(self):
#         print(self.object)
#         return Book.objects.filter(uploader=self.object.user)

#     def form_valid(self, form):
#         print("he",form)
#         return

@login_required
def UserDetailView(request, username):
    if request.method == 'POST':
        user = get_object_or_404(User, username=username)
        books = Book.objects.filter(uploader=user)

        form = request.POST
        
        if form['rating_class'] == "seller":
            if int(form['rating']) > 0:
                user.profile.seller_rating += int(form['rating'])
                user.profile.total_seller_ratings += 1
                user.save()
                return redirect(f'/user/{username}/')
        else:
            if int(form['rating']) > 0:
                user.profile.buyer_rating += int(form['rating'])
                user.profile.total_buyer_ratings += 1
                user.save()
                return redirect(f'/user/{username}/')
            
    else:
        user = get_object_or_404(User, username=username)
        books = Book.objects.filter(uploader=user)
    
    # Rating calculation
    if user.profile.total_seller_ratings > 0:
        seller_rating = round(user.profile.seller_rating/user.profile.total_seller_ratings)
    else:
        seller_rating = 0
    if user.profile.total_buyer_ratings > 0:
        buyer_rating = round(user.profile.buyer_rating/user.profile.total_buyer_ratings)
    else:
        buyer_rating = 0
    print(seller_rating, buyer_rating)
    context = {
                'books': books,
                'user': user,
                'seller_rating': seller_rating,
                'buyer_rating': buyer_rating
              }
    return render(request,'users/user_detail_view.html',context)