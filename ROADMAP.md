# 🗺️ Roadmap e Status do Projeto (AHD)

Este documento centraliza o que já foi feito, o que estamos fazendo agora e quais são os próximos passos da equipe. Se você acabou de chegar no projeto, procure uma tarefa na coluna "A Fazer" ou converse com a equipe.

---

## 🚀 Status: Fase 2 (Autenticação, Backend e Painéis) Concluída!
A base visual do site, o sistema de autenticação, os modelos de banco de dados, o painel do professor e a área da aluna foram implementados. O foco agora muda para **conectar os dados dinâmicos às páginas públicas e preparar o deploy**.

---

## 📋 Quadro de Tarefas (Kanban)

### ✅ Concluído (Feito)
*Estruturas que já estão prontas no código.*
- [x] **Configuração Base:** Projeto Django configurado, estrutura de pastas e banco de dados SQLite.
- [x] **Design System:** Cores (`var(--rosa)`, `var(--azul)`), tipografia (Share, Inter) e componentes documentados em `docs/design_system.md`.
- [x] **P01 - Home:** Landing page com visual imersivo e apresentação do projeto.
- [x] **P02 - Histórico:** Lista de alunas e eixo do tempo estilizados.
- [x] **P03 - Fotos:** Galeria dinâmica com visualizador Lightbox e filtros.
- [x] **P04 - Notícias:** Grid de notícias com animações "Ler mais" e "Carregar mais".
- [x] **P05 - Sobre:** Apresentação da missão, eixos e bolsistas com busca em tempo real.
- [x] **Painel do Professor (G01 a G04 / AD01 a AD02):** Telas do dashboard administrativo, gerenciamento de alunas, fotos, notícias, aprovação de cadastros e usuários.
- [x] **A01 - Tela de Cadastro:** Formulário de registro de alunas em etapas (wizard) conectado ao backend.
- [x] **A02 - Tela de Login:** Login integrado ao Django com redirecionamento dinâmico por perfil (aluna ou coordenação).
- [x] **A03 - Recuperar Senha:** Tela de redefinição de senha (`templates/auth/redefinir_senha.html`).
- [x] **Modelagem do Banco de Dados:** Models criados (`Usuario`, `AlunaPerfil`, `Eixo`, `Noticia`, `Relato`, `Foto`, `Album`) com migrations aplicadas.
- [x] **Área da Aluna Logada (L01, L02, L03):** Visualização de perfil, upload e moderação de fotos e envio de relatos.
- [x] **Edição de Perfil Público (Professores e Cursistas):** Formulários completos para edição de biografia, foto com preview, dados pessoais, redes sociais e reflexo dinâmico nos perfis públicos.

### 🔄 A Fazer (Próximos Passos Imediatos)
*Quem for pegar essas tarefas, lembre-se de criar uma branch (`feature/...`). Passo a passo detalhado em **[TAREFAS_EQUIPE.md](TAREFAS_EQUIPE.md)**.*
- [ ] **Páginas Públicas Dinâmicas:** Conectar as páginas de Notícias, Fotos e Histórico para puxar dados diretamente do banco via views.
- [ ] **Ações em Relatos da Aluna:** Permitir editar e excluir relatos publicados pela aluna.
- [ ] **Envio de E-mail de Recuperação de Senha:** Configurar backend de envio de e-mails para o fluxo de reset de senha.

### 🔮 Futuro (Backlog)
*Tarefas maiores para os próximos meses.*
- [ ] **Implantação (Deploy):** Configurar banco PostgreSQL, Gunicorn e WhiteNoise/Nginx para colocar o site no ar no servidor do IFRN.

