---
name: criativos-urgencia-mentorados
description: >
  Versao para MENTORADOS da skill criativos-urgencia.
  Gera criativos Meta Ads no formato Urgencia/Escassez. Fundo escuro, grid vermelho, foto seria do expert,
  headline bold de deadline. Stories (1080x1920) com foto IA + Feed (1080x1350) texto puro escuro.
  Usa as fotos e chave Gemini do mentorado salvas em ~/.criativos-mentorados/config.json.
  Se o config nao existir, roda o onboarding primeiro (/criativos-mentorados-setup).
  Use quando o mentorado pedir "criativo urgencia", "escassez", "ultimas horas", "deadline ads".
user_invocable: true
---

# Skill: Criativos Urgencia/Escassez (Meta Ads) — VERSAO MENTORADOS

Gera criativos de anuncio no formato **Urgencia/Deadline** — fundo escuro, grid tech, foto do expert com expressao seria, headline bold de escassez. Formato de FUNDO DE FUNIL.

## PASSO ZERO — Verificar Config do Mentorado (OBRIGATORIO)

ANTES de qualquer coisa, verificar se o mentorado ja fez o setup:

```bash
cat ~/.criativos-mentorados/config.json 2>/dev/null
```

**Se o arquivo NAO existir ou estiver vazio:**
- Informar: "Antes de criar seus criativos, preciso configurar suas fotos e chave Gemini. Vou iniciar o setup rapido."
- Executar o onboarding completo conforme a skill `/criativos-mentorados-setup`
- So prosseguir APOS o config estar salvo

**Se o arquivo EXISTIR:**
- Ler o config e extrair: `expertDescription`, `expertPhotos`, `expertName`, `geminiApiKey`
- Usar esses dados em vez dos hardcoded
- Mostrar: "Usando perfil de [nome]. [X] foto(s) cadastrada(s)."

## Configuracao dinamica

| Original (Tata) | Mentorado |
|---|---|
| `~/criativos-agent/assets/expert/foto1-3.png` | Valor de `config.expertPhotos` |
| `GEMINI_API_KEY` do `.env` | Valor de `config.geminiApiKey` |
| `expertDescription` hardcoded | Valor de `config.expertDescription` |
| `expertName` "Tata Goncalves" | Valor de `config.expertName` |

## Quando usar
- Ultimas 48-72h de carrinho aberto
- Virada de lote / preco vai subir
- Vagas encerrando
- Bonus saindo do ar
- Retargeting de quem visitou pagina de vendas
- Usuario pede "urgencia", "escassez", "ultimas horas", "deadline"

## Diferenca vs `/criativos-dor-beneficio-mentorados`
| Aspecto | Dor->Beneficio | Urgencia |
|---------|--------------|----------|
| **Funil** | Topo/Meio (gerar desejo) | Fundo (converter desejo) |
| **Emocao** | Esperanca | Medo de perda |
| **Fundo** | Claro/bege | Escuro + grid vermelho |
| **Expert** | Sorridente | Serio, olhando relogio |
| **Copy** | 3 dores + 3 beneficios (lista) | 1 headline + 1 body (minimalista) |
| **Elementos** | Caixas, icones, bullets | Zero — so texto grande |

## Stack tecnica
- **Projeto:** `~/criativos-agent/`
- **Gerador:** `node generate-urgencia.mjs --input data.json --output <dir>`
- **Renderer Story:** `lib/urgencia-render.mjs` (overlay: grid + fade + logo + headline + body)
- **Renderer Feed:** `lib/urgencia-feed-render.mjs` (texto puro sobre fundo escuro)
- **Fotos IA:** Gemini 2.5 Flash Image — 16:9, expressao SERIA, backlight dourado
- **Fotos ref:** Lidas de `~/.criativos-mentorados/config.json` → campo `expertPhotos`
- **API Key Gemini:** Lida de `~/.criativos-mentorados/config.json` → campo `geminiApiKey`

## Formatos

### Story (1080x1920) — COM foto IA
```
┌──────────────────────────────┐
│     FOTO DO EXPERT (56%)     │ <- 16:9, expressao seria
│     olhando relogio/serio    │   backlight dourado, fundo escuro
│  ┌──────┐                    │
│  │ LOGO │ (top-left, small)  │ <- discreto, nao protagonista
│  └──────┘                    │
│ ░░░ GRID VERMELHO ░░░░░░░░░ │ <- linhas 1px, 90px cells, 18% opac
│ ▓▓▓ FADE → ESCURO ▓▓▓▓▓▓▓▓ │
├──────────────────────────────┤
│                              │
│ Ultimas horas                │ <- BOLD 60px, branco puro
│ pra garantir acesso          │ <- Regular 60px, branco quente
│ pagando menos.               │   LEFT-aligned (nunca centralizado)
│                              │
│ O valor atual esta se        │ <- 30px cinza + bold branco
│ encerrando, garanta agora    │   + CTA em laranja #E8912A
│ clicando em saiba mais.      │
│                              │
│     [SAFE ZONE — botao]      │ <- 280px pro botao nativo Meta
└──────────────────────────────┘
```

### Feed (1080x1350) — SEM foto, fundo escuro
```
┌──────────────────────────────┐
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ <- fundo #0F0A08 + grid + glow
│ LOGO (top-left)              │
│                              │
│                              │
│ Ultimas horas                │ <- headline centralizado vertical
│ pra garantir acesso          │
│ pagando menos.               │
│                              │
│ O valor atual esta se        │
│ encerrando, garanta agora    │
│ clicando em saiba mais.      │
│                              │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
└──────────────────────────────┘
```

