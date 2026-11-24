from django.urls import path

from . import views

urlpatterns = [
    path("painel/fotos/moderar/<int:foto_id>/", views.moderar_foto, name="moderar_foto"),
    path("fotos/", views.fotos_publicas_view, name="fotos"),
    path("minha-area/fotos/", views.minhas_fotos, name="minhas_fotos"),
    path("minha-area/fotos/enviar/", views.enviar_foto, name="enviar_foto"),
    path("minha-area/fotos/excluir/<int:foto_id>/", views.excluir_foto, name="excluir_foto"),
]