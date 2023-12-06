from django.db import models
from core.models import Desafio, Usuario

class UserDesafio(models.Model):
  usuario = models.ForeignKey(Usuario, related_name='usuario_do_desafio', on_delete=models.SET_NULL, null=True)
  desafios = models.ForeignKey(Desafio, related_name='desafio_do_usuario', on_delete=models.CASCADE)

  class Meta:
    verbose_name = 'Desafio do Usuario'
    verbose_name_plural = 'Desafios dos Usuarios'

  def __str__(self):
    return f'Desafio {self.desafio.titulo} de {self.usuario.username}' 