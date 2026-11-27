import logging

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import UploadFotoForm
from .models import Album, Foto

logger = logging.getLogger(__name__)

TAMANHO_MAXIMO = 5 * 1024 * 1024  
TIPOS_PERMITIDOS = ("image/jpeg", "image/png", "image/webp")


@login_required
def minhas_fotos(request):
    if request.user.esta_aguardando_aprovacao():
        logout(request)
        messages.warning(request, 'Seu cadastro ainda está em análise pela coordenação. Aguarde a aprovação para acessar sua conta.')
        return redirect('login')

    fotos = Foto.objects.filter(usuario=request.user)
    form = UploadFotoForm(usuario=request.user)
    contexto = {
        "fotos": fotos,
        "form": form,
        "total_fotos": fotos.count(),
    }
    return render(request, "aluna/minhas_fotos.html", contexto)


@login_required
@require_POST
def enviar_foto(request):
    if request.user.esta_aguardando_aprovacao():
        logout(request)
        messages.warning(request, 'Seu cadastro ainda está em análise pela coordenação. Aguarde a aprovação para acessar sua conta.')
        return redirect('login')

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
            # Fotos da coordenação já entram publicadas; as das alunas esperam aprovação
            aprovada=request.user.is_superuser or request.user.tipo in ("professor", "admin"),
        )
        enviados += 1

    if enviados:
        if request.user.is_superuser or request.user.tipo in ("professor", "admin"):
            messages.success(request, f"{enviados} foto(s) publicada(s) com sucesso.")
        else:
            messages.success(request, f"{enviados} foto(s) enviada(s)! Elas aparecerão na galeria após a aprovação da coordenação.")
    return redirect("minhas_fotos")


@login_required
@require_POST
def excluir_foto(request, foto_id):
    
    foto = get_object_or_404(Foto, id=foto_id, usuario=request.user)
    foto.imagem.delete(save=False)
    foto.delete()
    messages.success(request, "Foto excluída.")
    return redirect("minhas_fotos")

def _coordenacao(user):
    return user.is_superuser or user.tipo in ('professor', 'admin')


@login_required
def gerenciar_fotos_view(request):
    if not _coordenacao(request.user):
        messages.error(request, 'Acesso restrito à coordenação.')
        return redirect('home')

    albuns = Album.objects.all().prefetch_related('fotos')
    fotos_pendentes = Foto.objects.filter(aprovada=False, recusada=False).select_related('usuario', 'album').order_by('-enviado_em')

    context = {
        'albuns': albuns,
        'fotos_pendentes': fotos_pendentes,
    }
    return render(request, 'painel/gerenciar_fotos.html', context)


@login_required
@require_POST
def moderar_foto(request, foto_id):
    """Aprova (publica) ou recusa (com justificativa e e-mail) uma foto enviada por aluna."""
    if not _coordenacao(request.user):
        messages.error(request, 'Acesso restrito à coordenação.')
        return redirect('home')
    foto = get_object_or_404(Foto, id=foto_id)
    if request.POST.get('acao') == 'aprovar':
        foto.aprovada = True
        foto.recusada = False
        foto.motivo_recusa = ''
        foto.save(update_fields=['aprovada', 'recusada', 'motivo_recusa'])
        messages.success(request, 'Foto aprovada e publicada na galeria.')
    elif request.POST.get('acao') == 'recusar':
        motivo = request.POST.get('motivo', '').strip()
        foto.aprovada = False
        foto.recusada = True
        foto.motivo_recusa = motivo
        foto.save(update_fields=['aprovada', 'recusada', 'motivo_recusa'])
        if foto.usuario.email:
            fotos_url = request.build_absolute_uri(reverse('minhas_fotos'))
            corpo = render_to_string('auth/email_foto_recusada.txt', {
                'nome': foto.usuario.first_name or foto.usuario.username,
                'nome_foto': foto.nome_original or 'Foto enviada',
                'motivo': motivo,
                'fotos_url': fotos_url,
            })
            try:
                send_mail(
                    subject='Aviso sobre a foto enviada — Ampliando Horizontes Digitais',
                    message=corpo,
                    from_email=None,
                    recipient_list=[foto.usuario.email],
                    fail_silently=False,
                )
                messages.success(request, 'Foto recusada e aluna notificada por e-mail.')
            except Exception:
                logger.error('Erro ao enviar e-mail de recusa de foto para %s', foto.usuario.email, exc_info=True)
                messages.success(request, 'Foto recusada com justificativa registrada.')
                messages.warning(request, 'Não foi possível enviar o e-mail de aviso automático.')
        else:
            messages.success(request, 'Foto recusada com justificativa registrada.')
    return redirect('gerenciar_fotos')


def fotos_publicas_view(request):
    """Galeria pública: somente fotos aprovadas, agrupadas por álbum. Aceita busca ?q= e ordem ?ordem=antigas."""
    busca = request.GET.get('q', '').strip()
    ordem = request.GET.get('ordem', 'recentes')
    fotos = Foto.objects.filter(aprovada=True)
    if busca:
        from django.db.models import Q
        fotos = fotos.filter(Q(nome_original__icontains=busca) | Q(album__nome__icontains=busca))
    fotos = fotos.order_by('enviado_em' if ordem == 'antigas' else '-enviado_em')

    grupos = {}
    soltas = []
    for f in fotos.select_related('album', 'usuario'):
        if f.album_id:
            grupos.setdefault(f.album, []).append(f)
        else:
            soltas.append(f)
    albuns = [{'album': a, 'fotos': fs} for a, fs in grupos.items()]
    return render(request, 'publico/fotos.html', {
        'albuns': albuns, 'soltas': soltas, 'busca': busca, 'ordem': ordem,
    })
