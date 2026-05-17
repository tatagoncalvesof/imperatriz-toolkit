---
name: dashboard-imperatriz
description: >
  Operador do Pilar 4 (Medição) da Travessia Imperatriz da Tata Gonçalves.
  Agrega KPIs primários por porta (26 portas A-Z) por mentorada, gera
  alertas de cor (verde/amarelo/vermelho) com regra de priorização e
  entrega 2 dashboards HTML interativos: visão Tata (Corte inteira) e
  visão mentorada (individual). Cruza com `dossie-mentorada` (profile
  16-kpis-dashboard), alimenta `tatou-2.0` (decisões de despacho) e
  bate com `gates-imperatriz` (status de saída). Roda mensalmente
  automatizado. Quatro modos: --tata (Corte agregada), --mentorada
  [nome] (individual), --alertas (só vermelhos urgentes),
  --prontas-investidura (quem sobe nível). Não escreve copy, não cria
  oferta, não ensina porta — só mede: porta verde, amarela ou
  vermelha? KPI bateu benchmark BR mentora high-ticket? mentorada
  pronta pra próxima Investidura? Use quando a Tata ou mentorada pedir
  "dashboard", "KPIs", "como tá a Corte", "quem precisa atenção",
  "quem tá pronta pra subir", "alertas", "métricas do mês",
  "agregado da Corte", "minha porta tá verde?", "benchmarks".
  Gatilhos: dashboard imperatriz, KPI travessia, alertas mentorada,
  visão Corte, prontas Investidura, medição travessia, benchmark
  mentora high-ticket, dashboard tata, dashboard mentorada, métricas
  porta, status portas, KPI vermelho, KPI verde.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Dashboard Imperatriz — Operador do Pilar 4 (Medição) da Travessia

Skill que mede tudo que a Travessia Imperatriz exige medir. 26 KPIs primários (1 por porta A-Z), benchmark BR mentora high-ticket, regra de cor por gate, agregação Corte inteira + visão individual da mentorada. HTML interativo + JSON pra integração.

Não é a metodologia. É o medidor da metodologia. As outras skills executam; esta marca o placar.

## Filosofia central

**"Sem KPI por fase, mentorada acha que andou."**

A Travessia tem 26 portas. Cada porta tem um KPI primário. Sem KPI declarado e medido, a mentorada confunde movimento com progresso, esforço com resultado, achismo com gate fechado.

1. **KPI por porta é absoluto.** Toda porta A-Z tem 1 indicador primário mensurável. Se não tem número, não tem porta — tem aspiração.
2. **Benchmark BR mentora high-ticket é a régua.** Não comparamos com SaaS americano. Não comparamos com infoproduto low-ticket. A régua é mentoria/consultoria/curso premium no Brasil — o que a Tata e as mentoradas vivem.
3. **Cor é binária por dentro: ou bate ou não bate.** Verde = bateu/superou benchmark. Amarelo = está dentro de 70-99% do benchmark (perto, mas não chegou). Vermelho = abaixo de 70% ou ausente.
4. **Alerta vermelho é prioridade absoluta.** Antes de aprovar avanço, antes de planejar lançamento, antes de pensar em Investidura — vermelho fecha. Skill devolve essa lógica sem negociar.
5. **Visão Tata vê tudo. Visão mentorada vê só ela.** Privacidade entre mentoradas. A Tata cruza Corte inteira pra decidir despacho; a mentorada só vê o próprio painel.
6. **Mensal é o ciclo padrão.** Roda dia 1 do mês com dado fechado do mês anterior. Mentorada vê o mês fechado, Tata vê o agregado.
7. **Pronta pra Investidura é critério, não promoção.** Subir nível hierárquico (Iniciada → Cortesã → Dama → Imperatriz) só com KPI verde nas portas que aquele nível exige. Sem subjetividade.

## Quando usar

