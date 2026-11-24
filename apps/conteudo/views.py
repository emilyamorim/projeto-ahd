from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Noticia, Relato

@login_required
def publicar_noticia_view(request):
    if request.user.tipo not in ['professor', 'admin']:
        messages.error(request, 'Acesso restrito à coordenação.')
        return redirect('home')

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        data = request.POST.get('data')
        categoria = request.POST.get('categoria')
        conteudo = request.POST.get('conteudo')
        imagem_capa = request.FILES.get('imagem_capa')

        if titulo and data and conteudo:
            Noticia.objects.create(
                titulo=titulo,
                data=data,
                categoria=categoria,
                conteudo=conteudo,
                imagem_capa=imagem_capa,
                autor=request.user
            )
            messages.success(request, 'Notícia publicada com sucesso!')
            return redirect('publicar_noticia')

    return render(request, 'painel/publicar_noticia.html')

@login_required
def meus_relatos_view(request):
    if request.user.tipo != 'aluna':
        messages.error(request, 'Página restrita para alunas.')
        return redirect('home')

    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        if conteudo:
            Relato.objects.create(
                autor=request.user,
                conteudo=conteudo
            )
            messages.success(request, 'Seu relato foi enviado e publicado com sucesso!')
            return redirect('meus_relatos')

    relatos = Relato.objects.filter(autor=request.user).order_by('-criado_em')
    context = {
        'relatos': relatos
    }
    return render(request, 'aluna/meus_relatos.html', context)



def noticias_publicas_view(request):
    """Lista pública de notícias (mais recentes primeiro), com paginação."""
    categoria = request.GET.get('categoria', '')
    qs = Noticia.objects.select_related('autor').order_by('-data', '-criado_em')
    if categoria in dict(Noticia.CATEGORIAS):
        qs = qs.filter(categoria=categoria)
    page = Paginator(qs, 9).get_page(request.GET.get('pagina'))
    return render(request, 'publico/noticias.html', {
        'page': page,
        'categorias': Noticia.CATEGORIAS,
        'categoria_atual': categoria,
    })


def noticia_detalhe_view(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'publico/noticia_detalhe.html', {'noticia': noticia})
