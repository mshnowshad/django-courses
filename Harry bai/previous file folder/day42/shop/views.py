from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
# from math import ceil


# Create your views  here. of shop folder




def indexshop(request):
    products = Product.objects.all()
    return render(request,'shop/indexshop.html',{'products': products})


def about(request):
    return render(request,'shop/about.html')

def cart(request):
    return render(request,'shop/cart.html')
def contact(request):
    if request.method=="POST":
        
        # print(request)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        
        
    
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tractsp.html')

def search(request):
    return render(request,'shop/serchsp.html')

def prodviews(request):
    productslist = Product.objects.all()
    return render(request,'shop/prodviewsp.html',{'product' : productslist})

def products(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request,'shop/products.html',{'product':product[0]})
def cheackout(request):
    return render(request,'shop/chekoutsp.html')








