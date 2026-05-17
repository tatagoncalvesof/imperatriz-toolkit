---
name: criativos-urgencia
description: Gera criativos Meta Ads no formato Urgência/Escassez. Fundo escuro, grid vermelho, foto séria do expert, headline bold de deadline. Stories (1080x1920) com foto IA + Feed (1080x1350) texto puro escuro.
user_invocable: true
---

# Skill: Criativos Urgência/Escassez (Meta Ads)

Gera criativos de anúncio no formato **Urgência/Deadline** — fundo escuro, grid tech, foto do expert com expressão séria, headline bold de escassez. Formato de FUNDO DE FUNIL.

## Quando usar
- Últimas 48-72h de carrinho aberto
- Virada de lote / preço vai subir
- Vagas encerrando
- Bônus saindo do ar
- Retargeting de quem visitou página de vendas
- Usuario pede "urgência", "escassez", "últimas horas", "deadline"

## Diferença vs `/criativos-dor-beneficio`
| Aspecto | Dor→Benefício | Urgência |
|---------|--------------|----------|
| **Funil** | Topo/Meio (gerar desejo) | Fundo (converter desejo) |
| **Emoção** | Esperança | Medo de perda |
| **Fundo** | Claro/bege | Escuro + grid vermelho |
| **Expert** | Sorridente | Sério, olhando relógio |
| **Copy** | 3 dores + 3 benefícios (lista) | 1 headline + 1 body (minimalista) |
| **Elementos** | Caixas, ícones, bullets | Zero — só texto grande |

## Stack técnica
- **Projeto:** `~/criativos-agent/`
- **Gerador:** `node generate-urgencia.mjs --input data.json --output <dir>`
- **Renderer Story:** `lib/urgencia-render.mjs` (overlay: grid + fade + logo + headline + body)
- **Renderer Feed:** `lib/urgencia-feed-render.mjs` (texto puro sobre fundo escuro)
- **Fotos IA:** Gemini 2.5 Flash Image — 16:9, expressão SÉRIA, backlight dourado
- **Fotos ref:** `~/criativos-agent/assets/expert/foto1.png`, `foto2.png`, `foto3.png`

## Formatos

### Story (1080x1920) — COM foto IA
```
┌──────────────────────────────┐
│     FOTO DO EXPERT (56%)     │ ← 16:9, expressão séria
│     olhando relógio/sério    │   backlight dourado, fundo escuro
│  ┌──────┐                    │
│  │ LOGO │ (top-left, small)  │ ← discreto, não protagonista
│  └──────┘                    │
│ ░░░ GRID VERMELHO ░░░░░░░░░ │ ← linhas 1px, 90px cells, 18% opac
│ ▓▓▓ FADE → ESCURO ▓▓▓▓▓▓▓▓ │
├──────────────────────────────┤
│                              │
│ Últimas horas                │ ← BOLD 60px, branco puro
│ pra garantir acesso          │ ← Regular 60px, branco quente
│ pagando menos.               │   LEFT-aligned (nunca centralizado)
│                              │
│ O valor atual está se        │ ← 30px cinza + bold branco
│ encerrando, garanta agora    │   + CTA em laranja #E8912A
│ clicando em saiba mais.      │
│                              │
│     [SAFE ZONE — botão]      │ ← 280px pro botão nativo Meta
└──────────────────────────────┘
```

### Feed (1080x1350) — SEM foto, fundo escuro
```
┌──────────────────────────────┐
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ ← fundo #0F0A08 + grid + glow
│ LOGO (top-left)              │
│                              │
│                              │
│ Últimas horas                │ ← headline centralizado vertical
│ pra garantir acesso          │
│ pagando menos.               │
│                              │
│ O valor atual está se        │
│ encerrando, garanta agora    │
│ clicando em saiba mais.      │
│                              │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
└──────────────────────────────┘
```

## Framework de copy — DCA (Deadline + Consequência + Ação)

### Headline (max 10 palavras)
Fórmula: `[GATILHO TEMPORAL bold] + [BENEFÍCIO DE AGIR AGORA regular]`

- Bold (800): o gatilho de urgência — "Últimas horas", "Último dia", "Faltam 3 horas"
- Regular (400): o que se ganha/protege — "pra garantir acesso pagando menos."

### Body (max 20 palavras)
Fórmula: `[CONTEXTO cinza] + [URGÊNCIA bold branco] + [INSTRUÇÃO cinza] + [CTA laranja]`

Representado como array `bodyParts`:
```json
[
  { "text": "O valor atual ", "bold": false, "cta": false },
  { "text": "está se encerrando, ", "bold": true, "cta": false },
  { "text": "garanta agora a sua vaga ", "bold": false, "cta": false },
  { "text": "clicando em saiba mais.", "bold": true, "cta": true }
]
```

## 4 Tipos de urgência (SEMPRE gerar 4 variações)

