from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, primeiro_nome, segundo_nome, data_nascimento, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo de e-mail deve ser definido')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            primeiro_nome=primeiro_nome,
            segundo_nome=segundo_nome,
            data_nascimento=data_nascimento,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, primeiro_nome, segundo_nome, data_nascimento, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, primeiro_nome, segundo_nome, data_nascimento, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Email", null=False)
    username = models.CharField(unique=True, verbose_name="Username", null=False)
    password = models.CharField(max_length=128, verbose_name="password", null=False)
    primeiro_nome = models.CharField(max_length=30, verbose_name="Primeiro Nome", null=False)
    segundo_nome = models.CharField(max_length=30, verbose_name="Segundo Nome", null=False)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", null=False)
    is_active = models.BooleanField(default=True)
    e_admin = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em", null=False)
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em", null=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'primeiro_nome', 'segundo_nome', 'data_nascimento']

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.email
