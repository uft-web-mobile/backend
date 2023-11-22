from django.urls import path
from core.views import UsuarioView, DesafiosView, DesafioDetailsView, ResultadosView, ResultadoDetailsView

urlpatterns = [
    path('usuarios/', UsuarioView.as_view(), name='usuario_list'),
    path('usuarios/<int:pk>/', UsuarioView.as_view(), name='usuario_detail'),
    
    path('desafios/', DesafiosView.as_view(), name='desafios_list'),
    path('desafios/<int:pk>', DesafioDetailsView.as_view(), name='desafio_detail'),
    path('desafios/<int:id_desafio>/resultado/', ResultadosView.as_view(), name='resultados_desafio'),
    path('desafios/resultado/<int:pk>', ResultadoDetailsView.as_view(), name='resultados_desafio_detail'),
]
