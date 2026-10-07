# 🎨 Guia Prático: Como Criar Novas Telas no Projeto AHD

Bem-vinda ao projeto **Ampliando Horizontes Digitais (AHD)**! 
Este guia foi feito especialmente para você que está assumindo a criação de novas telas. Nós já deixamos a "casa arrumada" para facilitar a sua vida!

---

## 1. Onde as telas ficam guardadas?
Todas as telas do nosso site (arquivos HTML) ficam dentro da pasta `templates/`. 
- **Páginas abertas ao público:** Ficam na pasta `templates/publico/` (ex: home, notícias, sobre).
- **Páginas de login e cadastro:** Ficam na pasta `templates/auth/`.

## 2. A "Mágica" do Cabeçalho e Rodapé
Você **não precisa** refazer o menu lá de cima nem o rodapé preto com as logomarcas em toda página nova. Nós usamos um recurso do Django que "herda" essas partes automaticamente.

Para criar uma página nova, crie um arquivo HTML (ex: `minha_tela.html`) e **sempre comece o arquivo colando isso aqui**:

```html
{% extends "base.html" %}
{% load static %}

{% block title %}Nome da sua Página - Ampliando Horizontes Digitais{% endblock %}

{% block content %}
<!-- TODO O SEU CONTEÚDO (TEXTOS, BOTÕES, IMAGENS) ENTRA AQUI DENTRO -->
{% endblock %}
```

## 3. Como usar as Nossas Cores (Design System)
Nós não usamos cores aleatórias. No nosso arquivo CSS, já deixamos as cores oficiais salvas como variáveis para garantir que o site fique chique e padronizado:
- Rosa oficial: `var(--rosa)`
- Azul oficial: `var(--azul)`
- Roxo escuro: `var(--roxo)`
- Fundo padrão: `var(--fundo)`

**Exemplo de como usar no CSS:**
```css
.meu-titulo {
    color: var(--rosa);
    background-color: var(--fundo);
}
```

## 4. Como usar nossos Botões prontos
Se você precisar criar um botão, não precisa inventar do zero. Use as "classes" (nomes) que já criamos. Basta colocar essas classes na sua tag de botão ou link (`<a>`):

- **Botão Sólido Rosa (Principal):** `class="btn-wizard-primary"`
- **Botão Transparente com Borda (Secundário):** `class="btn-wizard-outline"` ou `class="btn-outline"`

**Exemplo:**
```html
<button class="btn-wizard-primary">Salvar Perfil</button>
```

## 5. Passo a Passo Prático para Criar uma Tela Nova

Siga esta receitinha de bolo toda vez que for criar uma tela nova:

1. **Crie o Arquivo:** Vá na pasta `templates/` e crie o seu arquivo (ex: `recuperar_senha.html`). Cole a "mágica" do passo 2 lá dentro.
2. **Crie a Rota:** O site precisa saber que essa tela existe. Peça ajuda a quem cuida do "Backend", ou vá no arquivo `apps/usuarios/urls.py` (se for tela de usuário) e crie um caminho para ela.
3. **Estilize (CSS):** Vá na pasta `static/css/` e coloque suas regras visuais. Se for tela de login/cadastro, pode usar o `auth.css` que já tem os cartões bonitões centralizados.
4. **Ligue o Servidor:** Abra o terminal (tela preta) e digite `python manage.py runserver`.
5. **Veja a Mágica:** Abra o navegador e acesse `http://localhost:8000/sua-rota/`.

---
> **Dica de Ouro:** Dê uma olhada no arquivo `templates/auth/login.html`. Ele é um excelente exemplo de como nós juntamos o HTML com as nossas classes CSS oficiais. Você pode até copiar o código dele, colar na sua página nova e ir apagando e mudando o que precisar! Bom trabalho! 🚀

## 🎯 Suas Primeiras Missões (Tarefas Práticas)

Aqui estão as instruções detalhadas para as duas páginas que você recebeu como tarefa:

### Missão 1: Tela "Redefinir senha"
Esta tela é para quando a usuária esqueceu a senha. Ela pertence à área de fora do site (pública).

1. **Arquivo:** Crie o arquivo `templates/auth/redefinir_senha.html`.
2. **Base:** No topo do arquivo, cole a herança da base e o CSS oficial:
   ```html
   {% extends "base.html" %}
   {% load static %}
   
   {% block extra_css %}
   <link rel="stylesheet" href="{% static 'css/auth.css' %}?v=7">
   {% endblock %}
   ```
3. **A Estrutura Visual:** Queremos usar aquele "cartão" branco centralizado na tela. Coloque todo o seu código dentro das "caixas" (divs) chamadas `<div class="auth-container">` e `<div class="auth-card">`. 
   > **Super Dica:** Copie todo o código da tela `login.html`, cole na sua tela nova, e apague apenas o campo de Senha e as informações extras! 
4. **Componentes:** Use apenas o `<input type="email">` e mude o texto do botão para "Enviar link de redefinição" (`class="btn-wizard-primary"`).

### Missão 2: Tela "Meus Relatos" (Dashboard)
Esta tela fica *dentro* da área restrita (o painel da aluna). Ela tem aquele menu lateral com foto e informações que deve ficar fixo.

1. **Arquivo:** Crie o arquivo `templates/aluna/meus_relatos.html`.
2. **A Nova "Base":** Aqui está o pulo do gato! Em vez de usar a base normal do site, você vai usar a base especial do Dashboard que criamos para essa área. Comece o arquivo com:
   ```html
   {% extends "aluna/base_aluna.html" %}
   ```
3. **Pintando o Menu de Rosa:** Para que o botão "Meus Relatos" fique ativado (aceso) no menu da lateral, adicione esta linha mágica:
   ```html
   {% block nav_relatos %}active{% endblock %}
   ```
4. **Onde colocar o seu código:** Todo o seu HTML (a caixa de texto de relato, a lista, os botões) NÃO fica solto. Ele deve ficar dentro deste bloco para "encaixar" perfeitamente no lado direito da tela:
   ```html
   {% block dashboard_content %}
   <!-- Todo o seu código dos relatos entra aqui dentro! -->
   {% endblock %}
   ```
5. **Dicas de CSS Prontas:**
   - Para criar a linha divisória com o texto "Novo relato", você pode copiar o cabeçalho que usamos na tela "Meu Perfil": `<div class="content-header"> <h3>Novo relato</h3> </div>`.
   - Para os pequenos botões brancos de Editar/Excluir, use a classe `<button class="btn-sm-outline">`.
