from django.urls import path

from .views import Register, Login

from django.urls import re_path

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
]




