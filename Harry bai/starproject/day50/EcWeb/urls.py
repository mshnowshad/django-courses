"""
URL configuration for EcWeb project.

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


#===========> this is 'Ecweb' Urls <===============








from django.contrib import admin
from django.urls import path,include
from django.conf import settings  # eita use kora oise because admin panael a image deka jeno jay.
from django.conf.urls.static import static   # eita use kora oise because admin panael a image deka jeno jay.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('blg/',include('blg.urls'))]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  # eita diya admin panel a kunu images upload korle jeno deka jay..thai use kora oise





