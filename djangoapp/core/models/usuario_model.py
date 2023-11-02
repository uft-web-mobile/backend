from django.db import models


class Usuario(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email", null=False)
    username = models.CharField(unique=True, verbose_name="Email", null=False)
    primeiro_nome = models.CharField(max_length=30, verbose_name="Primeiro Nome", null=False)
    segundo_nome = models.CharField(max_length=30, verbose_name="Segundo Nome", null=False)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", null=False)
    senha = models.CharField(max_length=128, verbose_name="Senha", null=False)
    e_admin = models.BooleanField(default=False, verbose_name="E Administrador")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em", null=False)
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em", null=False)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.email
