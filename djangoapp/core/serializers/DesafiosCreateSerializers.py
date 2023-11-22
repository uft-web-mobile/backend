from rest_framework import serializers
from core.models import Desafio, Resultado

class ResultadoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = ['entrada', 'saida', 'visivel']

class DesafioCreateSerializer(serializers.ModelSerializer):
    resulta_desafio_related = ResultadoCreateSerializer(many=True)

    class Meta:
        model = Desafio
        fields = ['titulo', 'subtitulo', 'descricao', 'dificuldade', 'visivel', 'resulta_desafio_related']

    def create(self, validated_data):
        resultados_data = validated_data.pop('resulta_desafio_related')
        desafio = Desafio.objects.create(**validated_data)
        for resultado_data in resultados_data:
            Resultado.objects.create(desafio=desafio, **resultado_data)
        return desafio