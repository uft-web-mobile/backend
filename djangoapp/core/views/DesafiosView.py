from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Desafio
from core.serializers import DesafioSerializer, DesafioCreateSerializer, DesafioUpdateSerializer

class DesafiosView(APIView):
  queryset = Desafio.objects.all()
  
  def get(self, request):
    try:
        data = Desafio.objects.all()
        return Response({'desafios': DesafioSerializer(data, many=True).data}, status=200)
    except Exception as e:
        return Response({'error': str(e)})
  
  def post(self, request):
    serializer = DesafioCreateSerializer(data=request.data['desafio']) 
    print(serializer.is_valid())
    if serializer.is_valid():
      serializer.save()
      return Response({"Desafio Cadastrado": serializer.data}, status=200)
    
    return Response({'error': serializer.data}, status=500)

  
class DesafioDetailsView(APIView):
  queryset = Desafio.objects.all()
  
  def get(self, request, pk):
    try:
      desafio = Desafio.objects.filter(id=pk).first()
      return Response(DesafioSerializer(desafio).data, status=200)
    
    except Exception as e:
          return Response({'error': str(e)})
        
  def put(self, request, pk=None):
    try:
        desafio = Desafio.objects.get(pk=pk)
    except Desafio.DoesNotExist:
        return Response({'error': 'Desafio não encontrado'}, status=404)
    print('\033[34m')
      
    serializer = DesafioUpdateSerializer(desafio, data=request.data['desafio'], partial=True)
    
    print(serializer)
    
    print('\033[0m')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)

    return Response({'error': serializer.errors}, status=500)

  def delete(self, request, pk=None):
    try:
        desafio = Desafio.objects.get(pk=pk)
    except Desafio.DoesNotExist:
        return Response({'error': 'Desafio não encontrado'}, status=404)

    desafio.delete()
    return Response({'message': 'Desafio excluído com sucesso'}, status=200)
  