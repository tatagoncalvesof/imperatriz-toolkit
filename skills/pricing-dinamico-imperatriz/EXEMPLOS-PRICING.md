# Exemplos de Pricing — 3 Casos Resolvidos Completos

Tres cases reais reconstruidos, com input completo, processamento dos 7 fases, output em JSON e racional de decisao. Use como **referencia operacional** pra calibrar a skill em casos novos.

---

## CASE 1 — Mariana, mentora de copy (R$ 5.000 -> R$ 30.000)

### Contexto

Mariana e mentora de copywriting pra empreendedoras digitais. Atua ha 18 meses. Vende mentoria em grupo de 12 semanas.

### Input completo

```json
{
  "mentorada": "mariana-copy",
  "capacidade": 8,
  "faturamento_atual": 32000,
  "meta_12m": 120000,
  "posicionamento": "Duquesa em transicao pra Marquesa",
  "preco_atual": 4997,
  "custo_variavel_cliente": 600,
  "concorrencia": [
    {"nome": "Copy Imperio", "preco": 4997, "diferencial": "comunidade grande"},
    {"nome": "Mentora X", "preco": 7997, "diferencial": "metodo proprio"},
    {"nome": "Y Lab", "preco": 12000, "diferencial": "1:1 incluso"},
    {"nome": "Premium Z", "preco": 18000, "diferencial": "midia + autoridade"}
  ],
  "sazonalidade": {
    "forte": ["jan", "fev", "set"],
    "fraco": ["jul", "dez"]
  },
  "elasticidade_historica": -0.6,
  "stock_pricing": {
    "ja_subiu_preco_antes": true,
    "historico": "R$ 1.997 -> R$ 2.997 (12 meses) -> R$ 4.997 (8 meses)"
  }
}
```

### Diagnostico (FASE 2)

```
Taxa de ocupacao: 32000 / 4997 / 8 = 80% (gatilho ATIVO)
Margem atual: (4997 - 600) / 4997 = 88% (excelente)
Revenue Gap: (120000 - 32000) / 32000 = 275% (mudanca estrutural exigida)
Alertas:
  - Slot >80% por 60 dias -> G2 ativo (+20%)
  - Revenue Gap >100% -> nao adianta so subir preco, precisa mudar tier
  - Posicionamento em transicao Duquesa->Marquesa -> abre espaco pra agressivo
```

### Os 3 cenarios

**CONSERVADOR — R$ 5.997 (+20%)**
```
Slots projetados: 8 (sem perda — +20% nao age na elasticidade -0.6)
Receita: R$ 47.976/mes (+50%)
Margem: 90%
Risco volume: < 5%
Indicado pra: aplicar imediato (G2 ja ativo)
```

**REALISTA — R$ 9.997 (+100%)**
```
Slots projetados: 5 (-37%)
Receita: R$ 49.985/mes (+56%)
Margem: 94%
Risco volume: 30%
Indicado pra: 60-90 dias depois do conservador
Pre-requisito: aplicar G7 (transicao Duquesa->Marquesa)
```

**AGRESSIVO — R$ 30.000 (+500%)**
```
Slots projetados: 2 (-75%) — formato boutique 1:1
Receita: R$ 60.000/mes (+87%)
Margem: 97% (ajustando custo pra R$ 1.000 — atendimento premium)
Risco volume: 75%
Indicado pra: 6-12 meses depois (tempo de instalar Luxe Empire completo)
Pre-requisitos:
  - Rodar /luxe-empire (Pilares 1, 2, 4, 5, 6 completos)
  - Acumular 3 cases lendarios publicos
  - Lancar livro/curso premium parallel
  - Entrar em palco/midia (pagar autoridade externa)
  - Reformular com /skill-oferta-irresistivel + /high-ticket-strategist
```

### Recomendacao final

**Sequencia escalonada em 12 meses:**