- Tata abre call mensal de Corte e precisa ver quem está verde/amarelo/vermelho
- Mentorada quer ver o painel dela antes de pedir avanço pra próxima porta
- Tata vai decidir quem despacha pra próxima Investidura no trimestre
- Mentorada tem dúvida se KPI dela bate benchmark
- Tata quer saber receita agregada da Corte do mês
- Mentorada quer histórico de progresso dos últimos 3-6 meses
- Tata quer cases prontos pra documentar (KPIs verdes consistentes 3+ meses)
- Antes de chamar `/tatou-2.0` pra mandar próximo passo — esta skill traz o status real

## Quando NÃO usar

- Mentorada quer aprender o que é uma porta (chama Travessia direto)
- Tata quer escrever copy, criar oferta, montar funil (chama skill específica)
- Mentorada nunca rodou Travessia — não tem KPI pra agregar (chama `/anamnese-mentorada`)
- Tata quer auditar gate específico — esta skill mede, `/gates-imperatriz` audita

---

## MODOS DE OPERAÇÃO

A skill roda em 4 modos declaráveis:

- **`/dashboard-imperatriz --tata`** — visão geral da Corte inteira: lista todas as mentoradas, status visual por porta, quem precisa intervenção urgente, quem está pronta pra próxima Investidura, cases prontos, receita agregada
- **`/dashboard-imperatriz --mentorada [nome]`** — visão individual: porta atual + KPIs, próximo gate + critério, próximo passo recomendado pelo `/tatou-2.0`, histórico de progresso, distância pra próximo nível hierárquico
- **`/dashboard-imperatriz --alertas`** — só os KPIs vermelhos urgentes da Corte inteira, ordenados por gravidade (porta upstream contaminada > porta atual travada > ciclo recorrente vencido)
- **`/dashboard-imperatriz --prontas-investidura`** — quem está pronta pra subir nível hierárquico (Iniciada → Cortesã → Dama → Imperatriz), com checklist verde validado

Modo padrão (sem flag): pergunta qual operação a Tata quer rodar.

---

## INPUT ESPERADO

A skill busca contexto na seguinte ordem:

1. **Dossiê de cada mentorada** (de `/dossie-mentorada` profile `16-kpis-dashboard`): KPIs declarados, métricas registradas, datas
2. **Status de gates** (de `/gates-imperatriz`): qual porta cada uma está, quais já passaram
3. **Argumentos do comando**: nome da mentorada (modo individual) ou flag de modo
4. **Pergunta direta**: se faltar dado de KPI, pergunta qual mês está sendo medido

Se não tem dossiê preenchido na seção `16-kpis-dashboard`, a skill avisa: "rode `/dossie-mentorada` profile 16-kpis-dashboard primeiro pra eu medir com base real". Não invento KPI.

---

## PROCESSO POR MODO

### MODO `--tata`

**Fase 1.** Lê dossiê de cada mentorada (16-kpis-dashboard).

**Fase 2.** Para cada mentorada, calcula cor de cada porta (regras em `ALERTAS-LOGICA.md`).

**Fase 3.** Agrega: total verde, total amarelo, total vermelho por mentorada + por porta (qual porta é o gargalo da Corte).

**Fase 4.** Identifica:
- Quem precisa intervenção urgente (≥3 vermelhos OU vermelho em porta upstream A-D)
- Quem está pronta pra próxima Investidura (ver `--prontas-investidura`)
- Cases prontos (3+ meses verde consistente em portas K-N-Q)
- Receita agregada da Corte (soma de Q/Y de todas mentoradas no mês)

**Fase 5.** Gera dashboard HTML (visão Tata, layout em `VISAO-TATA.md`) + JSON.

**Output:**

```
# DASHBOARD CORTE — [Mês/Ano]

## Resumo
- Mentoradas ativas: [N]
- Receita agregada: R$ [X]
- Verde geral: [%]
- Vermelho geral: [%]

## Tabela mentorada × porta (cor por célula)
[matriz 26 portas × N mentoradas]

## Atenção urgente ([N])
- [Mentorada 1] — [porta][cor] — [razão]

## Prontas pra Investidura ([N])
- [Mentorada 2] — sobe pra [nível]

## Cases prontos pra documentar ([N])
- [Mentorada 3] — [porta][KPI] verde 3+ meses

## Arquivo
~/Documents/Obsidian Vault/03 - Projetos/Dashboard-Corte/[YYYY-MM]/dashboard-tata.html
~/Documents/Obsidian Vault/03 - Projetos/Dashboard-Corte/[YYYY-MM]/dashboard-tata.json
```

