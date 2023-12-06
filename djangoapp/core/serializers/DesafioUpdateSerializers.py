from rest_framework import serializers
from core.models import Desafio

class DesafioUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Desafio
        fields = ['titulo', 'subtitulo', 'descricao', 'dificuldade', 'visivel']