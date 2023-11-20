from django.urls import path

from .views.usuario_view import UsuarioView
from .views.compilador_view import ExecuteCodeView

urlpatterns = [
    path('usuarios/', UsuarioView.as_view(), name='usuario_list'),
    path('usuarios/<int:pk>/', UsuarioView.as_view(), name='usuario_detail'),
    path('execute-code/', ExecuteCodeView.as_view(), name='execute-code'),
]
