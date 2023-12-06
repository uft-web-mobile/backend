from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Desafio, Resultado
from core.serializers import ResultadosSerializers, ResultadoCreateSerializer, DesafioUpdateSerializer

class ResultadosView(APIView):
  queryset = Resultado.objects.all()
  
  def get(self, request, id_desafio):
    try:
        data = Resultado.objects.filter(desafio=id_desafio)
        return Response({'resultados': ResultadosSerializers(data, many=True).data}, status=200)
    except Exception as e:
        return Response({'error': str(e)})
  
  def post(self, request, id_desafio):
    data = request.data['resultado']
    data['desafio'] = id_desafio
    serializer = ResultadoCreateSerializer(data=data) 
    if serializer.is_valid():
      serializer.save()
      return Response({"Resuldato Cadastrado": serializer.data}, status=200)
    
    return Response({'error': serializer.data}, status=500)


class ResultadoDetailsView(APIView):
  queryset = Resultado.objects.all()
  
  def get(self, request, pk):
    try:
      resultado = Resultado.objects.filter(id=pk).first()
      return Response(ResultadosSerializers(resultado).data, status=200)
    
    except Exception as e:
          return Response({'error': str(e)})
        
  def put(self, request, pk=None):
    try:
        resultado = Resultado.objects.get(pk=pk)
    except Desafio.DoesNotExist:
        return Response({'error': 'Resultado não encontrado'}, status=404)
      
    serializer = ResultadoCreateSerializer(resultado, data=request.data['resultado'], partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)

    return Response({'error': serializer.errors}, status=500)

  def delete(self, request, pk=None):
    try:
        resultado = Resultado.objects.get(pk=pk)
    except Desafio.DoesNotExist:
        return Response({'error': 'Resultado não encontrado'}, status=404)

    resultado.delete()
    return Response({'message': 'Resultado excluído com sucesso'}, status=200)
  