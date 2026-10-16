"""
URLs do app de usuários.

Define as rotas para todas as 19 páginas do site,
organizadas por nível de acesso.
"""

from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views
from apps.galeria.views import gerenciar_fotos_view
from apps.conteudo.views import publicar_noticia_view

urlpatterns = [

    # ----------------------------------------------------------
    # PÁGINAS PÚBLICAS (qualquer visitante pode acessar)
    # ----------------------------------------------------------

    # P01 — Página inicial do site
    path(
        "",
        TemplateView.as_view(template_name="publico/home.html"),
        name="home",
    ),

    # P02 — Lista de todas as alunas do projeto
    path(
        "historico/",
        TemplateView.as_view(template_name="publico/historico.html"),
        name="historico",
    ),

      # P03 — Galeria de fotos do projeto
    path(
        "fotos/",
        TemplateView.as_view(template_name="publico/fotos.html"),
        name="fotos",
    ),


    # P04 — Notícias e novidades do projeto
    path(
        "noticias/",
        TemplateView.as_view(template_name="publico/noticias.html"),
        name="noticias",
    ),

    # P05 — Informações sobre o projeto
    path(
        "sobre/",
        views.sobre_view,
        name="sobre",
    ),

    # P06 — Perfil público de uma aluna específica
    # <int:pk> é o número de identificação da aluna na URL
    # Exemplo: /aluna/5/ mostra o perfil da aluna com id 5
    path(
        "aluna/<int:pk>/",
        views.perfil_aluna_view,
        name="perfil_aluna",
    ),

    # P07 — Perfil público de um professor
    path(
        "professor/<int:pk>/",
        views.perfil_professor_view,
        name="perfil_professor",
    ),

    # ----------------------------------------------------------
    # AUTENTICAÇÃO (login, cadastro, senha)
    # ----------------------------------------------------------

    # A01 — Formulário de cadastro em 3 passos
    path(
        "cadastro/",
        views.cadastro_view,
        name="cadastro",
    ),

    # A02 — Página de login
    path(
        "login/",
        views.CustomLoginView.as_view(),
        name="login",
    ),

    # A02B — Logout
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    # A03 — Página para redefinir a senha por e-mail
    path(
        "redefinir-senha/",
        TemplateView.as_view(template_name="auth/redefinir_senha.html"),
        name="redefinir_senha",
    ),

    # ----------------------------------------------------------
    # ÁREA DA ALUNA (apenas para alunas logadas)
    # ----------------------------------------------------------

    # L01 — Dados pessoais e foto de perfil
    path(
        "minha-area/perfil/",
        views.meu_perfil_aluna_view,
        name="meu_perfil",
    ),

    # ----------------------------------------------------------
    # PAINEL DO PROFESSOR (apenas para professores logados)
    # ----------------------------------------------------------

    # G01 — Visão geral: stats, pendentes e alunas sem atividade
    path(
        "painel/",
        views.dashboard_view,
        name="painel",
    ),

    # G01B — Editar o próprio perfil (nome, cidade, foto)
    path(
        "painel/meu-perfil/",
        views.editar_perfil_professor_view,
        name="editar_perfil_professor",
    ),

    # G02 — Lista e gerenciamento de todas as alunas
    path(
        "painel/alunas/",
        views.gerenciar_alunas_view,
        name="gerenciar_alunas",
    ),

    # G03 — Gerenciamento de álbuns e fotos
    path(
        "painel/fotos/",
        gerenciar_fotos_view,
        name="gerenciar_fotos",
    ),

    # G04 — Criar e editar notícias do projeto
    path(
        "painel/noticias/",
        publicar_noticia_view,
        name="publicar_noticia",
    ),

    # ----------------------------------------------------------
    # ÁREA DO ADMIN (apenas para administradores)
    # ----------------------------------------------------------

    # AD01 — Fila de cadastros aguardando aprovação
    path(
        "painel/cadastros/",
        views.aprovar_cadastros_view,
        name="aprovar_cadastros",
    ),

    # AD02 — Criar e editar contas de professores e admins
    path(
        "painel/usuarios/",
        views.gerenciar_usuarios_view,
        name="gerenciar_usuarios",
    ),
]