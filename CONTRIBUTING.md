# Como contribuir com o projeto

Leia este guia antes de começar a trabalhar no código.

---

## Configurando o ambiente

Siga o passo a passo do [README.md](README.md). Depois de configurar,
você estará pronto para contribuir.

---

## Criando uma branch para sua tarefa

Nunca trabalhe diretamente na `main` ou `develop`.
Crie sempre uma branch nova para cada tarefa:

```bash
# 1. Atualize o develop antes de começar
git checkout develop
git pull origin develop

# 2. Crie uma branch com o nome da sua tarefa
git checkout -b feature/nome-da-tarefa

# Exemplos de nomes:
# feature/tela-home
# feature/tela-login
# fix/erro-cadastro
# style/ajuste-navbar
```

---

## Fazendo commits

Escreva mensagens claras que expliquem o que foi feito:

```bash
# Boas mensagens
git commit -m "feat: adiciona página de login"
git commit -m "fix: corrige validação do e-mail no cadastro"
git commit -m "style: ajusta tamanho da fonte na navbar"
git commit -m "docs: atualiza instruções no README"

# Mensagens ruins (evite)
git commit -m "update"
git commit -m "arrumei"
git commit -m "alterações"
```

Prefixos disponíveis:
- `feat:` → novo recurso ou página
- `fix:` → correção de erro
- `style:` → mudança visual (CSS, HTML)
- `docs:` → atualização de documentação
- `refactor:` → melhoria de código sem mudar o resultado

---

## Subindo seu trabalho para o GitHub

```bash
# Salve seus arquivos e faça o commit
git add .
git commit -m "feat: adiciona tela de histórico"

# Suba para o GitHub
git push origin feature/nome-da-sua-branch
```

Depois, abra um **Pull Request** no GitHub apontando
sua branch para a `develop`.

---

## Reportando um erro

Se encontrar um erro no projeto, abra uma **Issue** no GitHub com:
- O que você estava tentando fazer
- O que aconteceu (mensagem de erro, se houver)
- Em qual página ou funcionalidade ocorreu