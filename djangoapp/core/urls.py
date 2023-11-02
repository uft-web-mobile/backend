from django.urls import path
from .views.usuario_view import UsuarioView

urlpatterns = [
    path('usuarios/', UsuarioView.as_view(), name='usuario_list'),
    path('usuarios/<int:pk>/', UsuarioView.as_view(), name='usuario_detail'),
]
