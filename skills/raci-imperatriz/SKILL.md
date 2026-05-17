---
name: raci-imperatriz
description: >
  Motor de execucao da Travessia Imperatriz — define QUEM faz cada skill em cada
  uma das 26 portas (A-Z) do imperio digital da mentorada. Aplica matriz RACI
  (Responsavel, Aprovador, Consultado, Informado) entre 5 atores (Mentorada,
  Time da mentorada, Agente IA, Tata + time, Terceirizado) e estima TEMPO
  (Iniciante x Avancada) + CUSTO (faixa em R$) por porta. Customiza a
  distribuicao por perfil lendo dossie-mentorada (recursos, time, orcamento,
  habilidades). Quatro modos: --gerar (RACI da porta), --orcamento (soma
  custos das proximas portas), --cronograma (timeline com tempos), --ajustar
  (recalcula com mais/menos recursos). Pilar 3 (Execucao) da Travessia
  Imperatriz Tata Goncalves. Use quando a mentorada perguntar "quem faz o
  que", "quanto tempo demora", "quanto custa", "como executar a porta X",
  "tenho time pra isso?", "posso terceirizar?", "qual o cronograma da
  travessia", "como dividir trabalho com agente IA", "preciso contratar
  alguem?". Integra com dossie-mentorada (input) e tatou-2.0 (handoff de
  execucao). Metodo Imperatriz de Execucao — propriedade Tata Goncalves.
---

# RACI Imperatriz — Pilar 3 da Travessia Imperatriz

Esta skill e o **motor de execucao** da Travessia Imperatriz. Enquanto a `tatou-2.0` decide ONDE a mentorada esta e PRA ONDE ela vai, a `raci-imperatriz` decide **QUEM faz, QUANTO TEMPO leva e QUANTO CUSTA** cada movimento.

## Filosofia central

> **Estrategia sem execucao e fantasia. Execucao sem RACI vira gargalo na mentorada.**

Toda mentorada que trava na Travessia trava por uma razao operacional: nao sabe distinguir o que ELA faz, o que o TIME faz, o que o AGENTE IA faz, o que a TATA orienta e o que precisa TERCEIRIZAR. RACI Imperatriz resolve isso porta-a-porta.

## Quando usar

- Mentorada esta prestes a entrar numa nova porta (ex: vai construir Porta H — Site)
- Mentorada esta travada porque "nao tem tempo" — sintoma classico de R mal alocado
- Mentorada quer planejar trimestre/semestre — precisa de cronograma + orcamento
- Mentorada esta contratando time e quer saber pra onde alocar
- Mentorada esta avaliando terceirizar (designer, dev, copywriter, social media)
- Tata quer auditar se mentorada esta fazendo coisa que deveria delegar
- Antes de rodar `/tatou-2.0` quando a duvida e operacional, nao estrategica

## Os 5 atores (definidos em ordem de prioridade)

### 1. Mentorada — Decisao estrategica + validacao final
- O que SO ela pode fazer: posicionamento, mecanismo unico (input bruto), historia pessoal, decisao de oferta, validacao de copy final, calls 1:1 high-ticket, voz de marca
- Carga ideal por porta: 2-8h/semana de trabalho focado dela mesmo
- Sinal de alerta: se ela esta como R em mais de 4 skills da mesma porta, esta sobrecarregada

### 2. Time da mentorada — Operacional humano
- Perfis tipicos: assistente executiva, social media, gestor de trafego in-house, atendente, editor de video
- O que faz: tarefas que precisam de julgamento humano mas nao precisam ser dela
- Quando aparece: a partir de Porta F-G (mentorada ja faturando 30k+/mes)
- Custo: R$2.000-15.000/mes por pessoa CLT/PJ

### 3. Agente IA — Tarefa repetitiva, padronizavel
- O que faz: gera variacoes (headlines, copy, posts), audita, transcreve, organiza, pesquisa, sumariza
- O que NAO faz: decisao final, voz de marca sem treino, pitch high-ticket, atendimento humanizado
- Carga: 70-80% da carga de copy/conteudo pode ir pra ele
- Custo: R$0-500/mes em APIs (Claude, Gemini, GPT, ferramentas)

### 4. Tata + time — Suporte estrategico via mentoria
- O que faz: orientacao 1:1, validacao de mecanismo, revisao de oferta, desbloqueio de gargalo, calls de imersao
- Quando aparece como C ou A: skills proprietarias da Tata (mecanismo-unico, headline-imperatriz, briefing-copy-360, imperatriz-das-vendas, reuniao-de-resultado)
- Custo: ja embutido na mentoria — nao soma como custo extra

