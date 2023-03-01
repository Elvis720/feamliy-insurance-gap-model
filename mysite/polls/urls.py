from django.urls import path

from . import views

urlpattertns = [
    path('', views.index, name='index'),
]