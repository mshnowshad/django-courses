# print('hello world')

###> এই কোডটা একটা ছোট ওয়েবসাইট তৈরি করছে, যার দুটো পেজ আছে:  ১. হোমপেজ (index) , ২. About পেজ



from django.http import HttpResponse  ##> এই লাইনটা একটা ফাংশনকে আমদানি করছে। এই ফাংশনটার নাম HttpResponse। এই ফাংশনটা দিয়ে ওয়েবসাইটের পেজগুলো তৈরি করা হবে।
                                        ###>>> 'HttpResponse' এই ফাংশনটি ওয়েব ব্রাউজারে দেখানোর জন্য তথ্য পাঠায়।
                                        ##>>>>> 'HttpResponse'  এটি ওয়েব পেজের মূল কন্টেন্ট, শিরোনাম, এবং অন্যান্য উপাদানগুলো তৈরি করতে ব্যবহার করা হয়।

##> 'a' is a variable
a = """> Hello I am Nowshad.                         
             I am beginner of django framework.
                I am first program write in the Django Frame work. 
                    Thanks for watching this Program. 
 

            """

def index(request):  ##> এই লাইনটা একটা ফাংশন তৈরি করছে। এই ফাংশনটার নাম index। এই ফাংশনটা হোমপেজ দেখানোর জন্য দায়ী।
    return HttpResponse(a)  ##> এই লাইনটা বার্তাটাকে ওয়েবপেজ হিসেবে পাঠিয়ে দিচ্ছে। যখন কেউ ওয়েবসাইটে যাবে, তখন সে এই বার্তাটা দেখতে পাবে।



def about(request):   #> line NO: 18
    return HttpResponse('Hello World')  ##> এই লাইনটা "Hello World" লেখাটা About পেজ হিসেবে পাঠিয়ে দিচ্ছে। যখন কেউ About পেজে যাবে, তখন সে এই লেখাটা দেখতে পাবে।

    
#date : 29 December 2023
    
'''মোটকথায়, এই কোডটা একটা ছোট ওয়েবসাইট তৈরি করছে, যার দুটো পেজ আছে: হোমপেজ এবং About পেজ।'''
    
    
