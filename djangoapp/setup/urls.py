from django.contrib import admin
from django.urls import include, path
from rest_framework import urls
from .views import LoginAPI
from django.views.generic import RedirectView

urlpatterns = [
    path('api/v1/login', include('core.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', LoginAPI.as_view(), name='login'), 
]
