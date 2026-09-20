from django.urls import path

from . import views

urlpatterns = [
    path("minha-area/fotos/enviar/", views.enviar_foto, name="enviar_foto"),
    path("minha-area/fotos/excluir/<int:foto_id>/", views.excluir_foto, name="excluir_foto"),
]