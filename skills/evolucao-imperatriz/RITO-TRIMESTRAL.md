# Rito Trimestral — Passo a Passo Operacional

> *"A cadência é o ritual. Sem dia marcado, evolução vira intenção. Intenção não fatura."*

Este documento detalha a execução completa do rito trimestral de revisão do ecossistema. **Modo `--revisar`** roda este rito do início ao fim.

---

## QUANDO RODAR

**Datas fixas:** primeiro dia útil de Janeiro, Abril, Julho e Outubro.

**Bloqueio na agenda:** 4h cravadas, sem call, sem mentorada, sem celular. Tata + skill + dados frios. Reunião do Conselho da Soberana acontece na semana seguinte (quarta-feira), com dossiê pronto.

**Pré-requisitos:**
- `/dashboard-imperatriz --tata` rodou nos 3 últimos meses (dado mensal fechado)
- `/dossie-mentorada` profile `17-feedback-skills` atualizado por mentorada
- Mês em andamento já fechou (não roda em primeiro dia útil se mês anterior ainda tem dado pendente)

Se algum pré-requisito falha, a skill avisa e PARA. Não inventa dado.

---

## AS 8 FASES DO RITO

### FASE 1 — COLETA (30-45 min)

**Objetivo:** consolidar dado bruto dos 3 meses do trimestre em um tabelão mestre.

**Ações:**
1. Lê `/dashboard-imperatriz --tata` agregado dos 3 meses
2. Lê profile `17-feedback-skills` de cada mentorada ativa
3. Lê histórico de versões de cada skill (`changelogs/`)
4. Lê catálogo de skills declaradas estratégicas (`manifesto-estrategico.md`)
5. Constrói **tabelão mestre** com 1 linha por skill

**Schema do tabelão (`01-tabelao-mestre.json`):**
```json
{
  "trimestre": "2026-Q2",
  "data_coleta": "2026-04-01",
  "skills": [
    {
      "nome": "headline-imperatriz",
      "versao_atual": "1.2",
      "estrategica": true,
      "uso": {
        "chamadas_trimestre": 247,
        "chamadas_trimestre_anterior": 189,
        "delta_pct": 30.7,
        "mentoradas_unicas": 18,
        "mentoradas_unicas_pct_corte": 60
      },
      "impacto": {
        "kpi_primario": "CTR de anúncios",
        "valor_medio": 2.3,
        "benchmark": 1.8,
        "vs_benchmark_pct": 27.8,
        "casos_high_impact": 7
      },
      "satisfacao": {
        "nps_medio": 72,
        "n_respostas": 14,
        "reclamacoes": 1,
        "elogios_textuais": 8
      },
      "saude": {
        "dias_desde_ultima_evolucao": 87,
        "sobreposicao_com": ["analise-anuncio-1000"],
        "sobreposicao_pct": 22,
        "gaps_reportados": []
      },
      "classificacao_provisoria": "quartil_superior_evoluir"
    }
  ]
}
```

**Output:** `01-tabelao-mestre.json` salvo em `~/imperio/evolucao/[YYYY-Q]/`.

---

### FASE 2 — MÉTRICAS AGREGADAS (Bloco 1) (15-20 min)

**Objetivo:** pulso geral do ecossistema em uma página.

**Calcula:**
- Total de chamadas no trimestre vs trimestre anterior (delta %)
- % de skills com uso > 0 no trimestre
- % de skills com uso = 0 (candidatas a museu)
- Mediana de uso (separa quartis)
- NPS médio do ecossistema (média ponderada por uso)
- Top 5 skills por uso absoluto
- Top 5 skills por NPS
- Top 5 skills com maior delta de uso (crescendo)
- Top 5 skills com maior queda de uso (perigo)

**Output:** primeira seção do `00-revisao-completa.md`:

```markdown
# REVISÃO TRIMESTRAL — 2026-Q2

## BLOCO 1 — MÉTRICAS AGREGADAS

### Pulso geral
- **Total de chamadas:** 4.892 (+18% vs Q1)
- **Skills ativas:** 158/225 (70%)
- **Skills museu:** 67/225 (30%) ← atenção
- **NPS médio do ecossistema:** 71

### Top 5 por uso
1. /tatou-2.0 — 412 chamadas
2. /briefing-copy-360 — 287
3. /headline-imperatriz — 247
4. /skill-pagina-vendas — 198
5. /voz-humana-br — 176

### Top 5 por NPS
1. /mecanismo-unico — 89
2. /headline-imperatriz — 87
3. /stories-pergunta-resposta — 82
4. /skill-oferta-irresistivel — 81
5. /imperatriz-bot — 78

### Crescendo (delta uso)
1. /imperatriz-bot — +147%
2. /copy-conversacional-dm — +89%
3. /reuniao-de-resultado — +56%

### Perigo (caindo)
1. /skill-X-velha — -78%
2. /skill-Y-obsoleta — -65%
```

