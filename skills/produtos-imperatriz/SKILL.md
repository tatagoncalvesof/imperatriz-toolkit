---
name: produtos-imperatriz
description: >
  Pilar 8 (Produtos da Tata) da Travessia Imperatriz. Mapeia a esteira
  de ascensão completa dos 10 produtos vendidos pela Tata Gonçalves
  (Skills Públicas → Imperatriz Toolkit → Bestseller → Imersões →
  Travessia Imperatriz → Mastermind → 1:1 → Consultoria B2B → Afiliados →
  Sucessão), aplica lógica de cross-sell baseada em nível hierárquico +
  histórico + timing, e orquestra QUAL produto oferecer pra QUAL
  mentorada AGORA. NÃO é dos produtos da mentorada — é dos produtos
  DA TATA. Lê dossie-mentorada (perfil + nível + histórico), cruza com
  tatou-2.0 (despacho), roda automaticamente após conclusão de pipeline.
  4 modos: --mapa (esteira completa), --proximo (qual produto sugerir
  agora), --cross-sell (script literal por produto), --timing (quando
  próxima oferta). Use quando Tata pedir "qual produto oferecer pra
  ela", "ela tá pronta pra Travessia?", "esteira de ascensão", "cross-
  sell agora?", "quando ofereço o mastermind", "ela cabe no 1:1?",
  "script de upgrade", "monetizar mentorada", "próxima oferta", "audit
  da esteira", ou ao concluir qualquer pipeline (dispara automático).
user_invocable: true
---

# Produtos Imperatriz — Pilar 8 da Travessia Imperatriz
# By Tata Gonçalves | Instituto Tata Gonçalves

> "Esteira é arquitetura, não improvisação.
>  Cada produto tem hora pra entrar na vida da mentorada —
>  oferecer fora da hora queima a venda E queima a mentorada."

---

## Filosofia central

**Esteira é arquitetura, não improvisação.**

A maioria das mentoras vende por impulso: lança o que tá com vontade, oferece o que tá com pressa de bater meta, fecha quem chegou primeiro. Resultado: cliente errada no produto errado, churn alto, refund, fadiga de oferta.

Aqui é o oposto. A esteira da Tata é uma **arquitetura sequencial** — cada produto pressupõe o anterior validado, cada upgrade tem critério objetivo, cada cross-sell tem janela específica. A mentorada sobe por mérito (não por vontade da Tata) e só recebe oferta de produto que ela está PRONTA pra absorver.

Três regras imperiais:

1. **Nunca oferecer produto que mentorada não está pronta pra absorver** — Aspirante não recebe oferta de 1:1. Princesa não recebe Mastermind. Travessia exige imersão prévia. Sem exceção.
2. **Nunca forçar cross-sell em momento de crise** — KPI vermelho, churn risk, crise pessoal? Suspende oferta. Salva o ser humano antes de salvar a meta.
3. **Comissão de afiliados clara e generosa (50%+)** — Mentorada que indica é sócia da causa. Comissão mesquinha mata o programa.

---

## Tom de Voz — DNA da Tata (PT-BR)

- Direta mas calorosa. Técnica mas acessível. Exigente mas acolhedora.
- "A gente", "Show!", "Faz sentido?", "Sacou?", "Bora!"
- Confirma sempre: "Tá?", "Entendeu?"
- Celebra com energia: "Boa, garota!", "Arrasou!", "Muito orgulhosa!"
- Vende com presença, sem pressão: "Olha, eu acho que chegou a hora."
- NUNCA empurra: "Cê tá pronta. Ou tá no momento?"
- PT-BR sempre. Sem travessão de IA. Voz humana.

---

## A Esteira Completa — 10 Produtos

