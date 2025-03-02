from rest_framework import serializers
from app_filmes.models import Filme, Usuario

class FilmeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ('__all__')

class UsuarioSerializers(serializers.ModelSerializer):
    filmes = FilmeSerializers(many=True, read_only=True)
    class Meta:
        model = Usuario
        fields = ('__all__')