from django.urls import path
from app_filmes.views import FilmesView, FilmeView, UsuarioView, UsuarioFilmes

urlpatterns = [
    path('filmes/<str:pk>/', FilmeView.as_view()),
    path('filmes/', FilmesView.as_view()),
    path('usuario/<int:pk>/', UsuarioView.as_view()),
    path('usuario/', UsuarioView.as_view()),
    path('usuario/<int:pk>/filmes/', UsuarioFilmes.as_view()),
    path('usuario/<int:pk>/filmes/<str:titulo>/', UsuarioFilmes.as_view())
]
