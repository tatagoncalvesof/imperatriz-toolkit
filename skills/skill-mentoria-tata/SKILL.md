---
name: skill-mentoria-tata
description: >
  Gerar estruturas completas de cursos, programas de mentoria, planos de aula,
  checklists de lancamento e estrategias de engajamento para o Instituto Tata Goncalves.
  Usar quando a usuaria mencionar: mentoria, curso, modulo, aula, plano de aula,
  checklist de lancamento, estrutura de curso, programa de mentoria, trilha de aprendizado,
  avaliacao de alunos, comunidade de alunos, engajamento, lancamento digital, produto digital,
  Hotmart, plataforma de ensino, conteudo educacional.
---

# Skill Mentoria Tata — Instituto Tata Goncalves

## Visao Geral

Criar estruturas profissionais de cursos online, programas de mentoria, planos de aula
detalhados, checklists de lancamento digital e estrategias de engajamento de alunos
para o Instituto Tata Goncalves. Todos os outputs em Portugues Brasileiro, alinhados
ao mercado de infoprodutos e educacao digital no Brasil.

## Arvore de Decisao

Identificar o que a usuaria precisa e seguir o fluxo correspondente:

```
Pedido da Tata
|
|-- "estrutura de curso" / "modulos" / "trilha"
|   --> Fluxo 1: Estrutura de Curso
|
|-- "plano de aula" / "aula" / "conteudo da aula"
|   --> Fluxo 2: Plano de Aula
|
|-- "lancamento" / "checklist" / "pre-lancamento"
|   --> Fluxo 3: Checklist de Lancamento
|
|-- "engajamento" / "comunidade" / "retencao"
|   --> Fluxo 4: Engajamento de Alunos
|
|-- "avaliacao" / "prova" / "exercicio" / "certificado"
|   --> Fluxo 5: Framework de Avaliacao
|
|-- "mentoria" / "programa de mentoria" / "grupo de mentoria"
|   --> Fluxo 6: Programa de Mentoria
```

---

## Fluxo 1: Estrutura de Curso

Carregar `references/templates-modulos.md` para templates detalhados.

### Etapas

1. Perguntar o tema central do curso e o publico-alvo (se nao informados)
2. Definir o nivel: iniciante, intermediario ou avancado
3. Gerar a estrutura com 6 a 12 modulos seguindo o formato padrao:
   - Nome do modulo
   - Objetivo de aprendizado (1 frase clara)
   - Topicos principais (3-5 por modulo)
   - Entregavel do modulo (exercicio, template, checklist)
   - Duracao estimada
4. Incluir modulo de boas-vindas/onboarding no inicio
5. Incluir modulo de encerramento/proximos passos no final
6. Organizar em trilha progressiva: fundamentos --> pratica --> avancado --> implementacao

### Formato de Saida

```markdown
# [Nome do Curso]
**Publico-alvo:** [descricao]
**Nivel:** [iniciante/intermediario/avancado]
**Duracao total:** [X semanas]
**Plataforma:** Hotmart

## Modulo 1: [Nome]
**Objetivo:** [O que o aluno sera capaz de fazer ao final]
**Topicos:**
1. [Topico 1]
2. [Topico 2]
3. [Topico 3]
**Entregavel:** [Exercicio pratico / Template / Checklist]
**Duracao:** [X horas]

[...repetir para cada modulo...]
```

---

## Fluxo 2: Plano de Aula

Carregar `references/templates-aulas.md` para templates detalhados.

### Etapas

1. Identificar o modulo e topico da aula
2. Definir objetivo de aprendizado especifico (usar verbos de acao: aplicar, criar, analisar, implementar)
3. Estruturar a aula no formato padrao:
   - Abertura (gancho + conexao com aula anterior)
   - Conteudo teorico (conceitos-chave, maximo 3)
   - Demonstracao pratica (exemplo real ou estudo de caso)
   - Exercicio do aluno (atividade hands-on)
   - Fechamento (resumo + call-to-action)
4. Incluir roteiro para gravacao de video (se solicitado)
5. Incluir materiais complementares: PDF, template, checklist