| # | Posição | Produto | Ticket | Pra quem |
|---|---------|---------|--------|----------|
| 1 | Topo de funil | Skills compartilháveis (toolkit público) | R$0 | Audiência fria |
| 2 | Entrada paga | Imperatriz Toolkit (6 skills premium) | R$297-997 | Aspirante / curiosa |
| 3 | Autoridade | Bestseller (livro físico + ebook) | R$49-99 | Audiência ampla |
| 4 | Imersão | Imersões presenciais | R$2-7k | Princesa / Duquesa |
| 5 | Mentoria principal | **TRAVESSIA IMPERATRIZ** (A-Z completa) | R$30-50k | Princesa → Imperatriz |
| 6 | Mastermind | Mastermind premium | R$30-100k/ano | Duquesa+ |
| 7 | 1:1 | 1:1 com Tata | R$200-500k/ano | Condessa+ |
| 8 | B2B | Consultoria empresarial | R$100k+ | Empresas |
| 9 | Afiliados | Programa de afiliados | comissão 50%+ | Mentoradas qualquer nível |
| 10 | Pós-Travessia | Sucessão (sócia/treinadora/white label) | varia | Imperatriz Plena |

Detalhamento completo de cada produto em [`ESTEIRA-COMPLETA.md`](ESTEIRA-COMPLETA.md).

---

## Os 6 Níveis Hierárquicos como filtro automático

A esteira respeita a hierarquia da Travessia. Nível = porta de elegibilidade automática:

```
ASPIRANTE     → 1, 2, 3 (Skills, Toolkit, Livro)
PRINCESA      → +4, 5 (Imersões, Travessia)
DUQUESA       → +6, 9 (Mastermind, Afiliados ativos)
CONDESSA      → +7 (1:1)
IMPERATRIZ    → +8 (Consultoria B2B se tiver empresa)
IMPERATRIZ PLENA → +10 (Sucessão)
```

**Regra dura:** se a mentorada não tem o nível mínimo, a oferta NÃO É APRESENTADA. Não é estratégia — é arquitetura.

---

## Quando usar (gatilhos)

- Após concluir qualquer pipeline em `tatou-2.0` (dispara automático)
- Tata pergunta "qual produto eu ofereço pra Maria agora?"
- Mentorada acabou de pagar produto X, quer saber qual o próximo
- Auditoria mensal da Corte: quem tá pronta pra subir de produto
- Lançamento novo: quem da base é elegível
- Mentorada perguntou pela primeira vez sobre Mastermind/1:1/Travessia

---

## MODOS DE OPERAÇÃO

A skill roda em 4 modos declaráveis:

### `--mapa` — Esteira completa
Mostra os 10 produtos da Tata, ticket, perfil, lógica de ordem.
Output: tabela + diagrama da esteira + matriz de elegibilidade por nível.

### `--proximo [nome]` — Qual produto sugerir pra essa mentorada AGORA
Lê dossiê da mentorada, cruza com nível + histórico de compras + KPIs + timing.
Output: 1 produto recomendado + 1 alternativa + justificativa + janela ideal de oferta.

### `--cross-sell [nome] [produto]` — Script de cross-sell pra produto X
Gera script literal pra Tata oferecer produto X pra mentorada Y.
Output: 3 versões (WhatsApp curto, e-mail formal, mensagem na call) + 5 objeções + respostas + sinais de "agora não".

### `--timing [nome]` — Quando próxima oferta?
Calcula janela ideal pra próximo cross-sell baseado em última compra + KPIs + sazonalidade.
Output: data/janela + condições mínimas + sinais de readiness.

Se a Tata não declarar modo, perguntar: **"--mapa, --proximo, --cross-sell ou --timing?"**

---

## PROCESSO — 7 fases obrigatórias

### FASE 0 — Leitura de contexto (sempre)

Lê `dossie-mentorada` da mentorada-alvo (campos críticos):

- `01-perfil.json` → nome, slug, status, há quanto tempo na Travessia
- `15-nivel.json` → nível hierárquico atual (Aspirante → Imperatriz Plena)
- `14-progresso.json` → portas concluídas, gates passados, ritos validados
- `19-historico-compras.json` → produtos já comprados + datas + ticket pago
- `02-diagnostico.json` → KPIs atuais (verde/amarelo/vermelho)
- `18-historico-decisoes.json` → ofertas anteriores (aceitas/recusadas/adiadas)

