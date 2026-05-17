---
name: skill-tts-natural
description: >
  Gera audio natural com voz clonada ElevenLabs a partir de conteudo escrito.
  Usa Gemini para reescrever o texto como roteiro falado conversacional em PT-BR,
  depois gera o audio com ElevenLabs TTS. Aplica em cursos, podcasts, aulas,
  artigos ou qualquer conteudo que precise virar audio de qualidade.
  Usar quando a usuaria mencionar: gerar audio, TTS, texto para voz, audio da aula,
  voz sintetica, ElevenLabs, converter texto em audio, gravar aula, audio natural,
  roteiro de audio, script de voz.
---

# Skill TTS Natural — Audio com Voz Clonada

## Visao Geral

Transforma qualquer conteudo escrito (aulas, artigos, posts, scripts) em audio natural
usando voz clonada do ElevenLabs. O segredo: Gemini reescreve o texto como roteiro
falado ANTES de mandar pro TTS. Resultado: audio que soa como uma pessoa ensinando
de verdade, nao como robo lendo texto.

## Arvore de Decisao

```
Pedido
|
|-- "gerar audio de uma aula/conteudo"
|   --> Fluxo 1: Audio Individual
|
|-- "gerar audio em lote/batch"
|   --> Fluxo 2: Audio em Lote
|
|-- "criar audio-generator.js pro meu projeto"
|   --> Fluxo 3: Implementacao Completa
|
|-- "melhorar qualidade do audio"
|   --> Fluxo 4: Otimizacao de Voz
|
|-- "criar roteiro/script de audio"
|   --> Fluxo 5: Apenas Roteiro (sem gerar audio)
```

---

## Principio Fundamental: NAO USE SUBSTITUICOES FONETICAS

**REGRA DE OURO:** O ElevenLabs eleven_multilingual_v2 com voz clonada em PT-BR
ja sabe pronunciar nomes de marcas, termos em ingles e siglas naturalmente.

**NUNCA faca:**
- "Claude" → "Clod" (o TTS le como "Clod" literal e fica horrivel)
- "ChatGPT" → "Tchet Ge Pe Te" (vira "Xati Gipiti")
- "GitHub" → "Guitrab"
- "Vercel" → "Verssel" (vira "Versal")
- Qualquer substituicao fonetica de marcas ou termos em ingles

**SEMPRE faca:**
- Escreva nomes de marcas NORMALMENTE: Claude Code, ChatGPT, GitHub, WhatsApp
- A voz sintetica clonada ja tem sotaque brasileiro natural
- Ela ja sabe pronunciar termos tech do jeito que brasileiros falam

**O que FUNCIONA substituir:**
- Numeros por extenso: "1000" → "mil", "2024" → "dois mil e vinte e quatro"
- Valores monetarios: "R$ 100" → "cem reais"
- Porcentagens: "50%" → "cinquenta por cento"

---

## Stack Tecnica

| Componente | Tecnologia |
|-----------|-----------|
| Roteirista | Google Gemini `gemini-2.5-flash` via `@google/genai` |
| TTS | ElevenLabs SDK `@elevenlabs/elevenlabs-js` |
| Modelo de voz | `eleven_multilingual_v2` |
| Runtime | Node.js (ES modules) |
| Audio format | MP3 44100Hz 128kbps |

### Pacotes npm necessarios

```bash
npm install @elevenlabs/elevenlabs-js @google/genai dotenv
```

### Variaveis de ambiente necessarias

```env
ELEVENLABS_API_KEY=sk_...
ELEVENLABS_VOICE_ID=...         # ID da voz clonada
ELEVENLABS_MODEL_ID=eleven_multilingual_v2
GEMINI_API_KEY=AIza...
```

---

## Fluxo 3: Implementacao Completa (audio-generator.js)

Quando o usuario pedir pra criar um gerador de audio, usar este template como base.
Carregar `references/audio-generator-template.js` e adaptar ao projeto.

### Arquitetura

```
Conteudo escrito (markdown/texto)
       |
       v
  [Gemini 2.5 Flash]  ← Prompt de roteirista (PT-BR natural)
       |
       v
  Roteiro falado (texto limpo, sem markdown)
       |
       v
  [Cleanup] ← Remove markdown residual
       |
       v
  [Chunking] ← Divide em pedacos de 4500 chars
       |
       v
  [ElevenLabs TTS] ← Chunk por chunk, com retry
       |
       v
  [Concatenar buffers] → arquivo .mp3
```

### Voice Settings Recomendados

```javascript
voice_settings: {
  stability: 0.50,          // 0.3=expressivo 0.7=estavel — 0.50 e equilibrado
  similarity_boost: 0.80,   // Quanto mais alto, mais parecido com a voz original
  style: 0.35,              // Quanto mais alto, mais dramatico — 0.35 e natural
  use_speaker_boost: true,  // Sempre true pra voz clonada
}
```

**Ajustes por caso de uso:**
- **Aula/curso:** stability 0.50, style 0.35 (natural, ensino)
- **Podcast energetico:** stability 0.35, style 0.50 (mais expressivo)
- **Narracão calma:** stability 0.65, style 0.20 (mais estavel)
- **Storytelling:** stability 0.40, style 0.55 (dramatico)

---

## Prompt do Gemini — Template Base

