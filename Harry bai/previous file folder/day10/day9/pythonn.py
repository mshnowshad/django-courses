##>>.......................  django site: coding the backend  <,<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

from django.http import HttpResponse
from django.shortcuts import render





def index(request):
    
    # indu = {'wellcome':'Welcome to the web ','page':'blog'}
    return render(request,'indess.html')
    # return HttpResponse(indu)
    
b = "hei, Remove punc 'on' please !"
# a = "hello , i am nowshed. i am beginner of django. i am complete of python basic to advance level"

def analyze(request):
    djtxt = request.GET.get('text','default')   
    removepunc = request.GET.get('removepunc','off')   #>> এই লাইনটি ওয়েবসাইট থেকে পাঠ্য ইনপুট সংগ্রহ করে। যদি ব্যবহারকারী কোনও পাঠ্য সরবরাহ না করে তবে এটি "default" মানটি ব্যবহার করবে।
    
    
    # print(removepunc) #> ei jaygar output pabo terminal pe. ja kisu shei website o input nibo
    # print(djtxt)
    
    
    if removepunc == "on":
        punctuations = '''.,?!:;'"()[]{}-_./-&$#@^*%'''
        analyzevari = " "
        
        for char in djtxt:
            if char not in punctuations:
                analyzevari += char
                
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzevari}   #> এই লাইনটি একটি তালিকা তৈরি করে যা purpose এবং analyzed_text নামক দুটি কী-মান জোড়া রয়েছে। purpose কীটি "Removed Punctuations" মানটি গ্রহণ করে এবং analyzed_text কীটি analyzevari ভেরিয়েবলের মান গ্রহণ করে।
        
        return render(request,'analyze.html',params)#> এই লাইনটি analyze.html নামক একটি HTML পৃষ্ঠা প্রদর্শন করে। params তালিকাটি analyze.html পৃষ্ঠায় প্রেরণ করা হয়।
    else:
        return HttpResponse(b)

    # return HttpResponse(a)
r'''       #> txt = request.GET.get('text','default'): এই লাইনটি ওয়েবসাইট থেকে পাঠ্য ইনপুট সংগ্রহ করে। যদি ব্যবহারকারী কোনও পাঠ্য সরবরাহ না করে তবে এটি "default" মানটি ব্যবহার করবে।

            3>> removepunc = request.GET.get('text','off'): এই লাইনটি ওয়েবসাইট থেকে একটি বিকল্প সংগ্রহ করে যা নির্ধারণ করে যে বিরামচিহ্ন অপসারণ করা উচিত কি না। বিকল্পটি "on" বা "off" হতে পারে
            
            #>>> print(removepunc): এই লাইনটি কেবলমাত্র টার্মিনালে removepunc মানটি মুদ্রণ করে। এটি কোডের কার্যকারিতাকে প্রভাবিত করে না, তবে এটি ডিবাগিংয়ের জন্য দরকারী হতে পারে।
 
           
            
              >>>>>params = {'purpose':'Removed Punctuations','analyzed_text':analyzevari}: এই লাইনটি একটি তালিকা তৈরি করে যা purpose এবং analyzed_text নামক দুটি কী-মান জোড়া রয়েছে। 
                                                            purpose কীটি "Removed Punctuations" মানটি গ্রহণ করে এবং analyzed_text কীটি analyzevari ভেরিয়েবলের মান গ্রহণ করে।
                                                            
            >>>>> return render(request,'analyze.html',params): এই লাইনটি analyze.html নামক একটি HTML পৃষ্ঠা প্রদর্শন করে। params তালিকাটি analyze.html পৃষ্ঠায় প্রেরণ করা হয়।
         
         
         
         
         
         
         
         '''







def menu(request):
    return HttpResponse('menu key')







""" ================================================================> this is generated with AI <==================================================================="""



# import string

# def analyze(request):
#     txt = request.GET.get('text','default')
#     removepunc = request.GET.get('text','off')
#     if removepunc == 'on':
#         analyzevari = ''.join(ch for ch in txt if ch not in string.punctuation)
#     else:
#         analyzevari = txt

#     params = {'purpose':'Removed Punctuations','analyzed_text':analyzevari}
     
#     return render(request,'analyze.html',params)





