---

### FASE 3 — QUARTIL SUPERIOR (Bloco 2) (30 min)

**Objetivo:** identificar as 25 skills que mais entregam e decidir o que fazer com cada.

**Critério de quartil superior:** posição combinada de uso (50%) + impacto vs benchmark (30%) + NPS (20%). Top 25 entram aqui.

**Para cada skill do top 25, decisão:**

| Status | Quando aplicar | Ação |
|--------|----------------|------|
| **MANTER** | Skill madura, NPS > 75, delta uso estável | Nada — deixa rodando, monitora |
| **EVOLUIR v2** | NPS bom mas há pedidos repetidos por funcionalidade nova | Roadmap inclui v2 no próximo trimestre |
| **ESCALAR** | Uso explodindo, mentoradas pedem mais — atenção pra não saturar | Comunicar como case, criar variantes |
| **PROTEGER** | Skill core que se quebrar mata ecossistema | Auditoria técnica obrigatória |

**Output:** `02-quartil-superior.md` com 25 entradas, cada uma:
```markdown
### #3 /headline-imperatriz — EVOLUIR v2

- **Uso:** 247 chamadas (60% da Corte)
- **Impacto:** CTR médio 2.3% vs benchmark 1.8% (+28%)
- **NPS:** 87
- **Status:** EVOLUIR v2

**Justificativa:** uso explodindo, NPS alto, mas mentoradas pediram (n=8) "headline pra base quente" e "headline retargeting carrinho" — gap claro.

**Próximo passo:** entrar no roadmap Q3 como v2.0 com 6 temperaturas + base quente.

**Dependências:** sem breaking change. v1 continua funcionando.
```

---

### FASE 4 — QUARTIL INFERIOR (Bloco 3) (45 min)

**Objetivo:** identificar as 25 skills que menos entregam e decidir destino.

**Critério:** bottom 25 por mesma fórmula combinada.

**Para cada skill do bottom 25, decisão:**

| Status | Quando aplicar | Ação |
|--------|----------------|------|
| **INVESTIGAR** | Uso baixo mas estratégica OU primeiro trimestre com uso 0 | Auditoria individual no próximo mês |
| **DEPRECAR** | Uso 0 em 2+ trimestres seguidos E não-estratégica | Plano de morte com 30d transição |
| **FUNDIR** | Sobreposição > 70% com skill irmã do quartil superior | Roadmap inclui fusão |
| **REPOSICIONAR** | Skill boa mas description ruim — ninguém acha | Reescrever description, manter código |

**Regra dura: skill estratégica nunca vai pra DEPRECAR sozinha.** Vai pra `INVESTIGAR` e Conselho decide.

**Output:** `03-quartil-inferior.md` com 25 entradas justificadas.

```markdown
### Bottom #1 /skill-X-velha — DEPRECAR

- **Uso:** 0 chamadas (0% da Corte)
- **Histórico:** 0 em Q1, 0 em Q2 (2 trimestres seguidos)
- **NPS:** N/A (sem uso)
- **Estratégica:** não
- **Sobreposição:** 45% com /skill-nova
- **Status:** DEPRECAR

**Justificativa:** 0 uso em 2 trimestres consecutivos. Funcionalidade absorvida por /skill-nova. Não é estratégica. Regra dos 2 trimestres aplica — morte autorizada sem precisar Conselho.

**Plano:**
1. Anunciar deprecação na nota de versão Q2
2. 30 dias de aviso (até 2026-05-15)
3. Mover skill pra `~/imperio/evolucao/deprecadas/`
4. Atualizar `CICLO-DE-VIDA-METODOLOGIA.md`
```

---

### FASE 5 — GAPS DETECTADOS (Bloco 4) (30 min)

**Objetivo:** transformar reclamação repetida em roadmap.

**Coleta de gaps:**
- Lê profile `17-feedback-skills` campo `pedidos_skill_inexistente`
- Lê dossiês campo `dores_recorrentes_sem_solucao`
- Lê transcript de calls de mentoria (se disponível)
- Cruza com catálogo: o pedido tem skill correspondente?