```
Mes 0-1:   Aplicar G2 — subir pra R$ 5.997 (Conservador)
Mes 1-3:   Estabilizar receita em R$ 47.976/mes
Mes 3:     Rodar /luxe-empire pra preparar transicao
Mes 3-6:   Acumular cases (meta: 3 lendarios)
Mes 6:     Aplicar G7 (Realista) — subir pra R$ 9.997
Mes 6-9:   Estabilizar em R$ 49.985/mes
Mes 9:     Iniciar transicao pra Agressivo
Mes 9-12:  Lancamento do tier boutique R$ 30.000
Mes 12+:   Operar mix: 2 boutique R$ 30k + 5 mentoria R$ 9.997
           Receita: R$ 60.000 + R$ 49.985 = R$ 110.000/mes
           Atinge meta de R$ 120k em mes 13.
```

### Ancoragem (modo --ancorar)

Pro tier Realista R$ 9.997:

```
Stack:
- Mentoria 12 semanas: R$ 30.000
- Comunidade vitalicia: R$ 12.000
- 4 sessoes 1:1: R$ 8.000
- Templates copy (40 pecas): R$ 5.000
- Bonus historia metodo: R$ 4.997
- Suporte WhatsApp 90 dias: R$ 7.000
TOTAL R$Y: R$ 66.997

R$Z: R$ 18.000 (Premium Z)
R$X: R$ 9.997 ou 12x R$ 833
```

### Insight

Caso classico onde **subir 6x o preco em 12 meses e legitimo**, mas exige sequencia. Tentar pular pra agressivo direto **destruiria** a base. A skill insiste em conservador -> realista -> agressivo.

---

## CASE 2 — Fernanda, infoprodutora (R$ 497 -> R$ 1.997)

### Contexto

Fernanda vende curso digital de organizacao financeira pra mulheres. Atua ha 8 meses. Curso gravado + comunidade Telegram.

### Input completo

```json
{
  "mentorada": "fernanda-financas",
  "capacidade": 200,
  "faturamento_atual": 49700,
  "meta_12m": 200000,
  "posicionamento": "Princesa em transicao pra Duquesa",
  "preco_atual": 497,
  "custo_variavel_cliente": 30,
  "concorrencia": [
    {"nome": "Curso Bem", "preco": 297, "diferencial": "barato + popular"},
    {"nome": "Money Power", "preco": 597, "diferencial": "afiliacao agressiva"},
    {"nome": "Riqueza Plena", "preco": 1497, "diferencial": "metodo proprio"},
    {"nome": "FinPlanner Pro", "preco": 2997, "diferencial": "1:1 incluso"}
  ],
  "sazonalidade": {
    "forte": ["jan", "abr", "set"],
    "fraco": ["jul", "dez"]
  },
  "elasticidade_historica": null,
  "stock_pricing": {
    "ja_subiu_preco_antes": false,
    "historico": "R$ 497 desde o lancamento"
  }
}
```

### Diagnostico (FASE 2)

```
Taxa de ocupacao: 100 vendas/mes (de capacidade 200) = 50%
Margem atual: (497 - 30) / 497 = 94% (excelente — produto digital)
Revenue Gap: (200000 - 49700) / 49700 = 302% (mudanca estrutural)
Alertas:
  - Capacidade <60% -> NAO ha gatilho de aumento por capacidade
  - Mas revenue gap altissimo -> precisa subir preco pra atingir meta
  - Sem historico de elasticidade -> usar -0.6 (conservador padrao)
  - Posicionamento Princesa -> max +50% sem reposicionamento
```

### Os 3 cenarios

**CONSERVADOR — R$ 597 (+20%)**
```
Slots projetados: 95 (-5%)
Receita: R$ 56.715/mes (+14%)
Margem: 95%
Risco volume: 5%
Indicado pra: primeira subida — Fernanda nunca subiu preco
Comunicacao: simples, sem comocao
```

