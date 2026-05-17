# LÓGICA DE CROSS-SELL — Matriz de Quando Oferecer o Quê

> *"A pergunta certa não é 'o que eu ofereço?'.  
>  É 'a mentorada está pronta pra absorver?'."*

Documento operacional que define **QUANDO** oferecer **QUAL** produto pra **QUAL** mentorada. Combina 4 filtros (hierarquia, pré-requisito, timing, saúde) em matriz de decisão objetiva.

---

## OS 4 FILTROS (ordem obrigatória)

Toda decisão de cross-sell passa por 4 filtros sequenciais. Se reprovar em qualquer um → BLOQUEIO.

```
FILTRO 1 — HIERARQUIA      "Nível dela permite o produto?"
        ↓ (se sim)
FILTRO 2 — PRÉ-REQUISITO   "Já comprou o produto anterior?"
        ↓ (se sim)
FILTRO 3 — TIMING          "Janela está aberta?"
        ↓ (se sim)
FILTRO 4 — SAÚDE           "Mentorada está saudável pra absorver?"
        ↓ (se sim)
        OFERTA APROVADA
```

---

## FILTRO 1 — HIERARQUIA

**Critério:** nível atual da mentorada permite o produto?

| Nível atual         | Pode receber oferta de                                 | NÃO pode receber                       |
|---------------------|--------------------------------------------------------|----------------------------------------|
| Aspirante           | Skills, Toolkit, Livro, Afiliados (com audiência)      | Imersão (exceção), Travessia, Mastermind, 1:1, Sucessão |
| Princesa            | + Imersão, Travessia                                   | Mastermind, 1:1, Sucessão              |
| Duquesa             | + Mastermind                                           | 1:1, Sucessão                          |
| Condessa            | + 1:1                                                  | Sucessão                               |
| Imperatriz          | + (oferta de upgrade dentro de produtos elite)         | Sucessão (até rito plena)              |
| Imperatriz Plena    | + Sucessão (3 caminhos)                                | (todos liberados)                      |

**Regra dura:** se nível < pré-requisito do produto → BLOQUEIO AUTOMÁTICO. Sem exceção.

**Como exceção qualificada funciona:**
- Aspirante avançada pode receber Imersão se: tem caso de receita comprovada (>R$15k/mês), recomendada por mentorada de nível Duquesa+, e KPIs verdes em 3 meses.
- Caso direto Travessia (sem Imersão) é **raríssimo** — só se Tata conhece a mentorada pessoalmente há 6+ meses e tem track record indiscutível.

---

## FILTRO 2 — PRÉ-REQUISITO DE PRODUTO

**Critério:** mentorada já comprou o produto anterior na esteira?

| Produto-alvo | Pré-requisito mínimo |
|--------------|----------------------|
| Toolkit      | (recomendado: skill pública usada) — não obrigatório |
| Livro        | nenhum |
| Imersão      | (recomendado: Toolkit OU Livro OU live assistida) |
| **Travessia**    | **Imersão prévia** OU caso direto raríssimo |
| Mastermind   | 6+ meses de Travessia validados (Estação 3 concluída) |
| 1:1          | 12+ meses em Mastermind OU operação B2B comprovada |
| B2B          | ICP empresarial (não aplica esteira pessoal) |
| Afiliados    | Audiência mínima + produto validado pela própria mentorada |
| Sucessão     | Rito de Imperatriz Plena validado + 12m elite |

**Regras duras:**
- Não pular pré-requisito por "vontade da mentorada"
- Não pular pré-requisito por "pressa de bater meta"
- Não pular pré-requisito por "ela tem grana"

Se faltou pré-requisito → ofertar produto intermediário primeiro.

---

## FILTRO 3 — TIMING

**Critério:** estamos na janela certa pra essa oferta?

### Regras de espaçamento entre cross-sells

