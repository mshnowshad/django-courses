# print()

from django.http import HttpResponse




def index(request):
    return HttpResponse("<h1>Hello World</h1>")



re = "<h1>Remove Punc</h1>"

def removep(request):
    return HttpResponse(re)


capita= "<h1>Capitalize punc</h1>"

def capitalize(request):
    return HttpResponse(capita)



newline= "<h1>New line remove Punc</h1>"

def newlineremove(request):
    return HttpResponse(newline)


space = """<h1>Space Remover Punc</h1><a href='/'> back </a>"""

def spaceremover(request):
    return HttpResponse(space)


 















































