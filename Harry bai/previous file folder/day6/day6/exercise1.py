# print()
print('++++++++++++++++++ > this is a personal navigator  <+++++++++++++++++++++++++++++++++')
print()


from django.http import HttpResponse






s=[ '''<h1> Wellcom to my New page of http:8000 </h2> ''',
    '''<h1> </h1>''',
    '''<h1> </h1>''',
    '''<h1> </h1>''',
    '''<h1>for Anything Search</h1><a href="https://www.google.com/"> Google Search Engine </a>'''
    '''<h1>For Django </h1><a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a>''',
    '''<h1>For FB LogIn</h1><a href="https://www.facebook.com/"> Facebook </a>''' ,
    '''<h1>For AI Help</h1><a href="https://chat.openai.com/c/f678f3fe-f6e4-4daf-895a-c41b66f2d4ed/"> ChatGPT </a>''',
    '''<h1>For Any Bangladeshi News</h1><a href="https://www.jugantor.com/"> Juganthor </a>''',
    '''<h1>This is Programmin Practice site</h1><a href="https://www.w3schools.com/"> W3 School</a>''',
    '''<h1> </h1>'''  ##>> ei line diya space deu a oise
    '''<a href="https://www.practicepython.org/"> Python Practice</a>''',
    '''<h1> </h1>''',
    '''<a href="https://leetcode.com/">Leet Code</a>''',
    '''<h1> </h1>''',
    '''<a href="https://www.codechef.com/dashboard/"> CodeChef </a>''',
    '''<h1> </h1>''',
    '''<a href="https://www.hackerrank.com/"> Hacker Rank </a>''',
    
]


def index(request):
    return HttpResponse(s,)
    




















# print("=======================================> this is an other <=====================================")





 
# Views.py 

# I have created this file - Harry



 
# from django.http import HttpResponse  #>  এটি HTTP রেসপন্স ফেরত দেয়।
# from django.shortcuts import render   


# def index(request):
#     return render(request, 'index.html')  #render মেথড ব্যবহার করে index.html নামের একটি HTML টেমপ্লেট রিটার্ন করে।

#     # return HttpResponse("Home")


# def index(request):   ##> <h1> ট্যাগ ব্যবহার করে শিরোনাম দেওয়া হয়েছে </h1> diye shironame line close kora hoyeche
#                         #>> <a> ট্যাগ ব্যবহার করে ক্লিকযোগ্য লিঙ্ক তৈরি করা হয়েছে (<a href="URL">Link Text</a>).
                        
#     sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
#              '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
#              '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
#              '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
#              ]
#     return HttpResponse(sites)




















