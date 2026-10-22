# 🚀 Guia de Deploy no PythonAnywhere — Projeto AHD

Este guia explica passo a passo como colocar o site do **Ampliando Horizontes Digitais (AHD)** no ar gratuitamente no **PythonAnywhere**.

---

## 1. Criar a Conta no PythonAnywhere

1. Acesse: [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Clique em **Pricing & signup** e escolha a opção **Create a Beginner account** (Gratuita).
3. Escolha seu nome de usuário (exemplo: `projetoahed` ou `emilyamorim`).
   > 💡 **Atenção:** O endereço do site será `https://seunome.pythonanywhere.com`.

---

## 2. Clonar o Projeto e Preparar o Ambiente

1. No painel do PythonAnywhere, vá na aba **Consoles** e clique em **Bash**.
2. No terminal preto que abrir, execute os comandos abaixo (substitua pelo seu repositório se necessário):

```bash
# 1. Clonar o repositório
git clone https://github.com/emilyamorim/projeto-ahd.git

# 2. Entrar na pasta do projeto
cd projeto-ahd

# 3. Criar o ambiente virtual com Python 3.10
python3.10 -m venv venv

# 4. Ativar o ambiente virtual
source venv/bin/activate

# 5. Instalar as dependências do projeto
pip install -r requirements.txt
```

---

## 3. Configurar as Variáveis de Ambiente (.env)

Ainda no terminal Bash:

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env
nano .env
```

Preencha os dados no editor `nano`:
- **SECRET_KEY**: Cole uma chave segura (ou gere uma com: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`).
- **DEBUG**: Coloque `False` (ou deixe `True` nos primeiros minutos apenas para testar se há erros).
- **ALLOWED_HOSTS**: Coloque `seunome.pythonanywhere.com,localhost`
- **CSRF_TRUSTED_ORIGINS**: Coloque `https://seunome.pythonanywhere.com`

> Para salvar no `nano`: pressione `Ctrl + O`, depois `Enter`. Para sair: `Ctrl + X`.

---

## 4. Rodar as Migrações e Coletar Estáticos

No mesmo terminal Bash (com o `(venv)` ativo):

```bash
# Aplicar as tabelas no banco de dados
python manage.py migrate

# Coletar os arquivos estáticos (CSS, JS, imagens)
python manage.py collectstatic --noinput

# (Opcional) Criar um usuário administrador para acessar o painel
python manage.py createsuperuser
```

---

## 5. Configurar o Web App no PythonAnywhere

1. Vá na aba **Web** no menu superior do PythonAnywhere.
2. Clique no botão azul **Add a new web app**.
3. Clique em **Next**.
4. Selecione **Manual configuration** (NÃO selecione a opção "Django" pronta, pois já temos o projeto configurado).
5. Selecione **Python 3.10** e clique em **Next**.

---

## 6. Configurar Pastas e Virtualenv

Na página de configurações da aba **Web**, role a página e preencha:

### A) Seção "Code":
- **Source code:** `/home/seunome/projeto-ahd`
- **Working directory:** `/home/seunome/projeto-ahd`

### B) Seção "Virtualenv":
- Clique no campo e digite: `/home/seunome/projeto-ahd/venv`

### C) Seção "Static files":
Adicione duas linhas de mapeamento:

| URL | Directory |
|---|---|
| `/static/` | `/home/seunome/projeto-ahd/staticfiles` |
| `/media/` | `/home/seunome/projeto-ahd/media` |

---

## 7. Configurar o Arquivo WSGI

Ainda na aba **Web**, procure a seção **Code** e clique no link do arquivo **WSGI configuration file** (algo como `/var/www/seunome_pythonanywhere_com_wsgi.py`).

1. Apague **todo** o conteúdo que estiver lá.
2. Cole o seguinte código (substitua `seunome` pelo seu usuário do PythonAnywhere):

```python
import os
import sys

# Caminho para o diretório do projeto
path = '/home/seunome/projeto-ahd'
if path not in sys.path:
    sys.path.append(path)

# Carrega variáveis do .env se existir
from dotenv import load_dotenv
project_folder = os.path.expanduser(path)
load_dotenv(os.path.join(project_folder, '.env'))

# Define o arquivo de settings do Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Inicia a aplicação WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

3. Clique no botão verde **Save** no topo da página.

---

## 8. Colocar no Ar! 🚀

1. Volte para a aba **Web**.
2. Clique no botão verde grande **Reload seunome.pythonanywhere.com**.
3. Acesse `https://seunome.pythonanywhere.com` no seu navegador!

---

## 🔄 Como atualizar o site após novos commits no GitHub:

Sempre que a equipe fizer novidades e subir no GitHub:
1. Abra o **Bash Console** no PythonAnywhere:
   ```bash
   cd ~/projeto-ahd
   git pull origin main  # ou develop
   source venv/bin/activate
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```
2. Vá na aba **Web** e clique em **Reload**.
