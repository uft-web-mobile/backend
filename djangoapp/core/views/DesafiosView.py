from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Desafio
from core.serializers import DesafioSerializer, DesafioCreateSerializer

class DesafiosView(APIView):
  queryset = Desafio.objects.all()
  
  def get(self, request):
    try:
        data = Desafio.objects.all()
        return Response({'desafios': DesafioSerializer(data, many=True).data}, status=200)
    except Exception as e:
        return Response({'error': str(e)})
  
  def post(self, request):

    print('\033[32m')
    
    print(request.data)
    
    print('\033[0m')
    
    # return Response({'Teste': True}, status=200)
    
    serializer = DesafioCreateSerializer(data=request.data['desafio']) 
    print(serializer.is_valid())
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=200)
    
    return Response({'error': serializer.data}, status=500)
  
class DesafioDetailsView(APIView):
  def get(self, request, pk):
    try:
      data = Desafio.objects.filter(id=pk).first()
      return Response(DesafioSerializer(data), status=200)
    except Exception as e:
          return Response({'error': str(e)})
  