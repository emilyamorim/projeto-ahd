# Como contribuir com o projeto (Workflow da Equipe)

Para não gerarmos conflitos no código de cada um, siga ESTRITAMENTE as regras abaixo.

---

## 1. Nunca mexa na `main` ou na `develop` diretamente
Sempre que for iniciar uma tarefa nova escolhida no [ROADMAP](ROADMAP.md), crie uma "ramificação" (*branch*) separada para você.

```bash
# 1. Garanta que você está na develop e está com a versão mais atual de todas
git checkout develop
git pull origin develop

# 2. Crie uma branch com o nome da sua tarefa
git checkout -b feature/nome-da-tarefa
```

## 2. Convenção de Nomes
Suas branches devem seguir estes padrões:
- `feature/...` → Para páginas ou recursos novos (Ex: `feature/tela-login`)
- `fix/...` → Para corrigir erros e bugs (Ex: `fix/erro-botoes-fotos`)
- `docs/...` → Apenas para atualizar documentos de texto (Ex: `docs/atualiza-roadmap`)

## 3. Mensagens de Commit (Padrão Semântico)
Explique exatamente o que você fez no commit:
- 🟢 `feat: adiciona formulario de login na auth`
- 🔴 `fix: corrige margin-top do grid de fotos`
- 🎨 `style: adiciona hover nos cards de noticia`

Evite mensagens genéricas como "arrumei o bug" ou "update".

## 4. Finalizando o Trabalho
Quando terminar e testar na sua máquina:
```bash
git add .
git commit -m "feat: sua mensagem"
git push origin feature/nome-da-tarefa
```
Vá ao repositório no GitHub e abra um **Pull Request (PR)** apontando a sua branch para a `develop`. Comunique a equipe no grupo para alguém revisar e aprovar seu código!
