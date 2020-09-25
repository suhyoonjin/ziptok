from django.contrib import admin
from django.urls import path, re_path
from restapi import views

urlpatterns = [
    path('rest_courses/',  views.list_courses),
    re_path('rest_courses/(?P<code>\w+)/$', views.course_details),
    path('rest_client/', views.client),
]