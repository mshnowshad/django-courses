from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
# from django.db.models import Q

# from math import ceil


# Create your views  here. of shop folder




def indexshop(request):
   
    products = Product.objects.all()
    # search_query = ""
    
    # if request.method == "POST": 
    #     # Check if the form was submitted and contains the 'search' button
    #     if "search" in request.POST:
    #         # Get the search query from the form
    #         search_query = request.POST.get("query")
    #         # Perform case-insensitive search for product name, price, and image fields
    #         products = Product.objects.filter(
    #             Q(product_name__icontains=search_query) |
    #             Q(price__icontains=search_query) |
    #             Q(image__icontains=search_query)
    #         )
    
    # Render the template with the products and search query
    return render(request,'shop/indexshop.html',{'products': products})


def category(request,foo):
    # Replace hypens with space
    # foo = foo.replace('-',' ')
    
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request,'shop/category.html',{'products': products,'category':category})
        
        
    except:
        messages.success(request,("that ctegory does't work"))
        return redirect('indexshop')
        
    
    
    # return render(request,'shop/category.html')



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

def prodlist(request):
    productslist = Product.objects.all()
    return render(request,'shop/prodlist.html',{'product' : productslist})

def prodviews(request,prdid):
    product = Product.objects.filter(id=prdid)
    return render(request,'shop/prodviews.html',{'product':product})
def cheackout(request):
    return render(request,'shop/chekoutsp.html')








