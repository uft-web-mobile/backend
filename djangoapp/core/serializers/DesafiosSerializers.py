from rest_framework import serializers
from core.models import Desafio, Resultado
from core.serializers.ResultadosSerializers import ResultadosSerializers

class DesafioSerializer(serializers.ModelSerializer):
  resulta_desafio_related = ResultadosSerializers(many=True)
  
  class Meta:
    model = Desafio
    fields = ['id', 'titulo', 'subtitulo', 'descricao', 'dificuldade', 'visivel', 'resulta_desafio_related']