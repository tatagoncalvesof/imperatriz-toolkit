---
name: deep-market-research
description: "Motor de pesquisa profunda de mercado em PT-BR — captura os 50 termos EXATOS que o público alvo digita em Google/YouTube/TikTok/Instagram/LinkedIn, mapeia 3 objeções por termo e gera ponte estratégica busca→produto. Usa WebSearch/WebFetch ao vivo. Diferente de /deep-research (relatórios formais multi-pass): esta skill é tática pra marketing — extrai linguagem real do comprador pra alimentar copy, anúncio, persona, calendário editorial. Use quando o usuário pedir: 'pesquisa de mercado profunda', 'o que meu público pesquisa', 'termos reais do meu nicho', 'objeções escondidas', 'ideias de conteúdo do zero', 'mapeamento de audiência multi-plataforma', 'voice of customer', 'VOC', 'social listening', 'thinking with the buyer's head'. Saída integra com /skill-persona-profunda, /briefing-copy-360, /headline-imperatriz, /calendario-imperatriz, /linha-editorial-imperatriz."
---

# Deep Market Research — Motor de VOC Multi-Plataforma

Captura a **linguagem real** do comprador em 5 plataformas, mapeia objeções por trás de cada termo e gera ponte estratégica busca → produto. Diferente de `/deep-research` (relatórios acadêmicos/B2B com format-control rígido), esta skill é o motor tático que abastece **toda a stack de copy/persona/conteúdo** da Tata com matéria-prima REAL extraída de Google/YouTube/TikTok/Instagram/LinkedIn ao vivo.

> Pensar com a cabeça do comprador, não com a do dono do produto.

## Quando usar

Ative quando o usuário pedir:

- "pesquisa de mercado profunda" / "pesquisa de mercado pra meu nicho"
- "o que meu público pesquisa de verdade"
- "quais as objeções do meu cliente"
- "ideias de conteúdo do zero" / "não sei sobre o que postar"
- "social listening" / "voice of customer" / "VOC"
- "mapeamento de audiência multi-plataforma"
- "thinking with the buyer's head"
- Antes de rodar `/skill-persona-profunda`, `/calendario-imperatriz`, `/briefing-copy-360` quando o nicho é novo ou pouco mapeado

NÃO use pra: relatório acadêmico/literatura/policy brief (→ `/deep-research`), análise de concorrente específico (→ `/competitors-analysis`), análise de anúncio existente (→ `/analise-anuncio-1000`).

## Modos

| Modo | Quando usar | Saída |
|---|---|---|
| `--full` (padrão) | Pesquisa completa 5 plataformas, 50 termos, 150 objeções | Relatório mestre + JSON canônico |
| `--canal=<google\|youtube\|tiktok\|instagram\|linkedin>` | Foco em um único canal | Relatório por canal |
| `--rapido` | 20 termos top, 1 objeção por termo, 1h de execução | Mini-relatório acionável |
| `--auditar=<arquivo>` | Audita pesquisa existente contra os 10 anti-patterns | Relatório de drift + correções |
| `--atualizar=<arquivo>` | Refaz pesquisa de relatório antigo, mostra o que mudou | Diff temporal |

## Workflow das 7 fases

```
[1] Briefing de Escopo         → entrevista o usuário em 8 perguntas
[2] Plano de Queries           → monta query set por plataforma
[3] Coleta Multi-Plataforma    → WebSearch/WebFetch ao vivo
[4] Extração de Linguagem      → captura termos EXATOS, não parafraseados
[5] Mapeamento de Objeções     → 3 objeções por top-50 termo
[6] Ponte Busca → Produto      → ideias de conteúdo conectando intent + oferta
[7] Empacotamento + Validação  → roda 10 validadores, salva no vault
```

### Fase 1 — Briefing de Escopo

Pergunte e capture (uma por vez, não despeje todas):

1. **Nicho/setor** específico (não "marketing", mas "marketing pra dentista")
2. **Produto/serviço** que vai ser vendido a partir dessa pesquisa
3. **Cliente ideal** em 1 frase (quem, idade aprox, dor central)
4. **Ticket** (até R$97 / R$97-997 / R$997-5k / R$5k+) — muda profundidade de objeção
5. **Estágio de consciência** Schwartz (inconsciente / consciente da dor / consciente da solução / consciente do produto / mais consciente)
6. **Geografia** (Brasil todo / Sul / SP / global PT-BR)
7. **Idioma** que o cliente usa internamente (português coloquial / jargão técnico / inglês-misturado)
8. **Concorrentes diretos** (3-5 nomes pra cruzar termos depois)

