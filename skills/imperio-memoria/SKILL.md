# IMPERIO MEMORIA — Sistema de Memoria para Agentes IA

> Skill que projeta e implementa o sistema de memoria de agentes IA — gestao de estado, contexto compartilhado e decisoes de RAG. Aplica 3 frameworks da "Apostila Imperio IA Agentes" by Tata Goncalves.

## ACTIVATION

Trigger this skill when:
- User mentions "memoria de agentes", "estado dos agentes", "state management agentes"
- User asks "como meus agentes lembram?", "agentes compartilham info?", "preciso de RAG?"
- User mentions "cerebro", "diario", "bussola" in context of AI agents
- User says `/imperio-memoria`
- User asks about shared context between agents, agent state, or RAG decisions

## FRAMEWORKS

This skill applies 3 proprietary frameworks from the Apostila Imperio IA Agentes:

### 1. CEREBRO (Gestao de Estado)
Every agent that runs more than once NEEDS a state file. Without it: actions duplicate, progress is lost, messages repeat, behavior becomes inconsistent.

### 2. DIARIO (Memoria Compartilhada)
When multiple agents operate in the same business, they MUST read from ONE source of truth. Without it: one agent promises a discount, another doesn't know about it.

### 3. BUSSOLA (Decisao RAG)
Not every system needs RAG. The BUSSOLA framework decides: simple files vs vector database, based on document count, update frequency, access patterns, and prompt size.

## EXECUTION FLOW

Execute steps 1-5 in order. Each step has a clear deliverable. NEVER skip steps. ALWAYS collect information before generating.

---

### STEP 1: Entender o Ecossistema de Agentes

**Objetivo:** Mapear todos os agentes, suas funcoes e interacoes.

Perguntar (uma pergunta por vez, aguardar resposta):

1. "Quantos agentes voce tem (ou vai ter) no seu negocio? Me lista eles com o que cada um faz."
2. "Esses agentes precisam compartilhar informacao entre si? Sobre o que? (ex: dados de clientes, decisoes comerciais, historico de conversas)"
3. "Voce tem agentes que rodam mais de 1 vez — tipo cron diario, reativo a evento? Quais?"

**Regras:**
- NAO prosseguir sem ter a lista completa de agentes
- Classificar cada agente como: `unico` (roda 1 vez) ou `recorrente` (roda N vezes)
- Identificar quais agentes interagem entre si (compartilham contexto)
- Montar um mapa mental simples: Agente -> Funcao -> Frequencia -> Depende de quem

**Output deste step:** Mapa do ecossistema em formato tabela:

```
| Agente | Funcao | Frequencia | Compartilha com |
|--------|--------|------------|-----------------|
| [nome] | [desc] | [cron/reativo/unico] | [lista] |
```

---

### STEP 2: CEREBRO — Projetar Arquivos de Estado

**Objetivo:** Criar um arquivo de estado ESPECIFICO para cada agente recorrente.

Para CADA agente classificado como `recorrente` no Step 1:

**Perguntar:** "O que o [nome do agente] precisa LEMBRAR entre uma execucao e outra?"

**Gerar template de estado personalizado:**

```json
{
  "agente": "[nome-do-agente]",
  "versao": "1.0",
  "ultima_execucao": "2026-04-10T08:00:00Z",
  "ultimo_resultado": {
    "status": "sucesso|erro|parcial",
    "detalhes": "[descricao especifica do que aconteceu]",
    "metricas": {}
  },
  "passo_atual": "[etapa atual se fluxo multi-step]",
  "contador_execucoes": 0,
  "contexto": {
    "[campo_especifico_1]": "[valor relevante para ESTE agente]",
    "[campo_especifico_2]": "[valor relevante para ESTE agente]",
    "ultimo_item_processado": "[referencia ao ultimo item]",
    "proximo_horario_permitido": "2026-04-10T09:00:00Z"
  },
  "flags": {
    "em_manutencao": false,
    "limite_diario_atingido": false,
    "erro_critico": false
  },
  "historico_erros": []
}
```