### MODO `--mentorada [nome]`

**Fase 1.** Lê dossiê da mentorada nomeada.

**Fase 2.** Identifica porta atual (`/gates-imperatriz`).

**Fase 3.** Calcula cor de cada porta (todas 26, mostrando histórico).

**Fase 4.** Calcula distância pra próximo nível hierárquico.

**Fase 5.** Puxa próximo passo recomendado de `/tatou-2.0` baseado no diagnóstico.

**Fase 6.** Gera dashboard HTML (visão mentorada, layout em `VISAO-MENTORADA.md`) + JSON.

**Output:**

```
# DASHBOARD INDIVIDUAL — [Nome] — [Mês/Ano]

## Status
- Porta atual: [letra]
- Nível hierárquico: [Iniciada/Cortesã/Dama/Imperatriz]
- KPIs verdes: [N]/26

## Sua porta atual
- KPI primário: [definição]
- Seu número: [valor]
- Benchmark: [valor BR mentora high-ticket]
- Cor: [verde/amarelo/vermelho]

## Próximo gate
- Porta: [letra]
- Critério: [texto]
- Distância: [o que falta]

## Próximo passo (tatou-2.0)
[ação concreta + skill recomendada]

## Histórico (últimos 6 meses)
[mês: cor de cada porta]

## Distância pra próximo nível
- [próximo nível]: faltam [N] KPIs verdes em [portas]

## Arquivo
~/Documents/Obsidian Vault/04 - Mentoradas/[Nome]/Dashboard/[YYYY-MM]/dashboard.html
```

### MODO `--alertas`

**Fase 1.** Varre Corte inteira (todas mentoradas).

**Fase 2.** Filtra só KPIs vermelhos.

**Fase 3.** Aplica priorização (regra em `ALERTAS-LOGICA.md`):
1. Vermelho em porta upstream contaminando downstream
2. Vermelho em porta atual da mentorada
3. Ciclo recorrente vencido (N semanal, X trimestral, Z mensal)
4. Vermelho em porta downstream sem upstream contaminada

**Fase 4.** Devolve lista priorizada com ação imediata por alerta.

**Output:**

```
# ALERTAS VERMELHOS — Corte — [Mês/Ano]

## Crítico ([N])
- [Mentorada] — porta [X] — KPI [Y] em [%] do benchmark
  → upstream contaminada, rollback pra porta [Z] via `/gates-imperatriz --rollback`

## Alto ([N])
- [Mentorada] — porta [X] — [razão]
  → ação: [skill recomendada]

## Ciclo vencido ([N])
- [Mentorada] — ciclo [letra] vencido há [dias]
  → roda `/[skill]`

## Médio ([N])
- [Mentorada] — porta [X] — [razão]
  → monitorar próximo mês
```

### MODO `--prontas-investidura`

**Fase 1.** Lê todas mentoradas.

**Fase 2.** Para cada uma, identifica nível hierárquico atual.

**Fase 3.** Aplica matriz de Investidura:
- **Iniciada → Cortesã**: portas A-F verdes (Aterrissagem, Bússola, Causa, Diferenciação, Estética, Fluência)
- **Cortesã → Dama**: A-F + G-L verdes (mais Garantia, Habitat, Ímã, Jornada, Tráfego, Lift)
- **Dama → Imperatriz**: A-V verdes (mais M-V, faltando só W-Z que são manutenção contínua)

**Fase 4.** Lista quem está pronta + quem está a 1-2 portas de subir + quem está longe.

**Output:**

