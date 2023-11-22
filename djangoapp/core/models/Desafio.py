from django.db import models
from core.models import Resultado

VALUES_CHOICES = (
  # (valor, nome do item)
  ('facil', 'Facil'),
  ('medio', 'Medio'),
  ('dificil', 'Difícil'),
)

class Desafio(models.Model):
  titulo = models.CharField(max_length=200)
  subtitulo = models.CharField(max_length=200)
  descricao = models.TextField()
  dificuldade = models.CharField(max_length=25, choices=VALUES_CHOICES)
  visivel = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.titulo} - {self.subtitulo}' 

  def visualizarResultados(self):
    resultados = Resultado.objects.filter(desafio=self)
    return resultados