### 1. TEMPORAL (deadline)
- Headline: "Últimas horas pra garantir acesso pagando menos."
- Body: "O valor atual **está se encerrando,** garanta agora a sua vaga **clicando em saiba mais.**"

### 2. PREÇO (price increase)
- Headline: "O preço sobe amanhã. Ainda dá pra entrar pagando menos."
- Body: "Essa condição **não volta.** Garanta o valor atual **clicando em saiba mais.**"

### 3. VAGAS (scarcity)
- Headline: "Últimas vagas. Depois disso, só lista de espera."
- Body: "A turma **está fechando** e não será reaberta. Reserve a sua **clicando em saiba mais.**"

### 4. BÔNUS (bonus expiry)
- Headline: "Os bônus saem do ar hoje às 23h59."
- Body: "Quem entrar hoje **ainda leva tudo incluso.** Amanhã, só o acesso básico. **Garanta agora.**"

## Regras de copy (OBRIGATÓRIO)

- PT-BR COM ACENTOS (é, ã, ç, ê, í, ó, ú)
- Headline max 10 palavras — urgência é curta
- Body max 20 palavras — instrução, não narrativa
- Tom: aviso factual, NÃO desespero ("sussurra seriedade")
- "pra" (não "para") — informal brasileiro
- "garantir/garanta" = verbo de proteção, usar sempre
- "sua vaga" — possessivo antes da ação (propriedade antecipada)
- "está se encerrando" — presente contínuo (acontecendo AGORA)
- Zero exclamação, zero emoji
- Zero explicação do produto (assume que público já conhece)
- CTA mecânico: "clicando em saiba mais" (diz exatamente o que fazer)
- Framing de ECONOMIA ("pagando menos") não de AMEAÇA ("antes que suba")

## Paleta de cores

```json
{
  "bgDark": "#0F0A08",
  "gridColor": "rgba(139, 26, 26, 0.18)",
  "gridSize": 90,
  "glowColor": "#E8912A",
  "textWhite": "#FFFFFF",
  "textWarm": "#F0EDE8",
  "textGray": "#B8B0A8",
  "ctaColor": "#E8912A",
  "badgeColor": "#E8912A"
}
```

## Regras de foto (Stories)
- Aspect ratio: **16:9** (fitted em 1080x1075 no topo 56%)
- Expressão: **SÉRIA, concentrada, NUNCA sorrindo** (urgência não sorri)
- Gesto ideal: olhando relógio no pulso / checando celular
- Iluminação: **backlight dourado/alaranjado** dramático (halo effect)
- Roupa: escura, sem estampas, relógio metálico visível
- Fundo da foto: escuro (será integrado ao bg escuro do criativo)

## Workflow

### Passo 1: Identificar tipo de urgência
Perguntar: qual deadline? preço sobe? vagas limitadas? bônus sai?

### Passo 2: Gerar 4 variações de copy
Uma por tipo de urgência (temporal, preço, vagas, bônus).

### Passo 3: Montar JSON
```json
{
  "expertDescription": "Brazilian woman, brown shoulder-length hair, serious expression, dark elegant clothing, natural makeup",
  "expertPhotos": [
    "/Users/macbookm2/criativos-agent/assets/expert/foto1.png",
    "/Users/macbookm2/criativos-agent/assets/expert/foto2.png",
    "/Users/macbookm2/criativos-agent/assets/expert/foto3.png"
  ],
  "variations": [
    {
      "content": {
        "logoSub": "IMERSÃO",
        "logoMain": "Negócio em 48H",
        "logoHighlight": "48H",
        "badge": "21 E 22 DE JUNHO",
        "headlineBold": "Últimas horas",
        "headlineRegular": "pra garantir acesso pagando menos.",
        "bodyParts": [
          { "text": "O valor atual ", "bold": false, "cta": false },
          { "text": "está se encerrando, ", "bold": true, "cta": false },
          { "text": "garanta agora a sua vaga ", "bold": false, "cta": false },
          { "text": "clicando em saiba mais.", "bold": true, "cta": true }
        ]
      },
      "scenePrompt": "looking at silver wristwatch, serious expression, dramatic orange backlight, dark background, medium shot waist up"
    }
  ]
}
```

### Passo 4: Executar
```bash
cd ~/criativos-agent && node generate-urgencia.mjs \
  --input /tmp/ad-urgencia-data.json \
  --output ~/criativos/$(date +%Y-%m-%d)-ads-urgencia/
```

### Passo 5: Entregar
- 4 stories (foto IA) + 4 feeds (texto escuro) = 8 PNGs
- Abrir pasta com `open <path>`

## Sequência numa campanha
```
Dias 1-4:   /criativos-dor-beneficio (gerar desejo)
Dias 3-5:   Mix (dor-benefício + urgências suaves)
Dias 5-7:   /criativos-urgencia dominante (converter)
Último dia: 100% urgência + "última chance"
```