```
# INVESTIDURA — [Mês/Ano]

## Prontas agora ([N])
- [Mentorada] — sobe de [nível] pra [nível]
  → todas portas exigidas verdes
  → cerimônia sugerida: [data]

## Quase lá ([N])
- [Mentorada] — falta [porta][razão]
  → estimativa: [N] meses

## Em construção ([N])
- [Mentorada] — nível [atual] — [N] portas verdes de [exigidas]
  → foco em [porta]
```

---

## REGRAS DURAS (a skill não negocia)

1. **Não declara KPI verde sem número registrado.** Vontade não conta. Achismo não conta.
2. **Não infere benchmark.** Os 26 benchmarks vêm fixos de `KPIS-POR-PORTA.md` — não invento e não ajusto sem decisão da Tata.
3. **Não mistura visões.** Visão mentorada NUNCA mostra dado de outra mentorada. Visão Tata é a única que cruza Corte.
4. **Não promove pra próximo nível sem critério verde.** "Acho que ela tá pronta" não fecha Investidura. KPI fecha.
5. **Não roda sem dossiê.** Pede `/dossie-mentorada` profile 16-kpis-dashboard antes.
6. **Não substitui skill de execução.** Quem cria mecanismo é `/mecanismo-unico`. Quem mede é esta skill.
7. **Não dá conselho emocional.** Diagnóstico técnico, próximo passo, fim.
8. **Sempre alimenta `/tatou-2.0`** — saída desta skill é input do construtor.
9. **Sempre cruza com `/gates-imperatriz`** — KPI verde sem gate passado é alerta de inconsistência.
10. **Sempre entrega HTML + JSON.** HTML pra ler, JSON pra integrar.

---

## ARQUIVOS DE REFERÊNCIA (carregar sob demanda)

- `KPIS-POR-PORTA.md` — todos 26 KPIs com benchmark BR mentora high-ticket + regras verde/amarelo/vermelho
- `VISAO-TATA.md` — layout do dashboard agregado da Corte
- `VISAO-MENTORADA.md` — layout do dashboard individual
- `ALERTAS-LOGICA.md` — regras de alerta + cores + priorização
- `TEMPLATE-HTML.md` — template HTML interativo (cores #D6A648, Inter, Instrument Serif, Mermaid)
- `README.md` — visão executiva da skill

---

## INTEGRAÇÃO COM O ECOSSISTEMA TATA

**Lê de:**
- `/dossie-mentorada` profile `16-kpis-dashboard` — KPIs declarados por mentorada
- `/gates-imperatriz` — status de cada porta (passou / parcial / não passou)
- `/perfil-mentorada` — peso por perfil (Iniciada não cobra os mesmos KPIs que Imperatriz)

**Alimenta:**
- `/tatou-2.0` — diagnóstico de KPIs vira input pra próximo passo
- `/raci-imperatriz` — ajuda decidir o que terceirizar baseado em gargalo

**Coordena com:**
- `/calendario-imperatriz` — KPI N (publicações/semana) é input direto
- `/diagnostico-gargalo-funil` — quando vermelho aparece em K-L-M, despacha
- `/reuniao-de-resultado` — KPIs alimentam reunião gerencial mensal da Tata com a Corte

**Roda automatizado:**
- Mensalmente, dia 1, com dado do mês anterior (cron do sistema da Tata)
- Trimestralmente em audit completo (porta X é trimestral)

**Não canibaliza:**
- Esta skill mede. Outras skills executam. `/gates-imperatriz` audita gates objetivos. Limite claro.

---

## VOZ DA SKILL

PT-BR direto, seco, técnico. Sem psicologismo. Sem hype. Vocabulário Tata: "KPI", "porta", "verde/amarelo/vermelho", "benchmark BR mentora high-ticket", "Corte", "Investidura", "Iniciada/Cortesã/Dama/Imperatriz", "agregado", "rollback".

Quando a mentorada está vermelha, a skill não conforta — mede. O conforto vem de saber exatamente onde está e o que falta.

---

**Travessia Imperatriz — propriedade intelectual Tata Gonçalves. Pilar 4 (Medição) operado por esta skill.**