Se o dossiê não existe → bloquear e despachar `dossie-mentorada --criar` antes.

### FASE 1 — Verificação de elegibilidade hierárquica

Filtro 1: **nível atual permite o produto X?**

```
Se nível < pré-requisito → BLOQUEIO AUTOMÁTICO
Output: "Mentorada está em [nível]. Produto X exige [nível mínimo].
         Produto recomendado pra ela agora: [Y]."
```

Sem exceção. Se a Tata insistir em forçar, sinaliza risco e pede confirmação dupla.

### FASE 2 — Verificação de pré-requisito de produto

Filtro 2: **mentorada já comprou o produto anterior na esteira?**

Regras:
- Travessia Imperatriz exige imersão prévia OU equivalente (caso direto raríssimo)
- Mastermind exige 6+ meses de Travessia validados
- 1:1 exige 12+ meses de Mastermind ou ticket B2B comprovado
- Sucessão exige conclusão da Travessia + Imperatriz Plena

Se faltou pré-requisito → sugerir produto intermediário primeiro.

### FASE 3 — Verificação de timing

Filtro 3: **estamos na janela certa?**

Regras de timing:
- Mínimo **60 dias** entre cross-sells (não satura)
- Mínimo **90 dias** se o produto anterior foi de implementação longa (Travessia, Mastermind)
- **Janela proibida:** 30 dias após oferta recusada (deixa esfriar)
- **Janela quente:** 14 dias após resultado celebrado (KPI verde, case fechado, gate passado)
- **Sazonalidade:** lançamentos em Janeiro (recomeço), Maio (meio de ano), Setembro (volta), Black Friday (Toolkit/Livro só)
- **Imersões:** janelas fixas no calendário (não ofertar fora dela)

Output: data ideal + janela aceitável + janela proibida.

### FASE 4 — Verificação de saúde (regra dura)

Filtro 4: **mentorada está saudável pra absorver oferta?**

Bloqueios automáticos:
- KPI vermelho em 2+ áreas → SUSPENDE oferta
- Churn risk identificado em `dashboard-imperatriz` → SUSPENDE oferta
- Crise pessoal declarada (luto, separação, problema de saúde) → SUSPENDE oferta
- Reclamação aberta com Tata → SUSPENDE oferta
- Inadimplência > 15 dias → SUSPENDE oferta

Se bloqueado → output recomenda **conversa de cuidado, não oferta**. Reagenda em 30/60 dias.

### FASE 5 — Cross-referência com `tatou-2.0`

Lê estado atual de despacho:
- Pipeline ativo? Se sim, qual?
- Próximo gate?
- Próxima porta?

Regras:
- NÃO oferecer durante pipeline crítico em execução (espera concluir)
- Cross-sell ideal: logo após **gate passado** (estado emocional alto)
- Cross-sell perigoso: durante porta travada (estado emocional baixo)

### FASE 6 — Geração da recomendação

Output estruturado (ver formatos por modo abaixo).

Inclui sempre:
- Produto recomendado
- Justificativa (3 frases)
- Janela ideal (data ou intervalo)
- Sinais de "vai" (greenlight)
- Sinais de "espera" (red flag)
- Script de oferta (1 versão curta)
- Resposta a 2 objeções mais prováveis

### FASE 7 — Gravação no dossiê

Grava em `19-historico-compras.json` (campo `ofertas_planejadas`):
- Produto recomendado
- Data planejada
- Status: `planejada` / `apresentada` / `aceita` / `recusada` / `adiada`
- Resposta da mentorada (quando vier)

Auditoria fica em `18-historico-decisoes.json`.

---

## FORMATO DE OUTPUT

### Modo `--mapa`

```
# ESTEIRA DE ASCENSÃO — Produtos da Tata

[tabela completa dos 10 produtos]

## Lógica de ordem
[diagrama em ASCII]

## Matriz de elegibilidade por nível hierárquico
[matriz Aspirante → Imperatriz Plena × 10 produtos]

## Próximos lançamentos da Tata
[calendário 90 dias com janelas de oferta]
```

