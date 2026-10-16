from django import forms
from .models import Usuario, AlunaPerfil, Eixo

class CadastroAlunaForm(forms.ModelForm):
    # Campos que vão direto para Usuario
    first_name = forms.CharField(max_length=50, required=True, label="Nome")
    last_name = forms.CharField(max_length=50, required=True, label="Sobrenome")
    email = forms.EmailField(required=True, label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Senha")
    
    # Campos de AlunaPerfil
    data_nascimento = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data de Nascimento"
    )
    cidade = forms.CharField(max_length=100, required=False, label="Cidade")
    ano_ingresso = forms.IntegerField(required=False, label="Ano de Ingresso no Projeto")
    eixos = forms.ModelMultipleChoiceField(
        queryset=Eixo.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Eixos de Atuação"
    )

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'cidade']
        labels = {
            'username': 'Nome de Usuário (login)'
        }

    def save(self, commit=True):
        # Salva o Usuario
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.tipo = 'aluna'
        if commit:
            user.save()
            
            # Cria o AlunaPerfil automaticamente com status Pendente
            perfil = AlunaPerfil.objects.create(
                usuario=user,
                data_nascimento=self.cleaned_data.get('data_nascimento'),
                ano_ingresso=self.cleaned_data.get('ano_ingresso'),
                is_aprovada=False
            )
            # Salva a relação ManyToMany (Eixos)
            if self.cleaned_data.get('eixos'):
                perfil.eixos.set(self.cleaned_data['eixos'])

        return user
