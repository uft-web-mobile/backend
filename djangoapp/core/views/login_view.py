from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from ..serializers.login_serialize import EmailPasswordSerializer
from ..models.usuario_model import Usuario

class LoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email_password_serializer = EmailPasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        
        email_password_serializer.is_valid(raise_exception=True)
        
        email = email_password_serializer.validated_data['email']
        password = email_password_serializer.validated_data['password']

        # Autenticação do usuário
        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Restante do código para obter ou criar o token
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'id': user.id,
            'username': user.username, 
            'email': user.email,
            'token': token.key
        })