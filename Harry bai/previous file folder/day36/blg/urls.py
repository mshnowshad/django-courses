from django.contrib import admin
from django.urls import path
from . import views



#>>>>>  this is "Shop" Urls


urlpatterns = [
    path('',views.indexblg,name="blghome"),
    path('about',views.about,name="about"),
    path('cheakout',views.cheakout,name=" cheackout"),
    path('contract',views.contract,name="contract"),
    path('prodviews',views.prodviews,name="prodviews"),
    path('search',views.search,name="search"),
    path('tracker',views.tracker,name="tracker"),
    
    
   
]














