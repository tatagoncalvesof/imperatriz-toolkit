/**
 * Audio Generator Template — TTS Natural com Voz Clonada
 *
 * COMO USAR:
 * 1. Copiar este arquivo pro seu projeto
 * 2. Adaptar imports do database (updateLessonAudio, getLessonById, etc)
 * 3. Adaptar SCRIPT_REWRITE_PROMPT pra persona do projeto
 * 4. Adaptar voice_settings pro caso de uso
 * 5. Configurar .env com ELEVENLABS_API_KEY, VOICE_ID, MODEL_ID, GEMINI_API_KEY
 *
 * REGRA DE OURO: NUNCA use substituicoes foneticas. O ElevenLabs multilingual v2
 * com voz clonada PT-BR ja sabe pronunciar marcas e termos em ingles naturalmente.
 */

import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import { GoogleGenAI } from '@google/genai';
import { writeFile, mkdir } from 'fs/promises';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { existsSync } from 'fs';
import dotenv from 'dotenv';

// ── ADAPTAR: imports do seu database ──
// import { updateAudio, updateAudioStatus, getItemById } from './database.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: join(__dirname, '..', '..', '.env') });

const AUDIO_DIR = join(__dirname, '..', '..', 'audio');
const CHUNK_SIZE = 4500;  // ElevenLabs limit ~5000, usar 4500 por seguranca
const RETRY_MAX = 3;
const RETRY_DELAY = 2000;

// ============================================================
// GEMINI — Roteirista IA
// ============================================================

const geminiClient = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// ── ADAPTAR: trocar persona, expressoes e contexto ──
const SCRIPT_REWRITE_PROMPT = `Voce e [NOME], [descricao da persona]. Voce esta gravando a versao em audio de [tipo de conteudo].

TAREFA: Reescreva o conteudo abaixo como um roteiro falado, natural, em portugues brasileiro. Como se voce estivesse ensinando pessoalmente. Esse texto vai ser lido por uma voz sintetica clonada.

COMO VOCE FALA:
- Calorosa, energetica, motivacional
- Linguagem simples do dia a dia, NUNCA soa como livro didatico
- Ritmo natural: frases curtas, depois mais longas, depois uma pausa
- Usa expressoes como: "olha so", "vem comigo", "presta atencao nisso", "sabe o que acontece?"
- Explica conceitos complexos com analogias do dia a dia
- NUNCA soa robotica, academica ou como manual

ESTRUTURA:
- Comece direto no conteudo, SEM saudacao
- Quebre em segmentos naturais com pausas para respirar
- Se tem listas, converta em enumeracao falada
- Se tem codigo, explique o que FAZ em linguagem simples
- Termine naturalmente, SEM despedida

REGRAS DE PRONUNCIA PARA VOZ SINTETICA:
- Escreva TODOS os numeros por extenso: "1000" vira "mil"
- Escreva valores monetarios por extenso: "R$ 100" vira "cem reais"
- Escreva porcentagens por extenso: "50%" vira "cinquenta por cento"
- Use virgulas para pausas curtas e reticencias para pausas longas
- NAO use markdown, bullet points, headers
- Escreva nomes de marcas NORMALMENTE — a voz ja sabe pronunciar
- NAO tente escrever foneticamente
- Escreva tudo natural como uma brasileira escreveria

SAIDA:
- APENAS o texto do roteiro falado
- Texto falado puro, sem formatacao`;

async function generateScript(title, content, retries = 2) {
  const prompt = `${SCRIPT_REWRITE_PROMPT}

--- TITULO ---
${title}

--- CONTEUDO PARA TRANSFORMAR EM ROTEIRO FALADO ---

${content}`;

  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      const response = await geminiClient.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: prompt,
      });

      const text = response.text;
      if (!text || text.trim().length < 100) {
        throw new Error('Script too short or empty');
      }
      return text.trim();
    } catch (err) {
      const status = err.status || err.httpStatusCode;
      const isRetryable = status === 503 || status === 429 || err.message?.includes('UNAVAILABLE');

      if (isRetryable && attempt < retries) {
        const delay = (attempt + 1) * 5000;
        console.log(`[Gemini] Retrying in ${delay / 1000}s...`);
        await new Promise(r => setTimeout(r, delay));
        continue;
      }
      throw err;
    }
  }
}

