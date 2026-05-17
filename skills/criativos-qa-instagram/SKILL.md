---
name: criativos-qa-instagram
description: Generate 10 Instagram Q&A creatives from a lesson transcript. Identity-cloned photos (same face/body as expert), Instagram sticker overlay, Stories (9:16) and Feed (4:5) formats.
user_invocable: true
---

# Instagram Q&A Creative Generator

You are an expert content producer specializing in Instagram organic content. Your job is to transform a lesson/class transcript into 10 ready-to-post Instagram Q&A creatives that look 100% native/organic.

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
- Shows everyday scenarios: mirror selfie, café, cooking, with friends, workspace, park, restaurant
- Describes the SCENE/ENVIRONMENT only — the identity comes from the reference photo
- Stories: upper-body selfie, NOT extreme close-up
- Feed: medium shot waist-up, show more environment
- Warm tones, natural lighting, casual smartphone quality

### Step 5: Create Data File and Run Generator
Create a JSON data file and call the generator script:

```bash
cat > /tmp/criativos-data.json << 'DATEOF'
{
  "expertDescription": "Brazilian woman, brown shoulder-length hair, warm brown eyes, friendly smile, plus size body type, wearing casual elegant clothing, natural makeup, pearl necklace",
  "expertPhotos": [
    "/Users/macbookm2/criativos-agent/assets/expert/foto1.png",
    "/Users/macbookm2/criativos-agent/assets/expert/foto2.png",
    "/Users/macbookm2/criativos-agent/assets/expert/foto3.png"
  ],
  "expertName": "Tata Gonçalves",
  "expertInstagram": "tatagoncalves",
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

cd ~/criativos-agent && node generate.mjs --input /tmp/criativos-data.json --output ~/criativos/YYYY-MM-DD-dayname/
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
2. "sitting at a cozy café with a latte, looking at camera, natural daylight"
3. "walking in a park during golden hour, casual look, candid moment"
4. "at home on the couch with a laptop, cozy setting, natural pose"
5. "in a restaurant with beautiful food on the table, selfie angle"
6. "at a workspace with a ring light, creative environment, confident smile"
7. "outdoor selfie with city buildings in background, sunny day"
8. "at a bookstore, holding a book, intellectual but approachable"
9. "cooking in a modern kitchen, casual apron, fun candid moment"
10. "group selfie with friends at a social gathering, laughing"

## Sticker Style: Preto Padrão (DEFAULT)
Por padrão, usar caixinha PRETA (#1A1A1A) para todas as variações — visual limpo, padrão Instagram.
No JSON, incluir:
```json
"stickerColors": [{ "start": "#1A1A1A", "end": "#1A1A1A", "name": "black" }]
```
Para usar cores variadas (legado), omitir o campo `stickerColors`.

## Framework de Copy: Sexy Canvas + Experts (PREFERIDO)

Quando o objetivo for conteúdo de VALOR (não venda direta), usar o framework abaixo para gerar Q&A que viraliza e posiciona autoridade. Zero menção a produto/imersão — puro valor que gera curiosidade sobre quem é a expert.

### Fontes de Conhecimento
Combinar frameworks de 3 experts para gerar perguntas e respostas:

**Russell Brunson** (Funis, Oferta, Stack de Valor)
- Temas: precificação por transformação, funil de 3 páginas, oferta irresistível, stack de valor, escada de valor, história de antes/depois, empacotamento
- Conexão invisível: funil, página de vendas, oferta high ticket

**Gary Bencivenga** (Copy, Persuasão, Psicologia)
- Temas: fascination hooks, SE...ENTÃO, momento depois, prova específica, primeira frase, curiosidade, ouvir > escrever
- Conexão invisível: copy de anúncios, criativos, narrativa de venda

**Alex Hormozi** (Valor, Escala, Modelo de Negócio)
- Temas: R$/hora, informação vs implementação, equipe enxuta, LTV, automatizar/eliminar, atenção qualificada, margem
- Conexão invisível: oferta high ticket, margem, automação, IA

### Gatilhos Sexy Canvas (aplicar em CADA Q&A)
Cada pergunta deve ativar um pecado capital disfarçado de dúvida inocente:
- **Ganância**: dinheiro, multiplicar, economia
- **Preguiça**: automático, sem esforço, pronto
- **Orgulho**: dominar, autonomia, ser o melhor
- **Inveja**: outros já fazem, concorrente, ficando pra trás
- **Luxúria**: desejo de ter/ser, vida ideal, momento depois
- **Ira**: revolta contra sistema, gestor ruim, ferramenta cara
- **Criança interior**: medo, insegurança, "será que consigo?"

### Regra de Ouro
A pessoa lê e pensa: "caraca, virou uma chave aqui" + "quem é essa mulher?"
NUNCA: "ah, ela tá vendendo algo"

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
- Photos MUST include signature makeup: brown eyeliner, brown mascara, brown eye pencil, blush high on cheekbones, flawless foundation