Se o usuário não souber 5/6/8, marque "INVESTIGAR" e siga — fases 3/4 vão devolver dados pra preencher.

Salve briefing em variável de sessão e referencie em TODAS as fases seguintes.

### Fase 2 — Plano de Queries

Pra cada plataforma, monte **8-12 queries** baseadas em:

- **Termo-raiz** (palavra-chave central do nicho)
- **Modificadores de dor** ("não consigo", "como resolver", "por que não funciona")
- **Modificadores de comparação** ("X vs Y", "melhor", "vale a pena")
- **Modificadores de jornada** ("começar", "primeiros passos", "depois de anos")
- **Modificadores demográficos** (idade, profissão, momento de vida)
- **Síndrome do impostor** ("será que sou capaz", "tenho perfil pra")
- **Negação/desistência** ("desistir de", "parar de tentar", "não é pra mim")

Detalhe completo em [references/01-platforms-playbook.md](references/01-platforms-playbook.md).

### Fase 3 — Coleta Multi-Plataforma

Execute WebSearch ao vivo, plataforma por plataforma. Pra cada query, capture:

- **Resultados orgânicos top 10** (títulos + descrições — linguagem usada)
- **Sugestões de autocomplete** (faça query `<termo>` e variações `<termo> que`, `<termo> como`, `<termo> porque`)
- **"People also ask"** do Google (objeções implícitas)
- **YouTube**: títulos top + 30 comentários top do vídeo nº1 (objeções explícitas)
- **TikTok/Instagram**: hooks de Reels populares + hashtags adjacentes + comentários
- **LinkedIn**: posts mais comentados sobre o termo + linguagem profissional

Pra cada peça coletada, anote:
```
[fonte] [plataforma] [data] [termo exato] [contexto: dor/objeção/comparação/celebração]
```

**Anti-pattern crítico**: Nunca parafrasear. Se a pessoa escreveu "to puta de cansada de tentar emagrecer", você captura ISSO, não "está frustrada com tentativas de emagrecimento".

### Fase 4 — Extração de Linguagem

Dos dados brutos da fase 3, destile:

- **50 termos exatos** que mais aparecem (frequência + relevância pra produto)
- **20 expressões idiomáticas** (gírias, frases típicas do nicho)
- **15 metáforas recorrentes** (como o público descreve a dor — "tô na corda bamba", "meu negócio é uma vela acesa")
- **10 anti-termos** (palavras que o público REJEITA — pra você NÃO usar)

Cada termo vai pra tabela com colunas: Termo Exato | Plataforma onde apareceu | Frequência | Contexto dominante | Nível de Schwartz | Score de oportunidade (1-10).

### Fase 5 — Mapeamento de Objeções

Pra cada um dos 50 termos top, identifique as **3 objeções dominantes** seguindo o framework PADC:

- **P**reço — "é muito caro?", "vale o investimento?"
- **A**utoridade — "será que essa pessoa sabe?", "tem prova?"
- **D**úvida pessoal — "vai funcionar PRA MIM?", "tenho perfil?"
- **C**ondição — "tenho tempo?", "tenho estrutura?", "é a hora certa?"

Pra cada objeção, capture:
- **Frase literal** que apareceu na coleta (não inventar)
- **Plataforma onde apareceu**
- **Como quebrar** (1 linha de copy-resposta — não escreve copy completo aqui, só semente)

Framework completo em [references/02-objection-mapping.md](references/02-objection-mapping.md).

### Fase 6 — Ponte Busca → Produto

Pra cada termo top-50, gere **1 sugestão de conteúdo** que:

1. Usa o termo exato no hook (não parafraseia)
2. Quebra a objeção principal daquele termo
3. Termina conectando ao produto/oferta do briefing (sem ser vendedor)
4. Especifica formato por plataforma (Reel, Carrossel, Post LinkedIn, Vídeo YT longo, Story)

Estrutura da ponte:
```
[HOOK: termo exato] → [VALOR: quebra objeção] → [PONTE: conexão com produto]
```

Framework detalhado em [references/03-content-bridge.md](references/03-content-bridge.md).

### Fase 7 — Empacotamento + Validação

