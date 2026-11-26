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
from django.db import connection
from django.http import HttpResponse
from django.urls import include, path, re_path
from django.conf import settings
from django.views.static import serve


def health_check(request):
    """Rota leve para monitores de uptime (ex.: UptimeRobot) manterem o Render e o Supabase ativos."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
    except Exception:
        pass
    return HttpResponse("ok", content_type="text/plain")


urlpatterns = [
    # Verificação de saúde / keep-alive
    path("health/", health_check, name="health"),

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

# Servir arquivos de mídia (fotos enviadas) pelo próprio Django.
# Só é usado com armazenamento local; com armazenamento externo (S3) as fotos
# são servidas direto pelo provedor.
if not getattr(settings, "USA_ARMAZENAMENTO_EXTERNO", False):
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ]
