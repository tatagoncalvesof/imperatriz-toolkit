# Template Markmap — base

## O que é Markmap

Markmap converte **markdown puro** em mapa mental HTML interativo (zoom, colapsa ramos, busca). É o output mais poderoso pra mentoradas — basta abrir o HTML no navegador.

## Sintaxe básica

Markmap usa markdown nativo. Cada nível de heading vira um nível do mapa.

```markdown
---
title: Mapa Mental
markmap:
  colorFreezeLevel: 2
  initialExpandLevel: 3
  duration: 500
---

# Tema Central

## Ramo 1

- Subitem 1.1
- Subitem 1.2
  - Detalhe 1.2.1

## Ramo 2

- Subitem 2.1
- Subitem 2.2

## Ramo 3
```

## Frontmatter — configurações

```yaml
---
title: <título>
markmap:
  colorFreezeLevel: 2          # nível em que cor é fixada
  initialExpandLevel: 3         # quantos níveis começam abertos
  duration: 500                 # animação em ms
  maxWidth: 300                 # largura máxima do nó
  zoom: true                    # permite zoom
  pan: true                     # permite arrastar
  spacingHorizontal: 80
  spacingVertical: 5
---
```

## Recursos avançados

### Listas

```markdown
## Tarefas

- [ ] Pendente
- [x] Feita
- ➕ Adicionar
- ⭐ Importante
```

### Código inline

```markdown
## Stack

- `Node.js` v25
- `Express` 5.x
- `SQLite` (better-sqlite3)
```

### Imagens

```markdown
## Visual

![alt](caminho/imagem.png)
```

### Links

```markdown
## Recursos

- [Documentação](https://docs.example.com)
- [Repo](https://github.com/...)
```

### Math (LaTeX)

```markdown
## Fórmulas

- $E = mc^2$
- $\sum_{i=1}^{n} x_i$
```

## Tema Imperatriz (cores)

Markmap aceita CSS custom via tag de estilo no HTML final. Padrão Imperatriz:

```css
.markmap-node-text {
  font-family: Inter, sans-serif;
}
.markmap-link {
  stroke: #7f8c8d;
}
.markmap-node-circle {
  fill: #9b59b6;
}
```

## Como gerar o HTML

```bash
npx markmap-cli input.md -o output.html
# ou com configurações
npx markmap-cli input.md -o output.html --no-toolbar
```

## Estrutura recomendada

```markdown
---
title: <Tema>
markmap:
  colorFreezeLevel: 2
  initialExpandLevel: 2
---

# <Tema do mapa>

## 🎯 Pilar 1

- Subitem
- Subitem
  - Detalhe

## 🚀 Pilar 2

- Subitem

## 💡 Pilar 3

## 📊 Pilar 4
```

## Vantagens vs Mermaid

| Aspecto | Markmap | Mermaid |
|---------|---------|---------|
| Visual | Mais limpo | Mais técnico |
| Interatividade | Zoom, colapsa, busca | Estático |
| Tamanho suportado | Centenas de nós | ~50 nós |
| Imagens | Sim | Não |
| Output | HTML interativo | SVG/PNG |
| Compartilhar | Link/arquivo HTML | Imagem |

## Quando usar

**Markmap >>** quando:
- Vai compartilhar com mentorada (interativo é foda)
- Mais de 30 nós
- Precisa de imagens/links
- Conteúdo complexo que precisa colapsar

**Mermaid >>** quando:
- Vai pro Obsidian (renderiza nativo)
- Precisa de PNG/SVG estático
- Mapa pequeno e estático