### 5. Terceirizado — Designer, dev, copywriter, editor, gestor de trafego freelancer
- Quando aparece: skills que exigem habilidade tecnica que mentorada+time+agente nao cobrem
- Tipicos: designer (R$500-5.000 por projeto), dev (R$3.000-30.000 por entrega), copywriter senior (R$3.000-20.000 por funil), editor de video (R$500-5.000 por VSL), gestor de trafego (R$2.000-10.000/mes + % ads)
- Regra: terceirizar quando custo/hora dela pra fazer > custo do terceirizado + supervisao

---

## RACI — definicoes operacionais (sem ambiguidade)

- **R (Responsavel)** — quem coloca a mao na massa e entrega o output. Pode ser mais de um se for trabalho conjunto.
- **A (Aprovador)** — quem assina embaixo. SEMPRE 1 unico aprovador por skill (regra dura RACI). Quase sempre e a Mentorada em decisoes estrategicas, ou um delegado claro.
- **C (Consultado)** — quem opina ANTES da entrega. Comunicacao bidirecional.
- **I (Informado)** — quem sabe DEPOIS da entrega. Comunicacao unidirecional.

Regra: toda skill tem **exatamente 1 R principal + 1 A unico**. C e I podem ser zero, um ou varios.

---

## MODOS DE OPERACAO

A skill roda em 4 modos declaraveis:

- **`/raci-imperatriz --gerar [nome] [porta]`** — gera matriz RACI customizada da porta pra mentorada especifica
- **`/raci-imperatriz --orcamento [nome]`** — soma custos das proximas N portas no roadmap dela
- **`/raci-imperatriz --cronograma [nome]`** — timeline visual das proximas portas com tempo estimado
- **`/raci-imperatriz --ajustar [nome] [recursos]`** — recalcula RACI/tempo/custo com mais ou menos recursos

Se usuario nao declarar modo, perguntar **"qual modo: gerar, orcamento, cronograma ou ajustar?"**.

---

## PROCESSO — 7 FASES OBRIGATORIAS

### FASE 0 — Leitura do dossie-mentorada

Antes de qualquer coisa, ler `dossie-mentorada/[nome]/perfil.md` (ou pedir input se nao existir).

Extrair:
- Nivel atual (Iniciante / Intermediaria / Avancada)
- Faturamento mensal (definir orcamento realista)
- Time atual (lista de pessoas + funcoes)
- Habilidades dela (ela mesma escreve copy? edita video? roda ads?)
- Ferramentas que ja paga
- Stack de skills/agentes IA ja instalados
- Portas ja concluidas (A-Z)
- Porta atual + proximas portas no roadmap

Se dossie nao existe, rodar `/dossie-mentorada` ANTES.

### FASE 1 — Identificar porta(s) alvo

Se usuario passou porta especifica (ex: "porta H"), usar ela.
Se usuario nao passou, ler dossie e sugerir as 1-3 proximas portas no roadmap.

### FASE 2 — Listar skills que rodam na porta

Cada porta tem um conjunto canonico de skills. Ver `MATRIZES-RACI-26-PORTAS.md` pra mapa completo.

Exemplo Porta J (Jornada de Copy):
- briefing-copy-360
- mecanismo-unico
- headline-imperatriz
- voz-humana-br
- skill-pagina-vendas / design-page-builder
- bencivenga-method
- analise-anuncio-1000

### FASE 3 — Aplicar matriz RACI base + customizar

Pra cada skill da porta:

1. Pegar RACI **base** (template padrao da skill na matriz)
2. Customizar de acordo com perfil da mentorada:
   - Se ela nao tem time → tarefas que iriam pro time vao pra ela ou pro agente IA
   - Se ela e iniciante e nao tem dinheiro → terceirizado vira agente IA + ela revisa
   - Se ela e avancada com time grande → ela sai como R em quase tudo, vira so A
3. Aplicar regra: 1 R principal + 1 A unico por skill

### FASE 4 — Estimar tempo

Aplicar tabela base (ver `TEMPO-ESTIMADO-DETALHADO.md`) ajustada por:
- Nivel da mentorada (Iniciante = +50% no tempo base)
- Tem time? (pode rodar paralelo, divide)
- Tem skills/agentes? (corta tempo de copy/conteudo em 60-80%)