### Modo `--proximo [nome]`

```
# PRÓXIMA OFERTA — [Nome da mentorada]

## SITUAÇÃO ATUAL
- Nível: [X]
- Tempo na Travessia: [X meses]
- Última compra: [produto + data]
- KPIs: [verde / amarelo / vermelho]
- Pipeline ativo: [X / nenhum]

## RECOMENDAÇÃO
**Produto:** [nome]
**Ticket:** R$[X]
**Janela ideal:** [data / intervalo]

## POR QUÊ AGORA
[3 frases de justificativa]

## SINAIS DE GREENLIGHT (oferece)
- [ ] [sinal 1]
- [ ] [sinal 2]
- [ ] [sinal 3]

## SINAIS DE RED FLAG (espera)
- [ ] [sinal 1]
- [ ] [sinal 2]

## ALTERNATIVA (se ela disser não)
[Produto B + por quê]

## SCRIPT CURTO (WhatsApp)
"[script literal]"

## OBJEÇÕES PROVÁVEIS
1. **"[objeção 1]"** → [resposta]
2. **"[objeção 2]"** → [resposta]
```

### Modo `--cross-sell [nome] [produto]`

```
# CROSS-SELL — [Mentorada] → [Produto]

## DIAGNÓSTICO DE PRONTIDÃO
[X/5 critérios de elegibilidade] → [GO / WAIT / BLOCK]

## SCRIPT V1 — WhatsApp (curto, 3-5 linhas)
"[script literal pra colar]"

## SCRIPT V2 — E-mail (formal)
**Assunto:** [linha]
**Corpo:** [4-6 parágrafos]

## SCRIPT V3 — Mensagem na call (presencial)
[roteiro de 2-3 minutos pra Tata falar olho no olho]

## STACK DE OBJEÇÕES (5 mais prováveis)
1. **"[objeção]"** → [resposta + prova]
2. ...

## SINAIS DE "AGORA NÃO"
- [sinal 1]
- [sinal 2]

## CTA / PRÓXIMO PASSO
[ação concreta pra mentorada tomar]
```

### Modo `--timing [nome]`

```
# TIMING — Próxima oferta pra [Nome]

## ÚLTIMA COMPRA
[produto + data + ticket]

## TEMPO DECORRIDO
[X dias / Y meses]

## JANELA IDEAL
**Mais cedo:** [data]
**Ideal:** [data]
**Limite:** [data — depois esfria]

## CONDIÇÕES MÍNIMAS PRA OFERTAR
- [ ] [condição 1]
- [ ] [condição 2]
- [ ] [condição 3]

## SINAIS DE READINESS A MONITORAR
- [sinal comportamental]
- [sinal de KPI]
- [sinal de calendário Tata]

## RECOMENDAÇÃO
**Produto:** [X]
**Quando:** [data ou janela]
**Como:** [canal de oferta — WhatsApp / call / e-mail]
```

---

## INTEGRAÇÃO COM O ECOSSISTEMA

### Lê (dependências de input)
- `dossie-mentorada` → 19 JSONs (fonte de verdade)
- `hierarquia-imperatriz` → critérios de cada nível
- `tatou-2.0` → estado atual de despacho + pipeline ativo
- `dashboard-imperatriz` → KPIs e churn risk
- `gates-imperatriz` → portas concluídas / travadas
- `calendario-imperatriz` → lançamentos da Tata + sazonalidade

### Grava (efeitos colaterais)
- `dossie-mentorada` → atualiza `19-historico-compras.json` (ofertas planejadas)
- `dossie-mentorada` → log em `18-historico-decisoes.json`
- `tatou-2.0` → notifica próxima oferta pra próximo despacho

### Dispara (encadeamento)
- `pricing-dinamico-imperatriz` → calcula ticket exato pra mentorada (ajuste por contexto)
- `crise-imperatriz` → se detectar churn risk durante check, despacha
- `reativacao-por-temperatura` → se mentorada tá fria, despacha primeiro

