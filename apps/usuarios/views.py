from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db import transaction
from django.contrib.auth.views import LoginView
from django.urls import reverse
from .models import AlunaPerfil, Eixo

Usuario = get_user_model()


# Equipe exibida na aba "Nosso time" da página Sobre (ordem de exibição).
# Se existir uma conta com o mesmo e-mail, a foto e o link do perfil vêm do banco.
EQUIPE_PROJETO = [
    ("Tatiana Amaral Sorrentino", "Coordenadora do projeto", "tatiana.sorrentino@ifrn.edu.br"),
    ("Helber Wagner da Silva", "Professor coordenador", "helber.silva@ifrn.edu.br"),
    ("Eberton Marinho", "Professor coordenador", "eberton.marinho@ifrn.edu.br"),
    ("Creusa Ribeiro", "Professora coordenadora", "creusa.ribeiro@ifrn.edu.br"),
    ("Ana Barros", "Professora colaboradora", "ana.barros@ifrn.edu.br"),
    ("Bruno Vitorino", "Professor colaborador", "bruno.vitorino@ifrn.edu.br"),
]


def sobre_view(request):
    emails = [email for _, _, email in EQUIPE_PROJETO]
    contas = {
        u.email.lower(): u
        for u in Usuario.objects.filter(email__in=emails, tipo__in=['professor', 'admin'])
    }
    equipe = []
    for nome, cargo, email in EQUIPE_PROJETO:
        conta = contas.get(email.lower())
        equipe.append({
            'nome': (conta.get_full_name() if conta else '') or nome,
            'cargo': cargo,
            'email': email,
            'conta': conta,
            'iniciais': ''.join(p[0] for p in nome.split()[:2]).upper(),
        })
    return render(request, 'publico/sobre.html', {'equipe': equipe})


class CustomLoginView(LoginView):
    """Login que redireciona cada usuário para a sua área conforme o tipo."""
    template_name = "auth/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        # Respeita o ?next= quando a pessoa tentou acessar uma página protegida
        next_url = self.get_redirect_url()
        if next_url:
            return next_url
        user = self.request.user
        tipo = getattr(user, "tipo", None)
        # Superusuário primeiro: o campo tipo tem 'aluna' como padrão
        if user.is_superuser or tipo in ("professor", "admin"):
            return reverse("painel")
        if tipo == "aluna":
            return reverse("meu_perfil")
        return reverse("home")

def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        # Captura os dados do Wizard (nomes usados no HTML)
        nome_completo = request.POST.get('nome', '').strip()
        data_nascimento = request.POST.get('data_nascimento')
        cidade = request.POST.get('cidade')
        escola = request.POST.get('escola')
        tipo_participacao = request.POST.get('tipo_participacao') # 'bolsista' ou 'cursista'
        eixos_selecionados = request.POST.getlist('eixos') # Lista com IDs selecionados ('01', '02', etc.)
        
        email = request.POST.get('email', '').strip()
        confirm_email = request.POST.get('confirm_email', '').strip()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validações Básicas
        if email != confirm_email:
            messages.error(request, 'Os e-mails não conferem.')
            return render(request, 'auth/cadastro.html')
            
        if password != confirm_password:
            messages.error(request, 'As senhas não conferem.')
            return render(request, 'auth/cadastro.html')

        if Usuario.objects.filter(email=email).exists() or Usuario.objects.filter(username=email).exists():
            messages.error(request, 'Já existe um cadastro com este e-mail.')
            return render(request, 'auth/cadastro.html')

        # Divide o nome completo em first_name e last_name
        partes_nome = nome_completo.split(' ', 1)
        first_name = partes_nome[0]
        last_name = partes_nome[1] if len(partes_nome) > 1 else ''

        try:
            with transaction.atomic():
                # 1. Cria o Usuário base
                user = Usuario.objects.create_user(
                    username=email, # O login será o e-mail
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    tipo='aluna'
                )

                # 2. Cria o perfil conectado ao usuário
                perfil = AlunaPerfil.objects.create(
                    usuario=user,
                    data_nascimento=data_nascimento or None,
                    cidade=cidade,
                    escola=escola,
                    tipo_participacao=tipo_participacao or 'cursista',
                    is_aprovada=False
                )

                # 3. Associa os eixos (precisamos converter '01', '02' para IDs reais do banco,
                # ou criar no banco se não existirem). 
                # Como não temos os eixos cadastrados no DB ainda, vamos ignorar ou criar sob demanda.
                for eixo_str_id in eixos_selecionados:
                    # Aqui uma lógica simples: vamos criar o eixo com esse "nome" temporário 
                    # só para não quebrar. Depois cadastramos via Painel Admin.
                    eixo_obj, created = Eixo.objects.get_or_create(nome=f"Eixo {eixo_str_id}")
                    perfil.eixos.add(eixo_obj)

            messages.success(request, f'Cadastro realizado com sucesso, {first_name}! Sua conta ficará em análise pela coordenação.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Erro ao realizar o cadastro: {str(e)}')
            return render(request, 'auth/cadastro.html')

    # GET request
    return render(request, 'auth/cadastro.html')

