---
name: criativos-retargeting-mentorados
description: >
  Versao para MENTORADOS da skill criativos-retargeting.
  Gera criativos Meta Ads de retargeting/pattern interrupt. Formato quadrado 1080x1080 com layout 2 colunas —
  texto confrontacional a esquerda + expert apontando a direita. Fundo escuro, glow quente.
  Usa as fotos e chave Gemini do mentorado salvas em ~/.criativos-mentorados/config.json.
  Se o config nao existir, roda o onboarding primeiro (/criativos-mentorados-setup).
  Use quando o mentorado pedir "retargeting", "pattern interrupt", "confrontacao", "para tudo ads".
user_invocable: true
---

# Skill: Criativos Retargeting / Pattern Interrupt (Meta Ads) — VERSAO MENTORADOS

Gera criativos de anuncio no formato **Retargeting Confrontacional** — expert apontando pra camera + texto que CONFRONTA a pessoa sobre seu comportamento (visitou pagina e nao comprou).

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
- Retargeting de visitantes da pagina de vendas
- Retargeting de checkout abandonado
- Retargeting de quem assistiu webinar e nao comprou
- Usuario pede "retargeting", "pattern interrupt", "confrontacao", "para tudo"
- NUNCA para publico frio — EXCLUSIVO retargeting

## Posicao no funil (3 formatos complementares)
```
Dias 1-4:  /criativos-dor-beneficio-mentorados  → Gerar desejo (topo/meio)
Dias 3-5:  /criativos-urgencia-mentorados       → Pressionar deadline (fundo)
Retarget:  /criativos-retargeting-mentorados    → Confrontar inacao (retargeting)
```

## Stack tecnica
- **Gerador:** `node generate-retargeting.mjs --input data.json --output <dir>`
- **Renderer:** `lib/retargeting-render.mjs` (overlay texto + glow)
- **Fotos IA:** Gemini — 1:1, pose confrontacional, expressao SERIA
- **Fotos ref:** Lidas de `~/.criativos-mentorados/config.json` → campo `expertPhotos`
- **API Key Gemini:** Lida de `~/.criativos-mentorados/config.json` → campo `geminiApiKey`

## Formato: Quadrado 1080x1080 (feed)

```
┌─────────────────────────────────────────┐
│            LOGO (topo centro)           │
│                                         │
│  ┌─────────────┐  ┌──────────────────┐  │
│  │ ▌Para tudo! │  │                  │  │
│  │             │  │  EXPERT FOTO     │  │
│  │ Voce entrou │  │  apontando dedo  │  │
│  │ na page e   │  │  expressao seria │  │
│  │ nao garantiu│  │                  │  │
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
- NAO menciona produto
- Barra vertical colorida (accent bar) a esquerda
- Exemplos: "Para tudo!", "Espera ai!", "Ei, voce!", "Volta aqui!", "Serio mesmo?"

### 2. BODY (Acusacao comportamental)
- Menciona a ACAO que a pessoa fez (pixel rastreou)
- Menciona a acao que NAO fez
- Termina com ? (interrogacao, nao afirmacao)
- **Negrito** no termo de culpa
- Max 2 linhas
- Formula: "Voce [ACAO QUE FEZ] e **nao [ACAO ESPERADA]** [OBJETO]?"

### 3. PROVOCACAO (italico, cor dourada)
- Arrependimento futuro + suavizador coloquial
- Tom de AMIGO que avisa, nao juiz que condena
- Suavizadores: "hein!", "ta?", "viu?", "ne?"
- Max 1 frase

### 4. CTA (frio, discreto)
- "Clique em saiba mais" / "Volte e garanta" / "Toque no link"
- Baixo atrito — nao "compre agora"
- Max 5 palavras

## 4 Variacoes por tipo de retargeting

### 1. Visitou pagina e saiu
```
"Para tudo!"
"Voce entrou na page e **nao garantiu** sua vaga?"
"Vai se arrepender depois, hein!"
```

### 2. Abandonou checkout
```
"Serio mesmo?"
"Voce foi ate o pagamento e **nao finalizou?**"
"Faltou so o clique. Depois nao diz que nao avisei, ta?"
```

### 3. Assistiu webinar e nao comprou
```
"Voce assistiu tudo."
"Ficou 2 horas no evento e **nao garantiu** sua vaga?"
"Nao e falta de interesse. E falta de decisao."
```

### 4. Viu anuncio anterior
```
"Ainda pensando?"
"Ja viu sobre a imersao por aqui e **nao deu o proximo passo?**"
"O momento certo raramente avisa que chegou."
```

## Regras de copy (OBRIGATORIO)
- PT-BR COM ACENTOS
- Tom confrontacional MAS com humor/cumplicidade
- A acusacao DEVE ser verdadeira pro publico de retargeting
- "hein!", "ta?", "viu?" = suavizadores OBRIGATORIOS
- Zero explicacao do produto (assume conhecimento)
- Zero urgencia de prazo (esse e papel do formato urgencia)
- Frequency cap: max 2-3 impressoes por pessoa

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
- Pose: **Apontando dedo pra camera** / bracos cruzados / palma em stop
- Expressao: **SERIA, determinada, NUNCA sorrindo**
- Olhar: DIRETO na camera (contato ocular com o viewer)
- Iluminacao: **backlight laranja/dourado dramatico** + **fill light frontal FORTE no rosto** (rosto DEVE estar claro e visivel, nunca escuro/silhueta)
- Roupa: escura, sem estampas
- Fundo: escuro (integra com bg do criativo)
- Scene prompt SEMPRE incluir: "well-lit face with bright frontal fill light ensuring face is clearly visible"

## Decisoes tecnicas ja resolvidas
- **SEM faixa/banda escura** — foto full bleed, texto com text-shadow (shadowBlur 12, rgba(0,0,0,0.7)) pra legibilidade. Apenas vinheta sutil (45% opacidade max, gradiente curto)
- **Glow:** camada de glow laranja composta com blend 'screen' ENTRE foto e overlay
- **Headline:** font-size 96px (era 48→72→96, testamos ate acertar)
- **Accent bar:** 14px largura (era 6→8→14)
- **Logo:** topo CENTRO (nao direita)
- **Texto coluna:** MARGIN 44px, TEXT_COL_END 530px
- **Distribuicao vertical:** conteudo empurrado pra baixo pra preencher canvas sem vazio no fundo

## Workflow

### Passo 0: Ler config do mentorado
```bash
cat ~/.criativos-mentorados/config.json
```
Se nao existir → rodar `/criativos-mentorados-setup` primeiro.

### Passo 1: Identificar tipo de retargeting
- Visitou pagina? Abandonou checkout? Assistiu webinar? Viu anuncio?

### Passo 2: Gerar 4 variacoes
Uma por tipo de retargeting.

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
        "headline": "Para tudo!",
        "body": "Voce entrou na page e **nao garantiu** sua vaga?",
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
cd ~/criativos-agent && GEMINI_API_KEY="<config.geminiApiKey>" node generate-retargeting.mjs \
  --input /tmp/ad-retargeting-data.json \
  --output ~/criativos/$(date +%Y-%m-%d)-ads-retargeting/
```

### Passo 5: Entregar
- 4 criativos quadrados (1080x1080) prontos pra feed
- Abrir com `open <path>`
