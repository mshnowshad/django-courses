from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.





def indexblg(request):
    return render(request,'blg/indexbg.html')

def about(request):
    return render(request,'blg/aboutbg.html')

def cheakout(request):
    return render(request,'blg/chekoutbg.html')

def contract(request):
    return render(request,'blg/contrtbg.html')

def prodviews(request):
    return render(request,'blg/prodviewbg.html')

def search(request):
    return render(request,'blg/serchbg.html')

def tracker(request):
    return render(request,'blg/tractbg.html')
