
from django.http import HttpResponse
from django.shortcuts import render


tamp = "<h1> ++++++++++++++This a Tamplates days++++++++++++++</h1>"

icon1 = """<h1>Congratulation! I Created one icon using Django</h1><a href='/'> Home </a>"""  #> this is a home 'botton'




def taplate(request):
    dics = {'name':'Nowshed','place':'Bangladesh'}
    return render(request,'index.html',dics)

    # return HttpResponse(tamp)

# def tamp1(request):
#     return HttpResponse(tamp)
def icon(request):
    return HttpResponse(icon1)









