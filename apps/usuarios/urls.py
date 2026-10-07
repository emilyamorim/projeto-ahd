"""
URLs do app de usuários.

Define as rotas para todas as 19 páginas do site,
organizadas por nível de acesso.
"""

from django.urls import path
from django.views.generic import TemplateView
from apps.galeria import views as galeria_views
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

    # L03 — Enviar fotos para os álbuns do projeto
    path(
        "minha-area/fotos/",
        galeria_views.minhas_fotos,
        name="minhas_fotos",
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
        TemplateView.as_view(template_name="publico/sobre.html"),
        name="sobre",
    ),

    # P06 — Perfil público de uma aluna específica
    # <int:pk> é o número de identificação da aluna na URL
    # Exemplo: /aluna/5/ mostra o perfil da aluna com id 5
    path(
        "aluna/<int:pk>/",
        TemplateView.as_view(template_name="publico/perfil_aluna.html"),
        name="perfil_aluna",
    ),

    # P07 — Perfil público de um professor
    path(
        "professor/<int:pk>/",
        TemplateView.as_view(template_name="publico/perfil_professor.html"),
        name="perfil_professor",
    ),

    # ----------------------------------------------------------
    # AUTENTICAÇÃO (login, cadastro, senha)
    # ----------------------------------------------------------

    # A01 — Formulário de cadastro em 3 passos
    path(
        "cadastro/",
        TemplateView.as_view(template_name="auth/cadastro.html"),
        name="cadastro",
    ),

    # A02 — Página de login
    path(
        "login/",
        TemplateView.as_view(template_name="auth/login.html"),
        name="login",
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
        TemplateView.as_view(template_name="aluna/meu_perfil.html"),
        name="meu_perfil",
    ),

    # L02 — Publicar, editar e excluir relatos
    path(
        "minha-area/relatos/",
        TemplateView.as_view(template_name="aluna/meus_relatos.html"),
        name="meus_relatos",
    ),

    # L03 — Enviar fotos para os álbuns do projeto
    path(
        "minha-area/fotos/",
        TemplateView.as_view(template_name="aluna/minhas_fotos.html"),
        name="minhas_fotos",
    ),

    # ----------------------------------------------------------
    # PAINEL DO PROFESSOR (apenas para professores logados)
    # ----------------------------------------------------------

    # G01 — Visão geral: stats, pendentes e alunas sem atividade
    path(
        "painel/",
        TemplateView.as_view(template_name="painel/dashboard.html"),
        name="painel",
    ),

    # G02 — Lista e gerenciamento de todas as alunas
    path(
        "painel/alunas/",
        TemplateView.as_view(template_name="painel/gerenciar_alunas.html"),
        name="gerenciar_alunas",
    ),

    # G03 — Gerenciamento de álbuns e fotos
    path(
        "painel/fotos/",
        TemplateView.as_view(template_name="painel/gerenciar_fotos.html"),
        name="gerenciar_fotos",
    ),

    # G04 — Criar e editar notícias do projeto
    path(
        "painel/noticias/",
        TemplateView.as_view(template_name="painel/publicar_noticia.html"),
        name="publicar_noticia",
    ),

    # ----------------------------------------------------------
    # ÁREA DO ADMIN (apenas para administradores)
    # ----------------------------------------------------------

    # AD01 — Fila de cadastros aguardando aprovação
    path(
        "painel/cadastros/",
        TemplateView.as_view(template_name="painel/aprovar_cadastros.html"),
        name="aprovar_cadastros",
    ),

    # AD02 — Criar e editar contas de professores e admins
    path(
        "painel/usuarios/",
        TemplateView.as_view(template_name="painel/gerenciar_usuarios.html"),
        name="gerenciar_usuarios",
    ),
]