| Situação | Espera mínima |
|----------|---------------|
| Última compra de produto leve (Toolkit, Livro) | 60 dias |
| Última compra de Imersão | 60 dias |
| Última compra de Travessia | 90 dias |
| Última compra de Mastermind / 1:1 | 120 dias |
| Oferta recusada (mentorada disse "não agora") | 30 dias mínimo, idealmente 60 dias |
| Oferta adiada ("depois eu vejo") | 45 dias |
| Pipeline ativo em `tatou-2.0` | até pipeline concluir |
| Gate travado em `gates-imperatriz` | até gate liberar |

### Janelas QUENTES (acelerar oferta)

Em janela quente, espera mínima cai pela metade. São situações de estado emocional alto:

- **+14 dias após gate passado** (mentorada em vibe de "tô vencendo")
- **+14 dias após resultado celebrado** (KPI verde, case fechado, prêmio recebido)
- **+7 dias após Imersão concluída** (peak de oferta de Travessia — janela curta de 15-30 dias)
- **+7 dias após depoimento espontâneo** (mentorada postou nas redes elogiando a Tata)

### Janelas PROIBIDAS (NÃO ofertar)

- 30 dias após oferta recusada
- 7 dias após reclamação aberta
- Durante crise pessoal declarada
- Durante pipeline crítico em execução
- Inadimplência em aberto
- Black Friday (pra Travessia/Mastermind/1:1) — sazonalidade não vale pra premium

### Sazonalidade da Tata (calendário)

| Mês | Foco de oferta |
|-----|----------------|
| Jan | Toolkit (recomeço) + reabertura afiliados |
| Fev-Abr | Pré-Imersão Olimpo |
| **Mai** | **Imersão Olimpo + abertura Travessia turma Maio** |
| Jun | Onboarding Travessia / Mastermind H2 prep |
| Jul | Lançamento Mastermind (turma anual) |
| Ago | Pré-Imersão Travessia |
| **Set** | **Imersão Travessia + abertura Travessia turma Outubro** |
| Out | Onboarding Travessia |
| **Nov** | **Black Friday: Toolkit + Livro APENAS** |
| Dez | Imersão Sucessão (Imperatriz Plena + ex-alunas) |

**Regra:** ofertar Travessia em mês fora de janela calendarizada = falha. Espera a janela.

---

## FILTRO 4 — SAÚDE

**Critério:** mentorada está saudável pra absorver oferta?

### Bloqueios automáticos (SUSPENDE oferta)

| Sinal | Ação |
|-------|------|
| KPI vermelho em 2+ áreas | SUSPENDE — despacha `crise-imperatriz` |
| Churn risk identificado em `dashboard-imperatriz` | SUSPENDE — agenda conversa de cuidado |
| Crise pessoal declarada (luto, separação, saúde) | SUSPENDE — reagenda em 30-60 dias |
| Reclamação aberta com Tata ou time | SUSPENDE — resolve antes de ofertar |
| Inadimplência > 15 dias | SUSPENDE — resolve cobrança antes |
| 2+ ofertas recusadas seguidas | SUSPENDE 90 dias — cool down |
| Mentorada pediu pausa explicitamente | SUSPENDE — respeita o pedido |

**Regra dura:** se saúde está comprometida, **conversa de cuidado primeiro, oferta depois**. Salva o ser humano antes de salvar a meta.

### Sinais de SAÚDE PLENA (greenlight reforçado)

- KPIs verdes em 3+ áreas por 60+ dias
- Pagamentos sempre em dia
- Engajamento alto na comunidade (posta, ajuda, comparece)
- Resultado público compartilhado nas redes
- Indicou outra mentorada (sinal de "tô feliz")
- Pediu mais (assinou newsletter VIP, mandou mensagem proativa)

Quando 3+ sinais de saúde plena estão presentes, janelas quentes ficam ainda mais quentes.

---

## MATRIZ DE DECISÃO — Cruzamento dos 4 Filtros

