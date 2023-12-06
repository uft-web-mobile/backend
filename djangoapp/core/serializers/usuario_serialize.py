from rest_framework import serializers
from ..models.usuario_model import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'primeiro_nome', 
                  'segundo_nome', 'data_nascimento', 'password', 
                  'e_admin', 'criado_em', 'atualizado_em']
