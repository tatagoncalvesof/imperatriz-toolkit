# Evolução Imperatriz — Pilar 6 da Travessia

> *"Sistema que não evolui não é sistema — é museu. E museu não dá retorno."*

Skill operadora do **Pilar 6 (Evolução)** do ecossistema Tata Gonçalves. Conduz o **rito trimestral** de revisão das ~225 skills, identifica gaps, propõe evolução e versiona a metodologia.

Sem essa skill, ecossistema vira coleção. Com essa skill, ecossistema vira organismo vivo — respira a cada 90 dias, descarta o que não serve, evolui o que funciona, cria o que falta.

---

## O QUE ELA FAZ

Em uma frase: **mede, classifica, decide e versiona o ecossistema inteiro a cada trimestre.**

Concretamente:

- **Mede** uso, impacto e NPS de cada uma das ~225 skills
- **Classifica** em quartis (top 25 / bottom 25 / intermediário / museu)
- **Identifica** gaps — demandas recorrentes sem skill correspondente
- **Propõe** plano de 90 dias: CRIAR / EVOLUIR / DEPRECAR / FUNDIR
- **Versiona** mudanças (skill v1.0 → v1.1 → v2.0 + Travessia v1 → v2)
- **Prepara** dossiê pro **Conselho da Soberana** (governança executiva)
- **Comunica** mudanças pro ecossistema (nota de versão pública)

---

## O QUE ELA NÃO FAZ

- Não escreve copy, não cria oferta, não monta funil
- Não EXECUTA mudança em skill — propõe e registra
- Não decide sozinha deprecação estratégica (passa pelo Conselho)
- Não substitui medição mensal (`/dashboard-imperatriz`)
- Não substitui melhoria tática contínua (`/kaizen-improvement`)

---

## QUANDO USAR

| Situação | Modo |
|----------|------|
| Primeiro dia útil de Jan/Abr/Jul/Out (rito marcado) | `--revisar` |
| Suspeita que skill X virou museu | `--auditar [skill]` |
| Apresentar plano 90 dias pro time / Conselho | `--roadmap` |
| Registrar formalmente mudança de versão | `--versionar [skill] [v]` |
| Antes de lançar Travessia v2 (ou versão maior) | `--revisar` + `--roadmap` |
| 5+ mentoradas pediram a mesma coisa em call | `--roadmap` (validar gap) |

---

## INSTALAÇÃO

### Onde mora

```
~/.claude/skills/evolucao-imperatriz/
├── SKILL.md                          ← cérebro (sempre carregado)
├── README.md                         ← este arquivo
├── RITO-TRIMESTRAL.md                ← passo a passo das 8 fases
├── METRICAS-DE-UMA-SKILL.md          ← como medir uso/impacto/satisfação
├── CICLO-DE-VIDA-METODOLOGIA.md      ← Travessia v1 → v2 + transição
└── EXEMPLOS-REVISOES.md              ← 3 revisões ficcionais com decisões
```

### Onde os outputs moram

```
~/imperio/evolucao/
├── 2026-Q2/                          ← uma pasta por trimestre
│   ├── 00-revisao-completa.md
│   ├── 01-tabelao-mestre.json
│   ├── 02-quartil-superior.md
│   ├── 03-quartil-inferior.md
│   ├── 04-gaps-detectados.md
│   ├── 05-roadmap-90dias.md
│   ├── 06-comunicacao-ecossistema.md
│   ├── 07-dashboard-trimestre.html
│   └── 08-ata-conselho-soberana.md
├── 2026-Q3/
├── auditorias/                       ← auditorias individuais (--auditar)
│   ├── headline-imperatriz-2026-04-15.md
│   └── voz-humana-br-2026-04-22.md
└── changelogs/                       ← histórico de versões por skill
    ├── headline-imperatriz/
    │   ├── v1.0.md
    │   ├── v1.1.md
    │   └── v2.0.md
    └── mecanismo-unico/
        └── v1.0.md
```

---

## OS 4 MODOS

### `--revisar` — rito trimestral completo

Executa o ritual de 8 fases (coleta → métricas → quartis → gaps → roadmap → comunicação → output → ata).

Demora 2-4h em execução real (precisa Tata responder bloco de contexto de mercado). Output vira pauta da reunião do Conselho.

```bash
/evolucao-imperatriz --revisar
```

### `--auditar [skill]` — auditoria individual

Mede uma skill específica contra o framework de `METRICAS-DE-UMA-SKILL.md`. Recomenda destino: manter / evoluir v2 / fundir / deprecar.

```bash
/evolucao-imperatriz --auditar headline-imperatriz
```

### `--roadmap` — plano 90 dias standalone

Sem revisão completa. Pega último estado conhecido e gera plano executável priorizado por ICE (Impact × Confidence × Ease).

```bash
/evolucao-imperatriz --roadmap
```

### `--versionar [skill] [versao]` — registra mudança formal

Documenta breaking changes, plano de migração, gera changelog e atualiza ciclo de vida.

```bash
/evolucao-imperatriz --versionar headline-imperatriz 2.0
```

---

## INTEGRAÇÃO COM O ECOSSISTEMA