| Cenário | Hierarquia | Pré-req | Timing | Saúde | Decisão |
|---------|-----------|---------|--------|-------|---------|
| Princesa, fez Imersão há 30d, KPI verde, sem pipeline | ✅ | ✅ (Imersão) | ⚠️ (janela quente Imersão dura 15-30d) | ✅ | **OFERTA TRAVESSIA AGORA** (peak window) |
| Princesa, sem Imersão, KPI verde | ✅ | ❌ | n/a | ✅ | OFERTA IMERSÃO primeiro |
| Aspirante com R$50k livres querendo Travessia | ❌ | ❌ | n/a | n/a | BLOQUEIO — ofertar Toolkit + Imersão |
| Duquesa, 6m Travessia, KPI verde, julho | ✅ | ✅ | ✅ (lançamento Mastermind) | ✅ | **OFERTA MASTERMIND** |
| Duquesa, 6m Travessia, KPI vermelho | ✅ | ✅ | ✅ | ❌ | SUSPENDE — `crise-imperatriz` |
| Condessa, 12m Mastermind, B2B comprovado | ✅ | ✅ | ✅ | ✅ | **OFERTA 1:1** |
| Princesa, fez Imersão, recusou Travessia há 20d | ✅ | ✅ | ❌ (janela proibida) | ✅ | ESPERA — reagenda em 30-45 dias |
| Imperatriz Plena, rito validado, 12m em 1:1 | ✅ | ✅ | ✅ | ✅ | **CONVITE SUCESSÃO** (não oferta — convite) |
| Aspirante com 5k seguidores, comprou Toolkit, usa há 90d | ✅ | ✅ | ✅ | ✅ | **OFERTA AFILIADOS** |
| Princesa, KPI verde, mas pipeline crítico em execução | ✅ | ✅ | ❌ | ✅ | ESPERA pipeline concluir |

---

## ÁRVORE DE DECISÃO RÁPIDA (cheat sheet)

```
A mentorada quer/precisa de upgrade?
│
├── Tem nível mínimo do produto-alvo?
│   ├── NÃO → BLOQUEIO. Sugere produto intermediário.
│   └── SIM ↓
│
├── Tem pré-requisito de produto?
│   ├── NÃO → Sugere produto intermediário primeiro.
│   └── SIM ↓
│
├── Está em janela de timing?
│   ├── NÃO (proibida) → ESPERA. Calcula quando reabre.
│   ├── (neutra) → AGENDA pra próxima janela quente.
│   └── (quente) ↓
│
├── Saúde permite?
│   ├── NÃO → SUSPENDE. Conversa de cuidado.
│   └── SIM ↓
│
└── OFERTA APROVADA → gera script via `--cross-sell`
```

---

## PADRÕES DE CROSS-SELL POR ESTADO

### Pós-Skill Pública usada → Toolkit
**Quando:** mentorada usou skill pública 3+ vezes em 30 dias  
**Sinal:** comentou no GitHub, postou nas redes, pediu suporte  
**Janela:** assim que sinal aparece (sem espera)  
**Canal:** DM ou e-mail direto  
**Ticket:** R$297 (entrada) ou R$497 (lifetime)  
**Probabilidade de fechar:** 30-40%

### Pós-Toolkit (60d+) → Imersão
**Quando:** Toolkit comprado há 60-120 dias + uso ativo  
**Sinal:** implementou skill no negócio + faturou com isso  
**Janela:** alinhada com calendário de Imersão (Mai/Set)  
**Canal:** e-mail formal + retargeting Instagram  
**Ticket:** lote 1 R$1.997  
**Probabilidade de fechar:** 15-25%

### Pós-Imersão (D+1 a D+15) → Travessia
**Quando:** mentorada saiu da Imersão até 15 dias atrás  
**Sinal:** foi até o último dia, conversou off-stage, perguntou ticket  
**Janela:** 48h pós-Imersão (janela curta, alta conversão) ou até 15 dias (janela média)  
**Canal:** call 1:1 com Tata ou time qualificado  
**Ticket:** lote Imersão R$30k  
**Probabilidade de fechar:** 30-50% (peak)

