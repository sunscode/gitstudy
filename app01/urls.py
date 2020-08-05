from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app01 import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^article/(\d+)$', views.article, name='article'),
    url(r'^backend/$', views.backend, name='backend'),

    url(r'^article_list/$', views.article_list, name='article_list'),

]
