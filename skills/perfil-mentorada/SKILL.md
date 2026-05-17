---
name: perfil-mentorada
description: >
  Motor de classificação proprietário da Travessia Imperatriz — recebe
  `00-anamnese.json` + pesquisa pública (deep-research) da mentorada e
  classifica em 1 dos 8 perfis canônicos (Iniciante Zero, Vendedora Avulsa,
  Mentora Estabelecida, Infoprodutora, Empresa Física → Mentora,
  Especialista Técnica, Empresa B2B, Coach/Terapeuta). Cada perfil tem rota
  customizada das 26 portas (A-Z), kit de skills, lista NÃO-USAR, tempo de
  travessia e nível inicial. Usa algoritmo de 12 sinais com scoring 0-100,
  detecta casos híbridos (top 1 vs top 2 com Δ < 15) e grava resultado
  validado pela mentorada em `01-perfil.json`. Use quando precisar
  "classificar mentorada", "definir perfil da mentorada", "qual perfil",
  "rota da travessia", "qual rota A-Z", "reclassificar mentorada", "listar
  os 8 perfis", ou simular um perfil para treinamento. Método Travessia
  Imperatriz — propriedade Tata Gonçalves.
---

# Perfil Mentorada — Motor de Classificação Travessia Imperatriz

> **Sem perfil definido, não existe rota. Sem rota, a Travessia vira passeio sem destino.** — Tata Gonçalves

Esta skill é o **roteador estratégico** da Travessia Imperatriz. Lê a anamnese da mentorada, cruza com pesquisa pública (deep-research), aplica algoritmo de 12 sinais e devolve o perfil correto + a rota A-Z customizada das 26 portas.

## Filosofia central

A Travessia Imperatriz tem 26 portas (A até Z) — mas **nenhuma mentorada percorre as 26 na mesma ordem**. Mentorada Iniciante Zero não passa por porta de Escala de Ads antes de ter Mecanismo Único. Empresa B2B não faz lançamento estilo Erico Rocha. Coach não recebe copy de urgência agressiva.

A skill garante que cada mentorada entre na rota certa, com o kit certo, evitando o que **NÃO** serve pra ela.

## Quando usar

- Mentorada acabou de preencher anamnese — definir rota
- Mentorada evoluiu (ex: Vendedora Avulsa virou Mentora Estabelecida) — reclassificar
- Tata quer ver os 8 perfis listados rapidamente pra calibragem mental
- Tata quer simular um perfil pra treinamento ou material novo
- Antes de qualquer skill de execução (mecanismo-unico, ads, lançamento) — perfil é pré-requisito
- Antes de gerar dossiê executivo da mentorada — dossiê precisa do perfil definido

## Pré-requisitos

1. `00-anamnese.json` preenchido (skill `/anamnese-mentorada`)
2. Acesso a deep-research público (Instagram, site, pegadas digitais)
3. Validação humana ao final — Tata e mentorada confirmam o perfil antes de gravar

---

## OS 8 PERFIS CANÔNICOS

Resumo. Detalhamento profundo em [`OS-8-PERFIS.md`](OS-8-PERFIS.md).

| # | Perfil | Faturamento | Sinal-âncora | Tempo travessia |
|---|--------|-------------|--------------|------------------|
| 1 | Iniciante Zero | R$ 0 | Sem produto, sem audiência, sem oferta | 3-4 meses |
| 2 | Vendedora Avulsa | R$ 5-30k/mês | Vende 1:1 sem digital, indicação manda | 6-9 meses |
| 3 | Mentora Estabelecida | R$ 30-100k/mês | Mentoria/curso 1+ ano, quer dobrar | 4-8 meses |
| 4 | Infoprodutora | R$ 30-200k/mês | Curso digital, lança 2-4×/ano | 6-12 meses |
| 5 | Empresa Física → Mentora | R$ 30-200k físico | Clínica/loja/escritório quer empacotar | 8-12 meses |
| 6 | Especialista Técnica | varia | Programadora/dev quer virar criadora skills | 6-12 meses |
| 7 | Empresa B2B | R$ 100k-1M/mês | Vende pra outras empresas, comercial central | 6-12 meses |
| 8 | Coach/Terapeuta | R$ 5-50k/mês | Transformação pessoal, sensível a copy agressivo | 6-18 meses |

