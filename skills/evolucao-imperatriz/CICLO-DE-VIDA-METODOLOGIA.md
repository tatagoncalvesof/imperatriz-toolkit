# Ciclo de Vida da Metodologia — Travessia v1 → v2 → ...

> *"Versionar é honrar quem veio antes. Mentorada antiga não é débito técnico — é fundação."*

Documento vivo que registra a evolução da metodologia inteira (Travessia Imperatriz) e de cada skill individual ao longo do tempo. Atualizado a cada rito trimestral e a cada `--versionar`.

---

## DOIS NÍVEIS DE VERSÃO

### Nível METODOLOGIA — Travessia v1, v2, v3...

A Travessia Imperatriz inteira (26 portas A-Z, 6 pilares, ecossistema de ~225 skills) tem versão maior.

**Travessia v1 (atual, 2026)** — primeira versão pública.
**Travessia v2 (projetada 2027)** — quando critério de upgrade for satisfeito.

### Nível SKILL — skill v1.0, v1.1, v2.0...

Cada skill individual tem versão própria, independente da Travessia. Skill pode estar em v3.2 enquanto Travessia ainda é v1.

**Semantic versioning aplicado:**
- **MAJOR (v1.0 → v2.0)** — breaking change. Mudança de input, mudança de lógica central, refundação. Mentorada precisa adaptar uso.
- **MINOR (v1.0 → v1.1)** — funcionalidade nova SEM breaking change. Adicionou modo, adicionou critério, adicionou referência. Quem usava v1.0 continua usando, ganha bônus.
- **PATCH (v1.0 → v1.0.1)** — bugfix. Corrigiu erro de descrição, ajustou edge case. Invisível pra mentorada.

---

## QUANDO LANÇAR TRAVESSIA v2

A v2 da metodologia inteira só nasce quando UM dos 4 critérios é satisfeito:

### Critério 1 — Massa crítica de skills v2

**Régua:** 30%+ das skills do ecossistema chegaram em v2.0 individual.

Quando 67+ skills (de ~225) já refundaram, é sinal de que a base mudou tanto que a Travessia precisa nova roupagem pra refletir o que ela é hoje.

### Critério 2 — Pilar inteiro reestruturado

**Régua:** 1 dos 6 pilares (Dados, Fluxo, Execução, Medição, Recuperação, Evolução) precisa de refundação maior — não cabe em refinamento incremental.

Exemplo hipotético: se Pilar 4 (Medição) precisar trocar de mensal pra semanal por mudança de mercado, isso força v2 da Travessia inteira pra alinhar Pilar 4 com Pilares 1-3-5-6.

### Critério 3 — Mudança de mercado disruptiva

**Régua:** mercado mudou tanto que metodologia v1 perde relevância em 2+ portas.

Exemplos hipotéticos:
- Plataforma central morre (Instagram colapsa) — várias portas precisam ressignificar
- Regulação muda radicalmente (LGPD vira lei mais dura, IA Act brasileiro)
- Nova categoria de produto domina (mentoria via IA agentic substitui mentoria humana)

### Critério 4 — Decisão estratégica do Conselho

**Régua:** Conselho da Soberana decide por unanimidade que é hora de v2, mesmo sem critério 1-3 batido. É opção, não obrigação.

Critério 4 é raro. Tata + 2-3 Imperatrizes precisam ver futuro que dado frio ainda não mostra.

---

## PROCESSO DE LANÇAMENTO DE v2 DA TRAVESSIA

### Etapa 0 — Decisão (Conselho da Soberana)

Reunião exclusiva. Decisão registrada em ata. Anúncio de "vamos pra v2" interno (Tata + time + Conselho), público só na etapa 4.

### Etapa 1 — Desenho de v2 (90-180 dias)

- Mapear o que muda (portas, pilares, nomes, lógicas)
- Mapear o que permanece (proteger fundação)
- Definir migração: o que mentorada antiga precisa fazer
- Atualizar manifesto da metodologia
- Validar com 5-10 mentoradas-imperatriz em "beta fechado"

### Etapa 2 — Plano de transição (60 dias antes do lançamento público)

Documento mestre de migração:

