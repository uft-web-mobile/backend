from django.contrib import admin
from django.urls import include, path
from rest_framework import urls
from django.views.generic import RedirectView

urlpatterns = [
    path('api/v1/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