**REALISTA — R$ 997 (+100%)**
```
Slots projetados: 60 (-40% — elasticidade conservadora -0.6)
Receita: R$ 59.820/mes (+20%)
Margem: 97%
Risco volume: 40%
Indicado pra: 90 dias depois do conservador, com prova social acumulada
Pre-requisito: 5 cases novos + reformulacao da pagina
```

**AGRESSIVO — R$ 1.997 (+300%)**
```
Slots projetados: 30 (-70%)
Receita: R$ 59.910/mes (+20%)
Margem: 98%
Risco volume: 70%
Indicado pra: 6-9 meses depois com reposicionamento Duquesa completo
Pre-requisitos:
  - Rodar /luxe-empire (Pilares 1, 2, 3)
  - Adicionar 1:1 mensal no stack (justifica preco premium)
  - 3 cases publicos com numero financeiro especifico
  - Reformular pagina com Stack Disclosure premium
```

### Recomendacao final

**Estrategia: subir preco, baixar volume, aumentar margem ABSOLUTA.**

Fernanda nao quer 200 alunas. Quer 30-60 alunas premium com mais entrega e mais margem.

```
Mes 0:      Aplicar Conservador R$ 597 (sem perda)
Mes 1-2:    Coletar 5 cases novos (com numeros)
Mes 3:      Aplicar Realista R$ 997 + adicionar 1:1 trimestral
Mes 3-6:    Estabilizar em 60 vendas/mes = R$ 59.820/mes
Mes 6-9:    Rodar /luxe-empire + reformular com /skill-oferta-irresistivel
Mes 9:      Lancar tier Premium R$ 1.997 com 1:1 mensal
Mes 9-12:   Operar 2 tiers:
            - Curso basic R$ 597 (mantido pra base ampla)
            - Curso premium R$ 1.997 (margem alta)
            Mix esperado: 80 basic + 20 premium = R$ 87.700/mes
            + bonus de afiliacao + venda de cross-sell
            Total estimado: R$ 110-130k/mes (proximo da meta)
```

### Ancoragem (modo --ancorar)

Pro tier Premium R$ 1.997:

```
Stack:
- Curso completo (12 modulos): R$ 4.000
- Comunidade Telegram vitalicia: R$ 2.400
- 1:1 mensal por 3 meses: R$ 6.000
- Templates de planilha (15 pecas): R$ 1.500
- Bonus livro digital: R$ 297
- Suporte WhatsApp 60 dias: R$ 3.000
TOTAL R$Y: R$ 17.197

R$Z: R$ 2.997 (FinPlanner Pro)
R$X: R$ 1.997 ou 12x R$ 167

Garantia: 30 dias com devolucao integral.
```

### Insight

Caso classico de **infoproduto digital** onde a mentorada **deixa muito dinheiro na mesa cobrando R$ 497** quando o mercado paga R$ 1.500-3.000. A skill nao recomenda pular direto pra R$ 1.997 — a sequencia em 9 meses converte mais base e mantem credibilidade.

**Lico:** infoproduto escalavel pode subir preco mais rapido que mentoria (margem ja e quase 100%, capacidade nao e travamento). Mas exige reposicionamento.

---

## CASE 3 — Camila, B2B/Consultoria (R$ 50.000 -> R$ 300.000)

### Contexto

Camila e consultora de gestao pra empresas medias (faturamento R$ 5-50M). Atua ha 6 anos. Atende 4 contratos/ano.

### Input completo

