# from django.contrib import admin

from django.urls import path
from .views import *




urlpatterns = [
   
    
    path('',index,name="index"),
    path('about',about,name="about"),
    path('login',login_user,name="login"),
    path('logout',logout_user,name="logout"),
    
    
    
    path('showprod/<int:pk>',showprod,name="showprod"),
    
    
    

]
