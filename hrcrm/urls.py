from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'hrcrm'
urlpatterns = [
    path('hrcrm/', views.index, name = 'index'),
    
]