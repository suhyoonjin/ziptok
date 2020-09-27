from django.contrib import admin
from django.urls import path, re_path, include
from login_test import views

urlpatterns = [
    path('', views.index_page),
    path('register_page/', views.register_page),
    path('register_page/register', views.register),

    path('register_page/check_data', views.check_data)
]