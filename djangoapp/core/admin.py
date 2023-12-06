from django.contrib import admin

from .models import Usuario, Desafio, Resultado, UserDesafio

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
@admin.register(Desafio)
class DesafioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'dificuldade', 'visivel')
    
@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('desafio', 'entrada', 'saida', 'visivel')
    
    def desafio(self, obj):
        return obj.desafio
    
@admin.register(UserDesafio)
class UserDesafioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'desafios')
    