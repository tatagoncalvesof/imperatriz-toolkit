---
name: pricing-dinamico-imperatriz
description: >
  Motor de pricing dinamico da Travessia Imperatriz Tata Goncalves — trata
  preco como SISTEMA VIVO (nao tabela estatica). Camada estrategica acima
  da pricing-strategy: cruza capacidade da mentorada (slots), faturamento
  atual + meta, posicionamento (Princesa/Duquesa/Marquesa/Condessa),
  concorrencia direta, custos fixos + variaveis, sazonalidade, elasticidade
  historica e stock pricing pra entregar 3 cenarios (Conservador/Realista/
  Agressivo), janelas de aumento por gatilho (>80% slot vendido, 30/60 dias,
  campanha sazonal, ex-cliente), ancoragens R$X-R$Y-R$Z e simulacao de
  receita esperada. 4 modos (gerar/simular/janela/ancorar). Skill da Porta
  G (Garantia) inicial + Porta Y (Yield) revisita anual + sob demanda
  quando capacidade esta cheia. Le dossie-mentorada profile 11-oferta +
  16-kpis. Use quando a mentorada perguntar "posso aumentar meu preco?",
  "quanto cobrar?", "estou cobrando barato?", "como ancorar preco?",
  "qual desconto pra ex-cliente?", "minha agenda esta cheia, e agora?",
  "como reposicionar premium?", "3 cenarios de preco". Gatilhos: pricing
  dinamico, janela de aumento, ancoragem, 3 cenarios, conservador realista
  agressivo, slot vendido, elasticidade, stock pricing, simular receita,
  preco premium travessia, Porta G Yield. Metodo Imperatriz de Pricing —
  propriedade Tata Goncalves. Integra com /pricing-strategy, /luxe-empire,
  /skill-oferta-irresistivel, /high-ticket-strategist, /dossie-mentorada,
  /gates-imperatriz.
---

# Pricing Dinamico Imperatriz — Metodo Proprietario Tata Goncalves

Skill da **Porta G (Garantia)** inicial + **Porta Y (Yield)** revisita anual + sob demanda quando capacidade esta cheia. **Camada estrategica** acima da `pricing-strategy` (que e base mecanica). Aqui a gente trata preco como o que ele realmente e: **sistema vivo**.

## Filosofia central

> **Preco nao e tabela. E sistema vivo.**
>
> Tabela estatica e foto. Sistema vivo e filme. A mentorada que trata preco como foto perde dinheiro em 3 frentes: cobra abaixo do valor percebido, nao aproveita janela de capacidade cheia, e nao tem ancoragem que faca o preco-alvo parecer barato. Sistema vivo respira com capacidade, sazonalidade, elasticidade historica e posicionamento. Sobe quando a agenda esta cheia. Ancora alto pra parecer barato. Cria janela de oferta com gatilho real (nao falsa escassez). Recompensa cliente fiel sem destruir margem. Esse e o jogo da **Porta G + Porta Y** da Travessia.

Tres principios inseparaveis:

1. **Capacidade dita preco** — slot vendido > 80% e gatilho automatico de +10%
2. **Ancoragem precede numero** — R$X sozinho e caro; R$X depois de R$Y parece barato
3. **Elasticidade revela teto** — historico mostra quanto o publico aguenta antes de cair volume

## Quando usar

- Mentorada esta na **Porta G** (Garantia) construindo oferta inicial e precisa precificar
- Mentorada esta na **Porta Y** (Yield) — revisita anual de margem/receita
- Agenda da mentorada esta **>80% cheia** (gatilho de aumento)
- Mentorada quer **reposicionar premium** (saiu de Princesa pra Duquesa/Marquesa)
- Mentorada vai rodar **campanha sazonal** (Black Friday, fim de ano, aniversario)
- Ex-cliente quer renovar e mentorada nao sabe **quanto cobrar de quem ja foi cliente**
- Mentorada **bateu meta de receita** — proximo passo e recalibrar preco
- Antes de rodar `/skill-oferta-irresistivel` ou `/luxe-empire` — pricing-dinamico precede a copy da oferta

## Diferenca vs pricing-strategy (NAO canibalizar)