---

## MODOS DE OPERAÇÃO

A skill roda em **4 modos declaráveis**:

- **`/perfil-mentorada --classificar`** *(padrão)* — lê `00-anamnese.json`, roda deep-research, aplica algoritmo, retorna perfil + rota
- **`/perfil-mentorada --reclassificar`** — pra mentorada que já tinha perfil mas evoluiu (ex: Vendedora Avulsa que produtizou e virou Mentora Estabelecida)
- **`/perfil-mentorada --listar-perfis`** — mostra os 8 com sinais distintivos resumidos (não roda classificação)
- **`/perfil-mentorada --simular [perfil]`** — gera exemplo fictício de mentorada daquele perfil (útil pra treinamento Tata e materiais)

Se a Tata não declarar modo, a skill assume **`--classificar`** e pergunta o caminho do `00-anamnese.json`.

---

## PROCESSO — 7 FASES OBRIGATÓRIAS

### FASE 0 — Validação de entrada

Antes de qualquer coisa:

1. Confirmar que `00-anamnese.json` existe e está preenchido
2. Validar campos obrigatórios mínimos: `nome`, `instagram_handle`, `faturamento_atual`, `produto_atual`, `tempo_no_mercado`, `tipo_de_cliente`, `formato_atual_de_venda`
3. Se faltar 3+ campos → pedir pra rodar `/anamnese-mentorada` antes
4. Se faltar 1-2 campos → tentar inferir via deep-research e marcar como "inferido"

### FASE 1 — Deep Research público

Rodar `/deep-research` com inputs da anamnese:

- Instagram da mentorada (bio, últimos 30 posts, destaques, frequência)
- Site (se houver) — produtos, preços, posicionamento, prova social
- LinkedIn (se B2B ou Especialista Técnica)
- Pegadas no Google (entrevistas, podcasts, citações)
- Concorrentes diretos mencionados na anamnese

**Extrair:**
- Sofisticação do conteúdo
- Volume e tipo de prova social
- Linguagem (corporativa? íntima? técnica? terapêutica?)
- Formato de venda visível (link na bio? DM? agenda? pixel ativo?)
- Ticket implícito
- Audiência aparente (seguidores, engajamento médio)

### FASE 2 — Extração dos 12 sinais

Algoritmo completo em [`LOGICA-CLASSIFICACAO.md`](LOGICA-CLASSIFICACAO.md). Resumo:

| # | Sinal | Pondera |
|---|-------|---------|
| 1 | Faixa de faturamento | 15% |
| 2 | Tipo de produto/oferta atual | 15% |
| 3 | Formato de venda predominante | 12% |
| 4 | Origem do cliente (indicação? ads? orgânico?) | 8% |
| 5 | Tempo no mercado | 6% |
| 6 | Audiência digital (tamanho + qualidade) | 8% |
| 7 | Maturidade de mecanismo único | 6% |
| 8 | Estrutura de time (sozinha? com equipe?) | 6% |
| 9 | Origem do conhecimento que vende | 6% |
| 10 | Tom/linguagem (terapêutica vs comercial vs técnica) | 6% |
| 11 | Sensibilidade a copy agressivo | 6% |
| 12 | Trilha desejada declarada na anamnese | 6% |

Cada sinal recebe 1 valor categórico → vira input pro scoring.

### FASE 3 — Scoring 0-100 por perfil

Para cada um dos 8 perfis, calcular score 0-100. Top 1 = perfil principal. Se top 2 com Δ < 15 → caso híbrido (ver [`CASOS-HIBRIDOS.md`](CASOS-HIBRIDOS.md)).

Exemplo:

