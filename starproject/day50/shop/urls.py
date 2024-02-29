from django.contrib import admin
from django.urls import path
from .views import *



#>>>>>  this is "Shop" Urls


urlpatterns = [
    path('',indexshop,name="indexshop"),
    path('category/<str:foo>',category,name="category"),
    
    path('about',about,name="about"),
    path('cart',cart,name="cart"),
    path('contact',contact,name="contact"),
    path('tracker',tracker,name="tracker"),
    path('search',search,name="search"),
    path('prodlist',prodlist,name="prodlist"),
    path('prodviews/<int:prdid>',prodviews,name="prodviews"),
    path('cheackout',cheackout,name="cheackout"),
    
    
    
   
]