## Framework de copy — DCA (Deadline + Consequencia + Acao)

### Headline (max 10 palavras)
Formula: `[GATILHO TEMPORAL bold] + [BENEFICIO DE AGIR AGORA regular]`

- Bold (800): o gatilho de urgencia — "Ultimas horas", "Ultimo dia", "Faltam 3 horas"
- Regular (400): o que se ganha/protege — "pra garantir acesso pagando menos."

### Body (max 20 palavras)
Formula: `[CONTEXTO cinza] + [URGENCIA bold branco] + [INSTRUCAO cinza] + [CTA laranja]`

Representado como array `bodyParts`:
```json
[
  { "text": "O valor atual ", "bold": false, "cta": false },
  { "text": "esta se encerrando, ", "bold": true, "cta": false },
  { "text": "garanta agora a sua vaga ", "bold": false, "cta": false },
  { "text": "clicando em saiba mais.", "bold": true, "cta": true }
]
```

## 4 Tipos de urgencia (SEMPRE gerar 4 variacoes)

### 1. TEMPORAL (deadline)
- Headline: "Ultimas horas pra garantir acesso pagando menos."
- Body: "O valor atual **esta se encerrando,** garanta agora a sua vaga **clicando em saiba mais.**"

### 2. PRECO (price increase)
- Headline: "O preco sobe amanha. Ainda da pra entrar pagando menos."
- Body: "Essa condicao **nao volta.** Garanta o valor atual **clicando em saiba mais.**"

### 3. VAGAS (scarcity)
- Headline: "Ultimas vagas. Depois disso, so lista de espera."
- Body: "A turma **esta fechando** e nao sera reaberta. Reserve a sua **clicando em saiba mais.**"

### 4. BONUS (bonus expiry)
- Headline: "Os bonus saem do ar hoje as 23h59."
- Body: "Quem entrar hoje **ainda leva tudo incluso.** Amanha, so o acesso basico. **Garanta agora.**"

## Regras de copy (OBRIGATORIO)
- PT-BR COM ACENTOS (e, a, c, e, i, o, u)
- Headline max 10 palavras — urgencia e curta
- Body max 20 palavras — instrucao, nao narrativa
- Tom: aviso factual, NAO desespero ("sussurra seriedade")
- "pra" (nao "para") — informal brasileiro
- "garantir/garanta" = verbo de protecao, usar sempre
- "sua vaga" — possessivo antes da acao (propriedade antecipada)
- "esta se encerrando" — presente continuo (acontecendo AGORA)
- Zero exclamacao, zero emoji
- Zero explicacao do produto (assume que publico ja conhece)
- CTA mecanico: "clicando em saiba mais" (diz exatamente o que fazer)
- Framing de ECONOMIA ("pagando menos") nao de AMEACA ("antes que suba")

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
- Expressao: **SERIA, concentrada, NUNCA sorrindo** (urgencia nao sorri)
- Gesto ideal: olhando relogio no pulso / checando celular
- Iluminacao: **backlight dourado/alaranjado** dramatico (halo effect)
- Roupa: escura, sem estampas, relogio metalico visivel
- Fundo da foto: escuro (sera integrado ao bg escuro do criativo)

## Decisoes tecnicas ja resolvidas
- **SEM faixa/banda escura** — foto full bleed, texto com text-shadow pra legibilidade
- **Glow:** camada de glow laranja composta com blend 'screen' ENTRE foto e overlay
- **Headline:** font-size 96px
- **Accent bar:** 14px largura
- **Logo:** topo CENTRO

## Workflow

### Passo 0: Ler config do mentorado
```bash
cat ~/.criativos-mentorados/config.json
```
Se nao existir → rodar `/criativos-mentorados-setup` primeiro.

### Passo 1: Identificar tipo de urgencia
Perguntar: qual deadline? preco sobe? vagas limitadas? bonus sai?

### Passo 2: Gerar 4 variacoes de copy
Uma por tipo de urgencia (temporal, preco, vagas, bonus).

### Passo 3: JSON
```json
{
  "expertDescription": "<VALOR DO CONFIG>",
  "expertPhotos": ["<VALORES DO CONFIG>"],
  "variations": [
    {
      "content": {
        "logoSub": "<PRODUTO>",
        "logoMain": "<SUBTITULO>",
        "logoHighlight": "<DESTAQUE>",
        "badge": "<BADGE>",
        "headlineBold": "Ultimas horas",
        "headlineRegular": "pra garantir acesso pagando menos.",
        "bodyParts": [
          { "text": "O valor atual ", "bold": false, "cta": false },
          { "text": "esta se encerrando, ", "bold": true, "cta": false },
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
cd ~/criativos-agent && GEMINI_API_KEY="<config.geminiApiKey>" node generate-urgencia.mjs \
  --input /tmp/ad-urgencia-data.json \
  --output ~/criativos/$(date +%Y-%m-%d)-ads-urgencia/
```

### Passo 5: Entregar
- 4 stories (foto IA) + 4 feeds (texto escuro) = 8 PNGs
- Abrir com `open <path>`

## Sequencia numa campanha
```
Dias 1-4:   /criativos-dor-beneficio-mentorados (gerar desejo)
Dias 3-5:   Mix (dor-beneficio + urgencias suaves)
Dias 5-7:   /criativos-urgencia-mentorados dominante (converter)
Ultimo dia: 100% urgencia + "ultima chance"
```
