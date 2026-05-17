# Alertas — Lógica de Cores e Priorização

Regras determinísticas pra calcular cor de cada KPI, gerar alertas e priorizar a fila do `--alertas`. Sem subjetivismo, sem caso a caso.

---

## 1. CORES POR KPI

### Regra base

Cada KPI tem 3 faixas definidas em `KPIS-POR-PORTA.md`:

| Cor | Condição |
|---|---|
| 🟢 Verde | KPI ≥ benchmark verde |
| 🟡 Amarelo | KPI < benchmark verde E KPI ≥ benchmark amarelo (faixa 70-99% do verde, normalmente) |
| 🔴 Vermelho | KPI < benchmark amarelo OU KPI ausente/não medido |
| ⬜ Cinza | Porta fora do escopo do nível hierárquico atual da mentorada |

### KPIs compostos (2 componentes)

Para portas com KPI composto (O, P, R, T, V):

| Resultado | Componente A | Componente B |
|---|---|---|
| 🟢 Verde | verde | verde |
| 🟡 Amarelo | amarelo | qualquer (não vermelho) |
| 🟡 Amarelo | qualquer (não vermelho) | amarelo |
| 🔴 Vermelho | vermelho | qualquer |
| 🔴 Vermelho | qualquer | vermelho |

Regra: **o pior componente puxa pra baixo.**

### KPI ausente

Se a mentorada não tem o KPI declarado/medido no mês de referência:
- **Vermelho automático** (não pode ser amarelo "sem dado")
- Mensagem: "KPI não medido no mês [X]. Atualize via /dossie-mentorada profile 16-kpis-dashboard."

---

## 2. CINZA (FORA DO ESCOPO)

A skill não cobra portas que estão acima do nível hierárquico da mentorada.

| Nível | Portas cobradas | Portas em cinza |
|---|---|---|
| Iniciada | A-F | G-Z |
| Cortesã | A-L | M-Z |
| Dama | A-V | W-Z (são ciclos contínuos) |
| Imperatriz | A-Z (todas) | nenhuma |

Cinza ≠ vermelho. Cinza significa "ainda não exigido nessa fase". Não conta como falha, não pesa no score.

---

## 3. SCORE DO MENTORADA

Cálculo:

```
score = (n_verdes / n_portas_no_escopo) × 100
```

Onde:
- `n_verdes` = quantos KPIs verdes (não conta amarelo nem cinza)
- `n_portas_no_escopo` = portas exigidas pelo nível hierárquico atual

Exemplo:
- Iniciada com A,B,D,E verdes (4) e C,F amarelos → score = 4/6 × 100 = 67%
- Cortesã com A,B,C,D,E,F,G,H verdes (8) e I,J,K,L amarelos/vermelhos → score = 8/12 × 100 = 67%

---

## 4. SCORE DA CORTE (visão Tata)

Dois agregados:

### Score por mentorada (média simples)
```
score_corte = média dos scores individuais
```

### Score por porta (gargalo da Corte)
```
score_porta_X = (n_mentoradas_verdes_em_X / n_mentoradas_no_escopo_X) × 100
```

Permite identificar qual porta é o gargalo coletivo (ex: Corte inteira tem K em 30% verde → problema sistêmico no tráfego pago, não problema individual).

---

## 5. ALERTAS — REGRAS DE GERAÇÃO

A skill gera alerta automaticamente quando:

| Tipo | Gatilho | Severidade |
|---|---|---|
| **CRÍTICO** | Vermelho na porta atual + porta-fonte upstream também vermelha (contaminação confirmada) | 1 |
| **CRÍTICO** | 3+ vermelhos no mesmo nível hierárquico | 1 |
| **ALTO** | Vermelho na porta atual sem upstream contaminada | 2 |
| **ALTO** | Ciclo recorrente vencido há mais de 30 dias (mensal) ou 90 dias (trimestral) | 2 |
| **ATENÇÃO** | Amarelo há 2+ meses consecutivos na mesma porta | 3 |
| **ATENÇÃO** | KPI ausente (não medido) há 2+ meses | 3 |
| **MÉDIO** | Vermelho em porta downstream sem upstream contaminada | 4 |
| **OBSERVAR** | Verde caiu pra amarelo no último mês (regressão) | 5 |

