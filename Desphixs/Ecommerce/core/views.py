
from django.shortcuts import render, redirect
from .models import Product,Category,Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django import forms
from django.db.models import Q
import json
from userauth.cart import Cart
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator



def detail(request,pv):
    products = Product.objects.get(id=pv)
    
    return render(request,'detail.html',{'products':products})



def home(request):
    product = Product.objects.all()
    paginator = Paginator(product, 8)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    if request.htmx:
        return render(request, 'home.html',{'page_obj':page_obj})
    
    
    return render(request,'home.html',{'page_obj':page_obj})


def products(request):
    
    product = Product.objects.all()
    paginator = Paginator(product, 9)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    if request.htmx:
        return render(request, 'products.html',{'page_obj':page_obj})
    
    return render(request,'products.html',{'page_obj':page_obj})

def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'chackout.html')


def testimonial(request):
    return render(request,'testimonial.html')

def error(request):
    return render(request,'404.html')






# Assuming you have your models and forms defined elsewhere
# ... (models.py and forms.py)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            return redirect('home')
        else:
            messages.error(request, ("Invalid username or password. Please try again."))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out...Thanks for stopping by..."))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user object
            # Create a profile for the newly registered user
            profile = Profile.objects.create(user=user)  # Create the associated profile
            messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
            return redirect('update_info')  # Redirect to profile creation page
        else:
            messages.error(request, ("Whoops! There was a problem Registering, please try again..."))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})



def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, "User Has Been Updated!")
            return redirect('home')
        return render(request, "update_user.html", {'user_form': user_form})


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your Password Has Been Updated...")
                # Consider redirecting to a different page after password change
                return redirect('update_user')  # Redirect to a suitable page
            else:
                for error in form.errors.values():
                    messages.error(request, error)
                return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form': form})


def update_info(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Info Has Been Updated!")
            return redirect('home')  # Redirect to home page after saving
        else:
            return render(request, "update_info.html", {'form': form})

    # Clear the form data after GET requests (optional)
    if request.method == 'GET':
        form = UserInfoForm()
        return render(request, "update_info.html", {'form': form})





def index(request):
    return render(request,'test/indexdemo.html')

