# Métricas de uma Skill — Como Medir Uso, Impacto e Satisfação

> *"O que não se mede, vira museu."*

Framework completo pra avaliar se uma skill está VIVA ou virou peça de exposição. Aplica-se tanto no rito trimestral (`--revisar`) quanto na auditoria individual (`--auditar`).

---

## OS 3 EIXOS DE MEDIÇÃO

Toda skill é medida em **3 eixos independentes**, cada um com 3-5 indicadores.

```
        USO
         │
         │
         ▼
  ┌──────────────┐
  │              │
  │     SKILL    │
  │              │
  └──────────────┘
   ▲           ▲
   │           │
IMPACTO   SATISFAÇÃO
```

Skill saudável tem os 3 eixos verdes. Skill museu tem os 3 vermelhos. Skill no meio precisa decisão (evoluir ou deprecar).

---

## EIXO 1 — USO

**Pergunta central:** *as pessoas chamam essa skill?*

### Indicadores

#### 1.1 Chamadas absolutas no trimestre

Quantas vezes a skill foi invocada (qualquer mentorada, qualquer modo).

**Régua:**
| Faixa | Status |
|-------|--------|
| 0 chamadas | MUSEU candidato |
| 1-5 chamadas | NICHO (pode ser ok se estratégica) |
| 6-50 chamadas | ATIVA |
| 51-200 chamadas | POPULAR |
| 200+ chamadas | CORE |

#### 1.2 Mentoradas únicas

Quantas mentoradas distintas usaram (não chamadas, pessoas).

**Régua:**
| Faixa | Status |
|-------|--------|
| 0 | MUSEU |
| 1-2 | USO PESSOAL DA TATA |
| 3-9 | NICHO |
| 10-30% da Corte | ADOÇÃO MÉDIA |
| 30-60% da Corte | POPULAR |
| 60%+ da Corte | CORE |

**Regra dura:** se chamadas absolutas é alta mas mentoradas únicas é baixa, é skill que UMA mentorada fanática usa muito. Não é skill core, é uso individual.

#### 1.3 Delta de uso vs trimestre anterior

Cresceu ou caiu?

**Régua:**
| Faixa | Status |
|-------|--------|
| -50% ou pior | DESPENCANDO ← investigar |
| -20% a -50% | CAINDO |
| -20% a +20% | ESTÁVEL |
| +20% a +100% | CRESCENDO |
| +100% ou mais | EXPLODINDO ← documentar como case |

#### 1.4 Distribuição de uso ao longo do trimestre

Uso concentrado em 1 mês (campanha) ou distribuído (skill diária)?

- **Concentrado** = skill de evento (lançamento, campanha) — ok ter pico
- **Distribuído** = skill de processo — ok ter regularidade
- **Concentrado em 1 dia + zero o resto** = uso anômalo, investigar

#### 1.5 Ratio de chamadas / mentoradas únicas

`chamadas_total / mentoradas_unicas` = quantas vezes cada mentorada usou em média.

**Régua:**
| Faixa | Status |
|-------|--------|
| 1.0 - 2.0 | USO ÚNICO (skill de setup, talvez ok) |
| 2.0 - 5.0 | USO RECORRENTE LEVE |
| 5.0 - 15.0 | USO RECORRENTE FORTE (skill de processo) |
| 15.0+ | USO INTENSIVO (skill diária ou semanal) |

---

## EIXO 2 — IMPACTO

**Pergunta central:** *quem usa, melhora?*

### Indicadores

#### 2.1 KPI primário ligado à skill

Toda skill tem 1 KPI primário declarado no manifesto. Exemplos:
- `/headline-imperatriz` → CTR de anúncios
- `/skill-pagina-vendas` → conversão da página
- `/voz-humana-br` → score "soa humano" (1-10)
- `/mecanismo-unico` → CPC reduzido em ads que aplicam

**Régua:**
| Comparação | Status |
|------------|--------|
| Abaixo do benchmark BR mentora high-ticket | VERMELHO |
| 70-99% do benchmark | AMARELO |
| 100-150% do benchmark | VERDE |
| 150%+ | EXCEPCIONAL |

#### 2.2 Casos high-impact

Mentoradas que tiveram resultado mensurável e atribuíram à skill.

**Régua:**
| Quantidade | Status |
|------------|--------|
| 0 casos | SEM PROVA |
| 1-2 casos | EVIDÊNCIA INICIAL |
| 3-5 casos | PADRÃO EMERGENTE |
| 6-15 casos | CONSOLIDADA |
| 15+ casos | ESCALÁVEL |

