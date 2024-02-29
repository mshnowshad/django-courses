from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.




def indexblg(request):
    return HttpResponse("welcome to blg")
