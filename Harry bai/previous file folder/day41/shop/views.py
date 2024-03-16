from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# from math import ceil
# Create your views  here. of shop folder




def indexshop(request):
    # categories  = Category.objects.all()
    products = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))
    
    # allProds = []
    # catprods = Product.objects.values('category','id')
    # cats = {item['category'] for item in catprods}
    # for cat in cats:
    #     prod = Product.objects.filter(category=cat)
    #     n = len(prod)
    #     nSlides = n//4 + ceil((n/4) - (n//4))
        
    #     allProds.append([prod,range(1,nSlides),nSlides])
        
    # params = {'allProds': allProds}
   

    return render(request,'shop/indexshop.html',{'products': products})

def aboutus(request):
    return render(request,'shop/abtshp.html')


def contract(request):
    return render(request,'shop/contrtsp.html')

def tracker(request):
    return render(request,'shop/tractsp.html')

def search(request):
    return render(request,'shop/serchsp.html')
def products(request,myid):
    product = Product.objects.filter(id=myid)

    return render(request,'shop/products.html',{'product': product[0]})

def prodviews(request):
    productslist = Product.objects.all()
    return render(request,'shop/prodviewsp.html',{'products' : productslist})

def cart(request):
    return render(request,'shop/cartshop.html')

def checkout(request):
    return render(request,'shop/checkout.html')