```
Iniciante Zero        18
Vendedora Avulsa      72  ← top 1
Mentora Estabelecida  61  ← top 2 (Δ = 11 → híbrido)
Infoprodutora         24
Empresa Física        12
Especialista Técnica   3
Empresa B2B            6
Coach/Terapeuta       38

PERFIL: Vendedora Avulsa (com nuance Mentora Estabelecida)
```

### FASE 4 — Apresentação à Tata + mentorada

Saída padrão (modo `--classificar`):

```
# CLASSIFICAÇÃO — [Nome da mentorada]

## Perfil Principal: [Nome do perfil]
**Score:** XX/100
**Confiança:** [Alta / Média / Baixa]

## Por que esse perfil
[3-5 bullets justificando com sinais concretos da anamnese e do deep-research]

## Sinais decisivos
- [Sinal 1 — valor encontrado — peso]
- [Sinal 2 — valor encontrado — peso]
- [Sinal 3 — valor encontrado — peso]

## Rota A-Z customizada
[Sequência das portas que essa mentorada vai percorrer]
Ex: A → B → C → F (PRIORIDADE) → G → I → J

## Kit de skills indicado
[Lista de skills do ecossistema Tata que entram nessa rota]

## NÃO usar com essa mentorada
[Lista de skills/abordagens que NÃO servem pra esse perfil]

## Tempo estimado de travessia
[X meses]

## Nível inicial sugerido
[Iniciante / Tático / Inteligente]

## Caso híbrido?
[Se sim: explicar combinação + tratamento]

---

## Validação
Tata, isso bate com o que você sabe da [Nome]?
- Confirmar e gravar 01-perfil.json
- Ajustar [campo X] e regravar
- Rodar reclassificar com mais inputs
```

### FASE 5 — Validação humana

A skill **NUNCA** grava `01-perfil.json` sem confirmação da Tata (e idealmente da mentorada também). Se Tata pedir ajustes, a skill regenera e re-apresenta.

### FASE 6 — Gravação do `01-perfil.json`

Schema completo em [`SCHEMA-JSON.md`](SCHEMA-JSON.md). Resumo:

```json
{
  "mentorada": "Nome",
  "data_classificacao": "2026-05-08",
  "perfil_principal": "vendedora-avulsa",
  "perfil_secundario": "mentora-estabelecida",
  "score_principal": 72,
  "score_secundario": 61,
  "hibrido": true,
  "rota_az": ["A", "F", "G", "J", "Q"],
  "porta_prioridade": "F",
  "kit_skills": ["..."],
  "nao_usar": ["..."],
  "tempo_meses": 7,
  "nivel_inicial": "tatico",
  "sinais_decisivos": [...],
  "validado_por": "Tata Goncalves",
  "validado_em": "2026-05-08"
}
```

Salvar em `~/Documents/Obsidian Vault/03 - Projetos/Travessia-Imperatriz/Mentoradas/[nome]/01-perfil.json`.

---

## MODO `--listar-perfis`

Saída resumida dos 8 perfis. Útil pra Tata calibrar mente antes de uma reunião 1:1 ou pra material de treinamento. Detalhe completo em [`OS-8-PERFIS.md`](OS-8-PERFIS.md).

## MODO `--simular [perfil]`

Gera mentorada fictícia daquele perfil com dados verossímeis (faturamento, Instagram inventado, dores típicas, anamnese simulada). Usado pra:
- Treinamento de novas multiplicadoras
- Conteúdo (carrossel, story) explicando os perfis
- Calibrar a skill (rodar simulação e ver se classifica certo)

Exemplos completos em [`EXEMPLOS-CLASSIFICACOES.md`](EXEMPLOS-CLASSIFICACOES.md).

## MODO `--reclassificar`

Lê `01-perfil.json` antigo + anamnese atualizada. Compara. Se mudou de perfil, gera novo `01-perfil.json` com `versao: 2` e arquiva o anterior em `01-perfil-v1.json`. Útil quando:
- Vendedora Avulsa produtizou e virou Mentora Estabelecida
- Mentora Estabelecida virou Infoprodutora (escalou via lançamento)
- Empresa Física empacotou conhecimento e virou híbrida
- Coach decidiu monetizar mais agressivo (mudou sensibilidade ao copy)

