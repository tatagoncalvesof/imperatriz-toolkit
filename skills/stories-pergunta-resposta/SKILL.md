---
name: stories-pergunta-resposta
description: Gera 10 stories Instagram (9:16) de Pergunta e Resposta com identidade clonada da Tata Gonçalves — cenários FECHADOS (dentro do carro com banco de couro caramelo OU escritório com mesa ipê e iluminação amarela), colar de ouro com esmeralda + joias douradas, maquiagem leve com blush Dior, iluminação dourada na pele, caixinha de pergunta NUNCA sobre o rosto. Use quando a Tata pedir "stories de pergunta e resposta", "Q&A pra story", "perguntinhas", "caixinha de perguntas" ou "10 stories de perguntas". APENAS Stories — não gera feed.
---

# Stories Pergunta e Resposta — Tata Gonçalves

Gerador de **10 stories nativos** de Pergunta e Resposta a partir de uma aula/live/mentoria da Tata. Cada story = 1 pergunta + 1 resposta + foto da Tata em cenário fechado, com regras visuais não-negociáveis.

## Restrições não-negociáveis

Estas regras existem para preservar a identidade visual da Tata. Aplique em TODA pergunta gerada.

1. **Apenas Stories 1080x1920 (9:16)**. NÃO gera Feed 4:5.
2. **Apenas 2 cenários**: dentro do carro (banco couro caramelo) OU escritório (mesa ipê + estante nichos com plantas + iluminação amarela). Veja [references/cenarios.md](references/cenarios.md).
3. **Joias obrigatórias em TODA foto**: colar de ouro com esmeralda pequenina + outras joias douradas. Veja [references/identidade-tata.md](references/identidade-tata.md).
4. **Maquiagem**: leve, blush Dior, iluminação dourada na pele.
5. **Caixinha de pergunta JAMAIS sobre o rosto**. Posicione SEMPRE abaixo do rosto. Margem de segurança: caixinha começa em 60% da altura (rosto fica nos 30-50% superiores).
6. **Cores e fontes**: Design System Tata (Direção A — IA com Alma como default). Veja [references/design-system.md](references/design-system.md).
7. **Foto = celular, não estúdio**: pele com poros, cabelo com frizz, leve ruído de câmera. NUNCA visual plástico/IA.
8. **Corpo idêntico à referência**: NUNCA emagrecer, alterar curvas ou idealizar.

## Workflow

### Passo 1 — Receber input
A Tata vai mandar UMA das opções:
- Caminho de transcrição de aula/live/mentoria
- Texto cru de aula
- Arquivo de áudio/vídeo (transcreva primeiro)

Pergunte se necessário: "Qual é a aula/live? Manda o link ou arquivo da transcrição."

### Passo 2 — Ler e analisar
Leia a transcrição inteira. Extraia:
- Tom de voz da Tata, bordões, frases típicas
- TODAS as perguntas (do público ou retóricas)
- TODOS os conselhos, dicas, situações reais discutidas
- Insights transformacionais

### Passo 3 — Extrair 10 pares Q&A
Selecione os 10 pares mais engajantes seguindo as regras de [references/copy-qa.md](references/copy-qa.md):

- **Pergunta**: max 80 caracteres, soa como seguidor real, português coloquial BR
- **Resposta**: max 200 caracteres, tom da Tata, com `**palavras**` em asteriscos pra marca-texto (2-3 por resposta)
- **Label do sticker**: hook contextual de até 50 caracteres (substitui "pergunte-me algo")
- **Variedade**: mix de dica prática + mudança de mentalidade + história + insight contraintuitivo
- **Sexy Canvas**: cada Q&A ativa um pecado capital disfarçado de dúvida inocente

### Passo 4 — Atribuir cenário a cada Q&A
Distribua os 10 Q&As entre os 2 cenários (~5 e ~5):
- **Carro** (`scenario: "carro"`): perguntas íntimas, confessionais, "no caminho", reflexões
- **Escritório** (`scenario: "escritorio"`): perguntas de execução, estratégia, ensino, autoridade

Cada item do JSON precisa do campo `scenario` ("carro" ou "escritorio"). Veja [references/cenarios.md](references/cenarios.md) para escolher pose e enquadramento dentro de cada cenário.

### Passo 5 — Montar JSON e rodar gerador

```bash
cat > /tmp/stories-qa-data.json << 'DATEOF'
{
  "expertDescription": "Brazilian woman, brown shoulder-length hair with frizz and natural movement, warm brown eyes, friendly smile, plus size body type, GOLD necklace with small emerald pendant, gold rings and gold earrings, light makeup with Dior blush, dewy golden-lit skin",
  "expertPhotos": [
    "/Users/tamiresgoncalves/criativos-agent/assets/expert/foto1.png",
    "/Users/tamiresgoncalves/criativos-agent/assets/expert/foto2.png",
    "/Users/tamiresgoncalves/criativos-agent/assets/expert/foto3.png"
  ],
  "expertName": "Tata Gonçalves",
  "expertInstagram": "tatagoncalves",
  "format": "stories-only",
  "outputFormats": ["story"],
  "stickerColors": [{ "start": "#0A1020", "end": "#0A1020", "name": "ink" }],
  "highlightColor": "#D6A648",
  "fontFamily": "Inter",
  "facePositionRule": "face-top-30-50pct",
  "stickerPositionRule": "below-60pct",
  "items": [
    {
      "question": "como você começou sem ninguém apoiar?",
      "answer": "Comecei **sozinha**, sem grupo, sem palmas. A diferença é que eu **não esperei** os outros aprovarem.",
      "mood": "reflective",
      "scenario": "carro",
      "scenePrompt": "sitting in driver's seat of car, golden hour light through windshield, warm caramel leather seat visible, hand on steering wheel, looking at camera over shoulder, candid iPhone selfie quality",
      "stickerLabel": "sobre começar do zero...",
      "colorIndex": 0
    }
  ]
}
DATEOF

cd ~/criativos-agent && node generate.mjs --input /tmp/stories-qa-data.json --output ~/criativos/YYYY-MM-DD-stories-qa/
```

