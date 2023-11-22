from rest_framework import serializers
from core.models import Resultado

class ResultadosSerializers(serializers.ModelSerializer):
  class Meta:
    model = Resultado
    fields = ['id', 'desafio', 'entrada', 'saida', 'visivel']