| Skill | Foco | Output |
|-------|------|--------|
| `/pricing-strategy` | Base mecanica — calcula custos, margens, modelos (assinatura/one-shot/freemium) | Tabela de preco fundamentada em custo |
| `/pricing-dinamico-imperatriz` | Camada estrategica — recomenda janelas de aumento, splits, ancoragens, 3 cenarios | Sistema vivo de pricing com gatilhos automaticos |

**Regra:** `/pricing-strategy` roda 1 vez (pra estabelecer base). `/pricing-dinamico-imperatriz` roda em ciclos (Porta G + Porta Y + sob demanda).

---

## MODOS DE OPERACAO

A skill roda em **4 modos declaraveis**:

- **`/pricing-dinamico-imperatriz --gerar [nome]`** — 3 cenarios completos (Conservador/Realista/Agressivo) com formulas, ancoragens e janelas
- **`/pricing-dinamico-imperatriz --simular [nome] [preco]`** — simula receita esperada num preco-alvo, com elasticidade aplicada
- **`/pricing-dinamico-imperatriz --janela [nome]`** — calcula proxima janela de aumento (gatilho ativo + cadencia)
- **`/pricing-dinamico-imperatriz --ancorar [nome]`** — gera tabela de ancoragens R$X-R$Y-R$Z pra uso em copy

Se a mentorada nao declarar modo em pedido grande, perguntar **"--gerar (3 cenarios), --simular (testar preco), --janela (proximo aumento) ou --ancorar (tabela)?"**.

---

## PROCESSO — 7 FASES OBRIGATORIAS

### FASE 0 — Leitura do dossie-mentorada

Antes de qualquer pergunta, ler:
- `~/imperio/mentoradas/[nome]/dossie/profile-11-oferta.json` — produto, preco atual, formato, prazo
- `~/imperio/mentoradas/[nome]/dossie/profile-16-kpis.json` — faturamento, meta, slots vendidos, churn, NPS
- `~/imperio/mentoradas/[nome]/dossie/profile-04-posicionamento.json` — Princesa/Duquesa/Marquesa/Condessa
- `~/imperio/mentoradas/[nome]/dossie/profile-09-concorrencia.json` (se existir)

Se faltar dossie, pedir pra rodar `/dossie-mentorada` antes — pricing-dinamico **nao opera sem profile 11 + 16**.

### FASE 1 — Coleta das 8 variaveis de input

A skill **nao gera cenario sem as 8 variaveis** abaixo. Se dossie nao tem, perguntar diretamente.

| # | Variavel | O que pergunta | Exemplo |
|---|----------|---------------|---------|
| 1 | **Capacidade** | Quantos clientes/mes a mentorada aguenta entregar com qualidade? | 6 mentoradas/mes |
| 2 | **Faturamento atual** | Quanto fatura hoje (media 3 ultimos meses)? | R$ 28.000/mes |
| 3 | **Meta** | Quanto quer faturar em 12 meses? | R$ 80.000/mes |
| 4 | **Posicionamento atual** | Princesa, Duquesa, Marquesa ou Condessa? (ver `luxe-empire`) | Duquesa |
| 5 | **Concorrencia direta** | 3-5 nomes + precos + diferenciais | Concorrente A R$ 4.997, B R$ 7.500, C R$ 12.000 |
| 6 | **Custos fixos + variaveis** | CAC, plataforma, time, comissao — pra calcular margem minima | Custo/cliente: R$ 800 |
| 7 | **Sazonalidade** | Mes forte? Mes fraco? Quanto varia? | Forte: jan, set / Fraco: jul, dez |
| 8 | **Historico de elasticidade** | Ja subiu preco antes? Sobe X%, vende quanto a menos? | +20% preco = -15% volume |

Bonus opcional:
- **Stock pricing** — cliente antigo paga preco antigo? Renovacao tem desconto? Politica de loyalty.

### FASE 2 — Diagnostico de saude do pricing atual

Calcular **3 indicadores criticos**:

**1. Taxa de ocupacao (Utilization Rate):**
```
Taxa = (slots vendidos / capacidade) x 100
< 60%  = preco alto demais OU oferta fraca (rodar /skill-oferta-irresistivel)
60-80% = pricing saudavel
> 80%  = GATILHO DE AUMENTO (subir preco em 30 dias)
> 95%  = AGENDA TRAVADA (subir preco AGORA — 2 semanas)
```