### Pós-Travessia 6m → Mastermind
**Quando:** 6+ meses de Travessia, Estação 3 concluída, KPI verde  
**Sinal:** liderança na Corte, faturamento Duquesa+, pediu mais  
**Janela:** lançamento Mastermind (Janeiro ou Julho)  
**Canal:** convite individual via call (não broadcast)  
**Ticket:** R$30-100k/ano  
**Probabilidade de fechar:** 40-60% (já validou Tata, é decisão de continuar)

### Pós-Mastermind 12m → 1:1
**Quando:** 12+ meses Mastermind + complexidade que excede grupo  
**Sinal:** problema estratégico recorrente, B2B aberto, M&A na mesa  
**Janela:** sob convite (raro, vagas limitadas 4-6)  
**Canal:** conversa privada com Tata, presencial idealmente  
**Ticket:** R$200-500k/ano  
**Probabilidade de fechar:** 60-80% (já é elite, é decisão de profundidade)

### Pós-Travessia + Mastermind (Imperatriz Plena) → Sucessão
**Quando:** rito Plena validado + perfil de transmissão + 12m elite  
**Sinal:** ajuda outras na Corte espontaneamente, tem audiência/equipe  
**Janela:** convite anual em Imersão Sucessão (Dezembro)  
**Canal:** convite presencial em retiro privado  
**Ticket:** varia por caminho  
**Probabilidade de fechar:** 50-70% (decisão de legado)

### Cross-sell lateral: Afiliados (qualquer momento)
**Quando:** mentorada com audiência + produto validado  
**Sinal:** indicou alguém espontaneamente OU pediu link de afiliado  
**Janela:** sempre aberta (não compete com esteira)  
**Canal:** automação (cadastro auto-serviço)  
**Comissão:** 50% (Toolkit/Livro/Imersão), 30% (Travessia)  
**Probabilidade de adesão:** 60-80% das que têm audiência

---

## ANTI-PATTERNS DE TIMING

| Erro | Por que mata | Antídoto |
|------|--------------|----------|
| "Vou ofertar tudo na Black Friday" | Premium high-ticket não compra por desconto, queima posicionamento | BF SOMENTE Toolkit + Livro |
| "Ela acabou de pagar Travessia, vamo fechar Mastermind agora" | Saturação. Refund risk. Quebra confiança. | Mínimo 90 dias após Travessia |
| "Recusou semana passada, vou tentar de novo" | Mentorada se sente perseguida, churn risk | 30-60 dias mínimos pós-recusa |
| "É só me chamar de volta no DM" | Sem janela calculada vira spam | Skill calcula janela específica |
| "Black Friday em Travessia 30% off" | Quem pagou cheio fica revoltado, queima receita futura | NUNCA Travessia/Mastermind/1:1 em BF |
| "Ofertar 1:1 pra Princesa porque ela tem grana" | Pula nível, Princesa não absorve, refund certo | Filtro hierarquia bloqueia |
| "Empurra cross-sell durante pipeline crítico" | Distração, perde foco do pipeline, conclui mal | Espera pipeline concluir |

---

## INDICADORES DE SUCESSO DA ESTEIRA (medir mensalmente)

| KPI | Meta saudável | Sinal de problema |
|-----|---------------|-------------------|
| Taxa de conversão Toolkit → Imersão | 15-25% | <10% = pré-Imersão fraca |
| Taxa de conversão Imersão → Travessia | 30-50% | <20% = pitch ou Imersão fraca |
| Taxa de conversão Travessia → Mastermind | 40-60% | <30% = experiência Travessia fraca |
| Taxa de retenção Mastermind ano 2 | 70-85% | <60% = Mastermind não está entregando |
| Taxa de upgrade Mastermind → 1:1 | 10-20% | <5% = ofertando errado |
| Tempo médio Aspirante → Princesa | 3-9 meses | >12m = funil travado |
| Tempo médio Princesa → Imperatriz | 12-18 meses | >24m = Travessia não conclui |
| % de mentoradas afiliadas ativas | 30-50% | <20% = comissão baixa demais ou programa mal divulgado |

---

**Pilar 8 da Travessia Imperatriz — propriedade intelectual Tata Gonçalves.**
