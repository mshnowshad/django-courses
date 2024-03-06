from django.shortcuts import render
from .models import*


def index(request):
    return render(request,'test/indexdemo.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'chackout.html')




def detail(request):
    return render(request,'shop-detail.html')




def products(request):
    return render(request,'products.html')




def testimonial(request):
    return render(request,'testimonial.html')

def error(request):
    return render(request,'404.html')