**IMPORTANTE:** Os campos dentro de `contexto` DEVEM ser especificos para o dominio do agente. Exemplos:
- Agente de prospecao: `leads_pendentes`, `ultimo_lead_processado`, `total_qualificados_hoje`
- Agente de conteudo: `posts_gerados_hoje`, `ultimo_tema_usado`, `proximos_temas`
- Agente de vendas: `deals_em_andamento`, `ultimo_followup`, `conversoes_semana`
- Agente de monitoramento: `alertas_pendentes`, `ultimo_check`, `status_servicos`

**Explicar o ciclo de leitura/escrita:**

```
ANTES de agir:
  1. Ler estado do arquivo
  2. Checar se ja executou (evitar duplicata)
  3. Checar flags (manutencao? limite atingido? erro critico?)
  4. Carregar contexto relevante da ultima execucao

DEPOIS de agir:
  1. Atualizar ultima_execucao com timestamp atual
  2. Atualizar ultimo_resultado com status + detalhes + metricas
  3. Atualizar contexto com dados relevantes para proxima execucao
  4. Incrementar contador_execucoes
  5. Salvar arquivo

EM CASO DE ERRO:
  1. Atualizar ultimo_resultado com status "erro" + detalhes do erro
  2. Adicionar entrada em historico_erros
  3. Se erro critico: setar flag erro_critico = true
  4. NAO incrementar contador (execucao falhou)
  5. Salvar arquivo
```

**Gerar codigo padrao de leitura/escrita (Node.js):**

```javascript
// padrao-estado.js — Copiar e adaptar para cada agente
import { readFileSync, writeFileSync, existsSync } from 'fs';

const ESTADO_PATH = `${process.env.HOME}/meu-imperio/escala-ia/estado/${AGENT_NAME}-estado.json`;

function lerEstado() {
  if (!existsSync(ESTADO_PATH)) {
    return criarEstadoInicial();
  }
  return JSON.parse(readFileSync(ESTADO_PATH, 'utf-8'));
}

function salvarEstado(estado) {
  estado.ultima_execucao = new Date().toISOString();
  writeFileSync(ESTADO_PATH, JSON.stringify(estado, null, 2));
}

function verificarPodeExecutar(estado) {
  if (estado.flags.em_manutencao) return { pode: false, motivo: 'Em manutencao' };
  if (estado.flags.erro_critico) return { pode: false, motivo: 'Erro critico pendente' };
  if (estado.flags.limite_diario_atingido) return { pode: false, motivo: 'Limite diario atingido' };
  return { pode: true };
}

// CICLO PRINCIPAL
const estado = lerEstado();
const { pode, motivo } = verificarPodeExecutar(estado);

if (!pode) {
  console.log(`[${AGENT_NAME}] Execucao bloqueada: ${motivo}`);
  process.exit(0);
}

try {
  // ... logica do agente aqui ...
  
  estado.ultimo_resultado = { status: 'sucesso', detalhes: '...' };
  estado.contador_execucoes++;
} catch (err) {
  estado.ultimo_resultado = { status: 'erro', detalhes: err.message };
  estado.historico_erros.push({
    data: new Date().toISOString(),
    erro: err.message
  });
}

salvarEstado(estado);
```

**Entregavel:** `~/meu-imperio/escala-ia/estado/[nome-agente]-estado.json` para CADA agente recorrente.

---

### STEP 3: DIARIO — Projetar Memoria Compartilhada

**Objetivo:** Criar a estrutura de contexto compartilhado para todos os agentes que interagem.

**Perguntar:** "Quais informacoes TODOS os agentes precisam compartilhar? (ex: dados de clientes, decisoes de desconto, historico de interacoes)"

