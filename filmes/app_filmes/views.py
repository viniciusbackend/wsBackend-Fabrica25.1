from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from app_filmes.models import Filme, Usuario
from app_filmes.serializers import FilmeSerializers, UsuarioSerializers
import json

class FilmesView(APIView):
    def get(self, request):
        filmes = Filme.objects.all()
        serializer = FilmeSerializers(filmes, many=True)
        return Response(serializer.data)

    def post(self, request):
        dicionario = json.loads(request.body)
        filme = Filme.pegar_dados(dicionario['titulo'])
        if filme:
            filme.save()
            serializer = FilmeSerializers(filme)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)  

class FilmeView(APIView):
        
    def get(self, request, pk):
            try:
                filme = Filme.objects.get(pk=pk)
                seralizer = FilmeSerializers(filme)
                return Response(seralizer.data)
            except Filme.DoesNotExist:
                 return Response(status=status.HTTP_404)
            
    def post(self, request):
        dicionario = json.loads(request.body)
        filme = Filme.pegar_dados(dicionario['titulo'])
        if filme:
            filme.save()
            serializer = FilmeSerializers(filme)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 
        
    def put(self, request, pk):
            filme = Filme.objects.get(pk=pk)
            seralizer = FilmeSerializers(filme, data=request.data)
            if seralizer.is_valid():
                seralizer.save()
                return Response(seralizer.data)
            return Response(seralizer.erros, status=status.HTTP_400_BAD_REQUEST )
        
    def delete(self, request, pk):
            filme = Filme.objects.get(pk=pk)
            if filme:
                filme.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                 return Response(status=status.HTTP_400_BAD_REQUEST)

class UsuarioView(APIView):
        
    def get(self, request, pk):
            usuario = Usuario.objects.get(pk=pk)
            seralizer = UsuarioSerializers(usuario)
            return Response(seralizer.data)
    
    def post(self, request):
         serializer = UsuarioSerializers(data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
         else: 
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
            usuario = Usuario.objects.get(pk=pk)
            seralizer = UsuarioSerializers(usuario, data=request.data)
            if seralizer.is_valid():
                seralizer.save()
                return Response(seralizer.data)
            else:
                return Response(seralizer.erros, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
            usuario = Usuario.objects.get(pk=pk)
            if usuario:
                usuario.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                  return Response(status=status.HTTP_400_BAD_REQUEST)
            
class UsuarioFilmes(APIView):
     def get(self, request, pk):
            try:
                usuario = Usuario.objects.get(pk=pk)
                serializer = FilmeSerializers(usuario.filmes, many=True)
                return Response(serializer.data)
            except Usuario.DoesNotExist:
                 return Response(status=status.HTTP_404_NOT_FOUND)
            
     def delete(self, request, pk, titulo):
            try:
                usuario = Usuario.objects.get(pk=pk)
                filme = Filme.objects.get(titulo=titulo)
                usuario.filmes.remove(filme)
                return Response(status=status.HTTP_200_OK)
            except (Usuario.DoesNotExist,Filme.DoesNotExist):
                 return Response(status=status.HTTP_404_NOT_FOUND)
            
     def post(self, request, pk, titulo):
            try:
                usuario = Usuario.objects.get(pk=pk)
                filme = Filme.objects.get(titulo=titulo)
                usuario.filmes.add(filme)
                return Response(status=status.HTTP_200_OK)
            except (Usuario.DoesNotExist,Filme.DoesNotExist):
                 return Response(status=status.HTTP_404_NOT_FOUND)
            