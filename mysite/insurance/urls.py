from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my-template/',views.my_template_view, name='my_template'),
    path('问卷',views.survey, name='survey')
]