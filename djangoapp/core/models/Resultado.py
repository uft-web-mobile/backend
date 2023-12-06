from django.db import models
from core.models import Desafio

class Resultado(models.Model):
  desafio = models.ForeignKey('Desafio', related_name='resulta_desafio_related', on_delete=models.CASCADE)
  entrada = models.CharField(max_length=255)  
  saida = models.CharField(max_length=255)
  visivel = models.BooleanField(default=True)
    
  def __str__(self):
    return f'123'

  class Meta:
    verbose_name = 'Resultado'
    verbose_name_plural = 'Resultados'