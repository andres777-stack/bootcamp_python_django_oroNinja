from django.urls import path     
from . import views
urlpatterns = [
    path('proccess_money', views.proccess),
    path('', views.index),
]