**Padroes comuns de contexto compartilhado:**
- Informacoes de clientes (nome, status, historico, preferencias)
- Decisoes de negocio (descontos dados, promessas feitas, excecoes aprovadas)
- Log de atividades (o que aconteceu, quando, por qual agente)
- Catalogo de produtos/servicos (referencia read-only)
- Regras comerciais (precos, politicas, limites)

**Projetar a estrutura da pasta `contexto/` personalizada para o negocio:**

```
~/meu-imperio/escala-ia/contexto/
├── clientes/
│   ├── _template.md          — template para cada arquivo de cliente
│   ├── joao-silva.md         — exemplo preenchido
│   └── maria-santos.md       — exemplo preenchido
├── decisoes.md               — log de decisoes importantes
├── produtos.md               — catalogo de produtos/servicos (read-only)
├── regras-comerciais.md      — regras de preco, desconto, politicas
└── historico/
    ├── 2026-04-09.jsonl      — log diario de atividades
    └── 2026-04-10.jsonl      — um arquivo por dia
```

**Gerar o TEMPLATE DE CLIENTE personalizado para o negocio do usuario:**

```markdown
# [Nome do Cliente]

## Dados Basicos
- **Nome:** 
- **Contato:** (telefone/email)
- **Canal de origem:** (Instagram/Google/indicacao/evento)
- **Data primeiro contato:** 
- **Status atual:** [lead | qualificado | agendado | cliente | alumni | inativo]
- **Valor do deal:** R$ 
- **Responsavel:** [agente ou pessoa]

## Historico de Interacoes
| Data | Agente | Acao | Resultado |
|------|--------|------|-----------|
| 2026-04-09 | HUGO | Prospecao | Lead qualificado, score 72 |
| 2026-04-09 | SOFIA | WhatsApp msg 1 | Entregue, sem resposta |
| 2026-04-10 | SOFIA | WhatsApp msg 2 | Lido, respondeu com interesse |

## Decisoes Especiais
- (descontos concedidos, promessas feitas, excecoes aprovadas)
- Ex: "10% desconto aprovado por Tata em 2026-04-09"

## Notas
- (contexto relevante para futuras interacoes)
- Ex: "Tem clinica em SP, nao atende fim de semana, prefere WhatsApp"

## Tags
- (tags para filtragem: #medico #clinica #high-ticket #instagram-fraco)
```

**Gerar o formato do LOG DE DECISOES:**

```markdown
# Decisoes Importantes

## Formato
Cada decisao segue o padrao:
`[DATA] [AGENTE/PESSOA] — [DECISAO] — [MOTIVO] — [VALIDADE]`

## Log
- [2026-04-09] Tata — Desconto 10% para Maria Santos — cliente indicou 3 pessoas — valido ate 2026-05-09
- [2026-04-10] SOFIA — Reagendou call de Joao Silva — pediu para ligar quinta — sem validade
```

**Gerar o formato do HISTORICO DIARIO (JSONL):**

```jsonl
{"ts":"2026-04-09T08:00:00Z","agente":"HUGO","acao":"prospeccao","alvo":"Maria Santos","resultado":"qualificado","score":72}
{"ts":"2026-04-09T08:30:00Z","agente":"SOFIA","acao":"whatsapp_msg1","alvo":"Maria Santos","resultado":"entregue","canal":"whatsapp"}
{"ts":"2026-04-09T14:00:00Z","agente":"IRIS","acao":"monitoramento","alvo":"@clinicamaria","resultado":"3_posts_analisados","sentimento":"positivo"}
```

**Explicar o ciclo de leitura/escrita compartilhada:**

```
ANTES de agir com um cliente:
  1. Ler contexto/clientes/[nome].md
  2. Ler contexto/decisoes.md (filtrar por cliente)
  3. Verificar se outro agente ja atuou recentemente (evitar sobreposicao)

DEPOIS de agir:
  1. Atualizar contexto/clientes/[nome].md com nova interacao na tabela
  2. Se tomou decisao importante: adicionar em contexto/decisoes.md
  3. Adicionar linha no contexto/historico/[data].jsonl

REGRA DE OURO: Quem interage, atualiza. Nenhum agente le sem depois escrever o que fez.
```

