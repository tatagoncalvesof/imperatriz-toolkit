---
name: criativos-retargeting
description: Gera criativos Meta Ads de retargeting/pattern interrupt. Formato quadrado 1080x1080 com layout 2 colunas — texto confrontacional à esquerda + expert apontando à direita. Fundo escuro, glow quente. Exclusivo para retargeting.
user_invocable: true
---

# Skill: Criativos Retargeting / Pattern Interrupt (Meta Ads)

Gera criativos de anúncio no formato **Retargeting Confrontacional** — expert apontando pra câmera + texto que CONFRONTA a pessoa sobre seu comportamento (visitou página e não comprou).

## Quando usar
- Retargeting de visitantes da página de vendas
- Retargeting de checkout abandonado
- Retargeting de quem assistiu webinar e não comprou
- Usuario pede "retargeting", "pattern interrupt", "confrontação", "para tudo"
- NUNCA para público frio — EXCLUSIVO retargeting

## Posição no funil (3 formatos complementares)
```
Dias 1-4:  /criativos-dor-beneficio  → Gerar desejo (topo/meio)
Dias 3-5:  /criativos-urgencia       → Pressionar deadline (fundo)
Retarget:  /criativos-retargeting    → Confrontar inação (retargeting)
```

## Stack técnica
- **Gerador:** `node generate-retargeting.mjs --input data.json --output <dir>`
- **Renderer:** `lib/retargeting-render.mjs` (overlay texto + glow)
- **Fotos IA:** Gemini — 1:1, pose confrontacional, expressão SÉRIA
- **Fotos ref:** `~/criativos-agent/assets/expert/foto1-3.png`

## Formato: Quadrado 1080x1080 (feed)

```
┌─────────────────────────────────────────┐
│            LOGO (topo centro)           │
│                                         │
│  ┌─────────────┐  ┌──────────────────┐  │
│  │ ▌Para tudo! │  │                  │  │
│  │             │  │  EXPERT FOTO     │  │
│  │ Você entrou │  │  apontando dedo  │  │
│  │ na page e   │  │  expressão séria │  │
│  │ não garantiu│  │                  │  │
│  │ sua vaga?   │  │     [PLACA       │  │
│  │             │  │      PARE]       │  │
│  │ Vai se      │  │                  │  │
│  │ arrepender! │  │                  │  │
│  │             │  │                  │  │
│  │ Clique em   │  │                  │  │
│  │ saiba mais  │  │                  │  │
│  └─────────────┘  └──────────────────┘  │
│   TEXTO (43%)       EXPERT (57%)        │
└─────────────────────────────────────────┘
```

## Framework de copy — PARE-PROVE-PROVOQUE

### 1. HEADLINE (Interruptor de scroll)
- Max 4 palavras, imperativo + !
- NÃO menciona produto
- Barra vertical colorida (accent bar) à esquerda
- Exemplos: "Para tudo!", "Espera aí!", "Ei, você!", "Volta aqui!", "Sério mesmo?"

### 2. BODY (Acusação comportamental)
- Menciona a AÇÃO que a pessoa fez (pixel rastreou)
- Menciona a ação que NÃO fez
- Termina com ? (interrogação, não afirmação)
- **Negrito** no termo de culpa
- Max 2 linhas
- Fórmula: "Você [AÇÃO QUE FEZ] e **não [AÇÃO ESPERADA]** [OBJETO]?"

### 3. PROVOCAÇÃO (itálico, cor dourada)
- Arrependimento futuro + suavizador coloquial
- Tom de AMIGO que avisa, não juiz que condena
- Suavizadores: "hein!", "tá?", "viu?", "né?"
- Max 1 frase

### 4. CTA (frio, discreto)
- "Clique em saiba mais" / "Volte e garanta" / "Toque no link"
- Baixo atrito — não "compre agora"
- Max 5 palavras

## 4 Variações por tipo de retargeting

### 1. Visitou página e saiu
```
"Para tudo!"
"Você entrou na page e **não garantiu** sua vaga?"
"Vai se arrepender depois, hein!"
```