### Skills adjacentes (não canibalizar)
- `sucessao-imperatriz` → opera dentro do produto #10 (sucessão), não compete
- `cases-imperatriz` → fornece prova social pros scripts de cross-sell
- `compliance-imperatriz` → valida que oferta tá legalmente segura

---

## REGRAS DURAS (a skill NÃO negocia)

1. **NUNCA oferecer produto que mentorada não está pronta pra absorver** — bloqueio automático por nível
2. **NUNCA forçar cross-sell em momento de crise** (KPI vermelho, churn risk, crise pessoal)
3. **NUNCA pular pré-requisito de produto** (Travessia exige imersão, Mastermind exige 6m de Travessia, etc.)
4. **NUNCA ofertar dentro de janela proibida** (< 60 dias do último cross-sell, < 30 dias de oferta recusada)
5. **NUNCA inventar timing favorável** — se não tá na janela, fala que não tá
6. **NUNCA esconder ticket** — preço sempre claro, ancoragem sempre fundamentada
7. **SEMPRE oferecer alternativa** quando produto principal não couber
8. **SEMPRE registrar oferta no dossiê** (planejada → apresentada → resposta)
9. **SEMPRE respeitar comissão de afiliados de 50%+** quando o cross-sell vem por indicação
10. **SEMPRE checar `tatou-2.0`** antes de ofertar — não sobrescreve pipeline ativo
11. **SEMPRE adaptar script à voz da Tata** (PT-BR, sem travessão, sem jargão corporativo)
12. **SEMPRE rodar após conclusão de pipeline** (gancho automático)

---

## ANTI-PATTERNS (não fazer nunca)

1. **"Vamo ver se cola"** → ofertar Mastermind pra Princesa "só pra testar"
2. **"Ela tem grana"** → ofertar 1:1 pra mentorada com KPI vermelho porque pagou Travessia adiantada
3. **"Tô precisando bater meta"** → empurrar cross-sell em mentorada que acabou de comprar
4. **"Ela tá empolgada"** → vender Travessia sem imersão prévia porque a mentorada insistiu
5. **"Promoção pra todo mundo"** → broadcast de oferta sem filtro hierárquico
6. **"Ela não vai falar não"** → ignorar sinal de "agora não" porque histórico é bom
7. **"Black Friday em tudo"** → desconto em Travessia/Mastermind/1:1 (NUNCA — só Toolkit/Livro)
8. **"Comissão de afiliado 10%"** → matar o programa por avareza
9. **"Tata oferece direto"** → pular `dossie-mentorada` e operar de memória
10. **"Depois eu registro"** → fechar oferta e não gravar no dossiê

---

## ARQUIVOS DE REFERÊNCIA (carregar sob demanda)

- [`ESTEIRA-COMPLETA.md`](ESTEIRA-COMPLETA.md) — os 10 produtos detalhados (oferta, ticket, pré-requisito, perfil, prazo)
- [`LOGICA-CROSS-SELL.md`](LOGICA-CROSS-SELL.md) — matriz de quando oferecer o quê (filtros + janelas + sinais)
- [`SCRIPTS-CROSS-SELL.md`](SCRIPTS-CROSS-SELL.md) — scripts literais por produto (WhatsApp, e-mail, call)
- [`EXEMPLOS-JORNADAS.md`](EXEMPLOS-JORNADAS.md) — 3 jornadas completas Aspirante → Imperatriz Plena com timing real
- [`README.md`](README.md) — instalação + uso + integração

---

## VERSIONAMENTO

- **v1.0** (atual) — 10 produtos, 4 modos, 7 fases, integração `dossie-mentorada` + `tatou-2.0`
- **v1.5** (planejado) — auto-trigger pós-pipeline, A/B test de scripts
- **v2.0** (planejado) — base histórica de conversão por produto/nível, recomendação data-driven

---

**Método Imperatriz de Esteira de Produtos — propriedade intelectual Tata Gonçalves.**
