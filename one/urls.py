from .views import MyView, MyTemplateView, MyDetailView, MyListView
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('myview/', MyView.as_view(), name='myview'),
    path('mytemplateview/', MyTemplateView.as_view(), name='mytemplateview'),
    re_path('^mydetailview/(?P<pk>\d+)/$', MyDetailView.as_view(), name='mydetailview'),   # отрисовует во views модель продукта, по pk
    path('mylistview/', MyListView.as_view(), name='mylistview'),

]
