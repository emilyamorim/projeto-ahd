"""
URLs do app de conteúdo.

Por enquanto vazio — as rotas serão adicionadas
quando as views do backend forem implementadas.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("minha-area/relatos/", views.meus_relatos_view, name="meus_relatos"),
]