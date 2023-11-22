from django.contrib import admin

from .models import Usuario, Desafio, Resultado

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'primeiro_nome', 'username', 'segundo_nome', 
                    'data_nascimento', 'senha', 'e_admin', 'criado_em', 
                    'atualizado_em')

@admin.register(Desafio)
class DesafioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'dificuldade', 'visivel')
    
@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('name', 'entrada', 'saida', 'visivel')
    
    def name(self, obj):
        return 'teste'