Severidade vai de 1 (mais urgente) a 5 (monitorar).

---

## 6. PRIORIZAÇÃO DA FILA `--alertas`

Ordem de exibição:

1. **Crítico com upstream contaminada** (porta-fonte identificada via `gates-imperatriz`)
2. **Crítico por concentração** (3+ vermelhos)
3. **Alto — vermelho porta atual**
4. **Alto — ciclo vencido**
5. **Atenção — amarelo crônico**
6. **Atenção — KPI não medido**
7. **Médio — vermelho isolado downstream**
8. **Observar — regressão verde→amarelo**

Dentro de cada nível, ordena por:
1. Mentorada com maior receita (maior risco financeiro)
2. Mentorada com maior nível hierárquico (maior risco reputacional pra Corte)
3. Tempo na cor (quanto mais antigo, mais urgente)

---

## 7. CONTAMINAÇÃO UPSTREAM (regra crítica)

A skill cruza com `gates-imperatriz` `MAPA-DEPENDENCIAS.md` pra identificar quando vermelho downstream tem causa upstream.

Exemplo de cascata documentada:

| Porta vermelha | Porta-fonte provável |
|---|---|
| K (ROAS baixo) | C (mecanismo) ou J (página) ou B (ICP) |
| M (conv funil) | J (página) + K (tráfego) + G (oferta) |
| G (aceitação pitch) | C (mecanismo) + D (diferenciação) |
| Q (CV fechamento alto) | B (ICP) + G (oferta) |
| R (NPS baixo) | F (voz) + entrega do produto (não-porta) |
| T (reativação) | F (voz) + N (conteúdo) |
| U (retenção 12m) | R (NPS) + entrega contínua |

Quando vermelho em downstream + upstream também não-verde:
- Alerta vira **CRÍTICO**
- Recomendação: rollback via `/gates-imperatriz --rollback [nome] [sintoma]`
- Marcação visual: linha vermelha cruzando do downstream pro upstream no heatmap

---

## 8. CICLOS RECORRENTES (regra adicional)

Algumas portas viram ciclos contínuos depois de fechadas:

| Porta | Ciclo | Cadência |
|---|---|---|
| L | Lift A/B | mensal (1+ teste/mês) |
| N | Narrativa | semanal (4+ pubs/sem) |
| T | Tração | mensal |
| W | Web/SEO | mensal |
| X | Audit | trimestral |
| Y | Yield | mensal |
| Z | Iteração | mensal |

Ciclo vencido = alerta automático. Mesmo com KPI verde no momento, se a cadência atrasou:
- Mensal vencido > 30d → alerta ALTO
- Trimestral vencido > 90d → alerta ALTO
- Semanal vencido > 7d → alerta ATENÇÃO

---

## 9. INVESTIDURA — REGRA DE ELEVAÇÃO

Mentorada está **PRONTA PRA INVESTIDURA** quando:

| Sobe pra | Critério |
|---|---|
| Cortesã | A-F todas verdes E sem alerta crítico ativo |
| Dama | A-L todas verdes E sem alerta crítico ativo E ciclos L,N em dia 3+ meses |
| Imperatriz | A-V todas verdes E sem alerta crítico ativo E ciclos W-Z em dia 3+ meses E score ≥ 95% |

Critério adicional pra TODOS os níveis:
- Score consistente nos últimos **3 meses** (sem regressão pra amarelo/vermelho na composição mínima)

Se a mentorada bateu critério apenas no mês de referência mas teve regressão nos 2 meses anteriores → marca como **"Quase lá"**, não "Pronta agora".

---

## 10. CASES PRONTOS PRA DOCUMENTAR

A skill marca como **CASE PRONTO** quando:
- KPI verde consistente 3+ meses na mesma porta
- Não houve regressão na cor no período
- Mentorada deu permissão pra documentar (campo `permite_case` no dossiê = true)

Portas mais valiosas pra cases (pra Tata mostrar):
- C (mecanismo único nomeado e validado)
- J (conversão página)
- K (ROAS)
- N (consistência editorial)
- Q (previsibilidade)
- U (retenção 12m)
- Y (margem)

