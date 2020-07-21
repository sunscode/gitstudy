from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app01 import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
]
