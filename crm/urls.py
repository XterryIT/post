from django.urls import path

from . import views

from django.urls import re_path

urlpatterns = [
    path('api/login', views.UserApiView.as_view()),

]




