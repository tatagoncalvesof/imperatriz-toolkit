# CICLOS RECORRENTES — Cadência fixa + skill por ciclo

Algumas portas, depois de fechadas pela primeira vez, viram **ciclo eterno**. Não basta passar uma vez. A travessia exige cadência. Sem cadência, a porta volta a abrir sozinha (regresso silencioso).

A skill `gates-imperatriz` cobra os ciclos no modo `--ciclos [nome]`: lista vencidos, em dia, próximos.

---

## REGRA GERAL

- Ciclo vencido = mentorada está em **risco de regresso** na porta correspondente.
- Vencido < 1 cadência = atenção. Vencido > 2 cadências = porta efetivamente regrediu.
- Skill cruza ciclo vencido com sintomas (em `TROUBLESHOOTING-REVERSO.md`) — geralmente o sintoma já apareceu antes da mentorada perceber.

---

## CICLO N — Narrativa (semanal)

**Cadência:** Semanal (toda segunda-feira como default).

**O que acontece no ciclo:**
- Revisar calendário editorial da semana
- Publicar conteúdo segundo o plano (cadência declarada por canal)
- Medir alcance / engajamento da semana anterior
- Ajustar próxima semana

**Skill associada:**
- `/skill-mentoria-tata` (planejamento de conteúdo)
- `/voz-humana-br` (humanização de copy gerada)
- `/headline-imperatriz` (headlines da semana)

**Sinal de vencido:**
- Mais de 7 dias sem publicação no canal principal
- Ou mais de 3 dias sem publicação se cadência declarada é diária

**Risco se atrasar:**
- Algoritmo perde tração
- Audiência esfria
- Sintoma 6 (conteúdo travado) aparece em 2-3 semanas

---

## CICLO L — Laboratório (mensal)

**Cadência:** Mensal (primeiro útil do mês).

**O que acontece no ciclo:**
- Mapear funil completo com métricas atualizadas
- Identificar gargalos do mês
- Propor 1-2 testes A/B
- Documentar hipótese e métrica-alvo
- Revisar resultado de testes do mês anterior

**Skill associada:**
- `/ads-audit` ou `/ads-meta` / `/ads-google` (audit do tráfego)
- `/page-cro` (otimização de página)
- `/ab-test-setup` (montar teste)

**Sinal de vencido:**
- Mais de 35 dias sem revisão de funil
- Ou nenhum teste A/B no último mês

**Risco se atrasar:**
- Gargalo cresce sem detecção
- CPA sobe
- Sintoma 1 (tráfego caro) aparece em 30-45 dias

---

## CICLO Z — Zelo (mensal)

**Cadência:** Mensal (último útil do mês).

**O que acontece no ciclo:**
- Implementar 1 melhoria do backlog (porta qualquer)
- Re-validar portas anteriores: nenhuma regrediu?
- Atualizar documentação
- Escolher melhoria do mês seguinte

**Skill associada:**
- `/reuniao-de-resultado` (rituais com time)
- `/kaizen-improvement` (melhoria contínua)
- A própria `gates-imperatriz` (re-audit das portas)

**Sinal de vencido:**
- Mais de 35 dias sem implementação
- Ou nenhum item do backlog atualizado

**Risco se atrasar:**
- Regresso silencioso em portas antigas
- Time perde foco
- Sintoma 7 (time desorientado) aparece em 60d

---

## CICLO T — Tesouro (trimestral)

**Cadência:** Trimestral (primeira semana do trimestre).

**O que acontece no ciclo:**
- Campanha de reativação na base ativa
- Recompra / upgrade / indicação
- Medir receita reativação / receita total
- Atualizar segmentação da base

**Skill associada:**
- `/campanha-interna` (montar campanha)
- `/email-sequence` (sequência)
- `/copy-conversacional-dm` (DM da reativação)
- `/referral-program` (indicação)

**Sinal de vencido:**
- Mais de 100 dias sem campanha de reativação
- Ou receita reativação no trimestre < 20% receita total

**Risco se atrasar:**
- LTV cai
- Margem comprime
- Sintoma 5 (margem baixa) aparece no próximo trimestre

---

## CICLO X — eXame (trimestral)

**Cadência:** Trimestral (última semana do trimestre).

