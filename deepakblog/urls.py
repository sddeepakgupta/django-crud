from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'deepakblog'

urlpatterns = [
    path('', views.index, name='index'),
    path('musicianDelete/<int:id>/', views.musicianDelete),
]