// ============================================================
// CLEANUP — Remove markdown residual
// ============================================================

function cleanup(script) {
  let text = script;
  text = text.replace(/^#{1,6}\s+/gm, '');
  text = text.replace(/\*\*([^*]+)\*\*/g, '$1');
  text = text.replace(/\*([^*]+)\*/g, '$1');
  text = text.replace(/`([^`]+)`/g, '$1');
  text = text.replace(/^[-*]\s+/gm, '');
  text = text.replace(/^\d+\.\s+/gm, '');
  text = text.replace(/\s{3,}/g, '  ');
  text = text.replace(/\.{4,}/g, '...');
  return text.trim();
}

// ============================================================
// CHUNKING — Divide texto respeitando limites de frase
// ============================================================

function chunkText(text, maxChars = CHUNK_SIZE) {
  const chunks = [];
  let remaining = text;

  while (remaining.length > 0) {
    if (remaining.length <= maxChars) {
      chunks.push(remaining);
      break;
    }

    // Tentar cortar no fim de frase
    let cutPoint = remaining.lastIndexOf('. ', maxChars);
    if (cutPoint === -1 || cutPoint < maxChars * 0.5) {
      cutPoint = remaining.lastIndexOf('? ', maxChars);
    }
    if (cutPoint === -1 || cutPoint < maxChars * 0.5) {
      cutPoint = remaining.lastIndexOf(' ', maxChars);
    }
    if (cutPoint === -1) {
      cutPoint = maxChars;
    }

    chunks.push(remaining.substring(0, cutPoint + 1).trim());
    remaining = remaining.substring(cutPoint + 1).trim();
  }

  return chunks;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// ============================================================
// GERACAO DE AUDIO
// ============================================================

/**
 * Gera audio pra um item (aula, episodio, artigo, etc)
 *
 * @param {string} title - Titulo do conteudo
 * @param {string} content - Conteudo escrito (markdown/texto)
 * @param {string} outputFilename - Nome do arquivo de saida (ex: "lesson-1.mp3")
 * @param {object} io - Socket.IO instance (opcional, pra progresso real-time)
 * @returns {object} { filename, duration, size, script }
 */
export async function generateAudio(title, content, outputFilename, io = null) {
  const apiKey = process.env.ELEVENLABS_API_KEY;
  const voiceId = process.env.ELEVENLABS_VOICE_ID;
  const modelId = process.env.ELEVENLABS_MODEL_ID || 'eleven_multilingual_v2';

  if (!apiKey || !voiceId) throw new Error('ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID required');
  if (!process.env.GEMINI_API_KEY) throw new Error('GEMINI_API_KEY required');

  // Step 1: Gemini reescreve como roteiro falado
  console.log(`[Audio] Generating script with Gemini...`);
  const rawScript = await generateScript(title, content);
  const script = cleanup(rawScript);
  console.log(`[Audio] Script ready (${script.length} chars)`);

  // Step 2: ElevenLabs gera audio
  const client = new ElevenLabsClient({ apiKey });
  const chunks = chunkText(script);
  const audioBuffers = [];

  console.log(`[Audio] Generating audio (${chunks.length} chunks)...`);

  for (let i = 0; i < chunks.length; i++) {
    let attempt = 0;
    let success = false;

    while (attempt < RETRY_MAX && !success) {
      try {
        attempt++;

        // ── ADAPTAR: voice_settings pro caso de uso ──
        const response = await client.textToSpeech.convert(voiceId, {
          text: chunks[i],
          model_id: modelId,
          output_format: 'mp3_44100_128',
          voice_settings: {
            stability: 0.50,          // 0.3=expressivo 0.7=estavel
            similarity_boost: 0.80,   // 0.5-0.9 — quanto mais alto, mais parecido
            style: 0.35,              // 0.1=neutro 0.7=dramatico
            use_speaker_boost: true,  // sempre true pra voz clonada
          },
        });

        const bufferChunks = [];
        for await (const chunk of response) {
          bufferChunks.push(chunk);
        }
        audioBuffers.push(Buffer.concat(bufferChunks));

        console.log(`[Audio] Chunk ${i + 1}/${chunks.length} done`);
        success = true;
      } catch (err) {
        console.error(`[Audio] Chunk ${i + 1} attempt ${attempt} failed:`, err.message);
        if (attempt < RETRY_MAX) {
          await sleep(RETRY_DELAY * attempt);
        } else {
          throw new Error(`Failed chunk ${i + 1} after ${RETRY_MAX} attempts`);
        }
      }
    }
  }

  // Step 3: Concatenar e salvar
  const fullAudio = Buffer.concat(audioBuffers);

  if (!existsSync(AUDIO_DIR)) {
    await mkdir(AUDIO_DIR, { recursive: true });
  }

  const filepath = join(AUDIO_DIR, outputFilename);
  await writeFile(filepath, fullAudio);

  const durationSeconds = Math.round(fullAudio.length / 16000); // 128kbps = 16KB/s

  console.log(`[Audio] COMPLETE: ${outputFilename} (${durationSeconds}s, ${Math.round(fullAudio.length / 1024)}KB)`);

  return {
    filename: outputFilename,
    duration: durationSeconds,
    size: fullAudio.length,
    script: script,
  };
}

// ============================================================
// ENDPOINT DE STREAMING (pra copiar no api.js)
// ============================================================

/*
// Copiar este trecho pro seu api.js:

import { statSync, createReadStream } from 'fs';

router.get('/audio/:id', authMiddleware, (req, res) => {
  const item = db.getItemById(parseInt(req.params.id));
  if (!item || !item.audio_path) {
    return res.status(404).json({ error: 'Audio not found' });
  }

  const audioPath = join(__dirname, '..', '..', item.audio_path);

  try {
    const stat = statSync(audioPath);
    const range = req.headers.range;

    if (range) {
      // Range request (seek no player)
      const parts = range.replace(/bytes=/, '').split('-');
      const start = parseInt(parts[0], 10);
      const end = parts[1] ? parseInt(parts[1], 10) : stat.size - 1;
      res.writeHead(206, {
        'Content-Range': `bytes ${start}-${end}/${stat.size}`,
        'Accept-Ranges': 'bytes',
        'Content-Length': end - start + 1,
        'Content-Type': 'audio/mpeg'
      });
      createReadStream(audioPath, { start, end }).pipe(res);
    } else {
      res.writeHead(200, {
        'Content-Length': stat.size,
        'Content-Type': 'audio/mpeg'
      });
      createReadStream(audioPath).pipe(res);
    }
  } catch (err) {
    res.status(404).json({ error: 'Audio file not found' });
  }
});
*/

// ============================================================
// FRONTEND: AudioPlayer com auth token
// ============================================================

/*
// No componente React do player, passar o JWT token via query param:

const token = localStorage.getItem('token');
const audioSrc = `/api/audio/${itemId}?token=${encodeURIComponent(token)}`;

// No authMiddleware do backend, aceitar token via query param:

export function authMiddleware(req, res, next) {
  let token;
  const header = req.headers.authorization;
  if (header && header.startsWith('Bearer ')) {
    token = header.split(' ')[1];
  }
  if (!token && req.query.token) {
    token = req.query.token;
  }
  if (!token) return res.status(401).json({ error: 'Token required' });
  try {
    req.user = verifyToken(token);
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid token' });
  }
}
*/
