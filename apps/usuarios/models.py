from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_CHOICES = (
        ('aluna', 'Aluna/Bolsista'),
        ('professor', 'Professor/Orientador'),
        ('admin', 'Administrador'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='aluna')
    foto_perfil = models.ImageField(upload_to='avatares/', blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True, verbose_name="Biografia / Apresentação")
    cargo = models.CharField(max_length=100, blank=True, default="Professor(a)")
    instituicao = models.CharField(max_length=150, blank=True, default="IFRN - Campus Canguaretama")
    link_lattes = models.URLField(max_length=255, blank=True, verbose_name="Currículo Lattes")
    link_linkedin = models.URLField(max_length=255, blank=True, verbose_name="LinkedIn")
    link_github = models.URLField(max_length=255, blank=True, verbose_name="GitHub")
    link_instagram = models.URLField(max_length=255, blank=True, verbose_name="Instagram")

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username


class Eixo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class AlunaPerfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_aluna')
    data_nascimento = models.DateField(null=True, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    escola = models.CharField(max_length=150, blank=True)
    TIPO_PARTICIPACAO_CHOICES = (
        ('bolsista', 'Bolsista'),
        ('cursista', 'Cursista'),
    )
    tipo_participacao = models.CharField(max_length=20, choices=TIPO_PARTICIPACAO_CHOICES, default='cursista')
    ano_ingresso = models.IntegerField(null=True, blank=True)
    eixos = models.ManyToManyField(Eixo, blank=True)
    is_aprovada = models.BooleanField(default=False)

    def __str__(self):
        return f"Perfil: {self.usuario.username}"
