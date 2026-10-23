# 🚀 Guia de Deploy no Render.com — Projeto AHD

Este guia explica passo a passo como colocar o site do **Ampliando Horizontes Digitais (AHD)** no ar gratuitamente no **Render.com**.

O deploy no Render é automático: sempre que você fizer um `git push` no seu repositório, ele compila e atualiza o site sozinho.

---

## 1. Criar a Conta no Render

1. Acesse: [https://render.com](https://render.com)
2. Clique em **Get Started for Free** (ou **Sign Up**).
3. Recomendado: entre usando sua conta do **GitHub**. Isso facilita vincular seus repositórios.

---

## 2. Criar o Novo Web Service

1. No painel inicial do Render (Dashboard), clique no botão **New +** no canto superior direito e selecione **Web Service**.
2. Conecte sua conta do GitHub (se ainda não conectou).
3. Na lista de repositórios, localize e clique em **Connect** ao lado de `projeto-ahd` (ou cole a URL do seu repositório: `https://github.com/emilyamorim/projeto-ahd`).

---

## 3. Configurar os Parâmetros do Projeto

Preencha os campos da página:

- **Name:** `projeto-ahd` (ou o nome que preferir — o site ficará `https://projeto-ahd.onrender.com`).
- **Region:** Escolha qualquer uma (ex: *Oregon (US West)* ou *Frankfurt*).
- **Branch:** `develop` (ou `main`, dependendo de qual branch você quer que fique no ar).
- **Root Directory:** deixe em branco.
- **Runtime:** `Python 3`
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn config.wsgi:application`
- **Instance Type:** Selecione **Free**.

---

## 4. Configurar as Variáveis de Ambiente (Environment Variables)

Role até a seção **Advanced** -> **Add Environment Variable** e adicione as seguintes variáveis:

| Key | Value | Descrição |
|---|---|---|
| `PYTHON_VERSION` | `3.10.12` | Versão do Python |
| `DEBUG` | `False` | Mantém o Django seguro em produção |
| `SECRET_KEY` | *(Clique em Generate ou cole uma chave longa aleatória)* | Chave de segurança do Django |
| `ALLOWED_HOSTS` | `.onrender.com,localhost` | Aceita requisições do domínio do Render |

> 💡 **Nota:** O projeto já foi configurado para reconhecer automaticamente o domínio gerado pelo Render (`RENDER_EXTERNAL_HOSTNAME`), garantindo proteção CSRF e carregamento rápido de CSS e JS com WhiteNoise.

---

## 5. Iniciar o Deploy

1. Clique no botão azul **Create Web Service** no final da página.
2. O Render começará a instalar as dependências, coletar os arquivos estáticos e aplicar as migrações automaticamente através do `build.sh`.
3. Em cerca de 2 a 3 minutos, você verá a mensagem verde **Live** e o link do seu site estará disponível no topo da tela!

---

## 6. Acesso do Administrador / Coordenador em Produção

Como o terminal interativo (**Shell**) do Render é restrito aos planos pagos, o arquivo `build.sh` já foi configurado para **criar o superusuário administrador automaticamente** no primeiro deploy!

### Credenciais padrão geradas:
* **E-mail / Usuário:** `admin@ahd.com`
* **Senha:** `admin123`

*(Opcional)* Se quiser definir outro e-mail ou senha diretamente nas variáveis de ambiente do Render, basta adicionar:
* `DJANGO_SUPERUSER_EMAIL`: seu e-mail
* `DJANGO_SUPERUSER_PASSWORD`: sua senha secreta