**2. Margem por cliente:**
```
Margem = (preco - custo variavel por cliente) / preco
< 50%  = ALERTA, margem ruim pra high-ticket
50-70% = saudavel
70-85% = excelente
> 85%  = teto, preco no limite ou produto digital escalavel
```

**3. Revenue Gap (gap entre atual e meta):**
```
Gap = (Meta - Faturamento atual) / Faturamento atual
< 30%  = otimizacao de preco resolve
30-100% = preco + escala de canal
> 100% = mudanca estrutural (mudar tier, criar produto novo)
```

### FASE 3 — Geracao dos 3 cenarios

Aplicar a formula de cada cenario (ver `OS-3-CENARIOS.md` pra detalhes completos):

**Cenario CONSERVADOR (baixo risco):**
```
Preco_conservador = Preco_atual x 1.10 a 1.20
```
- Risco de perda volume: < 5%
- Indicado pra: mentorada Princesa/Duquesa, primeira subida, ainda construindo autoridade
- Retencao de clientes existentes preservada

**Cenario REALISTA (calibrado):**
```
Preco_realista = max(
  Preco_atual x 1.30 a 1.50,
  Mediana_concorrencia x 1.10,
  Custo_variavel / (1 - margem_alvo_70%)
)
```
- Risco de perda volume: 10-20%
- Indicado pra: mentorada Duquesa/Marquesa com 6+ meses de prova social solida
- Calibrado por valor percebido + benchmark nicho

**Cenario AGRESSIVO (premium):**
```
Preco_agressivo = Preco_atual x 2.0 a 3.0
                  ou
                  Concorrente_topo x 1.20 a 1.50
```
- Risco de perda volume: 30-50% (compensado por margem dobrada)
- Indicado pra: mentorada Marquesa/Condessa com autoridade Luxe Empire instalada
- **Exige reposicionamento previo** (rodar `/luxe-empire` e `/skill-oferta-irresistivel` antes)

### FASE 4 — Calculo de janelas de aumento

Aplicar a **matriz de gatilhos** (ver `JANELAS-DE-AUMENTO.md` pra cadencia completa):

| Gatilho | Acao | Cadencia |
|---------|------|----------|
| Slot vendido > 80% por 30 dias | +10% | imediato (proxima venda) |
| Slot vendido > 80% por 60 dias | +20% | em 7 dias |
| Slot vendido > 95% (lista de espera) | +30% | em 48h |
| Campanha sazonal (Black Friday, aniversario) | -30% ancoragem (fica no preco real) | janela de 7 dias |
| Ex-cliente recompra | -50% (loyalty) ou +0% (retencao premium) | quando ele retornar |
| Reposicionamento (Princesa -> Duquesa) | +50% a +100% | unico, nao repetir em 12 meses |
| Caso de sucesso novo (proof) | +5 a +10% | a cada 3 cases medios OU 1 case lendario |

### FASE 5 — Geracao de ancoragens

Aplicar a **regra de 3 numeros** (ver `ANCORAGENS-ESTRATEGICAS.md`):

```
R$X = preco-alvo (o que voce quer cobrar)
R$Y = valor "real" mostrado (R$X x 10) — soma do stack de valor
R$Z = preco "concorrencia" ou "alternativa cara" (R$X x 2 a 3)
```

**Estrutura visual obrigatoria em copy:**
```
Valor total do que voce recebe: R$ Y (ancorado alto)
Preco da concorrencia premium: R$ Z (referencia de mercado)
Seu investimento hoje:          R$ X (parece barato depois de Y e Z)
```

### FASE 6 — Simulacao de receita esperada

Pra cada cenario, calcular:

```
Receita_projetada = Preco x Slots_vendidos_estimados x Meses
Margem_projetada  = Receita_projetada x (1 - Custo_variavel%)
```

Aplicar **elasticidade historica** se a mentorada ja subiu preco antes:
```
Slots_estimados = Slots_atuais x (1 - Elasticidade x Variacao_preco%)
```

Exemplo: se historico mostra elasticidade -0.75 (sobe 20%, perde 15%), e a mentorada vai subir 30%:
```
Variacao_volume = -0.75 x 30% = -22.5%
Slots_novos = Slots_atuais x 0.775
```

