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

O `build.sh` cria o superusuário automaticamente no deploy, **mas só se você definir a senha**
nas variáveis de ambiente (não existe mais senha padrão, por segurança):

* `DJANGO_SUPERUSER_EMAIL`: e-mail de acesso da coordenação
* `DJANGO_SUPERUSER_PASSWORD`: uma senha forte e secreta

> ⚠️ Depois do primeiro acesso, troque a senha pelo fluxo "Esqueci minha senha" e remova `DJANGO_SUPERUSER_PASSWORD` do painel do Render.

---

## 7. Fotos permanentes (obrigatório em produção)

O disco do plano gratuito do Render **é apagado a cada deploy**: todas as fotos de perfil e da galeria seriam perdidas.
Use um armazenamento externo compatível com S3 (recomendado: **Cloudflare R2**, **Backblaze B2** ou **Supabase Storage**, todos com plano gratuito):

1. Crie um *bucket* público para leitura e gere uma chave de acesso.
2. No Render, adicione: `AWS_STORAGE_BUCKET_NAME`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`,
   `AWS_S3_ENDPOINT_URL` e, se tiver, `AWS_S3_CUSTOM_DOMAIN`.
3. Faça um novo deploy. Os uploads passam a ser gravados no bucket automaticamente.

## 8. Banco de dados (PostgreSQL)

O SQLite também é apagado a cada deploy. Crie um banco PostgreSQL gratuito (Neon ou Supabase) e coloque a
*connection string* em `DATABASE_URL` (ex.: `postgresql://usuario:senha@host/banco?sslmode=require`).

## 9. E-mail (recuperação de senha)

Defina `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` e `DEFAULT_FROM_EMAIL`
(ex.: Gmail com *senha de app*: `smtp.gmail.com`, porta 587). Sem isso ninguém recebe o link de redefinição.

## 10. Checklist antes de divulgar

- [ ] `DEBUG=False` e `SECRET_KEY` gerada pelo Render
- [ ] `DATABASE_URL` apontando para PostgreSQL
- [ ] Armazenamento de fotos configurado (seção 7)
- [ ] E-mail configurado e testado (seção 9)
- [ ] Senha do superusuário trocada
- [ ] Depois de confirmar que o HTTPS funciona, aumente `SECURE_HSTS_SECONDS` (ex.: `31536000`)