**Gerar codigo padrao de contexto compartilhado (Node.js):**

```javascript
// padrao-contexto.js — Copiar e adaptar para cada agente
import { readFileSync, writeFileSync, appendFileSync, existsSync, mkdirSync } from 'fs';

const CONTEXTO_BASE = `${process.env.HOME}/meu-imperio/escala-ia/contexto`;

function lerCliente(nomeArquivo) {
  const path = `${CONTEXTO_BASE}/clientes/${nomeArquivo}.md`;
  if (!existsSync(path)) return null;
  return readFileSync(path, 'utf-8');
}

function atualizarHistoricoCliente(nomeArquivo, agente, acao, resultado) {
  const path = `${CONTEXTO_BASE}/clientes/${nomeArquivo}.md`;
  const conteudo = readFileSync(path, 'utf-8');
  const hoje = new Date().toISOString().split('T')[0];
  const novaLinha = `| ${hoje} | ${agente} | ${acao} | ${resultado} |`;
  
  // Inserir nova linha apos o header da tabela de historico
  const atualizado = conteudo.replace(
    /(## Historico de Interacoes\n\|.*\n\|.*\n)/,
    `$1${novaLinha}\n`
  );
  writeFileSync(path, atualizado);
}

function registrarAtividade(agente, acao, alvo, resultado, extras = {}) {
  const hoje = new Date().toISOString().split('T')[0];
  const dir = `${CONTEXTO_BASE}/historico`;
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });
  
  const entry = JSON.stringify({
    ts: new Date().toISOString(),
    agente,
    acao,
    alvo,
    resultado,
    ...extras
  });
  appendFileSync(`${dir}/${hoje}.jsonl`, entry + '\n');
}

function registrarDecisao(agente, decisao, motivo, validade = 'sem validade') {
  const hoje = new Date().toISOString().split('T')[0];
  const linha = `- [${hoje}] ${agente} — ${decisao} — ${motivo} — ${validade}\n`;
  appendFileSync(`${CONTEXTO_BASE}/decisoes.md`, linha);
}
```

**Entregavel:** `~/meu-imperio/escala-ia/contexto/` (estrutura completa com templates preenchidos).

---

### STEP 4: BUSSOLA — Decisao RAG

**Objetivo:** Decidir se o negocio precisa de RAG ou se arquivos simples resolvem.

**Avaliar 4 criterios para o caso especifico do usuario:**

| Criterio | Arquivo Simples | RAG |
|----------|----------------|-----|
| **Quantidade de documentos** | < 50 documentos | 100+ documentos |
| **Frequencia de atualizacao** | Raramente atualiza | Atualizacoes frequentes |
| **Padrao de acesso** | Todos agentes precisam de info similar | Diferentes agentes precisam de pedacos diferentes |
| **Tamanho do contexto** | Cabe no prompt (< 50k tokens) | Nao cabe no prompt |

**Decisao:**

Se **3+ criterios apontam para Arquivo Simples:**
```
RECOMENDACAO: ARQUIVO SIMPLES

Para o seu caso, recomendo arquivos simples porque:
- Voce tem [X] documentos (< 50)
- As informacoes atualizam [frequencia]
- [Motivos especificos do caso]

A estrutura de contexto/ que criamos no Step 3 ja cobre tudo.
Nao precisa de banco vetorial, embeddings, nem infra extra.
Simples, rapido e funciona.
```

Se **3+ criterios apontam para RAG:**
```
RECOMENDACAO: RAG (Retrieval-Augmented Generation)

Para o seu caso, recomendo RAG porque:
- Voce tem [X] documentos (100+)
- As informacoes atualizam [frequencia]
- [Motivos especificos do caso]

Implementacao sugerida:
1. Banco vetorial: [Chroma / Pinecone / pgvector] — [motivo da escolha]
2. Embeddings: [OpenAI text-embedding-3-small / all-MiniLM-L6-v2] — [motivo]
3. Chunk size: [500-1000 tokens] — [motivo]
4. Estrategia de indexacao: [por cliente / por tipo / hibrido]
5. Quando re-indexar: [a cada update / batch diario / webhook]
```

