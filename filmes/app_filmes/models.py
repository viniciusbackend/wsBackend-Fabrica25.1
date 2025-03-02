from django.db import models
import requests

    
class Filme(models.Model):
    titulo = models.CharField(max_length=150, primary_key=True, unique=True)
    ano = models.IntegerField()
    duracao = models.CharField(max_length=50)
    diretor = models.CharField(max_length=50)
    linguagem = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    
    def __str__(self):
        return self.titulo
    
    @staticmethod
    def pegar_dados(nome_filme):
        url = f'http://www.omdbapi.com/?t={nome_filme}&apikey=a5a9f910'
        response = requests.get(url)
        if response.status_code == 200:
            dados_json = response.json()
            return Filme(
                titulo = dados_json['Title'], 
                ano = dados_json['Year'], 
                duracao = dados_json['Runtime'],
                diretor = dados_json['Director'],
                linguagem = dados_json['Language'],
                genero = dados_json['Genre']
            )
        else:
            response.raise_for_status()
    

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    data_nascimento = models.DateField(max_length=50)
    filmes =  models.ManyToManyField(Filme, blank=True)

    def __str__(self):
        return self.nome
    
