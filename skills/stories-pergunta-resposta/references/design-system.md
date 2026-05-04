---
name: design-system
description: Cores e tipografia oficial da Tata Gonçalves para a caixinha de pergunta e card de resposta
---

# Design System — Stories Pergunta e Resposta

Extraído do **Tatá Gonçalves Design System**. Usado em TODA caixinha e card de resposta da skill.

> CSS completo em `assets/colors_and_type.css` (copiado do design system oficial).

## Direção visual: A — IA com Alma (default)

Editorial brasileiro. Cream + ink + accent terracotta + gold como marca-texto.

### Por que essa direção
- **Cream/off-white** = canvas das caixinhas (combina com iluminação dourada e couro caramelo)
- **Ink navy** = barra superior da caixinha + texto da pergunta (contraste alto, leitura fácil)
- **Gold** = marca-texto das palavras-chave (combina com o colar de ouro da Tata)
- **Terracotta** = reservado para acentos pontuais (botões, símbolos), NÃO usar como cor principal das stories

## Cores oficiais (use estes hex)

### Caixinha de pergunta (sticker)
| Elemento | Cor | Hex |
|---|---|---|
| Barra superior (label) | Ink 950 | `#0A1020` |
| Texto da label | Cream 50 | `#FAF7F0` |
| Fundo da pergunta | Cream 50 | `#FAF7F0` |
| Texto da pergunta | Ink 950 | `#0A1020` |
| Borda sutil | Ink 200 | `#D6D9E0` |

### Card de resposta
| Elemento | Cor | Hex |
|---|---|---|
| Fundo do card | Cream 50 com 92% opacidade | `rgba(250, 247, 240, 0.92)` |
| Texto da resposta | Ink 950 | `#0A1020` |
| Marca-texto (highlight) | Gold | `#D6A648` |
| Texto sobre marca-texto | Ink 950 | `#0A1020` |

### Overlay sobre a foto (legibilidade)
| Camada | Detalhe |
|---|---|
| Gradiente escuro | linear-gradient(to bottom, rgba(10,16,32,0) 50%, rgba(10,16,32,0.35) 100%) |
| Aplicação | apenas atrás da área da caixinha (60-100% vertical) |
| Função | garantir contraste do card sem escurecer a foto inteira |

## Tipografia

### Família: Inter (Google Fonts)
Importação:
```
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
```

### Pesos usados
| Elemento | Família | Peso | Tamanho |
|---|---|---|---|
| Label do sticker | Inter | 600 SemiBold | 28px |
| Pergunta | Inter | 700 Bold | 42px |
| Resposta (corpo) | Inter | 500 Medium | 36px |
| Marca-texto (palavra destacada) | Inter | 700 Bold | 36px |
| @ do instagram (rodapé opcional) | Inter | 500 Medium | 22px |

### Letter-spacing
- Label: 0.05em (levemente expandida)
- Pergunta: -0.01em (levemente apertada)
- Resposta: 0em (neutra)

### Line-height
- Label: 1.2
- Pergunta: 1.15
- Resposta: 1.4

## Composição da caixinha de pergunta

```
┌──────────────────────────────────────────┐
│ ▌▌▌ sobre começar do zero...             │  ← Label (28px SemiBold, ink, cream bg)
│                                          │     Padding: 16px 24px
├──────────────────────────────────────────┤
│                                          │
│  Como você começou sem                   │  ← Pergunta (42px Bold, ink)
│  ninguém apoiar?                         │     Padding: 24px 32px
│                                          │
└──────────────────────────────────────────┘
   ↑ border-radius: 24px
   ↑ shadow: 0 12px 32px rgba(10,16,32,0.18)
   ↑ width: 80% do frame (margem 10% cada lado)
   ↑ posicionamento: centralizado horizontal, top em 60% vertical
```

## Composição do card de resposta

```
┌──────────────────────────────────────────┐
│                                          │
│  Comecei [sozinha], sem grupo,           │  ← Resposta (36px Medium, ink)
│  sem palmas. A diferença é que eu        │     [palavra] = fundo gold
│  [não esperei] os outros aprovarem.      │     Padding: 28px 32px
│                                          │
└──────────────────────────────────────────┘
   ↑ border-radius: 16px
   ↑ background: rgba(250,247,240,0.92) — cream semi-transparente
   ↑ width: 80% do frame
   ↑ posicionamento: 12px abaixo do sticker
```

### Marca-texto: como renderizar
A palavra entre `**asteriscos**` no JSON ganha:
- Fundo: `#D6A648` (gold)
- Padding interno: 4px 8px
- Border-radius: 4px
- Texto: continua ink #0A1020 (NÃO branco)
- Peso: muda de 500 Medium → 700 Bold

Exemplo:
```
Resposta original: "Comecei **sozinha**, sem grupo."
Resposta renderizada: Comecei [sozinha em fundo gold], sem grupo.
```

## Logo / assinatura (opcional)

Se quiser adicionar identidade visual no rodapé do story:
- Wordmark SVG: `/tmp/tata-ds/assets/logo/wordmark-primary.svg`
- Tamanho: 90px de largura
- Posição: bottom-right, margem 32px
- Cor: cream 50 com 70% opacidade (sutil, não compete)

## Direção alternativa: C — Império (gold-on-navy)

Use APENAS quando a Tata pedir "vibe imperatriz" / "vibe premium dramática".

| Elemento | Cor | Hex |
|---|---|---|
| Fundo da caixinha | Navy escuro | `#0E1B2E` |
| Barra/borda | Gold | `#D6A648` |
| Texto pergunta | Cream | `#F5EBD4` |
| Marca-texto | Gold | `#D6A648` |

**Regra**: NUNCA misturar Direção A e C no mesmo conjunto de 10 stories. Escolha uma e mantenha.

## NÃO fazer

- ❌ Usar cores fora dessa paleta (sem rosa, roxo, verde, azul claro, etc.)
- ❌ Usar gradientes coloridos (rosa-roxo, azul-verde, etc.) na barra do sticker
- ❌ Trocar Inter por outra fonte (Helvetica, Arial, etc.) — usar fallback `system-ui` se faltar
- ❌ Usar marca-texto em mais de 3 palavras por resposta (vira poluído)
- ❌ Usar marca-texto em palavra de ligação (de, para, com, mas) — sempre em substantivo/verbo principal
- ❌ Adicionar emojis no card ou sticker
- ❌ Usar drop-shadow forte em texto (manter limpo, design system é "carved" não "fluffy")