Comparar **Receita_atual vs Receita_projetada** nos 3 cenarios — recomendar o que tem **maior margem** (nao maior receita necessariamente).

### FASE 7 — Output estruturado em JSON

Salvar em `~/imperio/mentoradas/[nome]/pricing-dinamico-[trimestre].json` (formato abaixo na secao OUTPUT).

Imprimir resumo legivel pra mentorada com:
- Diagnostico (3 indicadores)
- 3 cenarios lado a lado
- Janela ativa (se houver gatilho)
- Tabela de ancoragens
- Recomendacao final + proximos passos

---

## FORMATO DE OUTPUT (modo --gerar)

### JSON salvo

```json
{
  "mentorada": "[nome]",
  "trimestre": "2026-Q2",
  "data_geracao": "2026-05-08",
  "porta": "G ou Y",
  "diagnostico": {
    "taxa_ocupacao": 0.85,
    "margem_atual": 0.72,
    "revenue_gap": 0.45,
    "alertas": ["Slot >80% por 45 dias — gatilho de +10% ativo"]
  },
  "input": {
    "capacidade": 6,
    "faturamento_atual": 28000,
    "meta_12m": 80000,
    "posicionamento": "Duquesa",
    "preco_atual": 4997,
    "custo_variavel_cliente": 800,
    "concorrencia": [
      {"nome": "A", "preco": 4997, "diferencial": "..."},
      {"nome": "B", "preco": 7500, "diferencial": "..."}
    ],
    "sazonalidade": {"forte": ["jan", "set"], "fraco": ["jul", "dez"]},
    "elasticidade_historica": -0.75
  },
  "cenarios": {
    "conservador": {
      "preco": 5497,
      "variacao_pct": 10,
      "slots_estimados_mes": 6,
      "receita_projetada_mes": 32982,
      "margem_pct": 0.74,
      "risco_volume_pct": 5,
      "indicado_quando": "primeira subida, mentorada ainda Duquesa"
    },
    "realista": {
      "preco": 6997,
      "variacao_pct": 40,
      "slots_estimados_mes": 5,
      "receita_projetada_mes": 34985,
      "margem_pct": 0.79,
      "risco_volume_pct": 17,
      "indicado_quando": "6+ meses de prova solida, posicionamento Duquesa/Marquesa"
    },
    "agressivo": {
      "preco": 12000,
      "variacao_pct": 140,
      "slots_estimados_mes": 3,
      "receita_projetada_mes": 36000,
      "margem_pct": 0.85,
      "risco_volume_pct": 50,
      "indicado_quando": "exige reposicionamento Luxe + 3 cases lendarios + autoridade midiatica",
      "pre_requisitos": ["rodar /luxe-empire", "ter 3+ cases publicos", "reformular oferta com /skill-oferta-irresistivel"]
    }
  },
  "janelas_ativas": [
    {
      "gatilho": "slot >80% por 45 dias",
      "acao": "+10%",
      "prazo": "imediato",
      "comunicacao_cliente": "Texto sugerido na proxima venda: '...'"
    }
  ],
  "ancoragens": {
    "preco_alvo_X": 6997,
    "valor_real_Y": 69970,
    "preco_concorrencia_Z": 14000,
    "stack_valor_breakdown": [
      {"item": "Mentoria 12 semanas", "valor_ancora": 25000},
      {"item": "Acesso comunidade vitalicio", "valor_ancora": 10000},
      {"item": "Consultoria 1:1 mensal", "valor_ancora": 18000},
      {"item": "Templates + scripts", "valor_ancora": 5000},
      {"item": "Bonus historia metodo", "valor_ancora": 4970},
      {"item": "Suporte WhatsApp 90 dias", "valor_ancora": 7000}
    ]
  },
  "stock_pricing": {
    "preco_cliente_novo": 6997,
    "preco_renovacao": 4997,
    "preco_recuperacao_ex_cliente": 3498
  },
  "recomendacao_final": {
    "cenario_recomendado": "realista",
    "racional": "Slot >80%, posicionamento Duquesa, 8 cases solidos, elasticidade controlada. Margem sobe 7pp e receita +25%.",
    "proximos_passos": [
      "Rodar /skill-oferta-irresistivel pra atualizar copy com novo preco",
      "Atualizar landing com ancoragem R$X-R$Y-R$Z",
      "Comunicar reajuste pros leads quentes em 7 dias",
      "Rodar /pricing-dinamico-imperatriz --janela em 60 dias pra reavaliar"
    ]
  }
}
```

