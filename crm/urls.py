from django.urls import path

from . import views

from django.urls import re_path

urlpatterns = [
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('test_token', views.test_token),
]