### Formato de Saida

```markdown
# Plano de Aula: [Titulo]
**Modulo:** [X] | **Aula:** [Y]
**Duracao:** [X minutos]
**Objetivo:** Ao final desta aula, o aluno sera capaz de [verbo de acao + resultado]

## 1. Abertura (3-5 min)
- Gancho: [pergunta ou afirmacao provocativa]
- Conexao: [link com aula anterior]
- Promessa: [o que o aluno vai aprender hoje]

## 2. Conteudo (10-15 min)
### Conceito 1: [Nome]
[Explicacao clara e direta]

### Conceito 2: [Nome]
[Explicacao clara e direta]

## 3. Demonstracao (5-10 min)
[Exemplo pratico, estudo de caso ou passo-a-passo]

## 4. Exercicio Pratico (10-15 min)
**Instrucoes:** [passo-a-passo claro]
**Entregavel:** [o que o aluno deve produzir]

## 5. Fechamento (3-5 min)
- Resumo dos 3 pontos principais
- Tarefa para proxima aula
- CTA: [acao especifica]

## Materiais Complementares
- [ ] PDF da aula
- [ ] Template: [nome]
- [ ] Checklist: [nome]
```

---

## Fluxo 3: Checklist de Lancamento

Carregar `references/checklist-lancamento.md` para o checklist completo.

### Etapas

1. Identificar o tipo de lancamento:
   - **Lancamento Semente** (primeiro lancamento, lista pequena)
   - **Lancamento Interno** (para lista propria)
   - **Lancamento Externo** (com afiliados)
   - **Lancamento Perpetuo** (evergreen/automatizado)
2. Definir a data de abertura do carrinho
3. Gerar checklist completo com 3 fases:
   - Pre-lancamento (60-30 dias antes)
   - Lancamento (7 dias de carrinho aberto)
   - Pos-lancamento (30 dias apos)
4. Incluir timeline com datas especificas
5. Incluir templates de copy para cada etapa

### Fases Resumidas

**Pre-Lancamento (60-30 dias):**
- Pesquisa de mercado e validacao
- Criacao de conteudo de aquecimento
- Setup tecnico (Hotmart, paginas, emails)
- Sequencia de antecipacao (CPL 1, 2, 3)

**Lancamento (7 dias):**
- Abertura de carrinho + emails
- Lives de vendas
- Gestao de objecoes
- Fechamento com escassez real

**Pos-Lancamento (30 dias):**
- Onboarding de alunos
- Pesquisa de satisfacao
- Analise de metricas
- Planejamento do proximo lancamento

---

## Fluxo 4: Engajamento de Alunos

Carregar `references/engajamento-alunos.md` para estrategias detalhadas.

### Etapas

1. Identificar o formato do produto (curso gravado, mentoria ao vivo, hibrido)
2. Mapear os pontos criticos de abandono
3. Gerar plano de engajamento com:
   - Onboarding dos primeiros 7 dias
   - Gamificacao e marcos de progresso
   - Comunidade (WhatsApp/Telegram/Discord)
   - Encontros ao vivo periodicos
   - Sistema de accountability (parceiros/grupos)
4. Incluir templates de mensagens para cada momento
5. Definir metricas de acompanhamento

### Metricas-Chave

| Metrica | Meta Ideal | Alerta |
|---------|-----------|--------|
| Taxa de acesso em 48h | > 80% | < 50% |
| Conclusao do Modulo 1 | > 70% | < 40% |
| Conclusao total do curso | > 30% | < 15% |
| Participacao em lives | > 40% | < 20% |
| NPS | > 8.0 | < 7.0 |

---

## Fluxo 5: Framework de Avaliacao

### Etapas

1. Definir o tipo de avaliacao:
   - **Diagnostica** (antes do curso — mapear nivel)
   - **Formativa** (durante — exercicios por modulo)
   - **Somativa** (final — projeto ou prova)
   - **Autoavaliacao** (reflexao do aluno)
