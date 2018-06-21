from django.contrib import admin
from django.urls import path, include, re_path
from . import views



urlpatterns = [
    re_path('^product/(?P<product_id>\w+)/$', views.product, name='product')
]