---

## REGRAS DURAS (a skill NÃO negocia)

1. **Não classifica sem anamnese mínima preenchida** — pede pra rodar `/anamnese-mentorada` antes
2. **Não grava `01-perfil.json` sem validação humana** — Tata aprova
3. **Não inventa sinais** — se a anamnese não tem o dado e o deep-research não achou, marca como "desconhecido" e ajusta o peso
4. **Não força perfil único quando é híbrido** — se Δ < 15 entre top 1 e top 2, declara híbrido
5. **Não recomenda kit completo sem checar a NÃO-USAR** — cada perfil tem skills proibidas
6. **Não pula fase de deep-research** — anamnese pode ter cego, pesquisa pública revela
7. **Não trata Empresa B2B como Mentora** — denominação correta é "Empresa do Império"
8. **Não trata Coach com copy agressivo** — sensibilidade ao tom é regra fundadora
9. **Não classifica Especialista Técnica que está só estudando IA como Especialista** — precisa ter intenção declarada de monetizar via skills/agentes/apps
10. **Não confunde Vendedora Avulsa com Iniciante Zero** — Vendedora Avulsa já fatura R$ 5-30k/mês via 1:1
11. **Sempre apresenta justificativa em sinais concretos** — não basta dizer "achei que era esse"
12. **Sempre oferece reclassificação** após 90 dias na Travessia (mentorada evoluiu)

---

## INTEGRAÇÃO COM O ECOSSISTEMA TRAVESSIA

**Ordem ideal no funil de entrada da mentorada:**

```
/anamnese-mentorada              (coleta dados brutos)
       ↓
/deep-research                   (pesquisa pública)
       ↓
/perfil-mentorada                ← VOCE ESTA AQUI
       ↓
/dossie-mentorada                (gera dossiê executivo já com perfil)
       ↓
/voz-de-marca-builder            (calibra voz pra rota dela)
       ↓
[Rota A-Z personalizada começa]
```

**Skills do ecossistema Tata que cada perfil aciona:**
Ver [`OS-8-PERFIS.md`](OS-8-PERFIS.md) — coluna "Kit de skills" detalhada.

**Glossário da Tata:**
Linkar termos técnicos (Travessia, 26 portas, perfil canônico, rota A-Z, sinais decisivos) pro `/glossariodatata`.

---

## ARQUIVOS DE REFERÊNCIA (carregar sob demanda)

- [`OS-8-PERFIS.md`](OS-8-PERFIS.md) — detalhamento profundo dos 8 perfis (sinais, dor, rota, skills, NÃO usar, tempo, nível)
- [`LOGICA-CLASSIFICACAO.md`](LOGICA-CLASSIFICACAO.md) — algoritmo completo dos 12 sinais + scoring
- [`CASOS-HIBRIDOS.md`](CASOS-HIBRIDOS.md) — combinações comuns + tratamento
- [`EXEMPLOS-CLASSIFICACOES.md`](EXEMPLOS-CLASSIFICACOES.md) — 8 exemplos resolvidos (1 por perfil)
- [`SCHEMA-JSON.md`](SCHEMA-JSON.md) — estrutura do `01-perfil.json`
- [`README.md`](README.md) — instalação, uso, FAQ, distribuição

---

## VERSIONAMENTO

- **v1.0** *(atual)* — 8 perfis, 12 sinais, 4 modos, 7 fases, integração Travessia
- **v1.5** *(planejado)* — banco de mentoradas reais classificadas para benchmark
- **v2.0** *(planejado)* — auto-detecção de evolução (skill flagga "essa mentorada mudou de perfil")
- **v3.0** *(planejado)* — feedback loop com resultado real após 90 dias na Travessia

---

**Método Travessia Imperatriz — propriedade intelectual Tata Gonçalves.**