Entregar: tempo total da porta + breakdown por skill + dependencias (o que precisa terminar antes do que).

### FASE 5 — Estimar custo

Somar custos por skill:
- Custo de ferramentas/APIs (recorrente mensal)
- Custo de terceirizados (one-shot ou recorrente)
- Custo de tempo do time (hora x quantas horas)

Entregar 3 cenarios:
- **Mochila** (mais barato possivel — DIY + agente IA)
- **Realista** (mistura R e A entre todos os 5 atores)
- **Premium** (terceiriza tudo terceirizavel + mentorada so valida)

### FASE 6 — Identificar gargalos

Sinalizar:
- Mentorada como R em 5+ skills da mesma porta = sobrecarga
- Mentorada como R em skill que poderia ser do agente IA = desperdicio
- A unico mal definido (mais de 1 pessoa decidindo) = trava
- Skills sem nenhum C estrategico = risco de retrabalho
- Custo > 30% do faturamento mensal = inviavel financeiramente

### FASE 7 — Output estruturado

Ver formato abaixo conforme o modo (gerar / orcamento / cronograma / ajustar).

---

## FORMATO DE OUTPUT

### Modo `--gerar [nome] [porta]`

```
# RACI — [NOME MENTORADA] — PORTA [X] ([NOME PORTA])

## CONTEXTO
- **Nivel:** [Iniciante / Intermediaria / Avancada]
- **Faturamento:** R$ [X]/mes
- **Time atual:** [lista]
- **Skills instaladas:** [lista]
- **Tempo estimado total:** [X semanas / dias]
- **Custo estimado:** R$ [X] (cenario realista)

---

## MATRIZ RACI

| Skill | R (Responsavel) | A (Aprovador) | C (Consultado) | I (Informado) |
|-------|-----------------|---------------|----------------|---------------|
| skill-1 | [ator] | [ator] | [atores] | [atores] |
| skill-2 | [ator] | [ator] | [atores] | [atores] |
[...]

---

## TEMPO POR SKILL

| Skill | Tempo dedicado (horas) | Janela calendarica | Quem bloqueia (dep.) |
|-------|------------------------|--------------------|-----------------------|
| skill-1 | Xh | dia 1-3 | — |
| skill-2 | Xh | dia 4-7 | skill-1 |
[...]

**Total porta:** X semanas | X horas focadas

---

## CUSTO POR SKILL

| Skill | One-shot | Recorrente/mes | Quem paga |
|-------|----------|----------------|-----------|
| skill-1 | R$ X | R$ X | mentorada |
| skill-2 | R$ X | — | mentorada |
[...]

**Total porta:** R$ X one-shot + R$ X/mes

---

## GARGALOS DETECTADOS
[Lista de avisos se houver]

## RECOMENDACAO DE EXECUCAO
[Ordem ideal de execucao das skills + onde paralelizar]

## HANDOFF PARA TATOU-2.0
[Sinal de quando porta esta pronta pra avancar]
```

### Modo `--orcamento [nome]`

```
# ORCAMENTO TRAVESSIA — [NOME MENTORADA]

## PROXIMAS [N] PORTAS

| Porta | Nome | Tempo | Custo one-shot | Custo recorrente |
|-------|------|-------|----------------|------------------|
| H | Site | 2 sem | R$ 1.500 | R$ 80/mes |
| I | Conteudo | 30 dias | R$ 0 | R$ 200/mes |
| J | Copy | 2 sem | R$ 2.500 | R$ 100/mes |
[...]

## TOTAL
- **One-shot:** R$ X
- **Recorrente:** R$ X/mes (apos ramp-up)
- **Janela:** X semanas

## CENARIOS
- **Mochila:** R$ X (faz quase tudo com agente IA + DIY)
- **Realista:** R$ X (mix recomendado)
- **Premium:** R$ X (terceiriza maximo possivel)

## RECOMENDACAO
[Cenario sugerido + por que]
```

### Modo `--cronograma [nome]`

```
# CRONOGRAMA TRAVESSIA — [NOME MENTORADA]

## TIMELINE [X] SEMANAS

Semana 1-2: [Porta H] — Site
  - Skills: design-page-builder, skill-deploy-vps
  - Marco: site no ar

Semana 3-6: [Porta I] — Conteudo
  - Skills: skill-carrossel-instagram, voz-humana-br
  - Marco: 30 posts publicados

[...]

## DEPENDENCIAS CRITICAS
- Porta J nao pode comecar antes de Porta H
- Porta K precisa de Porta J + budget liberado

## MILESTONES DE VALIDACAO TATA
- Semana 2: validar copy do site
- Semana 6: revisao de mecanismo unico
[...]
```

