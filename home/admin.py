from django.contrib import admin
from .models import Perfil

class DetPerfil(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'nome_empresa', )
    list_display_links = ('nome', )
    search_fields = ('nome', 'email', 'nome_empresa')

admin.site.register(Perfil, DetPerfil)


# Register your models here.
