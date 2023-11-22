from django.urls import path
from core.views import UsuarioView, DesafiosView, DesafioDetailsView

urlpatterns = [
    path('usuarios/', UsuarioView.as_view(), name='usuario_list'),
    path('usuarios/<int:pk>/', UsuarioView.as_view(), name='usuario_detail'),
    
    path('desafios/', DesafiosView.as_view(), name='desafios_list'),
    path('desafios/<int:pk>', DesafioDetailsView.as_view(), name='desafio_detail'),
]