### Modo `--ajustar [nome] [recursos]`

```
# RACI AJUSTADA — [NOME MENTORADA]

## RECURSOS NOVOS DECLARADOS
- [+/- contratacao]
- [+/- orcamento]
- [+/- skill instalada]

## IMPACTO NO PLANO

### Antes
- Tempo: X | Custo: R$ X | Mentorada como R em [N] skills

### Depois
- Tempo: X | Custo: R$ X | Mentorada como R em [N] skills

## REALOCACOES PROPOSTAS
[Lista de skills que mudaram de ator]

## PROXIMOS PASSOS
[O que fazer pra implementar a nova alocacao]
```

---

## REGRAS DURAS (a skill NAO negocia)

1. **Sempre 1 unico A** por skill — nao existe co-aprovacao em RACI bem feita
2. **Mentorada nunca e R em mais de 4 skills** da mesma porta sem alerta de sobrecarga
3. **Skills proprietarias da Tata** (mecanismo-unico, briefing-copy-360, imperatriz-das-vendas, reuniao-de-resultado) sempre tem Tata como C, no minimo
4. **Decisao de oferta, preco e posicionamento** — A e SEMPRE a Mentorada, nao terceirizavel
5. **Voz de marca final** — A sempre da Mentorada, nunca do agente IA
6. **Calls high-ticket de fechamento** — R sempre da Mentorada (ou closer humano), nunca do agente IA
7. **Custo total da porta nao pode passar 30% do faturamento mensal** sem alerta de risco
8. **Tempo total da porta nao pode comprimir abaixo do minimo Avancada** — fisicamente impossivel
9. **Sempre le dossie-mentorada antes** — nao gera RACI generica sem perfil
10. **Sempre passa handoff pra tatou-2.0** ao final — nao deixa orfao
11. **Nao recomenda terceirizar** habilidades que sao parte do mecanismo unico da mentorada (autoridade pessoal)
12. **Sempre sinaliza** quando mentorada esta executando algo que deveria delegar pro agente IA

---

## ARQUIVOS DE REFERENCIA (carregar sob demanda)

- `MATRIZES-RACI-26-PORTAS.md` — RACI base de todas as 26 portas A-Z
- `TEMPO-ESTIMADO-DETALHADO.md` — tabela de tempo Iniciante x Avancada por porta
- `CUSTO-ESTIMADO-DETALHADO.md` — tabela de custo por porta com cenarios
- `EXEMPLOS-CASOS.md` — 3 casos completos (Iniciante / Intermediaria / Avancada)

---

## INTEGRACAO COM ECOSSISTEMA TATA

**Fluxo de execucao da Travessia:**

```
/dossie-mentorada              (input — quem ela e, o que tem)
       ↓
/tatou-2.0                     (estrategia — onde ela esta, pra onde vai)
       ↓
/raci-imperatriz  ← VOCE ESTA AQUI
       ↓
   execucao real
       ↓
/reuniao-de-resultado          (revisao de execucao com time)
       ↓
loop continuo
```

**Skills adjacentes:**
- `/perfil-mentorada` — define perfil arquetipico
- `/anamnese-mentorada` — diagnostico inicial profundo
- `/gates-imperatriz` — define criterios de aprovacao das portas
- `/voz-de-marca-builder` — alimenta voz que mentorada usa em skills

---

## VERSIONAMENTO

- **v1.0** (atual) — 26 portas, 5 atores, 4 modos, integracao dossie + tatou
- **v1.5** (planejado) — historico de execucao real (medio tempo + custo observados)
- **v2.0** (planejado) — auto-deteccao de gargalo via reuniao-de-resultado

---

## COMO COMPARTILHAR COM MENTORANDAS

Copiar pasta `/Users/tamiresgoncalves/Documents/travessia-imperatriz-site/skills-novas/raci-imperatriz/` pra `~/.claude/skills/` da mentorada.

Skill vira disponivel via `/raci-imperatriz`.

Ver `README.md` pra instrucoes completas.

---

**Metodo Imperatriz de Execucao — propriedade intelectual Tata Goncalves.**
