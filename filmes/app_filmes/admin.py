from django.contrib import admin
from app_filmes.models import Filme, Usuario

class UsuarioAdmin(admin.ModelAdmin):
    filter_horizontal = ('filmes',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Filme)