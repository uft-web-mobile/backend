from django.contrib import admin

from .models.usuario_model import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'primeiro_nome', 'username', 'segundo_nome', 
                    'data_nascimento', 'senha', 'e_admin', 'criado_em', 
                    'atualizado_em')