2. Criar rubrica de avaliacao com criterios claros
3. Gerar templates de exercicios praticos
4. Definir criterios para certificado de conclusao

### Formato de Rubrica

```markdown
## Rubrica de Avaliacao: [Nome do Exercicio]

| Criterio | Insuficiente (0-2) | Bom (3-4) | Excelente (5) |
|----------|-------------------|-----------|---------------|
| [Criterio 1] | [descricao] | [descricao] | [descricao] |
| [Criterio 2] | [descricao] | [descricao] | [descricao] |
| [Criterio 3] | [descricao] | [descricao] | [descricao] |

**Nota minima para aprovacao:** 3.0
**Peso na nota final:** X%
```

---

## Fluxo 6: Programa de Mentoria

### Etapas

1. Definir o formato da mentoria:
   - **Individual** (1:1, alto ticket)
   - **Grupo** (5-20 pessoas, ticket medio)
   - **Mastermind** (pares avancados, alto ticket)
2. Estruturar a jornada do mentorado:
   - Diagnostico inicial (formulario + call)
   - Plano de acao personalizado
   - Encontros periodicos (semanal/quinzenal)
   - Suporte assincrono (WhatsApp/Voxer)
   - Avaliacao de progresso mensal
3. Gerar framework de sessao de mentoria:
   - Check-in (5 min): como foi a semana, vitoria principal
   - Revisao de metas (10 min): o que foi feito vs planejado
   - Topico principal (20 min): ensino + coaching
   - Plano de acao (10 min): proximos passos concretos
   - Fechamento (5 min): compromisso e accountability
4. Definir criterios de resultado e KPIs do programa

### Formato de Sessao

```markdown
## Sessao de Mentoria #[numero]
**Data:** [data] | **Mentorado:** [nome]
**Formato:** [Individual/Grupo]

### Check-in
- Vitoria da semana:
- Maior desafio:

### Revisao de Metas
| Meta | Status | Observacao |
|------|--------|-----------|
| [meta 1] | [concluida/em andamento/bloqueada] | |
| [meta 2] | [concluida/em andamento/bloqueada] | |

### Topico Principal
[Notas do ensino/coaching]

### Plano de Acao (proxima semana)
1. [ ] [acao 1] — prazo: [data]
2. [ ] [acao 2] — prazo: [data]
3. [ ] [acao 3] — prazo: [data]

### Compromisso
[O que o mentorado se comprometeu a fazer]
```

---

## Diretrizes de Conteudo

### Tom de Voz

- Usar linguagem acessivel, direta e motivacional
- Tratar o aluno como "voce" (nunca "tu" ou "senhor/senhora")
- Incluir exemplos praticos do dia a dia do empreendedor brasileiro
- Evitar jargoes academicos — preferir linguagem do mercado digital
- Usar perguntas retoricas para engajar

### Estrutura de Conteudo

- Sempre comecar com o "por que" (motivacao) antes do "como" (tecnica)
- Limitar conceitos teoricos a 3 por aula
- Incluir pelo menos 1 exemplo pratico por conceito
- Fechar cada secao com acao concreta (nao deixar no abstrato)
- Usar analogias do cotidiano brasileiro

### Padroes Hotmart

- Organizar modulos em ordem sequencial com desbloqueio progressivo
- Incluir material complementar em PDF para cada modulo
- Prever aulas bonus para aumentar valor percebido
- Incluir modulo de FAQ com duvidas frequentes
- Considerar area de membros com comunidade integrada

## Referencias

Consultar os arquivos em `references/` para conteudo detalhado:

- **`references/templates-modulos.md`** — Templates completos para estruturas de modulos (6-12 modulos), com exemplos para diferentes nichos
- **`references/templates-aulas.md`** — Templates de planos de aula com objetivos, conteudo, exercicios e roteiros de gravacao
- **`references/checklist-lancamento.md`** — Checklist completo de lancamento digital em 3 fases (pre, durante, pos) com timelines e copy
- **`references/engajamento-alunos.md`** — Estrategias de engajamento, retencao, comunidade e gamificacao para cursos online
