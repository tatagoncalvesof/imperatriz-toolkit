---
name: skill-relatorio-ads
description: >
  Gera relatorios de performance de anuncios pagos com templates profissionais.
  Inclui relatorio semanal, mensal, trimestral, e dashboard de metricas.
  Calcula MER, ROAS, CPA, LTV:CAC e gera insights acionaveis.
  Use quando o usuario pedir "relatorio de ads", "relatorio de performance",
  "dashboard de metricas", "analise de resultados", "relatorio semanal",
  "relatorio mensal", "relatorio de campanha", "performance dos anuncios",
  "como estao meus ads", ou qualquer analise de performance de trafego pago.
---

# Relatorios de Performance de Ads

## Contexto
- **Formato:** Markdown estruturado, tabelas claras, insights acionaveis
- **Periodicidade:** Semanal, Mensal, Trimestral
- **Plataformas:** Meta Ads, Google Ads, TikTok (se aplicavel)
- **Moeda:** BRL (R$)

## Processo

### 1. Coleta de Dados
Perguntar ao usuario:
- Periodo do relatorio (datas)
- Plataforma(s) a analisar
- Dados disponiveis (export CSV, screenshots, ou manual)
- Tipo de relatorio (semanal/mensal/trimestral)
- Dados financeiros (receita total do periodo, se disponivel)

### 2. Template de Relatorio Semanal

```markdown
# Relatorio Semanal de Ads
**Periodo:** [data inicio] a [data fim]
**Plataformas:** [lista]

---

## Resumo Executivo

| Metrica | Esta Semana | Semana Anterior | Variacao |
|---------|-------------|-----------------|----------|
| Investimento | R$ | R$ | % |
| Leads Gerados | # | # | % |
| CPL (Custo por Lead) | R$ | R$ | % |
| Vendas | # | # | % |
| CPA (Custo por Venda) | R$ | R$ | % |
| Receita Atribuida | R$ | R$ | % |
| ROAS (Plataforma) | x | x | % |
| MER (Real) | x | x | % |

**Status Geral:** 🟢 Saudavel / 🟡 Atencao / 🔴 Critico

---

## Performance por Campanha

| Campanha | Gasto | Leads | CPL | Vendas | CPA | ROAS |
|----------|-------|-------|-----|--------|-----|------|
| [Nome 1] | R$ | # | R$ | # | R$ | x |
| [Nome 2] | R$ | # | R$ | # | R$ | x |
| [Nome 3] | R$ | # | R$ | # | R$ | x |
| **Total** | **R$** | **#** | **R$** | **#** | **R$** | **x** |

---

## Performance por Criativo (Top 5)

| Criativo | Formato | Gasto | CTR | CPC | Conversoes | CPA |
|----------|---------|-------|-----|-----|-----------|-----|
| [Nome 1] | Video | R$ | % | R$ | # | R$ |
| [Nome 2] | Imagem | R$ | % | R$ | # | R$ |
| [Nome 3] | Carrossel | R$ | % | R$ | # | R$ |

---

## Alertas

### 🔴 Criticos (Acao Imediata)
- [Alerta com acao recomendada]

### 🟡 Atencao (Monitorar)
- [Alerta com contexto]

### 🟢 Positivos (Manter/Escalar)
- [Destaque positivo com recomendacao]

---

## Acoes para Proxima Semana
1. [Acao 1 — especifica e acionavel]
2. [Acao 2]
3. [Acao 3]
```

### 3. Template de Relatorio Mensal

