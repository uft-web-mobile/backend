from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.hashers import make_password
from datetime import datetime
from ..models.usuario_model import Usuario
from ..serializers.usuario_serialize import UsuarioSerializer
import json



class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        
        # Verificar se todos os campos obrigatórios estão presentes
        required_fields = ['email', 'senha', 'primeiro_nome', 'segundo_nome', 'data_nascimento', 'e_admin']
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({'error': f'O campo {field} é obrigatório'}, status=400)

        # Verificar se o usuário já existe
        try:
            usuario_existente = Usuario.objects.get(email=data['email'])
            return JsonResponse({'error': 'Um usuário com este e-mail já existe'}, status=400)
        except ObjectDoesNotExist:
            pass  # Continue se o usuário não existir
        
        senha_criptografada = make_password(data['senha'])
        
        usuario = Usuario(
            email=data['email'],
            primeiro_nome=data['primeiro_nome'],
            segundo_nome=data['segundo_nome'],
            data_nascimento=data['data_nascimento'],
            senha=senha_criptografada,
            e_admin=data['e_admin']
        )
        usuario.save()
        
        serializer = UsuarioSerializer(usuario)
        
        return JsonResponse(serializer.data, safe=False)

    def delete(self, request, pk, *args, **kwargs):
        
        # Verificar se o usuário existe
        try:
            usuario = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Usuário não encontrado'}, status=404)

        # Excluir o usuário se existir
        usuario.delete()

        return JsonResponse({'message': 'Usuário excluído com sucesso!'})
    
    def put(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)

        # Verificar se todos os campos obrigatórios estão presentes
        required_fields = ['email', 'primeiro_nome', 'segundo_nome', 'data_nascimento', 'e_admin']
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({'error': f'O campo {field} é obrigatório'}, status=400)

        # Verificar se o usuário existe
        usuario = get_object_or_404(Usuario, pk=pk)

        # Atualizar os campos do usuário
        usuario.email = data['email']
        usuario.primeiro_nome = data['primeiro_nome']
        usuario.segundo_nome = data['segundo_nome']
        usuario.data_nascimento = data['data_nascimento']

        # Verificar e atualizar a senha, se presente nos dados
        if 'senha' in data:
            senha_criptografada = make_password(data['senha'])
            usuario.senha = senha_criptografada

        usuario.e_admin = data['e_admin']
        usuario.atualizado_em = datetime.now()
        usuario.save()

        serializer = UsuarioSerializer(usuario)

        return JsonResponse(serializer.data, safe=False)
