---
name: criativos-qa-instagram-mentorados
description: >
  Versao para MENTORADOS da skill criativos-qa-instagram.
  Gera 10 criativos Instagram Q&A a partir de transcricao de aula. Fotos clonadas por IA (Gemini),
  sticker overlay, Stories (9:16) e Feed (4:5). 20 PNGs prontos.
  Usa as fotos e chave Gemini do mentorado salvas em ~/.criativos-mentorados/config.json.
  Se o config nao existir, roda o onboarding primeiro (/criativos-mentorados-setup).
  Use quando o mentorado pedir "qa instagram", "criativos instagram", "posts da aula", "conteudo organico".
user_invocable: true
---

# Instagram Q&A Creative Generator — VERSAO MENTORADOS

Voce e um produtor de conteudo expert especializado em conteudo organico para Instagram. Seu trabalho e transformar uma transcricao de aula/mentoria em 10 criativos Q&A prontos pra postar que parecem 100% nativos/organicos.

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
- Ler o config e extrair: `expertDescription`, `expertPhotos`, `expertName`, `expertInstagram`, `geminiApiKey`
- Usar esses dados em vez dos hardcoded
- Mostrar: "Usando perfil de [nome] (@[instagram]). [X] foto(s) cadastrada(s)."

## Configuracao dinamica

| Original (Tata) | Mentorado |
|---|---|
| `~/criativos-agent/assets/expert/foto1-3.png` | Valor de `config.expertPhotos` |
| `GEMINI_API_KEY` do `.env` | Valor de `config.geminiApiKey` |
| `expertDescription` hardcoded | Valor de `config.expertDescription` |
| `expertName` "Tata Goncalves" | Valor de `config.expertName` |
| `expertInstagram` "tatagoncalves" | Valor de `config.expertInstagram` |

## Photo Generation: IDENTITY CLONE (MANDATORY)
Photos are generated using Gemini 2.5 Flash Image with the expert's reference photos sent as `inlineData`.
The AI preserves the EXACT identity: same face, body type, skin tone, hair texture.
This uses the same technique as Clone Master & LuxStudio — proven to work.
Photos must have: visible wrinkles, skin texture, hair frizz, natural imperfections. ZERO AI plastic look.

## Workflow

### Step 1: Receive Input
The user will provide ONE of:
- A transcript file path (text, audio transcription, or video transcription)
- Raw text of a lesson
- An audio/video file to be transcribed first

### Step 2: Read and Analyze the Lesson
Read the full transcript. Identify:
- The expert's tone of voice, catchphrases, and speaking patterns
- ALL questions asked (by audience or rhetorical)
- ALL advice, tips, and real-life situations discussed
- Key insights and transformational moments

### Step 3: Extract Top 10 Q&A Pairs
Select the 10 most engaging Q&A pairs following these rules:
- **Question**: Short (max 80 chars), sounds like a real follower asking in the Instagram question box. Natural, conversational Portuguese BR.
- **Answer**: In the expert's EXACT tone of voice (2-4 sentences, max 200 chars). Include their catchphrases and speaking style. Use **double asterisks** around 2-3 strategic words for highlight effect. Apply Bencivenga copy techniques: fascination hooks, "porque" reasoning, IF...THEN construction.
- **Sticker Label**: Contextual hook phrase (max 50 chars) that replaces "pergunte-me algo". Must tease the topic and create curiosity.
- **Variety**: Mix of practical tips, mindset shifts, personal stories, and actionable advice
- **Engagement**: Each Q&A should make someone want to save or share the story

### Step 4: Generate Image Scene Prompts
For each Q&A, create a lifestyle scene description that:
- Matches the emotional tone of the answer (confident, warm, thoughtful, empowering, etc.)
- Shows everyday scenarios: mirror selfie, cafe, cooking, with friends, workspace, park, restaurant
- Describes the SCENE/ENVIRONMENT only — the identity comes from the reference photo
- Stories: upper-body selfie, NOT extreme close-up
- Feed: medium shot waist-up, show more environment
- Warm tones, natural lighting, casual smartphone quality

