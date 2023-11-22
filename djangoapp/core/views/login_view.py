from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers.login_view import LoginSerializer

class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        # Aqui você pode retornar qualquer informação adicional que desejar sobre o usuário

        return Response({'token': user.auth_token.key}, status=status.HTTP_200_OK)