**Crítica:** caso high-impact precisa ter número (não opinião). "Aumentou 40% conversão depois de aplicar X" é caso. "Adorei a skill" é satisfação, não impacto.

#### 2.3 Tempo até resultado

Mentorada usa a skill — em quanto tempo aparece efeito mensurável?

**Régua:**
| Tempo | Status |
|-------|--------|
| Mesma sessão | EFEITO IMEDIATO (skill operacional) |
| Mesma semana | EFEITO RÁPIDO |
| Mesmo mês | EFEITO MÉDIO |
| 30-90 dias | EFEITO ESTRATÉGICO (skill de longo prazo) |
| 90+ dias ou nunca aparece | INVESTIGAR |

#### 2.4 Casos low-impact / negativos

Mentoradas que usaram e PIOR — ou ficou igual.

Sinaliza problema. Aceitável até 10% das mentoradas únicas. Acima disso = skill ruim.

#### 2.5 Skills downstream destravadas

Skill que destrava uso de outras skills (exemplo: `/briefing-copy-360` é pré-requisito de várias copy skills).

**Régua:** quantas outras skills foram chamadas DEPOIS dessa, em mesma sessão? Skill com efeito de cascata é estratégica.

---

## EIXO 3 — SATISFAÇÃO

**Pergunta central:** *quem usa, recomenda?*

### Indicadores

#### 3.1 NPS direto

Pergunta no profile `17-feedback-skills`: *"De 0 a 10, o quanto você recomendaria essa skill?"*

NPS = `% promotoras (9-10) - % detratoras (0-6)`.

**Régua:**
| NPS | Status |
|-----|--------|
| < 0 | CRÍTICO ← deprecar ou refundir |
| 0-30 | RUIM |
| 30-50 | OK |
| 50-70 | BOM |
| 70+ | EXCELENTE |

#### 3.2 Taxa de resposta de feedback

Quantas mentoradas que usaram a skill efetivamente deram feedback?

Taxa < 20% = NPS pouco confiável (amostra ruim). Marca como "NPS provisório".

#### 3.3 Reclamações textuais

Pega texto livre do feedback. Categoriza:
- **Funcional** — "não fez o que prometeu", "deu erro"
- **Cognitivo** — "complicado", "muitas perguntas", "não entendi"
- **Emocional** — "frustrante", "perdi tempo"
- **Mercado** — "não serve pro meu nicho", "muito genérico"

3+ reclamações da mesma categoria = sinaliza tipo de problema.

#### 3.4 Elogios textuais

Mesma análise mas pelo lado positivo. Detecta:
- O que a skill faz BEM
- Quais pedacinhos da skill são "amados" (proteger em v2)

#### 3.5 Pedidos de funcionalidade nova

Mentorada usou e pediu mais. Sinaliza demanda de v2.

5+ pedidos da mesma funcionalidade = entra no roadmap como `EVOLUIR v2`.

---

## EIXO 4 (BÔNUS) — SAÚDE TÉCNICA

**Pergunta central:** *a skill em si está bem cuidada?*

### Indicadores

#### 4.1 Dias desde última evolução

Skill core que ficou mais de 365 dias sem update = sinal amarelo. Mercado mudou, ela não.

#### 4.2 Sobreposição com outras skills

Mede % de description e funcionalidade que conflita com skills irmãs.

| Sobreposição | Ação |
|--------------|------|
| 0-30% | OK, refina description |
| 30-70% | Reposicionar (description ruim, ninguém escolhe) |
| 70%+ | FUNDIR |

#### 4.3 Quebras conhecidas

Skill teve bug reportado e não foi corrigido? Marca como "DÉBITO TÉCNICO" e entra no roadmap.

#### 4.4 Documentação interna atualizada

SKILL.md, README e arquivos de referência batem com versão atual? Skill com doc desatualizada = skill mal cuidada.

---

## A FÓRMULA COMBINADA — SCORE DA SKILL

**Score final 0-100** combina os 3 eixos:

```
SCORE = (USO × 0.4) + (IMPACTO × 0.4) + (SATISFAÇÃO × 0.2)
```

Cada eixo normalizado 0-100:
- **USO** = baseado em chamadas absolutas e % da Corte
- **IMPACTO** = baseado em vs benchmark e casos high-impact
- **SATISFAÇÃO** = NPS normalizado 0-100

### Faixas de classificação

