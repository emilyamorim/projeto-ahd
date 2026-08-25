# 🎨 Design System e Guia Visual

Para mantermos o visual do projeto sempre profissional e coeso, **todas as novas telas devem seguir estas regras**. Antes de criar um CSS novo do zero, verifique se a classe já não existe no `style.css`.

## 1. Cores Oficiais
Sempre use as variáveis CSS do projeto, nunca escreva o código da cor diretamente (hex) nos seus arquivos, exceto em casos muito específicos.
- **Rosa Principal:** `var(--rosa)` (Força, destaque, feminilidade)
- **Azul Principal:** `var(--azul)` (Tecnologia, conhecimento, botões secundários)
- **Cores de Texto:** `var(--preto)` (Textos escuros), `var(--branco)` (Textos claros), `var(--cinza-texto)` (Textos descritivos)
- **Fundos (Backgrounds):** `var(--fundo)` (Cinza clarinho do fundo do site)

*Exemplo de uso:* `color: var(--rosa);`

## 2. Tipografia
O projeto utiliza duas fontes do Google Fonts:
- **Títulos (H1, H2, H3):** Fonte `Share`. Sempre que possível, utilize a classe `.section-title` para padronizar os grandes títulos da página.
- **Corpo do texto e Botões:** Fonte `Inter`. Extremamente legível. (Carregada como padrão no `body`).

## 3. Botões ("Pílulas")
O padrão do projeto é utilizar botões com bordas totalmente arredondadas (`border-radius: 50px`).
*Se você for criar um botão novo, siga este padrão:*

```css
.meu-novo-botao {
  background: var(--rosa);
  color: var(--branco);
  border-radius: 50px;
  padding: 12px 32px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
}
.meu-novo-botao:hover {
  transform: translateY(-2px); /* Efeito de elevação */
  box-shadow: 0 4px 12px rgba(152, 24, 105, 0.3);
}
```

## 4. Cabeçalhos (Hero Sections)
Páginas principais usam o arquivo `hero_bg_real.jpg` coberto por uma fina camada de cor com 85% de opacidade (Azul ou Rosa) para dar um efeito de filme e aumentar a legibilidade do texto branco. Olhe como as classes `.sobre-header` ou `.noticias-header` foram feitas se precisar replicar em uma página nova.