```json
{
  "mentorada": "camila-consultoria",
  "capacidade": 4,
  "faturamento_atual": 50000,
  "meta_12m": 1200000,
  "posicionamento": "Marquesa",
  "preco_atual": 50000,
  "custo_variavel_cliente": 8000,
  "concorrencia": [
    {"nome": "BCG", "preco": 1500000, "diferencial": "marca + autoridade global"},
    {"nome": "Falconi", "preco": 800000, "diferencial": "metodo proprio + escala"},
    {"nome": "Consultora Sr", "preco": 200000, "diferencial": "boutique tematico"},
    {"nome": "Junior Consult", "preco": 30000, "diferencial": "preco baixo"}
  ],
  "sazonalidade": {
    "forte": ["mar", "abr", "set", "out"],
    "fraco": ["jan", "dez"]
  },
  "elasticidade_historica": -0.3,
  "stock_pricing": {
    "ja_subiu_preco_antes": true,
    "historico": "R$ 25k -> R$ 35k (24 meses) -> R$ 50k (12 meses)"
  }
}
```

### Diagnostico (FASE 2)

```
Taxa de ocupacao: 4 / 4 = 100% por 8 meses (saturado)
Margem atual: (50000 - 8000) / 50000 = 84% (saudavel)
Revenue Gap: (1200000 - 600000) / 600000 = 100% (precisa dobrar)
                                           ^^^^^^
              (faturamento anual: 50000 x 12 = 600000)

Alertas:
  - Capacidade 100% por 8 meses -> G3 ATIVO (+30%)
  - Lista de espera com 6 empresas -> demanda muito acima da oferta
  - Posicionamento Marquesa solido, transicao pra Condessa possivel
  - Concorrencia: gap enorme entre R$ 200k (boutique) e R$ 800k (Falconi)
                  Camila pode ocupar a faixa R$ 300-500k (boutique premium)
```

### Os 3 cenarios

**CONSERVADOR — R$ 65.000 (+30%)**
```
Slots projetados: 4 (sem perda — lista de espera absorve)
Receita: R$ 260.000/contrato | R$ 1.040k/ano (+73%)
Margem: 88%
Risco volume: 0% (lista de espera ativa)
Indicado pra: aplicar IMEDIATO (G3 ja ativo)
```

**REALISTA — R$ 150.000 (+200%)**
```
Slots projetados: 3 (-25% — elasticidade B2B baixa -0.3)
Receita: R$ 450.000/ano de cada um... espera, isso nao bate
Recalculando: 3 contratos/ano x R$ 150k = R$ 450.000/ano
Hmm, esta abaixo. Recalcular: contratos podem ter duracao diferente.

Modelo correto:
- Cada contrato dura 6 meses
- 3 contratos/ano com R$ 150k = R$ 450k/ano (insuficiente pra meta)
- 4 contratos/ano com R$ 150k = R$ 600k/ano (insuficiente)

Dado que meta e R$ 1.2M/ano, R$ 150k nao basta isolado.
Precisa: subir preco + adicionar produto secundario.

Receita projetada com mix:
  4 contratos consultivos R$ 150k = R$ 600k
  + 6 mentorias C-level R$ 30k    = R$ 180k
  + 12 palestras R$ 25k           = R$ 300k
  + retainer 1 cliente R$ 20k/mes = R$ 240k
  TOTAL ANUAL: R$ 1.320k (excede meta)
Margem: 90%
Risco volume: 25% (contratos)
Indicado pra: 3-6 meses com mix de produtos
```

**AGRESSIVO — R$ 300.000 (+500%)**
```
Slots projetados: 2 (-50%)
Receita: 2 contratos R$ 300k = R$ 600k
Necessario adicionar produtos premium parallel:
  + 4 mentorias C-level R$ 50k = R$ 200k
  + 6 palestras R$ 50k         = R$ 300k
  + 1 livro/curso             = R$ 100-200k
TOTAL: R$ 1.2-1.4M/ano
Margem: 92%
Risco volume: 50%
Pre-requisitos:
  - Lancar livro autoridade (ja em escrita)
  - Coluna em revista de negocios (Exame, Pequenas Empresas)
  - 2 cases lendarios (empresas listadas em ranking)
  - Reposicionamento Condessa via /luxe-empire completo
  - Time interno expandido (1 senior pra apoiar entregas)
```

### Recomendacao final

**Sequencia em 12 meses (B2B com transicao de tier):**