### Resumo legivel impresso

```
# PRICING DINAMICO — [nome] — 2026-Q2

## DIAGNOSTICO
- Taxa de ocupacao: 85% (>80% = gatilho de aumento ATIVO)
- Margem atual: 72% (saudavel)
- Revenue gap: 45% (otimizacao de preco resolve)

## 3 CENARIOS

### CONSERVADOR — R$ 5.497 (+10%)
Receita: R$ 32.982/mes | Margem: 74% | Risco volume: 5%
Indicado quando: primeira subida, ainda construindo autoridade

### REALISTA — R$ 6.997 (+40%)  RECOMENDADO
Receita: R$ 34.985/mes | Margem: 79% | Risco volume: 17%
Indicado quando: 6+ meses de prova solida, Duquesa/Marquesa

### AGRESSIVO — R$ 12.000 (+140%)
Receita: R$ 36.000/mes | Margem: 85% | Risco volume: 50%
EXIGE: reposicionamento Luxe + 3 cases lendarios + autoridade midiatica

## JANELA ATIVA
Gatilho: slot >80% por 45 dias -> +10% imediato

## ANCORAGEM
R$X (alvo)            R$ 6.997
R$Y (valor real)      R$ 69.970
R$Z (concorrencia)    R$ 14.000

## STOCK PRICING
Cliente novo:         R$ 6.997
Renovacao:            R$ 4.997
Ex-cliente (recovery) R$ 3.498

## RECOMENDACAO: CENARIO REALISTA
[Racional + 4 proximos passos]
```

---

## MODO --simular

Recebe `[nome] [preco]` e retorna:

```
# SIMULACAO — [nome] — Preco testado: R$ 8.500

Preco atual: R$ 4.997
Variacao: +70%
Elasticidade historica: -0.75

Slots estimados: 4/mes (vs 6 atuais)
Receita projetada: R$ 34.000/mes (vs R$ 29.982 atuais) = +13%
Margem projetada: 81% (vs 72% atual) = +9pp

ALERTA: variacao de 70% acima do realista (40%) — risco volume 50%+
RECOMENDACAO: testar primeiro cenario realista (R$ 6.997) por 90 dias.
```

---

## MODO --janela

Recebe `[nome]` e retorna proxima janela de aumento:

```
# PROXIMA JANELA — [nome]

GATILHO ATIVO: slot vendido 85% por 45 dias
ACAO: +10% (de R$ 4.997 pra R$ 5.497)
PRAZO: imediato — aplicar na proxima venda

COMUNICACAO SUGERIDA (lead quente):
"Oi [nome], passando pra avisar que minha agenda fecha proxima semana
e a partir do mes que vem o investimento sobe pra R$ 5.497.
Se voce ja decidiu que e essa mentoria que voce quer, fecha hoje no
preco atual de R$ 4.997. Te mando o link?"

PROXIMA JANELA APOS ESSA: 60 dias (se slot continuar >80%, +20%)
```

---

## MODO --ancorar

Recebe `[nome]` e gera tabela de ancoragens pra copy:

```
# TABELA DE ANCORAGENS — [nome]

PRECO-ALVO (X):       R$ 6.997
VALOR REAL (Y):       R$ 69.970 (10x)
PRECO CONCORRENCIA (Z): R$ 14.000 (2x)

## STACK BREAKDOWN (pra mostrar o R$Y)
- Mentoria 12 semanas: R$ 25.000
- Acesso comunidade vitalicio: R$ 10.000
- Consultoria 1:1 mensal: R$ 18.000
- Templates + scripts: R$ 5.000
- Bonus historia do metodo: R$ 4.970
- Suporte WhatsApp 90 dias: R$ 7.000
TOTAL: R$ 69.970

## USO EM COPY
Bloco de pagina de vendas:
"Valor total do que voce recebe: R$ 69.970
Preco da concorrencia premium:   R$ 14.000
Seu investimento hoje:           R$ 6.997 (ou 12x R$ 583)"

## VARIACOES POR CANAL
- VSL: usar R$Y na hora do reveal
- Email: usar R$Z no subject ("a versao de R$14.000 sai por...")
- Anuncio: usar R$X no preview, R$Y no clique
```