**Critério de validação:** **5+ pedidos da mesma coisa em 1 trimestre = gap validado.**

Pedidos com 1-4 menções vão pra "watchlist" e voltam no próximo trimestre.

**Classificação:**
- **CRIAR-CRÍTICO:** 10+ pedidos OU bloqueia uma porta
- **CRIAR-ALTO:** 5-9 pedidos
- **WATCHLIST:** 1-4 pedidos (não vira roadmap, fica em observação)

**Output:** `04-gaps-detectados.md`:
```markdown
## GAPS VALIDADOS (criar)

### Gap 1 — Skill de "métricas trimestrais por porta" — CRIAR-CRÍTICO
- **Pedidos:** 12 mentoradas em Q2
- **Sintoma:** "queria ver evolução da minha Porta C ao longo dos meses"
- **Skills existentes que tentam:** /dashboard-imperatriz (mensal, não trimestral)
- **Proposta:** /metricas-porta-trimestral
- **Esforço estimado:** 2 semanas
- **Impacto estimado:** alto (roda no rito da própria skill)

### Gap 2 — Skill de "checklist de auditoria de Stories" — CRIAR-ALTO
- **Pedidos:** 7 mentoradas
- ...
```

---

### FASE 6 — ROADMAP 90 DIAS (Bloco 5) (45 min)

**Objetivo:** plano executável priorizado pro próximo trimestre.

**Inputs:**
- EVOLUIR do Bloco 2 (quartil superior que precisa v2)
- DEPRECAR e FUNDIR do Bloco 3 (quartil inferior)
- CRIAR-CRÍTICO e CRIAR-ALTO do Bloco 4 (gaps)
- REPOSICIONAR do Bloco 3 (descriptions ruins)

**Priorização ICE:**
- **Impact:** 1-10 — quanto destrava no ecossistema?
- **Confidence:** 1-10 — certeza de que vai funcionar?
- **Ease:** 1-10 — quão barato é fazer?
- **Score ICE = (I × C × E) / 10** — ranqueia tudo

**Capacidade:** Tata + time conseguem ~6-10 movimentos por trimestre. Skill propõe 12-15 e sobra trabalho pra Conselho cortar.

**Output:** `05-roadmap-90dias.md`:
```markdown
## ROADMAP 2026-Q3

### Capacidade total: 8 movimentos
### Movimentos propostos: 12 (Conselho prioriza top 8)

| # | Tipo | Skill | Score ICE | Esforço | Owner | Prazo |
|---|------|-------|-----------|---------|-------|-------|
| 1 | EVOLUIR v2 | headline-imperatriz | 720 | 2sem | Tata | Q3-S2 |
| 2 | CRIAR | metricas-porta-trimestral | 640 | 2sem | Time | Q3-S4 |
| 3 | DEPRECAR | skill-X-velha | 480 | 1sem | Time | Q3-S1 |
| 4 | FUNDIR | skill-Y + skill-Z → skill-YZ | 420 | 3sem | Tata+Time | Q3-S6 |
| 5 | CRIAR | checklist-stories | 380 | 1sem | Time | Q3-S3 |
| 6 | REPOSICIONAR | skill-W (description) | 360 | 2dias | Tata | Q3-S1 |
| 7 | EVOLUIR v2 | voz-humana-br | 320 | 2sem | Tata | Q3-S5 |
| 8 | CRIAR | nova-skill-X | 280 | 2sem | Time | Q3-S6 |
| ... | ... | ... | ... | ... | ... | ... |

### Marcos do trimestre:
- Semana 2: skill-X deprecada
- Semana 4: 2 skills criadas (metricas-porta + checklist-stories)
- Semana 6: headline-imperatriz v2 lançada
- Semana 12: review intermediário
```

---

### FASE 7 — COMUNICAÇÃO ECOSSISTEMA (Bloco 6) (30 min)

**Objetivo:** o que vamos contar pras mentoradas e mercado.

**Estrutura da nota de versão pública:**

