from django.urls import path

from .views import DeliveryView

from django.urls import re_path

urlpatterns = [
    path('delivery', DeliveryView.as_view())
    
]