---

## REGRAS DURAS (a skill NAO negocia)

1. **Nao gera cenario sem as 8 variaveis de input** — pede pra rodar `/dossie-mentorada` se faltar
2. **Nao recomenda cenario agressivo sem reposicionamento previo** — exige rodar `/luxe-empire` antes
3. **Nao inventa elasticidade** — se mentorada nunca subiu preco, usar elasticidade conservadora padrao (-0.6) e sinalizar
4. **Nao recomenda preco abaixo da margem 50%** — sinaliza alerta vermelho
5. **Nao usa falsa escassez** — janela so abre com gatilho REAL (slot >80%, sazonalidade, ex-cliente)
6. **Nao recomenda aumento >50% em mentorada Princesa** — exige passar por Duquesa antes
7. **Nao copia preco da concorrencia** — usa como referencia, nunca como alvo (mentorada precisa ter mecanismo unico que justifique)
8. **Sempre apresenta 3 cenarios** — nunca um so (mentorada precisa ver as opcoes)
9. **Sempre calcula margem projetada** — receita sem margem e armadilha
10. **Sempre salva JSON** em `~/imperio/mentoradas/[nome]/pricing-dinamico-[trimestre].json`
11. **Sempre cruza com dossie-mentorada** profile-11-oferta + 16-kpis
12. **Sempre sugere proximos passos** integrando com `/skill-oferta-irresistivel` + `/luxe-empire` + `/gates-imperatriz`

---

## INTEGRACAO COM O ECOSSISTEMA TATA

**Ordem ideal no fluxo da Travessia:**

```
/dossie-mentorada (profile 11 + 16)
       v
/pricing-strategy (base mecanica — 1 vez)
       v
/pricing-dinamico-imperatriz   <- VOCE ESTA AQUI
       v
/luxe-empire (se cenario agressivo)
       v
/skill-oferta-irresistivel (atualizar oferta com novo preco + ancoragem)
       v
/high-ticket-strategist (pitch de fechamento com nova ancoragem)
       v
/gates-imperatriz (validar Porta G ou Porta Y concluida)
```

**Skills adjacentes:**
- `/pricing-strategy` — base mecanica (precede)
- `/luxe-empire` — pre-requisito do cenario agressivo
- `/skill-oferta-irresistivel` — atualiza copy apos novo preco
- `/high-ticket-strategist` — pitch + fechamento
- `/dossie-mentorada` — fonte de input
- `/gates-imperatriz` — valida saida da Porta G ou Y

**Ciclos de re-execucao:**
- **Porta G inicial** — uma vez, ao construir oferta
- **Porta Y revisita** — anual obrigatorio
- **Sob demanda** — quando capacidade >80%, quando bate meta, quando sazonalidade chega, quando ex-cliente retorna

---

## ARQUIVOS DE REFERENCIA (carregar sob demanda)

- `OS-3-CENARIOS.md` — formulas detalhadas de Conservador/Realista/Agressivo + 3 casos
- `JANELAS-DE-AUMENTO.md` — matriz completa de gatilhos + cadencia + comunicacao ao cliente
- `ANCORAGENS-ESTRATEGICAS.md` — 12 tecnicas de ancoragem premium BR
- `EXEMPLOS-PRICING.md` — 3 casos resolvidos (mentora R$5k->R$30k, infoprodutora R$497->R$1997, B2B R$50k->R$300k)

---

## VERSIONAMENTO

- **v1.0** (atual) — 4 modos, 7 fases, 3 cenarios, integracao Travessia
- **v1.5** (planejado) — auto-trigger via cron quando capacidade >80% (cruza com KPIs do dossie)
- **v2.0** (planejado) — feedback loop com receita real pos-aumento (ajusta elasticidade automaticamente)

---

**Metodo Imperatriz de Pricing — propriedade intelectual Tata Goncalves.**