```markdown
# Travessia v1 → v2 — Plano de Transição

## O QUE MUDA NA v2
- [Lista das mudanças estruturais]
- [Mudança de nome de portas, se houver]
- [Novos pilares ou pilares fundidos]

## O QUE NÃO MUDA
- [Garantia de continuidade]
- [Fundamentos preservados]

## QUEM PRECISA MIGRAR
- Mentoradas que estão em portas afetadas
- Mentoradas que usam skills que mudaram lógica

## QUEM NÃO PRECISA MIGRAR
- Mentoradas que estão em portas não-afetadas
- Mentoradas que terminaram a Travessia (status concluído permanece v1)

## CALENDÁRIO DE TRANSIÇÃO
- [Data X-90]: anúncio público interno
- [Data X-60]: documentação v2 publicada
- [Data X-30]: workshop de migração ao vivo (gravado)
- [Data X]: v2 entra em vigor
- [Data X+90]: deadline migração obrigatória
- [Data X+180]: v1 sai do ar

## O QUE MENTORADA ANTIGA GANHA
- Acesso v2 sem custo extra
- Workshop de migração ao vivo (gravado também)
- Suporte 1:1 dedicado durante 60 dias
- Período de overlap de 6 meses (v1 + v2 disponíveis)

## O QUE MENTORADA NOVA RECEBE
- Direto v2, sem v1
- Treinamento atualizado
```

### Etapa 3 — Beta fechado (30-60 dias)

5-10 mentoradas-imperatriz testam v2 em paralelo a v1. Coletam feedback bruto. Ajustes finais antes do público.

### Etapa 4 — Lançamento público (data X)

- E-mail pra Corte
- Workshop ao vivo de migração
- Documentação v2 publicada
- Página pública atualizada
- Story / vídeo / post explicativos
- Comunicação clara: "v1 continua válida por 6 meses, transição não é urgência"

### Etapa 5 — Overlap (6 meses)

v1 e v2 rodam em paralelo. Mentorada escolhe quando migrar (ou termina v1 se já tava na reta final).

### Etapa 6 — Sunset v1 (X+180)

v1 sai do ar oficial. Mentoradas que ainda estão em v1 continuam atendidas individualmente até finalizarem a porta atual, mas próxima porta já é v2.

---

## CICLO DE VIDA DE SKILL INDIVIDUAL

### Estado 1 — Concepção

Skill ainda é ideia. Demanda detectada (Bloco 4 do rito ou pedido direto). Vai pro roadmap.

### Estado 2 — Em desenvolvimento

Skill sendo escrita. Não está disponível pra mentoradas. Marca: `IN_DEV` no manifesto.

### Estado 3 — Beta interno

Skill rodando, Tata testou em casos próprios, ainda não compartilhou. 1-3 semanas. Marca: `BETA`.

### Estado 4 — Lançada (v1.0)

Skill pública pra mentoradas. Entra no rito trimestral seguinte com primeira medição.

### Estado 5 — Madura

Skill com 6+ meses de uso, NPS estável, casos high-impact documentados. Recebe patches mas não refundação.

### Estado 6 — Em evolução pra v2

Skill madura recebeu pedidos validados de funcionalidade nova. v2 sendo escrita. v1 continua disponível.

### Estado 7 — v2 lançada

Nova versão maior pública. v1 continua disponível por 30-90 dias dependendo da skill.

### Estado 8 — Sunset

v1 sai do ar oficial. Só v2 (ou v3, etc) disponível.

### Estado 9 — Deprecada

Skill saiu do ecossistema. Funcionalidade absorvida por outra ou descontinuada. Marca: `DEPRECATED` no manifesto, código vai pra `~/imperio/evolucao/deprecadas/`.

---

## REGRAS DURAS DE VERSIONAMENTO

1. **Toda mudança v1 → v2 documenta breaking changes**, mesmo que pareça pequena
2. **Mentorada antiga sempre tem mínimo 30 dias** de aviso antes de breaking change entrar em vigor
3. **Travessia v2 sempre tem 6 meses de overlap** com v1
4. **Nunca remover funcionalidade sem substituto** declarado
5. **Sempre publicar nota de versão pública** pra Corte
6. **Sempre atualizar este documento** após `--versionar` ou rito trimestral
7. **Nunca pular versão** (não pode ir direto de v1.0 pra v3.0 — passa por v2)
8. **Nunca rebaixar versão** (skill não volta de v2 pra v1; se v2 tá ruim, vai pra v2.1 com fix)

