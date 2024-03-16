from django.contrib import admin
from django.urls import path
from . import views



#>>>>>  this is "Shop" Urls


urlpatterns = [
    path('',views.indexshop,name="ShopHome")
   
]
