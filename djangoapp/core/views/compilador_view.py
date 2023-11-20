import json
import base64
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ..utils.compilador import execute_javascript, execute_python

class ExecuteCodeView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = []


    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        if data['language'] not in ['python', 'javascript'] or data['file'] == '':
            return Response({'error': 'Linguagem Invalida ou File Invalido.'}, status=status.HTTP_400_BAD_REQUEST)

        encoded_file_content = data['file']
        language = data['language']

        try:
            # Decodificar o arquivo base64
            file_content = base64.b64decode(encoded_file_content).decode('utf-8')
            
            if language == 'python':
                result = execute_python(file_content)
                return JsonResponse({'output': result})
                
            elif language == 'javascript':
                result = execute_javascript(file_content)
                return JsonResponse({'output': result})

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
