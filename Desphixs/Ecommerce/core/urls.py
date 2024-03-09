from django.urls import path
from .views import *


urlpatterns = [
    path('index/',index,name="index"),

    path('',home,name="home"),
    # path('cart/',cart,name="cart"),
    path('checkout/',checkout,name="checkout"),
    path('detail/<int:pv>', detail, name="detail"),
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
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('update_password/',update_password, name='update_password'),
    path('update_user/', update_user, name='update_user'),
    path('update_info/',update_info, name='update_info'),

    

]
