# 09 — Auditoria Editorial (Checklist)

## Quando rodar `--auditar`

- Mentorada relata "não sei mais o que postar"
- Time de conteúdo mudou
- Final de mês/trimestre (cron via `evolucao-imperatriz`)
- Antes de mudar de Porta na Travessia
- Após queda de engajamento detectada por `dashboard-imperatriz`

## O que a skill pede

Amostra de **10 a 30 peças dos últimos 30 dias**, em qualquer formato:

- Lista de URLs (IG, LinkedIn, e-mail web)
- Cole de captions/copy direto
- Print do feed
- Export do CRM/planilha de conteúdo

A skill aceita misto. Mínimo 10 peças (menos que isso vira amostra ruim).

## O que a skill faz

### Passo 1 — Classificação

Cada peça é classificada em:
- **Pilar** (qual dos 3-5 declarados)
- **Categoria TEAM** (T/E/A/M/S)
- **Canal** (IG feed, IG stories, IG reels, LinkedIn, e-mail, WhatsApp status)
- **Vocabulário** (usou palavra-âncora? usou palavra banida?)
- **Boundary** (entrou em algum NÃO declarado?)

### Passo 2 — Cálculo de aderência

Para cada dimensão, compara real vs declarado:

| Dimensão | Tolerância |
|---|---|
| Distribuição por pilar | ±10pp por pilar |
| Mix TEAM | ±10pp por categoria |
| Cadência por canal | ±20% da frequência declarada |
| Vocabulário-âncora | mínimo 60% das peças usa pelo menos 1 |
| Vocabulário banido | máximo 10% das peças contém alguma |
| Boundaries | zero violações de NÃO duro |

### Passo 3 — Detecção de drift

Identifica os 3 desvios mais críticos. Drift é categorizado:

| Tipo | Severidade | Exemplo |
|---|---|---|
| **Crítico** | 🔴 | Boundary duro violado / palavra banida em > 30% das peças |
| **Alto** | 🟠 | Pilar abandonado (< 5% quando declarado 25%) / Monetize em zero numa Porta de venda |
| **Médio** | 🟡 | Mix TEAM desbalanceado em 1 categoria (drift > 15pp) |
| **Baixo** | 🟢 | Cadência um pouco abaixo do declarado |

### Passo 4 — Detecção de canibalização

Cruza com a regra do `calendario-imperatriz` (1 ideia × 5 canais espaçada 2-3 dias). Marca peças que apareceram **copy-paste no mesmo dia em vários canais**.

### Passo 5 — Recomendação executável

Não devolve "melhore sua linha editorial". Devolve **3 ações concretas**:

> **Pare de fazer**: 4º carrossel didático/semana — está superando T em 35pp.
>
> **Volte a fazer**: posts de pergunta direta — Engage caiu pra 8% (declarado: 25%).
>
> **Ajuste**: na Porta J você precisa de 25% Monetize. Está em 5%. Subir nas próximas 4 semanas com 1 post/semana de "tem X vagas abrindo".

## Output da auditoria

```markdown
# Auditoria Editorial — [Nome] | [Data]
**Porta atual: J | Amostra: 23 peças (12-04 a 09-05)**

## Aderência Geral: 64/100 — Drift Médio

### Distribuição por Pilar
| Pilar | Declarado | Executado | Drift |
|---|---|---|---|
| Câmara da Conversão | 40% | 60% | +20pp 🟠 |
| Outras Imperatrizes | 30% | 13% | -17pp 🟠 |
| O Pitch que Vendeu | 20% | 22% | +2pp 🟢 |
| Bastidor de Soberana | 10% | 5% | -5pp 🟡 |

### Mix TEAM
| Categoria | Declarado | Executado | Drift |
|---|---|---|---|
| Teach | 25% | 60% | +35pp 🔴 |
| Engage | 25% | 8% | -17pp 🟠 |
| Authority | 20% | 22% | +2pp 🟢 |
| Monetize | 25% | 5% | -20pp 🔴 |
| Story | 5% | 5% | 0pp 🟢 |

### Vocabulário
- ✅ 78% das peças usaram palavra-âncora
- ⚠️ 18% usaram palavra banida ("ecossistema", "jornada", "alavancar")
- ⚠️ 4 peças com travessão (—)

### Boundaries
- ✅ Zero violações de NÃO duro
- ⚠️ 1 peça em fronteira — depoimento publicado sem confirmação escrita de permissão

### Canibalização
- ⚠️ 3 ideias publicadas copy-paste IG carrossel + LinkedIn no mesmo dia (perda de força)

---

## Recomendação (top 3)

1. **PARE** de produzir mais 1 carrossel didático/semana.
   Você está em 60% Teach numa Porta de venda. Substitua por posts de Monetize.

2. **VOLTE** a fazer perguntas diretas.
   Engage caiu pra 8%. Sem isso, o algoritmo te enterra. Mínimo 1 post/semana com pergunta.

3. **AJUSTE** os depoimentos.
   Crie protocolo de permissão escrita antes de qualquer post com nome de cliente. (Boundary já declarado, time não está aplicando.)

---

**Próximo passo sugerido**: rodar `--evoluir` antes de aplicar as mudanças (ver se a linha precisa ser recalibrada pra Porta J ou se executores precisam de retreinamento).
```

## Critérios de qualidade da auditoria

A skill **só** entrega auditoria se:

1. Amostra ≥ 10 peças
2. Cobertura mínima de 3 canais diferentes (senão não dá pra auditar mix)
3. Período mínimo 14 dias
4. Linha editorial canônica existe (`04-linha-editorial.json` no caminho)

Se algum falha, a skill avisa e pede o que falta.

## Anti-patterns

- ❌ Devolver "linha editorial está OK" sem números
- ❌ Devolver score sem recomendação executável
- ❌ Recomendar "diversifique mais" sem dizer **o quê** parar e **o quê** começar
- ❌ Auditar com amostra < 10 peças (vira opinião, não diagnóstico)
- ❌ Esquecer de cruzar com Porta atual (drift relativo à Porta, não ao default)