| Score | Classificação | Decisão padrão |
|-------|---------------|----------------|
| 0-20 | MUSEU | DEPRECAR (se não-estratégica) |
| 21-40 | RISCO | INVESTIGAR + refundir ou fundir |
| 41-60 | OK | MANTER, observar próximo trimestre |
| 61-80 | BOA | MANTER e/ou EVOLUIR v2 |
| 81-100 | EXCELENTE | PROTEGER + ESCALAR |

**Override de regras duras:**
- Skill com **uso = 0 em 2 trimestres** = DEPRECAR (mesmo que score parcial seja ok)
- Skill **estratégica** = nunca DEPRECAR sozinha (vai pra Conselho)
- Skill com **NPS < 0** = REFUNDIR ou DEPRECAR (mesmo com uso alto, satisfação ruim mata)

---

## TEMPLATE DE AUDITORIA INDIVIDUAL

Quando rodar `/evolucao-imperatriz --auditar [skill]`, output segue este template:

```markdown
# AUDITORIA — /[nome-skill]

**Data:** 2026-04-22
**Trimestre de referência:** 2026-Q1
**Versão atual:** 1.2

---

## EIXO 1 — USO (score 78/100)

- **Chamadas absolutas:** 247 (POPULAR)
- **Mentoradas únicas:** 18 (60% da Corte) — POPULAR
- **Delta vs Q4 2025:** +30% — CRESCENDO
- **Distribuição:** uniforme nos 3 meses
- **Ratio chamadas/mentoradas:** 13.7 — USO RECORRENTE FORTE

**Diagnóstico:** skill com uso saudável, distribuído, em crescimento.

---

## EIXO 2 — IMPACTO (score 85/100)

- **KPI primário:** CTR de anúncios
- **Valor médio das mentoradas que usaram:** 2.3%
- **Benchmark BR mentora high-ticket:** 1.8%
- **vs Benchmark:** +28% (VERDE)
- **Casos high-impact:** 7 (CONSOLIDADA)
- **Tempo até resultado:** mesma semana (rápido)
- **Casos low-impact:** 1 (3% — aceitável)
- **Cascata:** desbloqueia /skill-copy-ads-ptbr em 80% das chamadas

**Diagnóstico:** alto impacto comprovado, efeito rápido, destrava ecossistema.

---

## EIXO 3 — SATISFAÇÃO (score 87/100)

- **NPS:** 87
- **Taxa de resposta:** 78% — confiável
- **Reclamações:** 1 (categoria: funcional — pediu mais variações)
- **Elogios textuais:** 8
- **Pedidos de funcionalidade nova:** 8 ("headline pra base quente", "retargeting carrinho")

**Diagnóstico:** mentoradas amam, pedem mais variações.

---

## EIXO 4 — SAÚDE TÉCNICA (score 70/100)

- **Dias desde última evolução:** 87 (ok)
- **Sobreposição com outras:** 22% com /analise-anuncio-1000 (ok)
- **Quebras conhecidas:** 0
- **Documentação atualizada:** sim

---

## SCORE GERAL: 81/100 — EXCELENTE

## RECOMENDAÇÃO: EVOLUIR v2

### Justificativa
Skill está no quartil superior por todos os critérios. Pedidos validados (n=8) por funcionalidade nova ("headline pra base quente" e "retargeting carrinho") indicam claro caminho de evolução.

### Plano v2 sugerido
1. Adicionar 2 temperaturas novas: base quente + retargeting carrinho
2. Atualizar `OS-13-ELEMENTOS.md` com camada nova
3. Manter v1 funcional (sem breaking change)
4. Comunicar v2 na nota de versão Q3

### Esforço estimado: 2 semanas
### Owner sugerido: Tata
### Prazo: Q3 semana 6
```

---

## CHECKLIST RÁPIDO (ANTES DE DEPRECAR)

Antes de marcar uma skill como DEPRECAR, valida 7 perguntas. Se 6+ forem SIM, deprecação é segura.

- [ ] Uso = 0 em 2 trimestres consecutivos?
- [ ] NPS < 30 ou sem dado?
- [ ] Não tem casos high-impact documentados?
- [ ] Não destrava nenhuma outra skill?
- [ ] Não está marcada como estratégica no manifesto?
- [ ] Funcionalidade já existe em outra skill?
- [ ] Mentoradas que usaram não pediram nada novo?

Se todas 7 = SIM, deprecação é decisão da skill (autorizada).
Se 5-6 = SIM, deprecação vai pro Conselho com sugestão.
Se 4 ou menos = SIM, INVESTIGAR antes de cogitar deprecação.

---

**Métricas Imperatriz de Skill — propriedade Tata Gonçalves.**
