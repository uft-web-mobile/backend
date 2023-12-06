from rest_framework import serializers
from core.models import Resultado

class ResultadoCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Resultado
    fields = ['entrada', 'saida', 'visivel']