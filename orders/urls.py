from django.contrib import admin
from django.urls import path, include, re_path
from .import views


urlpatterns = [
    re_path('^basket_adding/$', views.basket_adding, name='basket_adding'),
    re_path('^checkout/$', views.checkout, name='checkout')
]