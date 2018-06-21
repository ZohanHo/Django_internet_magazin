from django.urls import path, include, re_path
from . import views
from django.conf.urls import url



urlpatterns = [
    path('subscribers/', views.subscribers, name = 'subscribers'),
    path('', views.home, name = 'home'),
]