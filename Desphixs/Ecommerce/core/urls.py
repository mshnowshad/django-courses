from django.urls import path
from .views import *


urlpatterns = [
    path('index/',index,name="index"),

    path('',home,name="home"),
    path('cart/',cart,name="cart"),
    path('checkout/',checkout,name="checkout"),
    path('detail/',detail,name="detail"),
    path('products/',products,name="products"),
    path('testimonial/',testimonial,name="testimonial"),
    path('contact/',contact,name="contact"),
    path('error/',error,name="error"),
    # path('index/',index,name="index"),
    # path('index/',index,name="index"),
    # path('index/',index,name="index"),
    # path('index/',index,name="index"),
    # path('index/',index,name="index"),
    # path('index/',index,name="index"),
    # path('index/',index,name="index"),
    # path('index/',index,name="index"),
    # path('index/',index,name="index"),
    # path('index/',index,name="index"),

    

]
