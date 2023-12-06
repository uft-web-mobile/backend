from django.contrib import admin

from .models.usuario_model import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display =  (
        'email',
        'username',
        'password',
        'primeiro_nome',
        'segundo_nome',
        'data_nascimento',
        'is_active',
        'e_admin',
        'criado_em',
        'atualizado_em',
    )