```markdown
# Relatorio Mensal de Ads
**Mes:** [mes/ano]
**Plataformas:** [lista]

---

## Dashboard Executivo

### Investimento vs Receita
| Metrica | Meta | Realizado | % Meta | Tendencia |
|---------|------|-----------|--------|-----------|
| Investimento Total | R$ | R$ | % | ↑↓→ |
| Receita Total | R$ | R$ | % | ↑↓→ |
| MER (Receita/Gasto) | x | x | % | ↑↓→ |
| Lucro Bruto Ads | R$ | R$ | % | ↑↓→ |

### Volume
| Metrica | Meta | Realizado | % Meta |
|---------|------|-----------|--------|
| Impressoes | # | # | % |
| Cliques | # | # | % |
| Leads | # | # | % |
| Vendas | # | # | % |

### Eficiencia
| Metrica | Meta | Realizado | Status |
|---------|------|-----------|--------|
| CPC | R$ | R$ | 🟢🟡🔴 |
| CPL | R$ | R$ | 🟢🟡🔴 |
| CPA | R$ | R$ | 🟢🟡🔴 |
| CTR | % | % | 🟢🟡🔴 |
| ROAS | x | x | 🟢🟡🔴 |

---

## Analise por Plataforma

### Meta Ads
| Campanha | Budget | Gasto | Leads | CPL | Vendas | CPA | ROAS |
|----------|--------|-------|-------|-----|--------|-----|------|
| Prospeccao | R$ | R$ | # | R$ | # | R$ | x |
| Nurture | R$ | R$ | # | R$ | # | R$ | x |
| Retargeting | R$ | R$ | # | R$ | # | R$ | x |
| Upsell | R$ | R$ | # | R$ | # | R$ | x |

### Google Ads (se aplicavel)
| Campanha | Budget | Gasto | Cliques | CPC | Conv | CPA | ROAS |
|----------|--------|-------|---------|-----|------|-----|------|
| Brand | R$ | R$ | # | R$ | # | R$ | x |
| Intent | R$ | R$ | # | R$ | # | R$ | x |
| YouTube | R$ | R$ | # | R$ | # | R$ | x |

---

## Analise de Criativos

### Top 5 Criativos (por ROAS)
| # | Criativo | Formato | CTR | CPA | ROAS | Idade (dias) |
|---|----------|---------|-----|-----|------|--------------|
| 1 | | | % | R$ | x | # |
| 2 | | | % | R$ | x | # |
| 3 | | | % | R$ | x | # |
| 4 | | | % | R$ | x | # |
| 5 | | | % | R$ | x | # |

### Criativos com Fadiga (CTR -20% em 14d)
| Criativo | CTR Inicial | CTR Atual | Queda | Acao |
|----------|-------------|-----------|-------|------|
| | % | % | % | Pausar/Renovar |

### Analise por Formato
| Formato | % Budget | CTR Medio | CPA Medio | ROAS |
|---------|----------|-----------|-----------|------|
| Video Reels | % | % | R$ | x |
| Imagem Feed | % | % | R$ | x |
| Carrossel | % | % | R$ | x |
| Stories | % | % | R$ | x |

---

## Analise de Audiencias

### Performance por Publico
| Publico | Gasto | Leads | CPL | Vendas | CPA | ROAS |
|---------|-------|-------|-----|--------|-----|------|
| LAL Buyers 1% | R$ | # | R$ | # | R$ | x |
| Interesses | R$ | # | R$ | # | R$ | x |
| LAL Email 1% | R$ | # | R$ | # | R$ | x |
| Retargeting PV | R$ | # | R$ | # | R$ | x |
| Broad | R$ | # | R$ | # | R$ | x |

### Frequencia por Campanha
| Campanha | Frequencia 7d | Status | Acao |
|----------|--------------|--------|------|
| Prospeccao | x | 🟢🟡🔴 | |
| Retargeting | x | 🟢🟡🔴 | |

---

## Funil Completo

```
Impressoes: [#] (100%)
    ↓ CTR [%]
Cliques: [#] ([%] das impressoes)
    ↓ CVR Landing [%]
Leads: [#] ([%] dos cliques)
    ↓ CVR Webinar [%]
Participantes: [#] ([%] dos leads)
    ↓ CVR Venda [%]
Vendas: [#] ([%] dos participantes)
    ↓ Ticket Medio R$[#]
Receita: R$[#]
```

---

## Insights e Recomendacoes

### O que Funcionou
1. [Insight 1 — por que funcionou e como replicar]
2. [Insight 2]
3. [Insight 3]

### O que NAO Funcionou
1. [Insight 1 — por que nao funcionou e como corrigir]
2. [Insight 2]

### Acoes para o Proximo Mes
| # | Acao | Prioridade | Impacto Esperado |
|---|------|-----------|-----------------|
| 1 | | P1 | |
| 2 | | P1 | |
| 3 | | P2 | |
| 4 | | P2 | |
| 5 | | P3 | |
```

### 4. Formulas e Calculos

```
CPL = Gasto Total / Leads Gerados
CPA = Gasto Total / Vendas
CPC = Gasto Total / Cliques
CTR = (Cliques / Impressoes) × 100
CVR = (Conversoes / Cliques) × 100
ROAS = Receita / Gasto (por plataforma)
MER = Receita Total / Gasto Total em Ads (cross-platform)
LTV = Receita Media por Cliente × Tempo de Retencao
CAC = Gasto Total Marketing / Novos Clientes
LTV:CAC = LTV / CAC (meta: > 3:1)
Breakeven ROAS = 1 / Margem (ex: 1/0.85 = 1.18x para margem 85%)
```

### 5. Benchmarks de Referencia (Infoprodutos BR)

| Metrica | Ruim | Ok | Bom | Otimo |
|---------|------|-----|-----|-------|
| CPC Meta | > R$5 | R$2-5 | R$1-2 | < R$1 |
| CPL Meta | > R$20 | R$10-20 | R$5-10 | < R$5 |
| CTR Meta | < 0.5% | 0.5-1% | 1-2% | > 2% |
| CPA (low-ticket) | > R$100 | R$50-100 | R$25-50 | < R$25 |
| CPA (high-ticket) | > R$500 | R$200-500 | R$100-200 | < R$100 |
| ROAS Front-end | < 1x | 1-2x | 2-3x | > 3x |
| MER Blended | < 2x | 2-3x | 3-5x | > 5x |
| Frequencia Prosp. | > 5 | 3-5 | 2-3 | < 2 |
| Frequencia Retarg. | > 12 | 8-12 | 4-8 | < 4 |

### 6. Sistema de Alertas

| Condicao | Tipo | Mensagem |
|----------|------|----------|
| CPA > 3x meta | 🔴 Critico | "Campanha [X] gastou 3x CPA sem converter — PAUSAR" |
| Frequencia > 4 | 🟡 Atencao | "Audiencia [X] com fadiga — renovar criativos" |
| CTR caiu > 20% em 14d | 🟡 Atencao | "Criativo [X] com fadiga — substituir" |
| ROAS > meta + 30% | 🟢 Positivo | "Campanha [X] performando acima — considerar escalar" |
| Budget nao gasto > 20% | 🟡 Atencao | "Campanha [X] nao gastando budget — verificar bid" |
| CPM subiu > 30% | 🟡 Atencao | "CPM subindo — possivel saturacao ou sazonalidade" |

## Output

Entregar arquivo formatado:
- `RELATORIO-[TIPO]-[PERIODO].md` — Relatorio completo com todas as secoes
- Graficos em ASCII quando possivel (barras de progresso)
- Insights claros e acionaveis (nao apenas numeros)
- Comparacao com periodo anterior sempre que possivel