**Importante**: o `scenePrompt` descreve APENAS ambiente + pose + iluminação — a identidade vem das fotos de referência. Veja prompts prontos em [references/cenarios.md](references/cenarios.md).

### Passo 6 — Verificar e relatar
Após gerar:
- Lista os 10 PNGs de story (1080x1920)
- Mostra os pares Q&A usados
- Mostra o caminho da pasta de saída
- Confirma que NENHUMA caixinha está sobre o rosto

Se algum story tiver a caixinha cobrindo o rosto, regere ESSE story específico ajustando o `scenePrompt` para deixar mais espaço inferior.

## Layout do story (composição visual)

```
┌─────────────────────────────┐
│                             │
│        [ROSTO DA TATA]      │  ← 30-50% (rosto livre, joias visíveis)
│                             │
│                             │
│  ┌───────────────────────┐  │  ← 60% — começa a caixinha
│  │ ▌▌▌ sobre começar...  │  │  ← Sticker (label + pergunta)
│  │ Como você começou?    │  │
│  └───────────────────────┘  │
│                             │
│  ┌───────────────────────┐  │
│  │ Comecei [sozinha], sem │  │  ← Card resposta
│  │ grupo. A diferença é   │  │     (marca-texto gold)
│  │ que [não esperei].     │  │
│  └───────────────────────┘  │
│                             │
└─────────────────────────────┘
```

**Sticker**: card cream (#FAF7F0) com barra superior ink (#0A1020), pergunta em ink centralizada
**Card de resposta**: cream semi-transparente, texto ink, palavras com `**` ganham fundo gold (#D6A648) — combina com colar de ouro da Tata
**Fonte**: Inter (Regular pro corpo, SemiBold pra label, Bold pras palavras destacadas)

## Especificações de saída

- **Dimensão**: 1080x1920 (Stories 9:16)
- **Quantidade**: 10 PNGs (1 por Q&A)
- **Nome**: `01-story-1080x1920.png`, `02-story-...`
- **Pasta**: `~/criativos/YYYY-MM-DD-stories-qa/` (data de hoje)
- **Resumo**: `resumo.json` com pares Q&A, cenário usado e metadados

## Quando usar cada cenário

Use [references/cenarios.md](references/cenarios.md) para todos os detalhes visuais. Resumo da escolha:

| Tipo de Q&A | Cenário | Por quê |
|---|---|---|
| Confessional, íntima, "deixa eu te contar" | Carro | Aproximação visual, pose lateral, golden hour |
| Estratégica, técnica, "vou te ensinar" | Escritório | Autoridade, plantas + livros = expertise |
| Mindset, virada de chave | Qualquer um | Escolha pelo tom — carro pra emoção, escritório pra clareza |
| Resposta longa/densa | Escritório | Plano médio — sobra espaço pra texto |
| Resposta curta/punchline | Carro | Selfie de perto — caixinha menor pode caber |

## Regras de qualidade (checklist final)

Antes de entregar os 10 PNGs, verifique:

- [ ] Todos os 10 são 1080x1920 (story)
- [ ] Em TODOS, o colar de ouro com esmeralda está visível
- [ ] Em TODOS, NENHUMA caixinha cobre o rosto
- [ ] Maquiagem leve + blush Dior + pele com brilho dourado em todos
- [ ] Cabelo com frizz natural, pele com textura visível em todos
- [ ] Cenários distribuídos entre carro e escritório (variedade)
- [ ] Cada resposta tem 2-3 palavras com marca-texto gold
- [ ] Todas as perguntas soam como seguidor real (não institucional)
- [ ] Tom da Tata preservado em todas as respostas

## Skill irmã

Esta skill é uma **variação curada** da `criativos-qa-instagram` (que gera Story+Feed com cenários abertos). Use esta quando precisar de **APENAS stories** com **identidade visual fechada** (carro/escritório + joias + maquiagem específica). Use a `criativos-qa-instagram` quando puder variar mais.

## Recursos bundled

- `assets/colors_and_type.css` — CSS oficial do Design System Tata (cores + tipografia)
- `references/cenarios.md` — descrições visuais e prompts prontos dos 2 cenários
- `references/identidade-tata.md` — joias, maquiagem, pele, corpo, cabelo (regras fechadas)
- `references/design-system.md` — cores, fontes, layouts da caixinha e card
- `references/copy-qa.md` — framework de extração e copy das perguntas/respostas
