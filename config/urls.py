"""
URLs principais do projeto Ampliando Horizontes Digitais.

Este arquivo conecta os endereços (URLs) do site
com os apps responsáveis por cada parte.

Como funciona:
- Quando alguém acessa uma URL, o Django verifica esta lista
  e redireciona para o app correto.
- Cada app tem seu próprio arquivo urls.py com as rotas detalhadas.
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Painel de administração padrão do Django
    # Acesso: http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),

    # URLs do app de usuários
    # (home, histórico, login, cadastro, perfil, painel, etc.)
    path("", include("apps.usuarios.urls")),

    # URLs do app de conteúdo
    # (relatos, notícias, atividades)
    path("", include("apps.conteudo.urls")),

    # URLs do app de galeria
    # (fotos e álbuns)
    path("", include("apps.galeria.urls")),
]

# Em desenvolvimento, o Django serve os arquivos de mídia
# (fotos enviadas pelos usuários) diretamente.
# Em produção, isso é feito pelo servidor web (nginx, etc.)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )