from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('friendship/', views.my_friendship, name='my_friendship'),
    path('friendship/new', views.new_friendship, name='new_friendship'),
    path('friendship/process', views.friendship_process, name='friendship_process'),
    path('friendship/test/<str:code>', views.friendship_test, name='friendship_test'),
]
