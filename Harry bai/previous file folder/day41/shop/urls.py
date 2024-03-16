from django.contrib import admin
from django.urls import path
from . import views



#>>>>>  this is "Shop" Urls


urlpatterns = [
    path('',views.indexshop,name="indexshop"),
    
    path('contract',views.contract,name="contract"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('tracker',views.tracker,name="tracker"),
    path('search',views.search,name="search"),
    path('prodviews',views.prodviews,name="prodviews"),
    path('products/<int:myid>',views.products,name="products"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    

]