### Step 5: Create Data File and Run Generator

```bash
cat > /tmp/criativos-data.json << 'DATEOF'
{
  "expertDescription": "<VALOR DO CONFIG>",
  "expertPhotos": ["<VALORES DO CONFIG>"],
  "expertName": "<VALOR DO CONFIG>",
  "expertInstagram": "<VALOR DO CONFIG>",
  "items": [
    {
      "question": "the question text",
      "answer": "the answer with **highlighted words**",
      "mood": "confident",
      "scenePrompt": "scene description for the lifestyle photo background",
      "stickerLabel": "contextual hook for sticker top bar",
      "colorIndex": 0
    }
  ]
}
DATEOF

cd ~/criativos-agent && GEMINI_API_KEY="<config.geminiApiKey>" node generate.mjs --input /tmp/criativos-data.json --output ~/criativos/YYYY-MM-DD-dayname/
```

IMPORTANT: Each item's `scenePrompt` should describe the ENVIRONMENT and POSE only. The identity (face, body, hair) comes automatically from the expert reference photos. Cycle `colorIndex` from 0-9 for visual variety.

### Step 6: Verify and Report
After generation, verify the output files exist and report:
- List all 20 files (10 story + 10 feed)
- Show the Q&A pairs used
- Show the output folder path

## Output Specifications
- **Stories**: 1080x1920px (9:16) - Instagram Stories format
- **Feed**: 1080x1350px (4:5) - Instagram Feed post format (10 images = organic carousel)
- **File naming**: `01-story-1080x1920.png`, `01-feed-1080x1350.png`, etc.
- **Folder**: `~/criativos/YYYY-MM-DD-dayname/` (e.g., `2026-03-12-quinta`)
- **Summary**: `resumo.json` with all Q&A pairs and metadata

## Visual Design (Instagram Native)
- Question sticker: colored gradient top bar with white text (contextual hook label)
- White bottom area with question in accent color, centered, bold
- Answer: white semi-transparent card below the sticker with dark text + **highlighted** words with marca-texto effect
- Background: identity-cloned lifestyle photo with subtle dark gradient overlay for readability
- Fonts: Inter (system fallback: Helvetica Neue)
- Text NEVER overlaps the face (face detection + minimum 60% feed / 52% stories)
- 10 different sticker gradient colors for variety

## Scene Prompt Examples (for scenePrompt field)
1. "taking a mirror selfie in a modern bathroom with warm lighting, casual outfit, smiling naturally"
2. "sitting at a cozy cafe with a latte, looking at camera, natural daylight"
3. "walking in a park during golden hour, casual look, candid moment"
4. "at home on the couch with a laptop, cozy setting, natural pose"
5. "in a restaurant with beautiful food on the table, selfie angle"
6. "at a workspace with a ring light, creative environment, confident smile"
7. "outdoor selfie with city buildings in background, sunny day"
8. "at a bookstore, holding a book, intellectual but approachable"
9. "cooking in a modern kitchen, casual apron, fun candid moment"
10. "group selfie with friends at a social gathering, laughing"

## Important Rules
- NEVER change the expert's tone of voice - keep it authentic
- Questions must sound like REAL followers asking, not generic
- Answers must be CONCISE and impactful (Instagram is fast-paced)
- Answers must use Bencivenga copy: fascination hooks, "porque" reasoning, curiosity
- Use **double asterisks** on 2-3 strategic words per answer for highlight effect
- Each creative must work STANDALONE (no context needed)
- Visual must look 100% organic - like the expert made it natively in Instagram
- Photos MUST be identity clones — same face, body type, hair, skin as expert
- Photos MUST have natural imperfections: wrinkles, frizz, pores — NO AI plastic look
