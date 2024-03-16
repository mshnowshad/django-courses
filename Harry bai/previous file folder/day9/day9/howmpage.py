##>> craeting a homepage of ot textUtils Website




from django.http import HttpResponse
from django.shortcuts import render





def index(request):
    
    # indu = {'wellcome':'Welcome to the web ','page':'blog'}
    return render(request,'indess.html')
    # return HttpResponse(indu)
    
    
a = "hello , i am nowshed. i am beginner of django. i am complete of python basic to advance level"
    
def about(request):
    print(request.GET.get('text','default')) #> ei jaygar output pabo terminal pe. ja kisu shei website o input nibo
    return HttpResponse(a)

def menu(request):
    return HttpResponse('menu key')




































