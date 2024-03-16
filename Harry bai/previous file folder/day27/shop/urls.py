from django.contrib import admin
from django.urls import path
from . import views



#>>>>>  this is "Shop" Urls


urlpatterns = [
    path('',views.indexshop,name="ShopHome"),
    path('about',views.about,name="about"),
    path('contract',views.contract,name="contract"),
    path('tracker',views.tracker,name="tracker"),
    path('search',views.search,name="search"),
    path('prodviews',views.prodviews,name="prodviews"),
    path('cheackout',views.cheackout,name="cheackout"),
    
    
   
]