1. Rode os **10 validadores anti-AI-slop** ([references/05-anti-ai-slop.md](references/05-anti-ai-slop.md)). Bloqueia entrega se algum falhar:
   - V1: Termos são literais (não parafraseados)
   - V2: Objeções têm frase de origem citada
   - V3: Pelo menos 3 plataformas representadas
   - V4: Nenhum termo é abstração ("ferramenta de produtividade" sem nome)
   - V5: Sugestões de conteúdo são específicas (não "fazer um post")
   - V6: Ponte busca→produto não é genérica
   - V7: Score de oportunidade tem racional (não chutado)
   - V8: Linguagem do output respeita o registro do nicho (não "leverage synergies" pra esteticista)
   - V9: Anti-termos foram listados (não só os termos pra usar)
   - V10: Output passa por `/voz-humana-br` antes de salvar

2. Gere 3 artefatos:
   - **Relatório mestre** em [templates/relatorio-mestre.md](templates/relatorio-mestre.md)
   - **JSON canônico** em [templates/saida-canonica.json](templates/saida-canonica.json) — lido por outras skills
   - **Recortes por canal** ([templates/relatorio-por-canal.md](templates/relatorio-por-canal.md))

3. Salve em:
   ```
   ~/Documents/Obsidian Vault/05 - Pesquisa de Mercado/[nicho-slug]/
   ├── relatorio-mestre.md
   ├── saida-canonica.json
   ├── recorte-google.md
   ├── recorte-youtube.md
   ├── recorte-tiktok.md
   ├── recorte-instagram.md
   └── recorte-linkedin.md
   ```

## Integração com a stack Tata

O JSON canônico desta skill é lido automaticamente por:

| Skill | O que consome |
|---|---|
| `/skill-persona-profunda` | 50 termos + 20 expressões idiomáticas + objeções PADC → alimentam dimensões psicográficas |
| `/briefing-copy-360` | Linguagem real + anti-termos → preenchem bloco "Voz do Cliente" |
| `/headline-imperatriz` | Top 10 termos por temperatura → viram hooks por nível Schwartz |
| `/mecanismo-unico` | Objeções recorrentes → revelam "vilão externo" pro mecanismo |
| `/calendario-imperatriz` | 50 sugestões de conteúdo → pauta de 30-60 dias |
| `/linha-editorial-imperatriz` | Anti-termos + registro detectado → vocabulário OFF |
| `/copy-conversacional-dm` | Objeções literais → roteiro de quebra em DM |
| `/analise-anuncio-1000` | Termos top → benchmarks pra angle de criativo |

Detalhe completo de cada integração em [references/06-integracao-stack.md](references/06-integracao-stack.md).

## Anti-patterns (NÃO faça)

1. **Parafrasear o que o público disse** — captura LITERAL ou nada
2. **Inventar objeções "que faz sentido"** — toda objeção tem que ter frase-origem
3. **Pular plataformas porque "não é onde meu público está"** — você não sabe até pesquisar
4. **Confundir busca com volume** — termo de cauda longa com 100 buscas/mês pode ser ouro
5. **Ignorar comentários** — comentário é onde mora a objeção; descrição/título é onde mora o desejo
6. **Misturar produto da Tata com produto do cliente** — o produto do briefing é o ÚNICO ponto de conexão
7. **Saída em inglês quando o público é BR** — sempre PT-BR, exceto jargão técnico que o nicho usa
8. **Pular validadores anti-slop** — sem validar, não entrega
9. **Output em arquivo solto** — sempre no vault, nicho organizado
10. **Não cruzar com `/voz-humana-br`** — toda peça final passa pelo humanizador

## Tom de saída

- **Direto, sem hedging** ("você precisa" não "talvez seja interessante considerar")
- **PT-BR coloquial** quando o nicho é B2C; **PT-BR profissional** quando B2B
- **Frases curtas misturadas com longas** (regra `/voz-humana-br`)
- **Zero jargão de IA** ("delivers value", "insights acionáveis", "unlock potential" estão banidos)
- **Citação obrigatória da fonte** quando capturar frase literal

## Output canônico

Salva sempre em `~/Documents/Obsidian Vault/05 - Pesquisa de Mercado/[nicho-slug]/`. Se a pasta `05 - Pesquisa de Mercado` não existir, crie. O JSON canônico vai pra `saida-canonica.json` no mesmo diretório e é a fonte de verdade lida pelas outras skills.

Formato detalhado dos outputs: [references/04-output-formats.md](references/04-output-formats.md).
