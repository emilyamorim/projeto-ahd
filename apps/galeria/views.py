from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import UploadFotoForm
from .models import Album, Foto

TAMANHO_MAXIMO = 5 * 1024 * 1024  
TIPOS_PERMITIDOS = ("image/jpeg", "image/png", "image/webp")


@login_required
def minhas_fotos(request):
    
    fotos = Foto.objects.filter(usuario=request.user)
    form = UploadFotoForm(usuario=request.user)
    contexto = {
        "fotos": fotos,
        "form": form,
        "total_fotos": fotos.count(),
    }
    return render(request, "galeria/minhas_fotos.html", contexto)


@login_required
@require_POST
def enviar_foto(request):
    
    album = None
    album_id = request.POST.get("album")
    if album_id:
        album = get_object_or_404(Album, id=album_id, usuario=request.user)

    arquivos = request.FILES.getlist("imagens")
    if not arquivos:
        messages.error(request, "Selecione ao menos uma foto.")
        return redirect("minhas_fotos")

    enviados = 0
    for arquivo in arquivos:
        if arquivo.content_type not in TIPOS_PERMITIDOS:
            messages.warning(request, f'"{arquivo.name}" foi ignorada: formato não permitido.')
            continue
        if arquivo.size > TAMANHO_MAXIMO:
            messages.warning(request, f'"{arquivo.name}" foi ignorada: maior que 5MB.')
            continue

        Foto.objects.create(
            usuario=request.user,
            album=album,
            imagem=arquivo,
            nome_original=arquivo.name,
        )
        enviados += 1

    if enviados:
        messages.success(request, f"{enviados} foto(s) enviada(s) com sucesso.")
    return redirect("minhas_fotos")


@login_required
@require_POST
def excluir_foto(request, foto_id):
    
    foto = get_object_or_404(Foto, id=foto_id, usuario=request.user)
    foto.imagem.delete(save=False)
    foto.delete()
    messages.success(request, "Foto excluída.")
    return redirect("minhas_fotos")