**Gerar documento de decisao:**

```markdown
# Decisao BUSSOLA — Sistema de Memoria

## Data: [hoje]
## Negocio: [nome do negocio]

## Avaliacao
| Criterio | Valor | Aponta para |
|----------|-------|-------------|
| Documentos | [X] | [Arquivo/RAG] |
| Atualizacao | [freq] | [Arquivo/RAG] |
| Acesso | [padrao] | [Arquivo/RAG] |
| Contexto | [tamanho] | [Arquivo/RAG] |

## Decisao: [ARQUIVO SIMPLES / RAG]

## Justificativa
[Explicacao clara e direta do porque]

## Proximos passos
[O que implementar baseado na decisao]
```

**Entregavel:** `~/meu-imperio/escala-ia/decisao-bussola.md`

---

### STEP 5: Guia de Integracao

**Objetivo:** Gerar um guia pratico mostrando como tudo se conecta.

**O guia deve conter:**

#### 5.1 Mapa Visual do Sistema

```
┌─────────────────────────────────────────────────┐
│                SISTEMA DE MEMORIA                │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ Agente 1 │  │ Agente 2 │  │ Agente 3 │      │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘      │
│       │              │              │             │
│  ┌────▼─────┐  ┌────▼─────┐  ┌────▼─────┐      │
│  │ Estado 1 │  │ Estado 2 │  │ Estado 3 │      │
│  │ (CEREBRO)│  │ (CEREBRO)│  │ (CEREBRO)│      │
│  └──────────┘  └──────────┘  └──────────┘      │
│       │              │              │             │
│       └──────────────┼──────────────┘             │
│                      │                            │
│              ┌───────▼────────┐                   │
│              │   CONTEXTO     │                   │
│              │   (DIARIO)     │                   │
│              │                │                   │
│              │ clientes/      │                   │
│              │ decisoes.md    │                   │
│              │ historico/     │                   │
│              └────────────────┘                   │
│                                                  │
│              ┌────────────────┐                   │
│              │    BUSSOLA     │                   │
│              │ Arquivo/RAG?   │                   │
│              └────────────────┘                   │
└─────────────────────────────────────────────────┘
```

#### 5.2 Padrao de Execucao de Cada Agente

Para cada agente, gerar o fluxo:

```
[AGENTE] roda:
  1. Le estado/[agente]-estado.json          (CEREBRO)
  2. Verifica flags e ultima execucao         (CEREBRO)
  3. Le contexto/clientes/[relevantes].md    (DIARIO)
  4. Le contexto/decisoes.md                 (DIARIO)
  5. >>> EXECUTA SUA LOGICA <<<
  6. Atualiza estado/[agente]-estado.json    (CEREBRO)
  7. Atualiza contexto/clientes/[afetados].md (DIARIO)
  8. Registra em contexto/historico/[data].jsonl (DIARIO)
```

#### 5.3 Convencoes de Nomenclatura

```
ARQUIVOS DE ESTADO:
  estado/[nome-agente]-estado.json
  Exemplos: estado/hugo-estado.json, estado/sofia-estado.json

ARQUIVOS DE CLIENTE:
  contexto/clientes/[nome-slug].md
  Slug: lowercase, hifens, sem acentos
  Exemplos: contexto/clientes/joao-silva.md, contexto/clientes/maria-santos.md

HISTORICO DIARIO:
  contexto/historico/[YYYY-MM-DD].jsonl
  Exemplos: contexto/historico/2026-04-09.jsonl

DECISOES:
  contexto/decisoes.md (arquivo unico, append-only)
```

#### 5.4 Regras de Concorrencia

