"""
URL configuration for new project.

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
from django.contrib import admin
from django.urls import path
from . import createownfiledjango  #> file name is "createownfiledjango"

urlpatterns = [  #> এখানে একটা লিস্ট তৈরি করা হচ্ছে, যার নাম urlpatterns। এই লিস্টে ওয়েবসাইটের বিভিন্ন URL বা লিংকগুলো সংরক্ষণ করা হবে।
               
    path('admin/', admin.site.urls),
    path('',createownfiledjango.index, name='index'),    #>এই লাইনটা আরেকটা URL যোগ করছে। এই URLটা হচ্ছে মূল ওয়েবসাইটের লিংক (যেমন, http://localhost:8000/)। যখন কেউ এই লিংকটা ব্যবহার করবে, তখন createownfiledjango ফাইলের ভেতরে থাকা index নামের ফাংশনটা চালু হবে।
    path('about',createownfiledjango.about, name='about'),  #> এই লাইনটা আরেকটা URL যোগ করছে। এই URLটা হচ্ছে about পৃষ্ঠার লিংক। যখন কেউ এই লিংকটা ব্যবহার করবে, তখন createownfiledjango ফাইলের ভেতরে থাকা about নামের ফাংশনটা চালু হবে। about পৃষ্ঠায় যেতে চায়, তাহলে তাকে http://localhost:8000/about লিংকটা ব্যবহার করতে হবে।
    
]
