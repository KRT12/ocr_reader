"""ocr_reader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include

from user.views import BaseView, UploadImage, RegisterUser

urlpatterns = [
    url(r'^first/',BaseView.as_view(),name= 'base-view'),
    url(r'^upload-image/',UploadImage.as_view(),name= 'upload-image'),
    url(r'^register-user/',RegisterUser.as_view(),name= 'register-user'),
]
