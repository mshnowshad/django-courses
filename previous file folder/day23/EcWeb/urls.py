"""
URL configuration for EcWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


#===========> this is 'Ecweb' Urls <===============








from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('blg/',include('blg.urls'))]   





"""path: এটা হলো ডি'জ্যাঙ্গোতে URL রাউটিং এর জন্য ব্যবহৃত একটি ফাংশন।
                                                                'shop/': এটি একটি স্ট্রিং যা একটি URL প্যাটার্ন নির্দেশ করে। 
                                                                এটি নির্দেশ করে যে কোন ওয়েবসাইট এর URL যা shop/ দিয়ে শুরু হবে, সেই URL এর পরবর্তী অংশ এই নির্দিষ্ট কনফিগারেশনের জন্য ব্যবহার করা হবে।
                                                                
                                        include('shop.urls'): এটি অন্যান্য URL কনফিগারেশন মডিউল থেকে URL হ্যান্ডলিং করার জন্য 'shop.urls' মডিউলকে ইনক্লুড এবং ব্যবহার করে। 
                                                            include ফাংশনটি ডি'জ্যাঙ্গোতে অন্যান্য মডিউল বা ফাইল থেকে অন্যান্য URL কনফিগারেশন ইনক্লুড করার জন্য ব্যবহৃত হয়। 
                                                            
                                        তাই, shop/ দিয়ে শুরু হওয়া যে কোন ওয়েবসাইটের URL এর ক্ষেত্রে, ডি'জ্যাঙ্গো সেই URL টি স্পেসিফিক কনফিগারেশনে নির্দিষ্ট করে তা কিভাবে হ্যান্ডল করবে সেটি দেখার জন্য shop.urls ফাইল/মডিউলে দেখবে।
                                                        সারাংশঃ এই কোড লাইন দিয়ে বুঝানো হয়েছে যে, 
                                                        যখন একজন ব্যবহারকারী yourwebsite.com/shop/anything-after-shop/ এই ধরনের একটি URL এ অ্যাক্সেস করবে,
                                                             তখন ডি'জ্যাঙ্গো সেই URL প্যাটার্ন হ্যান্ডল করার জন্য shop.urls ফাইল/মডিউল এ দেখবে এবং সেখানে নির্দিষ্ট করা থাকা অনুযায়ী পরবর্তী পদক্ষেপ গ্রহণ করবে।"""