def perfil_aluna_view(request, pk):
    aluna = get_object_or_404(Usuario, pk=pk, tipo='aluna')
    try:
        perfil = aluna.perfil_aluna
    except AlunaPerfil.DoesNotExist:
        perfil = None
        
    context = {
        'aluna': aluna,
        'perfil': perfil,
    }
    return render(request, 'publico/perfil_aluna.html', context)


@login_required
def aprovar_cadastros_view(request):
    if request.user.tipo == 'aluna':
        messages.error(request, 'Acesso restrito à coordenação.')
        return redirect('home')

    if request.method == 'POST':
        acao = request.POST.get('acao')
        perfil_id = request.POST.get('perfil_id')
        
        if acao and perfil_id:
            perfil = get_object_or_404(AlunaPerfil, id=perfil_id)
            
            if acao == 'aprovar':
                perfil.is_aprovada = True
                perfil.save()
                messages.success(request, f'Cadastro de {perfil.usuario.first_name} aprovado com sucesso!')
            elif acao == 'recusar':
                user = perfil.usuario
                user.delete()
                messages.success(request, 'Cadastro recusado e excluído do sistema.')
                
        return redirect('aprovar_cadastros')

    pendentes = AlunaPerfil.objects.filter(is_aprovada=False).order_by('-usuario__date_joined')
    
    return render(request, 'painel/aprovar_cadastros.html', {'pendentes': pendentes})


@login_required
def dashboard_view(request):
    if request.user.tipo not in ['professor', 'admin']:
        messages.error(request, 'Acesso restrito à coordenação.')
        return redirect('home')
        
    total_bolsistas = AlunaPerfil.objects.filter(is_aprovada=True, tipo_participacao='bolsista').count()
    total_cursistas = AlunaPerfil.objects.filter(is_aprovada=True, tipo_participacao='cursista').count()
    total_pendentes = AlunaPerfil.objects.filter(is_aprovada=False).count()
    total_relatos = 0 # Placeholder for future implementation
    
    pendentes_recentes = AlunaPerfil.objects.filter(is_aprovada=False).order_by('-usuario__date_joined')[:3]
    alunas_recentes = AlunaPerfil.objects.filter(is_aprovada=True).order_by('-usuario__date_joined')[:3]
    
    context = {
        'total_bolsistas': total_bolsistas,
        'total_cursistas': total_cursistas,
        'total_pendentes': total_pendentes,
        'total_relatos': total_relatos,
        'pendentes_recentes': pendentes_recentes,
        'alunas_recentes': alunas_recentes,
    }
    
    return render(request, 'painel/dashboard.html', context)

@login_required
def gerenciar_alunas_view(request):
    if request.user.tipo not in ['professor', 'admin']:
        messages.error(request, 'Acesso restrito à coordenação.')
        return redirect('home')
        
    alunas = AlunaPerfil.objects.filter(is_aprovada=True).order_by('usuario__first_name')
    return render(request, 'painel/gerenciar_alunas.html', {'alunas': alunas})

@login_required
def gerenciar_usuarios_view(request):
    if request.user.tipo != 'admin':
        messages.error(request, 'Acesso restrito aos administradores.')
        return redirect('home')
        
    usuarios = Usuario.objects.filter(tipo__in=['professor', 'admin']).order_by('first_name')
    return render(request, 'painel/gerenciar_usuarios.html', {'usuarios': usuarios})

@login_required
def meu_perfil_aluna_view(request):
    if request.user.tipo != 'aluna':
        messages.error(request, 'Página restrita para alunas.')
        return redirect('home')
        
    try:
        perfil = request.user.perfil_aluna
    except AlunaPerfil.DoesNotExist:
        perfil = None
        
    context = {
        'perfil': perfil
    }
    return render(request, 'aluna/meu_perfil.html', context)

def perfil_professor_view(request, pk):
    professor = get_object_or_404(Usuario, pk=pk, tipo__in=['professor', 'admin'])
    return render(request, 'publico/perfil_professor.html', {'professor': professor})


@login_required
def editar_perfil_professor_view(request):
    user = request.user
    if not (user.is_superuser or user.tipo in ['professor', 'admin']):
        messages.error(request, 'Acesso restrito à coordenação.')
        return redirect('home')

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        if not first_name:
            messages.error(request, 'O nome não pode ficar vazio.')
            return redirect('editar_perfil_professor')

        user.first_name = first_name
        user.last_name = request.POST.get('last_name', '').strip()
        user.cidade = request.POST.get('cidade', '').strip()

        foto = request.FILES.get('foto_perfil')
        if foto:
            if not foto.content_type.startswith('image/'):
                messages.error(request, 'Envie um arquivo de imagem (JPG, PNG ou WEBP).')
                return redirect('editar_perfil_professor')
            if foto.size > 5 * 1024 * 1024:
                messages.error(request, 'A foto deve ter no máximo 5 MB.')
                return redirect('editar_perfil_professor')
            if user.foto_perfil:
                user.foto_perfil.delete(save=False)
            user.foto_perfil = foto
        elif request.POST.get('remover_foto') == '1' and user.foto_perfil:
            user.foto_perfil.delete(save=False)
            user.foto_perfil = None

        user.save()
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('editar_perfil_professor')

    return render(request, 'painel/editar_perfil.html')