---

## TABELA HISTÓRICA — TRAVESSIA

| Versão | Data lançamento | Mudanças principais | Status |
|--------|----------------|---------------------|--------|
| v1.0 | 2026-Q1 | Lançamento público. 26 portas A-Z, 6 pilares, ~225 skills | ATIVA |
| v1.1 | 2026-Q2 (projetado) | Refinamento de portas C-G após primeiro rito trimestral | PLANEJADA |
| v2.0 | 2027-Q? (projetada) | Critério de upgrade ainda não atingido | PROJETADA |

---

## TABELA HISTÓRICA — SKILLS (exemplos)

(Lista vai crescendo a cada `--versionar`. Apenas as primeiras entradas mostradas como template.)

| Skill | Versão | Data | Tipo | Mudança | Status |
|-------|--------|------|------|---------|--------|
| /headline-imperatriz | 1.0 | 2026-01-15 | MAJOR | Lançamento. 6 temperaturas | LANÇADA |
| /headline-imperatriz | 1.1 | 2026-02-20 | MINOR | Adicionou retargeting carrinho | ATIVA |
| /headline-imperatriz | 1.2 | 2026-03-10 | PATCH | Bugfix em scoring Bencivenga | ATIVA |
| /headline-imperatriz | 2.0 | 2026-Q3 (projetada) | MAJOR | Refundação com base quente + 8 temperaturas | PLANEJADA |
| /mecanismo-unico | 1.0 | 2026-01-20 | MAJOR | Lançamento. 23 critérios | LANÇADA |
| /voz-humana-br | 1.0 | 2026-02-05 | MAJOR | Lançamento. 500 palavras banidas | LANÇADA |
| /skill-X-velha | 1.0 | 2025-09-01 | MAJOR | Lançamento original | DEPRECATED 2026-Q2 |

---

## CHANGELOG INDIVIDUAL (template)

Toda vez que `--versionar [skill] [v]` é chamado, gera arquivo em `~/imperio/evolucao/changelogs/[skill]/v[X].md`:

```markdown
# /[nome-skill] — v2.0

**Data lançamento:** 2026-04-15
**Tipo:** MAJOR (breaking change)
**Versão anterior:** 1.2

---

## O QUE MUDOU

### Funcionalidade nova
- [Lista]

### Funcionalidade modificada (BREAKING)
- [Lista — destaca o que quebra]

### Funcionalidade removida
- [Lista]

### Bugs corrigidos
- [Lista]

---

## PLANO DE MIGRAÇÃO

### Quem precisa migrar
- Mentoradas que usavam [funcionalidade X]
- Mentoradas que dependiam de [output Y]

### O que precisa fazer
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

### Tempo estimado de migração
- 30 minutos por mentorada (média)

### Suporte
- Documentação: [link]
- Workshop ao vivo: [data]

---

## PRAZO DE TRANSIÇÃO

- v1.2 continua disponível até: 2026-05-15 (30 dias)
- A partir de 2026-05-16: só v2.0

---

## COMUNICAÇÃO PÚBLICA

[Texto curto pra publicar pra Corte]

---

## DOCUMENTOS RELACIONADOS

- SKILL.md atualizado: [versão]
- Arquivos de referência atualizados: [lista]
- Testes rodados: [lista]
```

---

## CONSELHO DA SOBERANA — DECISÕES SOBRE CICLO DE VIDA

Conselho decide:

- [ ] Lançar Travessia v2? (e quando)
- [ ] Aprovar plano de transição v1 → v2?
- [ ] Aprovar deprecação de skill estratégica?
- [ ] Aprovar fusão de skills core?
- [ ] Aprovar mudança de nomenclatura (porta, pilar, nível hierárquico)?

Conselho NÃO decide:
- Patch incremental de skill (Tata + time)
- Minor de skill (Tata + time)
- Major de skill não-estratégica (Tata + time, registra na ata seguinte)

---

**Ciclo de Vida Imperatriz — propriedade Tata Gonçalves.**
**Documento vivo, atualizado a cada rito trimestral e cada `--versionar`.**
