from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'deepakblog'

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userLogout, name='userlogout'),
    path('musicianDelete/', views.musicianDelete, name="musicianDelete"),
    path('productMaster/', views.productMaster, name="productMaster"),
    path('productMasterDetails/', views.productMasterDetails, name="productMasterDetails"),
]