---

## 11. INCONSISTÊNCIA KPI × GATE

Quando a skill detecta:
- **KPI verde** (esta skill) E **gate `gates-imperatriz` parcial/não-passou**

Marca **alerta de inconsistência** (severidade 2):
- Possível razão: número bateu mas evidência qualitativa falta (ex: ROAS verde mas sem CAPI configurada)
- Ação: revisar gate via `/gates-imperatriz --validar [nome] [porta]` antes de declarar verde

A inversa também é alerta:
- **KPI amarelo/vermelho** (esta skill) E **gate `gates-imperatriz` passou**
- Possível razão: gate passou em momento anterior, KPI regrediu agora
- Ação: re-validar gate

---

## 12. TIMING DE GERAÇÃO

| Modo | Gatilho |
|---|---|
| Automático mensal | Cron dia 1 do mês, com dado do mês anterior fechado |
| Manual | Tata roda `/dashboard-imperatriz --tata` ou mentorada roda `/dashboard-imperatriz --mentorada [nome]` |
| Trimestral expandido | Cron dia 1 dos meses março, junho, setembro, dezembro — inclui audit X completo |
| Ad-hoc alertas | Push automatizado se aparecer CRÍTICO no meio do mês (rastreador detecta KPI atualizado) |

---

## 13. NOTIFICAÇÕES (canal por severidade)

| Severidade | Canal padrão | Quem recebe |
|---|---|---|
| 1 — Crítico | WhatsApp Tata + Marketing Command app | Tata |
| 2 — Alto | E-mail diário consolidado + dashboard | Tata |
| 3 — Atenção | Dashboard | Tata + mentorada |
| 4 — Médio | Dashboard | Tata + mentorada |
| 5 — Observar | Dashboard (badge) | Mentorada |

A mentorada nunca vê alertas de outras. Notificação dela é só do dashboard dela.

---

## 14. SUPRESSÃO DE FALSO POSITIVO

A skill suprime alerta quando:
- Mentorada está em pausa declarada (campo `pausa_ativa` no dossiê = true) — nesse mês não cobra
- Mentorada está em transição de modelo (mudou de produto/oferta) — janela de 60 dias de tolerância
- Métrica do mês tem volume insuficiente pra significância (< mínimo declarado por KPI) — marca como "dado insuficiente", não vermelho

---

## 15. EXEMPLO COMPLETO — Larissa em maio/2026

Estado:
- Nível: Iniciada
- Porta atual declarada: K
- KPIs:
  - A: 100 → 🟢
  - B: 2,3x → 🟢
  - C: 1,4% CTR → 🔴 (benchmark 2,4%)
  - D: 3 motivos → 🟢
  - E: 3/3 ativos → 🟢
  - F: 1 piloto última 8 sem → 🟡
  - G: 18% aceitação → 🟡 (benchmark 25%)
  - H: 3/3 → 🟢
  - I: 38 leads/mês → 🟡 (benchmark 50)
  - J: 0,4% conv frio → 🔴
  - K: 1,8x ROAS → 🔴 (benchmark 3x)
  - L-Z: cinza (fora do escopo Iniciada)

Score: 4/6 portas no escopo verde (A,B,D,E) = **67%** (mas atenção: J e K em vermelho contaminam mesmo sendo fora do escopo formal de Iniciada — porque ela está tentando rodar K)

Alertas gerados:
1. **CRÍTICO** — vermelho em K + upstream C também vermelho → contaminação confirmada → rollback C
2. **ALTO** — vermelho em J → afeta K
3. **ATENÇÃO** — amarelo em F (piloto solo)
4. **ATENÇÃO** — amarelo em G (aceitação)
5. **OBSERVAR** — I em 38/50 (precisa subir pra próximo mês)

Recomendação consolidada:
1. Suspender atividade em K
2. Rollback C (`/mecanismo-unico --auditar`)
3. Refazer J depois de C
4. Re-medir em 60 dias

---

**Lógica de alertas é determinística. A skill não negocia regra. Só cor.**
