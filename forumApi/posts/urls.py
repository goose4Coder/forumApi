from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.main_page),
    path("user_info/", views.get_user_info),
]

