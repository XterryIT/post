from django.contrib import admin
from django.urls import path, include
from crm.views import UserApiView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login', UserApiView.as_view())
]
