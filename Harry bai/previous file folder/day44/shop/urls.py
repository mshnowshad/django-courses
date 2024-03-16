from django.contrib import admin
from django.urls import path
from . import views



#>>>>>  this is "Shop" Urls


urlpatterns = [
    path('',views.indexshop,name="indexshop"),
    path('about',views.about,name="about"),
    path('cart',views.cart,name="cart"),
    path('contact',views.contact,name="contact"),
    path('tracker',views.tracker,name="tracker"),
    path('search',views.search,name="search"),
    path('prodviews',views.prodviews,name="prodviews"),
    path('products/<int:myid>',views.products,name="products"),
    path('cheackout',views.cheackout,name="cheackout"),
    
    
    
   
]
