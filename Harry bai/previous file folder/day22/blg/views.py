from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.




def indexblg(request):
    return render(request,'blg/indexblg.html')

    
