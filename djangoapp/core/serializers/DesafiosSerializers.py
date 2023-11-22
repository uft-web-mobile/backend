from rest_framework import serializers
from core.models import Desafio, Resultado

class DesafioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Desafio
    fields = ['id', 'titulo', 'subtitulo', 'descricao', 'dificuldade', 'visivel']