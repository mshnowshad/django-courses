﻿


# from turtle import RawTurtle
from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


def home(request):
    category = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'home.html',{'products':products,'category':category})



def about(request):

    return render(request, 'about.html',{})



def product(request,pk):
    product = Product.objects.get(id=pk)

    return render(request, 'product.html',{'product':product})



def category(request,foo):
    
    foo = foo.replace('-',' ')
    
    #grab the category from the url
    try:
        
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products})
        
    except:
        messages.success(request,('there category does not'))
        return redirect('home')

    
    
        

    # return render(request, 'category.html',{})


# def about(request):

#     return render(request, 'about.html',{})

def login_user(request):
    
     #এটি প্রথমে রিকুয়েস্ট পদ্ধতি ("POST") চেক করে। যদি পদ্ধতি "POST" হয়, তাহলে এটি ফর্ম থেকে সাবমিট করা ডাটা অ্যাক্সেস করে।
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        #এটি ব্যবহারকারের দেওয়া ইউজারনেম এবং পাসওয়ার্ড সংরক্ষণ করে।
        user = authenticate(request, username=username, password=password)
        
        #authenticate ফাংশনটি ব্যবহার করে এটি দেওয়া ক্রেডেনশিয়াল (ইউজারনেম এবং পাসওয়ার্ড) যাচাই করে।
        if user is not None:
            
            # যদি ক্রেডেনশিয়াল সঠিক হয়, তাহলে এটি ব্যবহারকারকে লগইন করিয়ে দেয় (login) এবং একটি সফল মেসেজ প্রদর্শন করে। এরপর, এটি হোম পেজে ফিরিয়ে দেয়।
            login(request, user)
            messages.success(request, 'You have logged in successfully.')
            return redirect('home')  # Return an HttpResponse upon successful login
        

           #যদি ক্রেডেনশিয়াল ভুল হয়, তাহলে এটি একটি ত্রুটি মেসেজ প্রদর্শন করে এবং লগইন পেজে ফিরিয়ে দেয়
        else:
            messages.error(request, 'There was an error. Please try again.')
            return redirect('login')  # Redirect back to login page if authentication fails
    
        
     # যদি রিকুয়েস্ট পদ্ধতি "POST" না হয়, তাহলে এটি কেবল লগইন ফর্ম টেমপলেট (login.html) রেন্ডার করে।
    else:
        return render(request, 'login.html', {})
     
     
                
    


 # এই ফাংশনটি একটি লগইন করা ব্যবহারকারকে লগআউট করতে সাহায্য করে।
def logout_user(request):
    
    logout(request)# এটি logout ফাংশনটি কল করে ব্যবহারকারকে লগআউট করে।
    
    #এটি একটি সফল মেসেজ প্রদর্শন করে।
    messages.success(request,('You have been logged out..'))
    
    return redirect('home')#এটি হোম পেজে ফিরিয়ে দেয়।

 
#এই ফাংশনটি একটি নতুন ব্যবহারকারকে রেজিস্টার করতে সাহায্য করে।
def register_user(request):
    
    form = SignUpForm() #এটি প্রথমে একটি খালি SignUpForm (forms.py) অবজেক্ট তৈরি করে।
   
    # যদি রিকুয়েস্ট পদ্ধতি "POST" হয়, তাহলে এটি ফর্ম থেকে সাবমিট করা ডাটা নিয়ে একটি নতুন SignUpForm অবজেক্ট তৈরি করে|
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
        
        if form.is_valid():#এটি ফর্মের বৈধতা যাচাই করে (is_valid)
            
            form.save() # যদি ফর্ম বৈধ হয়, তাহলে এটি ফর্মের ডাটা সংরক্ষণ করে (save)।
            
            #এটি সংরক্ষিত ডাটা থেকে ইউজারনেম এবং পাসওয়ার্ড পুনঃপ্রাপ্ত করে।
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            
            #login user
            #এটি নতুন তৈরি করা ব্যবহারকারকে লগইন করে (authenticate এবং login)।
            user = authenticate(username=username,password=password)
            login(request,user)
            
            #এটি একটি সফল মেসেজ প্রদর্শন করে এবং হোম পেজে ফিরিয়ে দেয়।
            messages.success(request,('You have Registered success full.!'))
            return redirect('home')
        

        #যদি ফর্মের তথ্য বৈধ না হয়, তাহলে এটি একটি ত্রুটি মেসেজ প্রদর্শন করে এবং রেজিস্ট্রেশন পেজে ফিরিয়ে দেয়।
        else:
            messages.success(request,('Whoops! There was a problem of Registering, please try again!'))
            return redirect('register')
    
        
    #যদি রিকুয়েস্ট পদ্ধতি "POST" না হয়, তাহলে এটি রেজিস্ট্রেশন ফর্ম টেমপলেট (register.html) রেন্ডার করে এবং ফর্ম অবজেক্টকে টেমপলেটে পাঠায়।
    else:
        return render(request, 'register.html',{'form':form})
     
    
   
    


