from django.conf import settings
from django.db import models

class Album(models.Model):
    nome =models.CharField(max_length=150)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="albuns",

    )
    def __str__(self):
        return self.nome

class Foto(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="fotos",
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="fotos",
        null=True,
        blank=True,
    )
    imagem =models.ImageField(upload_to="fotos/%y/%m/")
    nome_original = models.CharField(max_length=255, blank=True)
    enviado_em = models.DateTimeField(auto_now_add=True)
    aprovada = models.BooleanField(default=False, help_text="Só fotos aprovadas aparecem na galeria pública.")
    recusada = models.BooleanField(default=False, help_text="Foto recusada pela coordenação.")
    motivo_recusa = models.TextField(blank=True, default="", help_text="Justificativa exibida para a aluna quando a foto é recusada.")

    class Meta:
        ordering =["-enviado_em"]
    def __str__(self):
        return self.nome_original or self.imagem.name

