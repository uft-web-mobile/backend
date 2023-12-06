from rest_framework import serializers
from django.contrib.auth import authenticate

class EmailPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")

        # Adicione lógica de validação personalizada aqui, se necessário

        return data
