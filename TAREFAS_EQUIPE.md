# 📝 Tarefas da Equipe (para iniciantes)

Cada pessoa pega **uma tarefa**, faz na **sua própria branch** e abre um Pull Request para `develop`.
Combine no grupo quem faz qual para não duas pessoas mexerem no mesmo arquivo.

| # | Tarefa | Dificuldade | Responsável |
|---|---|---|---|
| 1 | Notícias dinâmicas (lista) | 🟢 Fácil | _______ |
| 2 | Página de detalhe da notícia | 🟢 Fácil | _______ |
| 3 | Histórico das alunas dinâmico | 🟢 Fácil | _______ |
| 4 | Excluir relato (área da aluna) | 🟡 Médio | _______ |

> ⚠️ As tarefas 1 e 2 mexem no mesmo arquivo (`apps/conteudo/views.py`). Faça **a 1 primeiro**, e quem pegar a 2 faz `git pull origin develop` depois que a 1 for aprovada.

---

## Antes de começar (todas as tarefas)

```bash
git checkout develop
git pull origin develop
git checkout -b feature/nome-da-tarefa     # ex: feature/noticias-dinamicas

source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- Login de teste (coordenação): `admin@ahd.com` / `admin123`
- Para criar notícias de teste: entre como admin e acesse `/painel/noticias/`.
- Cores e botões: use as variáveis de [docs/design_system.md](docs/design_system.md). Não invente CSS novo.
- Regras de Git e commits: [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Tarefa 1 — Notícias dinâmicas 🟢

**Objetivo:** a página `/noticias/` deve mostrar as notícias cadastradas no banco, e não os cartões fixos.

**Arquivos:** `apps/conteudo/views.py`, `apps/conteudo/urls.py`, `apps/usuarios/urls.py`, `templates/publico/noticias.html`

**Passo a passo:**

1. Em `apps/conteudo/views.py`, crie a view:
   ```python
   def noticias_view(request):
       noticias = Noticia.objects.all().order_by('-data')
       return render(request, 'publico/noticias.html', {'noticias': noticias})
   ```
2. Em `apps/conteudo/urls.py`, adicione:
   ```python
   path("noticias/", views.noticias_view, name="noticias"),
   ```
3. Em `apps/usuarios/urls.py`, **apague** o `path("noticias/", TemplateView...)` (senão a rota fica duplicada e a antiga vence).
4. Em `templates/publico/noticias.html`, troque os cartões fixos por um único cartão dentro de um laço:
   ```html
   {% for noticia in noticias %}
     ... use {{ noticia.titulo }}, {{ noticia.data|date:"d M Y" }},
         {{ noticia.get_categoria_display }}, {{ noticia.conteudo|truncatewords:30 }}
   {% empty %}
     <p>Nenhuma notícia publicada ainda.</p>
   {% endfor %}
   ```
   Se `noticia.imagem_capa` existir, mostre `<img src="{{ noticia.imagem_capa.url }}">`.

**Como testar:** crie 2 notícias pelo painel e confira se aparecem em `/noticias/`.

**Pronto quando:** as notícias do banco aparecem, e sem notícias aparece a mensagem de vazio.

---

## Tarefa 2 — Detalhe da notícia 🟢

**Objetivo:** ao clicar em "Ler notícia", abrir uma página com o texto completo.

**Arquivos:** `apps/conteudo/views.py`, `apps/conteudo/urls.py`, novo `templates/publico/noticia_detalhe.html`, `templates/publico/noticias.html`

**Passo a passo:**

1. View (importe `get_object_or_404` — já está importado):
   ```python
   def noticia_detalhe_view(request, pk):
       noticia = get_object_or_404(Noticia, pk=pk)
       return render(request, 'publico/noticia_detalhe.html', {'noticia': noticia})
   ```
2. URL: `path("noticias/<int:pk>/", views.noticia_detalhe_view, name="noticia_detalhe"),`
3. Crie `templates/publico/noticia_detalhe.html` começando com:
   ```html
   {% extends "base.html" %}
   {% block title %}{{ noticia.titulo }} - Ampliando Horizontes Digitais{% endblock %}
   {% block content %}
     <!-- título, data, categoria, autor, imagem de capa, conteúdo completo -->
     <a href="{% url 'noticias' %}">← Voltar para notícias</a>
   {% endblock %}
   ```
   Use `{{ noticia.conteudo|linebreaks }}` para manter os parágrafos.
4. Em `noticias.html`, faça o cartão apontar para `{% url 'noticia_detalhe' noticia.pk %}`.

**Pronto quando:** clicar na notícia abre a página dela e o botão voltar funciona.

---

## Tarefa 3 — Histórico das alunas dinâmico 🟢

**Objetivo:** `/historico/` lista as alunas **aprovadas** do banco.

**Arquivos:** `apps/usuarios/views.py`, `apps/usuarios/urls.py`, `templates/publico/historico.html`

**Passo a passo:**

1. Em `apps/usuarios/views.py`:
   ```python
   def historico_view(request):
       perfis = (AlunaPerfil.objects
                 .filter(is_aprovada=True)
                 .select_related('usuario')
                 .prefetch_related('eixos')
                 .order_by('usuario__first_name'))
       return render(request, 'publico/historico.html', {'perfis': perfis})
   ```
2. Em `apps/usuarios/urls.py`, troque o `TemplateView` da rota `historico/` por `views.historico_view`.
3. Em `historico.html`, deixe **um** cartão dentro de `{% for perfil in perfis %}` com:
   - nome: `{{ perfil.usuario.get_full_name }}`
   - cidade: `{{ perfil.cidade }}`
   - tipo: `{{ perfil.get_tipo_participacao_display }}`
   - eixos: `{% for eixo in perfil.eixos.all %}{{ eixo.nome }}{% endfor %}`
   - link: `{% url 'perfil_aluna' perfil.usuario.id %}`
   - foto: `perfil.usuario.foto_perfil` (se não houver, mostre as iniciais)
4. Adicione `{% empty %}` com "Nenhuma aluna cadastrada ainda."

**Como testar:** entre como admin, aprove uma aluna em `/painel/cadastros/` e veja ela aparecer.

**Pronto quando:** só alunas aprovadas aparecem e o clique leva ao perfil público.

> Filtros (busca/eixo/bolsista-cursista) já têm JS em `static/js/historico.js`; **não precisa mexer neles** nesta tarefa.

---

## Tarefa 4 — Excluir relato 🟡

**Objetivo:** o botão de lixeira em "Meus relatos" apaga o relato da aluna logada.

**Arquivos:** `apps/conteudo/views.py`, `apps/conteudo/urls.py`, `templates/aluna/meus_relatos.html`

**Passo a passo:**

1. View:
   ```python
   from django.views.decorators.http import require_POST

   @login_required
   @require_POST
   def excluir_relato_view(request, pk):
       relato = get_object_or_404(Relato, pk=pk, autor=request.user)
       relato.delete()
       messages.success(request, 'Relato excluído com sucesso!')
       return redirect('meus_relatos')
   ```
   O `autor=request.user` impede que uma aluna apague o relato de outra.
2. URL: `path("minha-area/relatos/excluir/<int:pk>/", views.excluir_relato_view, name="excluir_relato"),`
3. No template, troque o botão de lixeira por um formulário:
   ```html
   <form method="POST" action="{% url 'excluir_relato' relato.pk %}"
         onsubmit="return confirm('Excluir este relato?');">
     {% csrf_token %}
     <button type="submit" style="border:none;background:none;color:#d9534f;cursor:pointer;">
       <i class="ti ti-trash"></i>
     </button>
   </form>
   ```

**Como testar:** publique um relato, exclua, confirme que sumiu. Tente também acessar a URL de exclusão direto pelo navegador (GET): deve dar erro 405.

**Pronto quando:** exclui só o próprio relato, com confirmação e mensagem de sucesso.

---

## Entregando

```bash
python manage.py check          # deve dizer "no issues"
git add .
git commit -m "feat: descrição curta do que você fez"
git push origin feature/nome-da-tarefa
```

Abra o Pull Request para `develop` no GitHub e avise no grupo. **Não faça merge sozinho.**