**Inputs (lê de):**
- `/dashboard-imperatriz` — uso e KPI por skill
- `/dossie-mentorada` (profile `17-feedback-skills`) — NPS, reclamações, pedidos
- `/gates-imperatriz` — status de portas (cruzar com skills associadas)
- `/imperio-qualidade` — auditoria técnica
- `/kaizen-improvement` — melhorias táticas que viraram demanda

**Outputs (alimenta):**
- Conselho da Soberana — dossiê pra reunião decisória
- Time da Tata — pipeline de execução (CRIAR / EVOLUIR / DEPRECAR / FUNDIR)
- Comunicação ecossistema — nota de versão pública pras mentoradas
- `CICLO-DE-VIDA-METODOLOGIA.md` — registro histórico vivo

---

## CICLO DE VIDA — RESUMO

**Skill individual:**
- v1.0 — primeira versão pública
- v1.x — patches e melhorias incrementais
- v2.0 — refundação (breaking change OK)
- DEPRECATED — uso 0 em 2 trimestres = morte

**Travessia (metodologia inteira):**
- v1.0 (2026) — 26 portas, 6 pilares, ~225 skills
- v2.0 (projetado 2027) — quando 30%+ skills evoluíram OU pilar inteiro mudou
- Decisão sempre passa pelo Conselho da Soberana
- Mentoradas antigas: acesso v2 sem custo + 6 meses de overlap

Detalhamento em `CICLO-DE-VIDA-METODOLOGIA.md`.

---

## CONSELHO DA SOBERANA

Órgão de governança que decide mudanças grandes na metodologia.

**Composição:**
- Tata Gonçalves (Soberana, voto de Minerva)
- 2-3 mentoradas-imperatriz (alunas que chegaram no nível Imperatriz, com 12+ meses de Travessia, vivem o método)
- 1 representante de dado frio (a própria skill `/evolucao-imperatriz` apresenta tabelão sem opinião)

**Cadência:** 1× por trimestre, na semana seguinte ao rito de revisão.

**Decide:**
- Aprovar plano de 90 dias proposto pela skill
- Aprovar deprecação de skill estratégica
- Aprovar fusão de skills (>70% sobreposição)
- Aprovar lançamento de v2 da Travessia
- Aprovar mudança de nomenclatura central

**NÃO decide:** mudança técnica de skill individual (Tata + time fazem direto), patch incremental, criação de skill nova de baixo risco.

---

## REGRAS DURAS

1. Não invento métrica — sem `/dashboard-imperatriz`, paro
2. Não deprecam skill estratégica sozinha — Conselho decide
3. Não fundo skills sem sobreposição real (>70%)
4. Não versiono sem changelog documentado
5. Não comunico mudança sem prazo de transição mínimo (30 dias)
6. Não pulo Conselho em decisão grande
7. Não escondo dado feio — apresento exato
8. Não recomendo CRIAR skill sem 5+ pedidos validados
9. Não evoluo skill do quartil inferior — skill ruim com uso baixo morre
10. Não opero dentro do ecossistema — governo o ecossistema

---

## EXEMPLOS DE USO

### Caso 1 — Rito de Abril
> "Tata, é primeiro dia útil de abril. Roda revisão Q1."

```
/evolucao-imperatriz --revisar
```
Skill puxa dados Q1 (jan-fev-mar), gera 6 blocos, prepara dossiê pro Conselho marcado pra próxima quarta.

### Caso 2 — Suspeita de museu
> "Acho que ninguém usa /skill-X há meses."

```
/evolucao-imperatriz --auditar skill-X
```
Skill mede uso real, NPS, sobreposição. Recomenda: deprecar, fundir com /skill-Y ou manter como nicho.

### Caso 3 — Reunião de planejamento
> "Vou apresentar plano 90 dias pro time amanhã."

```
/evolucao-imperatriz --roadmap
```
Output pronto pra colar no Notion / board, com priorização ICE.

### Caso 4 — Lançar headline-imperatriz v2
> "Reescrevi headline-imperatriz com 6 temperaturas + base quente. Versionar."

```
/evolucao-imperatriz --versionar headline-imperatriz 2.0
```
Gera changelog, plano de migração de mentoradas que usam v1, nota pública.

---

## VERSIONAMENTO DESTA SKILL

| Versão | Data | Mudanças |
|--------|------|----------|
| v1.0 | 2026-Q2 | Primeira versão. 4 modos, 6 blocos, integração com dashboard + dossiê |
| v1.5 | 2026-Q4 (planejado) | Automação parcial via cron mensal + alerta de skill em risco |
| v2.0 | 2027-Q2 (planejado) | Conselho da Soberana com voto frio (mentoradas-imperatriz votam quartis) |
| v3.0 | 2028 (planejado) | Auto-sugestão de fusão por análise semântica de descriptions |

---

## COMO COMPARTILHAR COM MENTORANDAS

Esta skill **NÃO É COMPARTILHADA**. É de uso exclusivo da Tata + Conselho da Soberana.

Por quê: governar o ecossistema é trabalho de Soberana. Mentorada usa o ecossistema, não decide a evolução dele. Compartilhar essa skill seria entregar a chave do museu pra quem vai visitá-lo.

A mentorada-imperatriz que entra no Conselho recebe acesso temporário durante o trimestre que vai votar. Acesso revogado depois.

---

**Método Imperatriz de Evolução — propriedade intelectual Tata Gonçalves.**