```
Mes 0:      Aplicar G3 (R$ 65.000 imediato)
Mes 0-3:    Comunicar nova faixa de preco pra lista de espera
            Receita Q1: R$ 195k (3 contratos a R$ 65k)
Mes 3-6:    Iniciar produtos secundarios (palestras + retainer)
            Receita Q2: R$ 250k
Mes 6:      Aplicar Realista R$ 150k (saltao calculado)
            Comunicado: novo tier "consultoria boutique"
Mes 6-12:   Mix:
            - 2 contratos R$ 150k = R$ 300k
            - 6 mentorias C-level R$ 30k = R$ 180k
            - 8 palestras R$ 25k = R$ 200k
            - 1 retainer R$ 20k/mes x 6 = R$ 120k
            Total semestre: R$ 800k
            Total anual: R$ 1.05M (proximo da meta)
Mes 12:     Avaliar transicao pra Agressivo (R$ 300k)
            Pre-requisito: livro publicado + 2 cases premium
```

### Ancoragem (modo --ancorar)

Pro tier Realista R$ 150.000:

```
Stack:
- Diagnostico estrategico 360 (1 mes): R$ 60.000
- 6 meses de consultoria executiva: R$ 360.000
- Time tactico de implementacao: R$ 150.000
- Acesso direto Camila (WhatsApp + Calendly): R$ 80.000
- Documentacao + frameworks proprietarios: R$ 40.000
- Mentoria C-level 6 sessoes: R$ 90.000
TOTAL R$Y: R$ 780.000

R$Z: R$ 800.000 (Falconi — comparavel)
R$X: R$ 150.000

Comparativo:
  Falconi:     R$ 800.000 — metodo escala, distancia
  BCG:         R$ 1.500.000 — global, distancia
  Camila:      R$ 150.000 — boutique, acesso direto
```

### Insight

Caso B2B mostra que **elasticidade e bem menor** (publico nao e sensivel a preco — e sensivel a resultado e risco). Camila pode multiplicar 6x o preco em 12 meses **se** instalar:
1. Mix de produtos (nao depender so de contrato grande)
2. Autoridade midiatica (livro + coluna)
3. Cases premium (empresas listadas)

Sem o mix, mesmo cobrando R$ 300k ela nao chega na meta — capacidade limita. **A skill detecta e exige mix de produtos**, nao so subida de preco.

---

## Padroes que emergem dos 3 casos

### 1. Posicionamento e teto de variacao

| Posicionamento | Variacao maxima por execucao |
|----------------|------------------------------|
| Princesa | +20-30% |
| Duquesa | +50-100% |
| Marquesa | +100-200% |
| Condessa | +300-500% |

### 2. Sequencia recomendada

**Sempre conservador -> realista -> agressivo.** Nunca pular. Entre cada um, **minimo 60-90 dias** de estabilizacao.

### 3. Quando subir preco nao basta

Se Revenue Gap > 100%, **subir preco isolado nao resolve**. Precisa:
- Adicionar produto secundario (mix)
- Reposicionar tier
- Expandir capacidade (digitalizar, time, escala)

### 4. Custo do tempo de implementacao

| Cenario | Tempo realista pra estabilizar |
|---------|-------------------------------|
| Conservador | 30 dias |
| Realista | 90 dias |
| Agressivo | 6-12 meses |

### 5. Stock pricing como retencao

Em todos os 3 casos, stock pricing virou **bonus de fidelidade** pra cliente atual:
- Mariana: cliente da fase R$ 4.997 mantem R$ 4.997 na renovacao
- Fernanda: aluna do curso basic ganha desconto de 50% no premium
- Camila: cliente do retainer mantem R$ 20k/mes mesmo apos reajuste

Stock pricing **reduz churn** e cria **embaixadores** (cliente fiel virou referencia interna).

---

**Exemplos de Pricing — propriedade intelectual Tata Goncalves.**
