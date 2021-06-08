from django.contrib import admin
from django.urls import path,include
from .views import homepage,showContact

urlpatterns = [
    path('',homepage,name='home'),
    path('contact/',showContact,name="contact"),
]