Este e o prompt que transforma texto escrito em roteiro falado. ADAPTAR a persona
e o contexto para cada projeto.

```
Voce e [NOME DA PERSONA], [DESCRICAO DA PERSONA]. Voce esta gravando a versao
em audio de [TIPO DE CONTEUDO] do seu [PROJETO].

TAREFA: Reescreva o conteudo abaixo como um roteiro falado, natural, em portugues
brasileiro. Como se voce estivesse [CONTEXTO] pessoalmente. Esse texto vai ser
lido por uma voz sintetica clonada.

COMO [PERSONA] FALA:
- [Adjetivo 1], [adjetivo 2], [adjetivo 3]
- Linguagem simples do dia a dia, NUNCA soa como livro didatico
- Ritmo natural: frases curtas, depois mais longas, depois uma pausa
- Usa expressoes como: [lista de expressoes tipicas da persona]
- Explica conceitos complexos com analogias do dia a dia
- NUNCA soa robotica, academica ou como manual

ESTRUTURA:
- Comece direto no conteudo, SEM saudacao
- Quebre em segmentos naturais com pausas para respirar
- Se tem listas, converta em enumeracao falada
- Se tem codigo/tecnico, explique em linguagem simples
- Termine naturalmente, SEM despedida

REGRAS DE PRONUNCIA PARA VOZ SINTETICA:
- Escreva TODOS os numeros por extenso
- Escreva valores monetarios por extenso
- Escreva porcentagens por extenso
- Use virgulas para pausas curtas e reticencias para pausas longas
- NAO use markdown, bullet points, headers
- Escreva nomes de marcas NORMALMENTE — a voz ja sabe pronunciar
- NAO tente escrever foneticamente

SAIDA:
- APENAS o texto do roteiro falado
- Texto falado puro, sem formatacao
```

---

## Fluxo 1: Audio Individual

1. Receber o conteudo escrito (markdown, texto, etc)
2. Gerar roteiro com Gemini usando o prompt adaptado ao projeto
3. Limpar markdown residual
4. Dividir em chunks de 4500 caracteres
5. Gerar audio chunk por chunk com ElevenLabs
6. Concatenar buffers em um unico MP3
7. Salvar arquivo e atualizar banco de dados

## Fluxo 2: Audio em Lote

1. Listar todos os itens pendentes no banco
2. Para cada item:
   a. Gerar roteiro com Gemini
   b. Gerar audio com ElevenLabs
   c. Salvar e marcar como pronto
   d. Aguardar 2 segundos (rate limiting)
3. Pular itens ja prontos
4. Logar progresso: [N/TOTAL] DONE/ERROR/SKIP

## Fluxo 4: Otimizacao de Voz

Se o audio esta soando ruim, verificar nesta ordem:

1. **Tem substituicoes foneticas?** → REMOVER TODAS
2. **Voice settings:** Ajustar stability/style conforme caso de uso
3. **Roteiro natural?** Verificar se o Gemini esta gerando texto conversacional
4. **Markdown no roteiro?** Aplicar cleanup pra remover formatacao residual
5. **Chunks quebrando frases?** Verificar se o chunking respeita limites de frase
6. **Modelo correto?** Usar `eleven_multilingual_v2` pra PT-BR

## Fluxo 5: Apenas Roteiro

Quando so precisa do texto falado sem gerar audio:
1. Enviar conteudo pro Gemini com o prompt de roteirista
2. Aplicar cleanup
3. Retornar texto pronto pra ser usado em qualquer TTS

---

## Checklist de Integracao

Ao implementar em um novo projeto:

- [ ] Instalar pacotes: `@elevenlabs/elevenlabs-js @google/genai dotenv`
- [ ] Configurar .env com as 4 variaveis (ELEVENLABS_API_KEY, VOICE_ID, MODEL_ID, GEMINI_API_KEY)
- [ ] Criar diretorio de audio (ex: `audio/`)
- [ ] Adaptar o prompt do Gemini pra persona do projeto
- [ ] Adaptar voice_settings pro caso de uso
- [ ] Criar endpoint de API pra geracao (individual + batch)
- [ ] Criar endpoint de streaming de audio com suporte a Range requests
- [ ] No frontend: passar JWT token via query param (`?token=`) pra tag `<audio>`
- [ ] Testar UMA aula antes de rodar batch
- [ ] Se soar estranho: VERIFICAR se tem substituicao fonetica e REMOVER

---

## Erros Comuns e Solucoes

| Erro | Causa | Solucao |
|------|-------|---------|
| Audio robotico | Roteiro e texto escrito, nao falado | Usar Gemini pra reescrever como roteiro |
| Pronuncia estranha de marcas | Substituicoes foneticas | REMOVER TODAS as substituicoes |
| "Clod Cude" | Map fonetico convertendo Claude Code | Escrever normalmente |
| "Xati Gipiti" | Map fonetico convertendo ChatGPT | Escrever normalmente |
| "Versal gratuita" | Map fonetico convertendo Vercel | Escrever normalmente |
| Audio nao toca no browser | Tag `<audio>` nao envia header Auth | Passar token via `?token=` na URL |
| Voz nao parece clonada | similarity_boost baixo | Aumentar pra 0.80+ |
| Voz instavel/variando | stability muito baixo | Aumentar pra 0.50+ |
| Audio cortado | Chunk quebrando no meio da frase | Melhorar logica de chunking |
