from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



def index(request):
    product = Product.objects.all()
    paginator = Paginator(product, 8)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    if request.htmx:
        return render(request, 'index.html',{'page_obj':page_obj})
    return render(request,'index.html',{'page_obj':page_obj})





def about(request):
    return render(request,'about.html')




# login and logout 


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('you have a logged in'))
            return redirect('index')
        else:
            messages.success(request,('Authentication failed'))
            return redirect('login')
    
    else:
        return render(request,'login.html')


def logout_user(request):
    logout(request)
    messages.success(request,('you have a logged out'))
    return redirect('index')





# def addprod(request):
#     product = Product.objects.all()
#     return render(request,'addprod.html',{'product':product})


def showprod(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'showprod.html',{'product':product})