```markdown
# Travessia Imperatriz — Nota de Versão 2026-Q2

## O que muda no próximo trimestre

### Novidades
- Nova skill `/metricas-porta-trimestral` — você pede e ela mostra evolução da sua porta
- Nova skill `/checklist-stories` — pra auditar seu Q&A antes de postar

### Evoluções
- `/headline-imperatriz` v2 — agora com 6 temperaturas (incluindo base quente)
- `/voz-humana-br` v2 — banco de jargão atualizado pra 2026

### Despedidas
- `/skill-X-velha` — sai do ar em 30 dias. Funcionalidade absorvida por `/skill-nova`. Migração: nada precisa fazer, apenas usar `/skill-nova`.

### Próximos 90 dias
- Estamos focando em: medição trimestral, headline retargeting, fusão de skills duplicadas

## O que NÃO muda
- Travessia continua v1 (26 portas A-Z)
- Pilares continuam os mesmos (6 pilares)
- Sua progressão por porta continua válida

## Como reagir
- Se você usa `/skill-X-velha`: passa pra `/skill-nova` em 30 dias
- Se você usa `/headline-imperatriz`: nada muda, mas v2 lança em 6 semanas e tem coisa nova
- Resto: tudo segue normal
```

**Canais de divulgação:**
- E-mail pra Corte
- Post no canal exclusivo da mentoria
- Documentação atualizada
- Story curto pra Tata explicar a evolução em 60s

---

### FASE 8 — OUTPUT + ATA DO CONSELHO (15 min)

**Objetivo:** empacotar tudo + preparar reunião do Conselho da Soberana.

**Outputs finais:**
1. `00-revisao-completa.md` — documento mestre (consolidação dos 6 blocos)
2. `01-tabelao-mestre.json` — dado bruto
3. `02-quartil-superior.md`
4. `03-quartil-inferior.md`
5. `04-gaps-detectados.md`
6. `05-roadmap-90dias.md`
7. `06-comunicacao-ecossistema.md`
8. `07-dashboard-trimestre.html` — interativo, com gráficos
9. `08-ata-conselho-soberana.md` — template pra reunião

**Template da ata do Conselho:**
```markdown
# Ata Conselho da Soberana — 2026-Q2 → Q3

**Data:** 2026-04-08 (quarta-feira após rito de 2026-04-01)
**Presentes:** Tata Gonçalves (Soberana), [Imperatriz 1], [Imperatriz 2], [Imperatriz 3]
**Pauta:** revisão Q2 + aprovação roadmap Q3

## Decisões pra votar

### Decisão 1 — Aprovar plano de 90 dias?
[ ] Sim, integral
[ ] Sim, com cortes (especificar)
[ ] Não, refazer

### Decisão 2 — Aprovar deprecação de /skill-X-velha?
[ ] Sim
[ ] Não (justificar)

### Decisão 3 — Aprovar fusão skill-Y + skill-Z?
[ ] Sim
[ ] Não (justificar)

### Decisão 4 — Skills estratégicas com uso baixo (lista da Fase 4 INVESTIGAR)
- Discutir caso a caso
- Decisão por skill: manter / deprecar / refundir

## Encaminhamentos
- [ ] Time inicia execução em [data]
- [ ] Comunicação publicada em [data]
- [ ] Próxima reunião: [data Q3]
```

---

## TEMPO TOTAL ESTIMADO

- Fase 1 (Coleta): 45 min
- Fase 2 (Métricas): 20 min
- Fase 3 (Quartil superior): 30 min
- Fase 4 (Quartil inferior): 45 min
- Fase 5 (Gaps): 30 min
- Fase 6 (Roadmap): 45 min
- Fase 7 (Comunicação): 30 min
- Fase 8 (Output + Ata): 15 min
- **Total:** ~4h em modo focado

Conselho da Soberana acontece na semana seguinte (1h-1h30).

---

## CHECKLIST DO RITO

Imprimir e marcar manualmente. Rito não é "rodou comando" — é ritual.

- [ ] Agenda bloqueada 4h, sem interrupção
- [ ] `/dashboard-imperatriz --tata` rodou nos 3 meses
- [ ] Profile `17-feedback-skills` atualizado
- [ ] Tata respondeu bloco de contexto de mercado
- [ ] Fase 1 (Coleta) concluída
- [ ] Fase 2 (Métricas) concluída
- [ ] Fase 3 (Quartil superior) concluída
- [ ] Fase 4 (Quartil inferior) concluída
- [ ] Fase 5 (Gaps) concluída
- [ ] Fase 6 (Roadmap) concluída
- [ ] Fase 7 (Comunicação) concluída
- [ ] Fase 8 (Output + Ata) concluída
- [ ] Reunião do Conselho marcada
- [ ] Convocação enviada pras Imperatrizes do Conselho
- [ ] Dossiê compartilhado 48h antes da reunião

---

**Rito Trimestral Imperatriz — propriedade Tata Gonçalves.**
