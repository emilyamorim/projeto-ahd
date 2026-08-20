# Ampliando Horizontes Digitais

Site do projeto de mentoria de meninas do IFRN Campus Canguaretama,
financiado pelo CNPq (Chamada Nº 31/2023).

---

## O que é esse projeto?

O **Ampliando Horizontes Digitais (AHD)** apoia meninas da região do
Litoral Sul Potiguar na área de tecnologia. Este repositório é o site
do projeto, onde as alunas podem ver seu histórico, enviar fotos e
deixar relatos. Os professores gerenciam as atividades e publicam
notícias.

---

## Tecnologias usadas

- **Python 3.10** — linguagem de programação
- **Django 4.2** — framework web
- **SQLite** — banco de dados (usado só no desenvolvimento local)
- **HTML, CSS e JavaScript** — frontend

---

## Como rodar o projeto no seu computador

### 1. Pré-requisitos

Antes de começar, você precisa ter instalado:
- Python 3.10 ou superior
- Git

Verifique se estão instalados:

```bash
python3 --version
git --version
```

### 2. Clone o repositório

```bash
git clone https://github.com/emilyamorim/projeto-ahd.git
cd projeto-ahd
```

### 3. Crie o ambiente virtual

O ambiente virtual isola as dependências do projeto.
Sempre ative-o antes de trabalhar.

```bash
# Criar
python3 -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate
```

Quando ativo, o terminal mostra `(venv)` no início da linha.

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Abra o `.env` e preencha a SECRET_KEY. Para gerar uma:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Cole o resultado no `.env`:

```
SECRET_KEY=cole-aqui-o-resultado
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 6. Rode as migrations

Migrations criam as tabelas no banco de dados.

```bash
python manage.py migrate
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000**

---

## Estrutura de pastas

```
projeto-ahd/
│
├── config/                  → Configurações do Django
│   ├── settings.py        → Configurações gerais
│   └── urls.py            → Rotas principais
│
├── apps/                  → Funcionalidades do site
│   ├── usuarios/          → Login, cadastro e perfis
│   ├── conteudo/          → Relatos, notícias e atividades
│   └── galeria/           → Fotos e álbuns
│
├── templates/             → Arquivos HTML das páginas
│   ├── base.html          → Template base (navbar e rodapé)
│   ├── publico/           → Páginas públicas
│   ├── auth/              → Login, cadastro e senha
│   ├── aluna/             → Área da aluna logada
│   └── painel/            → Painel do professor e admin
│
├── static/                → CSS, JavaScript e imagens
│   ├── css/style.css      → Estilo visual do site
│   ├── js/main.js         → Scripts do site
│   └── img/               → Logo e imagens
│
├── media/                 → Fotos enviadas pelos usuários
├── docs/                  → Documentação do projeto
├── .env.example           → Modelo das variáveis de ambiente
├── .gitignore             → Arquivos que o Git ignora
├── manage.py              → Comando principal do Django
├── requirements.txt       → Lista de dependências
└── README.md              → Este arquivo
```

---

## Páginas do site

| Código | Página | Quem acessa |
|---|---|---|
| P01 | Home | Todos |
| P02 | Histórico das alunas | Todos |
| P03 | Fotos | Todos |
| P04 | Notícias | Todos |
| P05 | Sobre | Todos |
| P06 | Perfil público da aluna | Todos |
| P07 | Perfil público do professor | Todos |
| A01 | Cadastro | Visitantes |
| A02 | Login | Visitantes |
| A03 | Redefinir senha | Visitantes |
| L01 | Meu perfil | Aluna logada |
| L02 | Meus relatos | Aluna logada |
| L03 | Minhas fotos | Aluna logada |
| G01 | Painel | Professor |
| G02 | Gerenciar alunas | Professor |
| G03 | Gerenciar fotos | Professor |
| G04 | Publicar notícia | Professor |
| AD01 | Aprovar cadastros | Admin |
| AD02 | Gerenciar usuários | Admin |

---

## Como trabalhar com Git

### Branches

- `main` → versão final, estável
- `develop` → onde juntamos o trabalho de todos
- `feature/nome-da-tarefa` → branch para cada tarefa

```bash
# Sempre parta do develop atualizado
git checkout develop
git pull origin develop

# Crie sua branch para a tarefa
git checkout -b feature/tela-home

# Depois de terminar, suba para o GitHub
git push origin feature/tela-home
# E abra um Pull Request para develop no GitHub
```

### Mensagens de commit

```bash
git commit -m "feat: adiciona página de histórico das alunas"
git commit -m "fix: corrige erro no formulário de cadastro"
git commit -m "style: ajusta cores da navbar"
git commit -m "docs: atualiza o README"
```

Prefixos:
- `feat:` → algo novo foi adicionado
- `fix:` → um erro foi corrigido
- `style:` → mudança visual
- `docs:` → documentação atualizada

---

## Time

| Nome | Papel |
|---|---|
| Tatiana Amaral Sorrentino | Coordenadora |
| Helber Wagner da Silva | Professor coordenador |
| Eberton Marinho | Professor coordenador |
| Creusa Ribeiro | Professora coordenadora |
| Ana Barros | Professora colaboradora |
| Bruno Vitorino | Professor colaborador |
| Emily Amorim do Nascimento | Desenvolvedora (bolsista) |

---

Dúvidas? Fale com a equipe: **ampliandohorizontesdigitais.cang@ifrn.edu.br**