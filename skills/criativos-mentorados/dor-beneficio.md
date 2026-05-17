---
name: criativos-dor-beneficio-mentorados
description: >
  Versao para MENTORADOS da skill criativos-dor-beneficio.
  Gera criativos Meta Ads no formato Dor -> Beneficio. Stories (1080x1920) com foto IA clonada + Feed (1080x1350) texto puro.
  3 variacoes com angulos diferentes. Pronto pra subir em campanhas.
  Usa as fotos e chave Gemini do mentorado salvas em ~/.criativos-mentorados/config.json.
  Se o config nao existir, roda o onboarding primeiro (/criativos-mentorados-setup).
  Use quando o mentorado pedir "criativo dor beneficio", "anuncio dor", "ad creative dor beneficio".
user_invocable: true
---

# Skill: Criativos Dor -> Beneficio (Meta Ads) — VERSAO MENTORADOS

Gera criativos de anuncio no formato **Dor -> Beneficio** com 2 formatos independentes:
- **Story (1080x1920):** Foto do expert clonada por IA (Gemini) no topo + copy embaixo
- **Feed (1080x1350):** Layout texto puro (sem foto) — header escuro + copy que CABE inteira

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

Ao longo de TODA esta skill, onde aparecer referencia a fotos ou chave, usar os dados do config:

| Original (Tata) | Mentorado |
|---|---|
| `~/criativos-agent/assets/expert/foto1-3.png` | Valor de `config.expertPhotos` |
| `GEMINI_API_KEY` do `.env` | Valor de `config.geminiApiKey` |
| `expertDescription` hardcoded | Valor de `config.expertDescription` |
| `expertName` "Tata Goncalves" | Valor de `config.expertName` |

## Stack tecnica
- **Projeto:** `~/criativos-agent/`
- **Gerador:** `node generate-dor-beneficio.mjs --input data.json --output <dir>`
- **Renderer Story:** `lib/dor-beneficio-render.mjs` (Canvas + Sharp — foto + overlay)
- **Renderer Feed:** `lib/dor-beneficio-feed-render.mjs` (Canvas — texto puro, sem foto)
- **Fotos IA:** Gemini 2.5 Flash Image com identity preservation (inlineData)
- **Fotos de referencia:** Lidas de `~/.criativos-mentorados/config.json` → campo `expertPhotos`
- **API Key Gemini:** Lida de `~/.criativos-mentorados/config.json` → campo `geminiApiKey`
- **Fontes:** Inter (Regular, Medium, SemiBold, Bold) em `~/criativos-agent/fonts/`

## Formatos de output

### Story (1080x1920) — COM foto IA
```
┌──────────────────────────────┐
│        FOTO DO EXPERT        │ <- 40% topo (768px) — foto 16:9
│     (gerada por Gemini)      │   fitted na zona, SEM crop no rosto
│                              │
│   [PRODUTO]                  │ <- overlay: logo + badge sobre a foto
│   [SUBTITULO]                │   fade gradiente foto → fundo bege
│   [BADGE]                    │
├──────────────────────────────┤
│ X Dor 1                      │ <- caixas bordo, icone X, bold
│ X Dor 2                      │
│ X Dor 3                      │
├──────────────────────────────┤
│   Frase de transicao         │ <- texto escuro centralizado
├──────────────────────────────┤
│ V Beneficio 1                │ <- caixas verde-escuro, check, bold
│ V Beneficio 2                │
│ V Beneficio 3                │
├──────────────────────────────┤
│   CTA + Botao                │
└──────────────────────────────┘
```

### Feed (1080x1350) — SEM foto, texto puro
```
┌──────────────────────────────┐
│ ████████████████████████████ │ <- header escuro dinamico (200-380px)
│   [PRODUTO]                  │   expande pra preencher espaco
│   [SUBTITULO]                │   logo + badge centralizados
│   [BADGE]                    │
├──────────────────────────────┤
│ X Dor 1                      │ <- fundo bege claro
│ X Dor 2                      │   TODA a copy cabe sem cortes
│ X Dor 3                      │
├──────────────────────────────┤
│   Frase de transicao         │
├──────────────────────────────┤
│ V Beneficio 1                │
│ V Beneficio 2                │
│ V Beneficio 3                │
├──────────────────────────────┤
│   CTA + Botao                │
└──────────────────────────────┘
```

**Naming:** `01-ad-dor-beneficio-1080x1920.png` (story) + `01-ad-dor-beneficio-1080x1350.png` (feed)
**Diretorio:** `~/criativos/<YYYY-MM-DD>-ads-dor-beneficio/`

## DECISOES TECNICAS JA RESOLVIDAS (seguir sempre)

