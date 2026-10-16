from django.db import models
from django.conf import settings

class Noticia(models.Model):
    CATEGORIAS = (
        ('eventos', 'Eventos'),
        ('olimpiadas', 'Olimpíadas'),
        ('avisos', 'Avisos'),
    )
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='eventos')
    imagem_capa = models.ImageField(upload_to='noticias/capas/', blank=True, null=True)
    conteudo = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='noticias')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Relato(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='relatos')
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return f"Relato de {self.autor} em {self.criado_em.strftime('%d/%m/%Y')}"