### 2. Abandonou checkout
```
"Sério mesmo?"
"Você foi até o pagamento e **não finalizou?**"
"Faltou só o clique. Depois não diz que não avisei, tá?"
```

### 3. Assistiu webinar e não comprou
```
"Você assistiu tudo."
"Ficou 2 horas no evento e **não garantiu** sua vaga?"
"Não é falta de interesse. É falta de decisão."
```

### 4. Viu anúncio anterior
```
"Ainda pensando?"
"Já viu sobre a imersão por aqui e **não deu o próximo passo?**"
"O momento certo raramente avisa que chegou."
```

## Regras de copy (OBRIGATÓRIO)
- PT-BR COM ACENTOS
- Tom confrontacional MAS com humor/cumplicidade
- A acusação DEVE ser verdadeira pro público de retargeting
- "hein!", "tá?", "viu?" = suavizadores OBRIGATÓRIOS
- Zero explicação do produto (assume conhecimento)
- Zero urgência de prazo (esse é papel do formato urgência)
- Frequency cap: max 2-3 impressões por pessoa

## Paleta de cores
```json
{
  "bgDark": "#0D0A08",
  "glowColor": "#D4600A",
  "accentBar": "#E8451A",
  "textWhite": "#FFFFFF",
  "textWarm": "#F0EDE8",
  "textGold": "#E8A832",
  "textGray": "#B3AFA8",
  "badgeColor": "#E8871E"
}
```

## Regras de foto
- Formato: **1:1** (quadrado, expert ocupa lado direito)
- Pose: **Apontando dedo pra câmera** / braços cruzados / palma em stop
- Expressão: **SÉRIA, determinada, NUNCA sorrindo**
- Olhar: DIRETO na câmera (contato ocular com o viewer)
- Iluminação: **backlight laranja/dourado dramático** + **fill light frontal FORTE no rosto** (rosto DEVE estar claro e visível, nunca escuro/silhueta)
- Roupa: escura, sem estampas
- Fundo: escuro (integra com bg do criativo)
- Scene prompt SEMPRE incluir: "well-lit face with bright frontal fill light ensuring face is clearly visible"

## Decisões técnicas já resolvidas
- **SEM faixa/banda escura** — foto full bleed, texto com text-shadow (shadowBlur 12, rgba(0,0,0,0.7)) pra legibilidade. Apenas vinheta sutil (45% opacidade máx, gradiente curto)
- **Glow:** camada de glow laranja composta com blend 'screen' ENTRE foto e overlay
- **Headline:** font-size 96px (era 48→72→96, testamos até acertar)
- **Accent bar:** 14px largura (era 6→8→14)
- **Logo:** topo CENTRO (não direita)
- **Texto coluna:** MARGIN 44px, TEXT_COL_END 530px
- **Distribuição vertical:** conteúdo empurrado pra baixo pra preencher canvas sem vazio no fundo

## Workflow

### Passo 1: Identificar tipo de retargeting
- Visitou página? Abandonou checkout? Assistiu webinar? Viu anúncio?

### Passo 2: Gerar 4 variações
Uma por tipo de retargeting.

### Passo 3: JSON
```json
{
  "expertDescription": "Brazilian woman, serious determined expression, dark clothing, natural makeup",
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
        "headline": "Para tudo!",
        "body": "Você entrou na page e **não garantiu** sua vaga?",
        "provocation": "Vai se arrepender depois, hein!",
        "cta": "Clique em saiba mais"
      },
      "scenePrompt": "pointing finger at camera, serious expression, orange backlight, dark background, medium shot"
    }
  ]
}
```

### Passo 4: Executar
```bash
cd ~/criativos-agent && node generate-retargeting.mjs \
  --input /tmp/ad-retargeting-data.json \
  --output ~/criativos/$(date +%Y-%m-%d)-ads-retargeting/
```

### Passo 5: Entregar
- 4 criativos quadrados (1080x1080) prontos pra feed
- Abrir com `open <path>`