```
REGRA 1: Um agente por vez no mesmo cliente
  - Antes de agir, checar historico: outro agente atuou nos ultimos 30min?
  - Se sim: pular este cliente, processar proximo

REGRA 2: Append-only no historico
  - NUNCA editar linhas antigas do .jsonl
  - Sempre adicionar novas linhas no final

REGRA 3: Lock simples no estado
  - Ao ler estado, checar campo "locked_by"
  - Se locked: esperar ou pular
  - Ao terminar: remover lock
```

#### 5.5 Checklist de Implementacao

```markdown
## Checklist — Sistema de Memoria

### CEREBRO (Estado)
- [ ] Criar pasta ~/meu-imperio/escala-ia/estado/
- [ ] Gerar arquivo de estado para cada agente recorrente
- [ ] Implementar funcao lerEstado() em cada agente
- [ ] Implementar funcao salvarEstado() em cada agente
- [ ] Testar ciclo: ler -> executar -> salvar -> ler de novo

### DIARIO (Contexto Compartilhado)
- [ ] Criar pasta ~/meu-imperio/escala-ia/contexto/
- [ ] Criar subpastas: clientes/, historico/
- [ ] Criar template de cliente (_template.md)
- [ ] Criar decisoes.md com formato padrao
- [ ] Criar produtos.md e regras-comerciais.md
- [ ] Implementar leitura de contexto em cada agente
- [ ] Implementar escrita de contexto em cada agente
- [ ] Testar: agente A escreve, agente B le

### BUSSOLA (Decisao RAG)
- [ ] Avaliar 4 criterios
- [ ] Documentar decisao em decisao-bussola.md
- [ ] Se RAG: implementar pipeline de indexacao
- [ ] Se arquivo: confirmar que contexto/ cobre tudo

### INTEGRACAO
- [ ] Testar fluxo completo: estado -> contexto -> acao -> estado
- [ ] Validar que nenhum agente age sem ler estado primeiro
- [ ] Validar que nenhum agente age sem atualizar contexto depois
- [ ] Monitorar historico/ por 1 semana para detectar gaps
```

**Entregavel:** `~/meu-imperio/escala-ia/guia-memoria.md`

---

## DELIVERABLES SUMMARY

Ao final dos 5 steps, o usuario tera:

```
~/meu-imperio/escala-ia/
├── estado/
│   ├── [agente1]-estado.json
│   ├── [agente2]-estado.json
│   └── [agenteN]-estado.json
├── contexto/
│   ├── clientes/
│   │   ├── _template.md
│   │   └── [exemplos].md
│   ├── decisoes.md
│   ├── produtos.md
│   ├── regras-comerciais.md
│   └── historico/
│       └── [data].jsonl
├── decisao-bussola.md
└── guia-memoria.md
```

## RULES

1. **Portugues BR SEMPRE** — toda comunicacao, todo arquivo gerado, toda explicacao
2. **Tom da Tata** — direto, pratico, sem enrolacao, com analogias do dia a dia
3. **Estado ESPECIFICO por agente** — campos de contexto DEVEM refletir o dominio do agente (prospecao vs conteudo vs vendas)
4. **Templates refletem o negocio REAL** — nao usar exemplos genericos, personalizar para o negocio do usuario
5. **Explicar o PORQUE** — cada campo de estado, cada arquivo de contexto tem um motivo. Explicar.
6. **Padroes concretos de leitura/escrita** — mostrar CODIGO, nao conceitos abstratos
7. **Pasta contexto/ funciona para multi-agente** — qualquer agente le e escreve no mesmo formato
8. **NUNCA pular steps** — seguir 1 -> 2 -> 3 -> 4 -> 5 em ordem
9. **NUNCA gerar sem coletar** — cada step tem perguntas. Fazer as perguntas. Esperar respostas. Depois gerar.
10. **Arquivos criados em ~/meu-imperio/escala-ia/** — estrutura padrao do Imperio IA
