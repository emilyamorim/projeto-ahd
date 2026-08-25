# 🗺️ Roadmap e Status do Projeto (AHD)

Este documento centraliza o que já foi feito, o que estamos fazendo agora e quais são os próximos passos da equipe. Se você acabou de chegar no projeto, procure uma tarefa na coluna "A Fazer" ou converse com a equipe.

---

## 🚀 Status: Fase 1 (Frontend Público) Concluída!
A base visual do site e as principais páginas de apresentação (Área Pública) foram finalizadas com sucesso, recebendo um design premium e responsivo. O foco agora muda para a **Área de Autenticação e Backend (Django)**.

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

### 🔄 A Fazer (Próximos Passos Imediatos)
*Quem for pegar essas tarefas, lembre-se de criar uma branch (`feature/...`).*
- [ ] **A02 - Tela de Login:** Criar `templates/auth/login.html` seguindo o design system.
- [ ] **A01 - Tela de Cadastro:** Criar formulário de registro de alunas `templates/auth/cadastro.html`.
- [ ] **A03 - Recuperar Senha:** Telas de "Esqueci minha senha".
- [ ] **Backend de Autenticação:** Conectar essas telas com o sistema de `auth` nativo do Django (models, views e forms).

### 🔮 Futuro (Backlog)
*Tarefas maiores para os próximos meses.*
- [ ] **Modelagem do Banco de Dados:** Criar os *models* reais de Alunas, Notícias, Fotos e Relatos no `models.py`.
- [ ] **Área da Aluna Logada (L01, L02, L03):** Painel onde a aluna visualiza seu progresso e envia relatos.
- [ ] **Painel do Professor (G01 a G04):** Telas de aprovação de cadastros, gerenciamento e postagem de notícias.
- [ ] **Implantação (Deploy):** Configurar banco PostgreSQL, Gunicorn e Nginx para colocar o site no ar no servidor do IFRN.