### Foto do expert no Story
- **Aspect ratio da foto: 16:9** (NAO 9:16). A zona da foto ocupa 40% do topo (1080x768px), proporcao ~16:9. Gerar foto 9:16 causa crop agressivo mostrando so a testa.
- **Fitting:** Redimensionar a foto pra 1080x768 (`sharp.resize(1080, 768, fit: cover, position: top)`), depois colocar no topo de um canvas transparente 1080x1920. O overlay eh composto por cima.
- **Cadeia de fallback:** Gemini 2.5 Flash → 3.1 Flash → Imagen 4.0 → foto real redimensionada

### Feed sem foto
- O feed (1080x1350) usa renderer PROPRIO (`dor-beneficio-feed-render.mjs`), NAO eh crop do story.
- Sem foto do expert — so header escuro com logo + bullets + CTA em fundo bege.
- Header dinamico: calcula a altura total do conteudo e expande o header pra preencher o espaco restante (min 200px, max 380px). Isso evita espaco vazio embaixo.

### Acentos (OBRIGATORIO)
- TODA copy DEVE ter acentos corretos em PT-BR: e, e, a, o, c, i, o, u, a
- "Negocio", "Confianca", "voce", "pagina", "dominio", "anuncios", "trafego", "execucao", "constancia"
- NUNCA gerar copy sem acentos. Se o usuario fornecer sem acentos, adicionar.

## REGRA: 3 Variacoes com angulos DIFERENTES

SEMPRE gerar 3 variacoes, cada uma atacando um angulo distinto de dor/desejo:

### Variacao 1 — Angulo FINANCEIRO
- **Dores:** dinheiro perdido com freelancers, ferramentas caras, cursos que nao deram resultado
- **Desejos:** economia, ROI, parar de gastar e comecar a lucrar, IA trabalhando de graca
- **Tom:** "Chega de pagar...", "Ferramenta cara que...", "Curso que termina e..."

### Variacao 2 — Angulo TEMPO/AUTONOMIA
- **Dores:** demora pra ter resultado, depender dos outros, travar na execucao
- **Desejos:** velocidade, independencia, fazer sozinha, resultado rapido
- **Tom:** "Meses esperando...", "Depende de terceiros...", "Sabe o que quer mas trava..."

### Variacao 3 — Angulo STATUS/CREDIBILIDADE
- **Dores:** concorrentes vendendo, se sentir atrasada, falta de credibilidade profissional
- **Desejos:** posicionamento, autoridade, confianca, ser vista como referencia
- **Tom:** "Ve concorrentes vendendo...", "Sente que esta atrasada...", "Nao passa credibilidade..."

### Regra dos abridores
- "Chega de" so na PRIMEIRA dor da variacao 1
- Variar abridores nas outras: "Meses esperando...", "Depende de...", "Ve...", "Sente que..."
- NUNCA repetir o mesmo abridor nas 3 variacoes

## Framework de copy

### Bullets de dor (X)
- Maximo **55 caracteres** por bullet (sem contar `**`)
- **Negrito** em 1-2 termos de maior peso emocional
- Cada bullet deve caber em 1 linha no celular

### Frase de transicao
- Pode variar entre as 3 variacoes (NAO precisa ser identica)
- Prazo SEMPRE < 7 dias e numerico
- "vai sair com" / "voce sai com" = certeza

### Bullets de beneficio (V)
- Maximo **55 caracteres** por bullet
- Progressao: tangivel → alavanca → emocional
- **Negrito** no termo mais forte de cada bullet

### CTA
- Verbo de PROTECAO: Garanta, Reserve (NUNCA "Compre")
- Reframe: "vaga", "lugar" (NUNCA "acesso", "curso")
- Pode variar o CTA entre variacoes

### Regras gerais de copy
- PT-BR COM ACENTOS (obrigatorio)
- Tom direto, zero adjetivos decorativos
- Linguagem de mensagem de texto (informal)
- Sem exclamacoes excessivas

## Temas de cor

### Default (Vermelho/Verde)
```json
{
  "bgDark": "#1A1210", "bgLight": "#F5F0E8",
  "painBg": "rgba(74, 14, 14, 0.88)", "painBorder": "#8B1A1A", "painIcon": "#E53535",
  "benefitBg": "rgba(10, 61, 31, 0.88)", "benefitBorder": "#1B8C4A", "benefitIcon": "#34C759",
  "badgeColor": "#D42B2B"
}
```