**O que acontece no ciclo:**
- Audit completo do negócio (copy, tracking, ofertas, atendimento, financeiro, time)
- Score 0-100
- Plano de ação pra itens abaixo de 80
- Re-validação das 26 portas (rápida)

**Skill associada:**
- `/scale-audit` (audit de produção em escala)
- `/security-audit` (segurança técnica)
- `/health-score` (saúde geral)
- A própria `gates-imperatriz` em modo --validar pra cada porta crítica

**Sinal de vencido:**
- Mais de 110 dias sem audit
- Ou score do último audit < 80

**Risco se atrasar:**
- Falhas estruturais acumulam invisíveis
- Múltiplos sintomas aparecem ao mesmo tempo

---

## CICLO Y — Yield (anual)

**Cadência:** Anual (planejamento começa 60 dias antes do fim do ano fiscal).

**O que acontece no ciclo:**
- Revisão de margem dos 12 meses
- Projeção próximo ano
- Decisões de preço, estrutura, contratação, cortes
- Plano financeiro anual

**Skill associada:**
- `/skill-relatorio-ads` (consolidação aquisição)
- `/pricing-strategy` (revisão de preço)
- `/launch-strategy` (planejamento de lançamentos do ano)

**Sinal de vencido:**
- Mais de 13 meses sem revisão anual de margem
- Ou variação mês-a-mês > 20% nos meses fora de Q1

**Risco se atrasar:**
- Decisões reativas o ano inteiro
- Sintoma 5 (margem baixa) cronifica

---

## DASHBOARD DE CICLOS — formato esperado

Quando a skill roda `--ciclos [nome]`, devolve neste formato:

```
# CICLOS RECORRENTES — [Nome]

## Vencidos (atenção imediata)
- N (semanal) — última: 2026-04-22 — atrasado 9 dias — RISCO ALTO
  → ação: rodar /voz-humana-br + publicar 3 peças hoje
- L (mensal) — última: 2026-03-15 — atrasado 24 dias — RISCO MÉDIO
  → ação: rodar /ads-meta esta semana

## Em dia
- Z (mensal) — última: 2026-04-30 — próxima: 2026-05-31
- T (trimestral) — última: 2026-04-08 — próxima: 2026-07-08
- X (trimestral) — última: 2026-03-30 — próxima: 2026-06-30

## Bloqueados (porta ainda não fechou primeira vez)
- Y (anual) — depende de K +12 meses (mentorada está em K há 4 meses)

## Recomendação de ordem
1. N HOJE (cadência crítica)
2. L esta semana
3. Z e T no fluxo normal

## Skills a executar
ver coluna "skill associada" deste arquivo
```

---

## INTEGRAÇÃO COM `/tatou-2.0`

Quando a skill `gates-imperatriz` detecta ciclo vencido, ela passa o output como input pra `/tatou-2.0`, que então constrói o "como rodar esse ciclo agora" usando a skill associada. Divisão clara:

- `gates-imperatriz` diagnostica: "ciclo N vencido"
- `tatou-2.0` constrói: o passo a passo + executa as skills

---

## REGRAS DURAS

1. **Mentorada não pode pular ciclo "porque está ocupada".** Skill cobra. Atraso vira risco.
2. **Ciclo trimestral X é inegociável** mesmo em fase de crescimento — sem audit, regressos viram crônicos.
3. **Ciclo anual Y planeja antes do início do ano fiscal**, não depois.
4. **Ciclos vencidos viram input automático** do próximo audit `--validar`.

---

## TABELA RESUMO

| Ciclo | Cadência | Skill principal | Risco se atrasa |
|---|---|---|---|
| N | Semanal | conteúdo + voz humana | algoritmo cai |
| L | Mensal | ads-audit + page-cro | gargalo invisível |
| Z | Mensal | reunião-resultado + kaizen | regresso silencioso |
| T | Trimestral | campanha-interna | LTV/margem cai |
| X | Trimestral | scale-audit + gates-imperatriz | falhas estruturais |
| Y | Anual | pricing + launch + relatório | reativo o ano todo |

---

**Travessia Imperatriz — Pilar 2 (Fluxo). Propriedade intelectual Tata Gonçalves.**
