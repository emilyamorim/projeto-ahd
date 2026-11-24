"""
URLs do app de conteúdo.

Por enquanto vazio — as rotas serão adicionadas
quando as views do backend forem implementadas.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("noticias/", views.noticias_publicas_view, name="noticias"),
    path("noticias/<int:pk>/", views.noticia_detalhe_view, name="noticia_detalhe"),
    path("minha-area/relatos/", views.meus_relatos_view, name="meus_relatos"),
]