### Tema Luxo (Dourado/Preto)
```json
{
  "bgDark": "#0A0A0A", "bgLight": "#1A1A1A",
  "painBg": "rgba(80, 20, 20, 0.9)", "painBorder": "#8B3030", "painIcon": "#FF4444",
  "benefitBg": "rgba(20, 60, 20, 0.9)", "benefitBorder": "#2D8B2D", "benefitIcon": "#44CC44",
  "badgeColor": "#D4AF37", "backlight": "rgba(212, 175, 55, 0.3)"
}
```

### Tema Azul Corporate
```json
{
  "bgDark": "#0D1B2A", "bgLight": "#E8EEF5",
  "painBg": "rgba(74, 14, 14, 0.88)", "painBorder": "#8B1A1A", "painIcon": "#E53535",
  "benefitBg": "rgba(10, 40, 80, 0.88)", "benefitBorder": "#1B4A8C", "benefitIcon": "#3498DB",
  "badgeColor": "#2980B9"
}
```

## Cenas para foto IA (Stories)
Sempre incluir "medium shot waist up" no prompt pra garantir enquadramento correto.
1. Palco profissional com headset, plateia atras — autoridade maxima
2. Estudio tech com telas/dashboards atras — tecnologia
3. Home office premium, luz natural da janela — autonomia
4. Palco minimalista com microfone e spotlight — credibilidade
5. Workshop com laptop e gesto de ensino — expertise
6. Escritorio premium com vista da cidade — sucesso

## Regras de foto (identity preservation)
- Mesma face, corpo, pele, cabelo da foto de referencia
- DEVE parecer foto real de smartphone — SEM "AI plastic look"
- Preservar imperfeicoes naturais
- Maquiagem conforme descricao do mentorado no config (se houver)

## Workflow completo

### Passo 0: Ler config do mentorado
```bash
cat ~/.criativos-mentorados/config.json
```
Se nao existir → rodar `/criativos-mentorados-setup` primeiro.

Extrair e guardar:
- `EXPERT_NAME` = config.expertName
- `EXPERT_DESC` = config.expertDescription
- `EXPERT_PHOTOS` = config.expertPhotos (array de paths)
- `GEMINI_KEY` = config.geminiApiKey

### Passo 1: Coletar info do produto
Perguntar se nao fornecido:
- Nome do produto/evento
- Badge (data, edicao, turma)
- O que o produto entrega (pra gerar beneficios)
- Publico-alvo (pra gerar dores certeiras)
- Prazo de transformacao

### Passo 2: Gerar 3 variacoes de copy
Criar copy nos 3 angulos (financeiro, tempo, status) seguindo as regras acima.
SEMPRE com acentos corretos.

### Passo 3: Montar JSON de input
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
        "pains": [
          "Chega de pagar **freelancer** que nao entrega.",
          "Ferramenta cara que voce usa **3% do potencial.**",
          "**Curso** que termina e o negocio continua parado."
        ],
        "transition": "Se voce garantir sua vaga agora,\nna segunda-feira voce sai com:",
        "benefits": [
          "**Equipe de IA** trabalhando por voce 24h.",
          "Pagina de vendas no ar e **recebendo cliques.**",
          "Zero freelancer — **voce controla tudo.**"
        ],
        "ctaText": "Garanta sua vaga.",
        "ctaButton": "Garanta sua vaga"
      },
      "scenePrompt": "on a professional stage with headset microphone, warm golden stage lighting, confident smile, medium shot waist up"
    }
  ]
}
```

**IMPORTANTE:** Antes de executar, criar um `.env` temporario com a chave do mentorado:
```bash
GEMINI_API_KEY_BACKUP=$(grep GEMINI_API_KEY ~/criativos-agent/.env 2>/dev/null | cut -d= -f2)
echo "Usando chave Gemini do mentorado..."
```

O gerador usa a env var `GEMINI_API_KEY`. Setar antes de rodar:
```bash
export GEMINI_API_KEY="<valor do config.geminiApiKey>"
```

### Passo 4: Executar
```bash
cd ~/criativos-agent && GEMINI_API_KEY="<config.geminiApiKey>" node generate-dor-beneficio.mjs \
  --input /tmp/ad-dor-beneficio-data.json \
  --output ~/criativos/$(date +%Y-%m-%d)-ads-dor-beneficio/
```

### Passo 5: Entregar
- Mostrar as imagens ao usuario (Read nos PNGs)
- Abrir pasta com `open <path>`
- Confirmar: 3 stories (com foto) + 3 feeds (texto puro) = 6 PNGs

## Output total por execucao
- 3x Story (1080x1920) — cada angulo com foto IA diferente
- 3x Feed (1080x1350) — cada angulo com layout texto puro
- 1x resumo.json
- **Total: 6 criativos prontos pra Meta Ads**
