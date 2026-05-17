---
name: anamnese-mentorada
description: >
  Primeira skill ativada quando uma mentorada nova entra na Travessia
  Imperatriz da Tata Goncalves. Coleta dados em 8 blocos (historico
  pessoal, negocio atual, tentativas anteriores, dores especificas,
  objetivos, recursos, identidade, expectativas) e abastece o ecossistema
  inteiro: alimenta `/perfil-mentorada` (classificacao por estagio),
  `/dossie-mentorada` (ficha viva) e `/imperio-diagnostico` (FRIO + DOMINIO
  + PENTA). Quatro modos: --formulario (HTML standalone pra mentorada
  preencher offline), --call (entrevista guiada estruturada pra Tata fazer
  pre-call), --auto (deep-research extrai info publica e marca campos
  pendentes), --validar (audita anamnese existente). Output em
  `~/imperio/mentoradas/[slug]/00-anamnese.json`. Use quando a Tata
  mencionar nova mentorada, abrir ficha de mentorada, fazer pre-call,
  enviar formulario inicial, anamnese de aluna, briefing de entrada,
  onboarding de mentoria, ou disser "tem mentorada nova", "vou entrevistar
  fulana", "manda o formulario pra ela", "preciso preparar a call dela".
  Metodo Imperatriz de Anamnese — propriedade Tata Goncalves.
---

# Anamnese Mentorada — Porta de Entrada da Travessia Imperatriz

Esta e a **primeira skill** que roda quando uma mentorada nova entra na Travessia Imperatriz. E o **exame medico completo** que abastece todas as outras skills do ecossistema. Sem anamnese feita, nenhuma decisao estrategica boa sai. Sem anamnese **honesta**, a Tata erra o tom da call.

## Filosofia central

> **Anamnese mal feita = mentoria mal feita. A Tata nao chuta. A Tata diagnostica.**

Anamnese vem da medicina: e o relato que o paciente faz **antes** de qualquer exame ou tratamento. Sem anamnese boa, o medico erra remedio. Sem anamnese boa, a Tata erra plano de 6 meses.

A skill **nao gera plano**. A skill **abastece** os planos das outras skills. E o ato 0. A camada de dados crus que vira ouro depois.

## Quando usar

- Mentorada acabou de fechar contrato e entra hoje na Travessia
- Tata vai fazer pre-call de entrada e precisa de briefing
- Mentorada antiga voltou pra second mentorship — refazer anamnese
- Tata quer ressuscitar dossie de mentorada parada ha 6+ meses
- Antes de rodar `/perfil-mentorada` ou `/imperio-diagnostico` — anamnese e pre-requisito
- Tata vai delegar onboarding pra time (Severino) — formulario sai daqui

## Diferenca entre anamnese, dossie, perfil e diagnostico

- **Anamnese** = entrevista de entrada. Coleta crua de fatos. UMA VEZ.
- **Perfil** = classificacao da mentorada (Construtora / Frustrada / Premium / etc) baseada na anamnese.
- **Dossie** = ficha viva que evolui durante a mentoria toda (atualizada toda call).
- **Diagnostico** = FRIO + DOMINIO + PENTA aplicado sobre a anamnese pra gerar plano.

A skill foca em **anamnese**. Se a Tata pedir plano, classificacao ou diagnostico, redirecionar pras skills corretas.

---

## OS 4 MODOS DE OPERACAO

A skill roda em 4 modos declaraveis. Se a Tata nao declarar, perguntar **"formulario, call, auto ou validar?"**.

### `--formulario`
**Quando:** Tata quer enviar pra mentorada preencher offline (email/WA antes da call).
**Output:** arquivo HTML standalone (sem dependencia externa) com 8 blocos navegaveis, voz Tata (provocativa, direta, intima), botao "exportar JSON" no final.
**Entrega:** mentorada baixa, preenche, exporta JSON, manda de volta. Tata roda `/anamnese-mentorada --validar` no JSON recebido.

### `--call`
**Quando:** Tata vai fazer call de entrada com a mentorada e quer roteiro estruturado em maos.
**Output:** roteiro de entrevista de 60-90min com tempo por bloco, perguntas literais, sondas (probing questions) pra cada resposta evasiva, espacos pra Tata anotar.
**Entrega:** markdown imprimivel, 8 blocos, ate 35 perguntas, cronometragem.

### `--auto`
**Quando:** Tata ja conhece a mentorada por outras vias (Insta publico, lista de espera, mentoria anterior) e quer pre-popular a anamnese antes da call.
**Output:** JSON com campos preenchidos a partir de deep-research (nome, idade aproximada, localizacao, Instagram, faturamento publico, formacao se publica, nicho aparente). Campos nao confirmaveis sao marcados `pendente: true` com `motivo: "exige confirmacao na call"`. **NUNCA inventa dado**.
**Entrega:** JSON pre-populado pronto pra ser confirmado/refinado em call.

### `--validar`
**Quando:** anamnese ja existe (a mentorada preencheu o formulario, ou anamnese antiga precisa ser revisada).
**Output:** auditoria contra os 8 blocos — campos faltantes, respostas vagas, contradicoes internas, riscos identificados, perguntas que faltam fazer na call.
**Entrega:** relatorio com score (0-100) + lista de gaps + sugestao de proxima acao.

---

## PROCESSO — 6 FASES OBRIGATORIAS

### FASE 0 — Slug e setup

Toda anamnese vive em `~/imperio/mentoradas/[slug]/00-anamnese.json`.

Slug = `nome-sobrenome` em lowercase, sem acento, separado por hifen. Exemplo: "Tamires Gonçalves" → `tamires-goncalves`.

Antes de qualquer coisa:
```bash
mkdir -p ~/imperio/mentoradas/[slug]/
```

Se ja existir `00-anamnese.json` no caminho, AVISAR a Tata e perguntar:
- Sobrescrever (refazer do zero)
- Atualizar (merge nos campos novos)
- Cancelar

### FASE 1 — Identificacao do modo + leitura de contexto

Se a Tata mandou:
- Link de Instagram da mentorada → considerar `--auto`
- "Vou fazer call amanha" → `--call`
- "Manda o formulario pra ela" → `--formulario`
- JSON existente → `--validar`

Sempre ler o que a Tata mandou ANTES de perguntar. Extrair tudo que for extraivel.

### FASE 2 — Coleta dos 8 blocos

Os 8 blocos sao **obrigatorios** em qualquer modo. O que muda e o **como** se coleta:

1. **Historico pessoal** — quem ela e
2. **Negocio atual** — onde ela esta
3. **Tentativas anteriores** — o que ja tentou
4. **Dores especificas** — o que tira o sono
5. **Objetivos** — onde quer chegar
6. **Recursos** — o que tem disponivel
7. **Identidade** — voz, nicho, posicionamento
8. **Expectativas** — o que espera da Travessia

Detalhe completo de cada bloco e perguntas literais em **`OS-8-BLOCOS.md`**.

**Regra de qualidade:** cada bloco precisa de 70%+ dos campos preenchidos pra ser considerado completo. Abaixo disso, marcar bloco como `incompleto: true`.

### FASE 3 — Deteccao de sinais de alerta

Durante a coleta, marcar como `alerta` qualquer um destes padroes:

- **Dor crônica** (parada ha 12+ meses no mesmo lugar) → `risco: estagnacao`
- **Faturamento alto + sem time** (R$50k+/mês sozinha) → `risco: gargalo_pessoal`
- **Investiu R$30k+ em mentorias e nada andou** → `risco: vitima_de_curso`
- **Expectativa de "transformacao em 30 dias"** → `risco: expectativa_irrealista`
- **Negocio sem produto definido apos 2+ anos** → `risco: confusao_estrategica`
- **Vinda por indicacao mas sem saber o que a Tata faz** → `risco: alinhamento`

Cada alerta vira campo no JSON com `tipo`, `severidade` (baixa/media/alta) e `acao_sugerida`.

### FASE 4 — Output JSON estruturado

Schema completo em **`SCHEMA-JSON.md`**. Sempre validar contra schema antes de salvar.

Salvar em:
```
~/imperio/mentoradas/[slug]/00-anamnese.json
```

### FASE 5 — Entrega + proxima acao

Apos salvar, ENTREGAR pra Tata:

1. **Resumo executivo** (10 linhas) com:
   - Quem ela e (1 linha)
   - Onde ela esta no negocio (2 linhas)
   - Top 3 dores (3 linhas)
   - Top 3 objetivos (3 linhas)
   - Alertas detectados (1 linha)

2. **Score de completude** (0-100) por bloco.

3. **Proxima skill recomendada:**
   - Score >= 80 → `/perfil-mentorada` (classificar)
   - Score 60-80 → `/anamnese-mentorada --validar` (preencher gaps)
   - Score < 60 → repetir coleta (formulario ou call)

4. **Caminho do arquivo:** `~/imperio/mentoradas/[slug]/00-anamnese.json`

---

## OS 8 BLOCOS — VISAO RAPIDA

(Detalhamento completo em `OS-8-BLOCOS.md`.)

| # | Bloco                | Campos | Tempo Call | Critico? |
|---|----------------------|--------|------------|----------|
| 1 | Historico pessoal    | 8      | 8 min      | Sim      |
| 2 | Negocio atual        | 6      | 12 min     | Sim      |
| 3 | Tentativas anteriores| 4      | 8 min      | Medio    |
| 4 | Dores especificas    | 4      | 12 min     | CRITICO  |
| 5 | Objetivos            | 4      | 10 min     | Sim      |
| 6 | Recursos             | 4      | 8 min      | Medio    |
| 7 | Identidade           | 5      | 8 min      | Sim      |
| 8 | Expectativas         | 3      | 8 min      | CRITICO  |

Total: ~37 campos, 74 minutos de call.

---

## REGRAS DURAS (a skill NAO negocia)

1. **Nao inventa dado.** Se nao tem informacao, marca `pendente: true` com motivo. Nunca preenche por achismo.
2. **Nao julga a mentorada.** Coleta neutra. Sem "ela parece confusa" ou "deve ser dificil de mentorar". So fato.
3. **Nao gera plano.** Plano e do `/celeste`. Anamnese e camada crua.
4. **Nao expoe dado sensivel.** Faturamento, divida, intimidade — fica no JSON local. Nunca em outputs publicos.
5. **Nao pula bloco.** Os 8 sao obrigatorios. Se a mentorada fugiu de um, marcar `incompleto` e seguir — mas registrar que faltou.
6. **Nao fecha anamnese sem dores top 3.** Bloco 4 e CRITICO. Se a mentorada nao consegue articular 3 dores, sondar mais. Sem dor, nao tem alavanca.
7. **Nao fecha anamnese sem objetivo de 12 meses.** Bloco 5 — sem norte, nao tem destino.
8. **Sempre sobrescreve com confirmacao.** Se ja existe `00-anamnese.json`, perguntar antes de apagar.
9. **Sempre salva backup** quando atualizar (`00-anamnese.json.bak`).
10. **Sempre marca data e versao.** Schema tem `versao_skill`, `data_coleta`, `coletado_por` (call/formulario/auto).
11. **Sempre roda em PT-BR.** Voz Tata: provocativa, direta, intima. Nada de jargao corporativo gringo.
12. **Sempre detecta alertas** da fase 3 — mesmo que a mentorada nao mencione, a skill cruza dados.

---

## ANTI-PATTERNS (NAO FAZER)

1. **Anamnese-formulario-de-banco** — ficar em "qual seu CEP, RG, CPF" sem extrair narrativa. Mentorada nao quer cadastro, quer ser ouvida.
2. **Pergunta-aberta-demais** — "me conta sua vida" trava qualquer humano. Especificar.
3. **Pergunta-multipla-mascarada** — "qual seu nicho, posicionamento e voz?" ja tem 3 perguntas. Separar.
4. **Inventar dor por afinidade** — "deve ser sindrome do impostor, ne?" sugestiona resposta. Deixar a mentorada nomear.
5. **Aceitar resposta vaga** — "quero crescer" nao e objetivo. Sondar: crescer quanto, em quanto tempo, em qual eixo?
6. **Pular tentativas anteriores** — bloco 3 parece "fraco" mas e ouro: ali esta o cemiterio que voce nao deve repetir.
7. **Anamnese sem timeline pessoal** — bloco 1 sem trajetoria deixa a Tata sem ancoragem emocional na call.
8. **Output sem alertas** — anamnese sem fase 3 e curriculo, nao diagnostico.
9. **Compartilhar JSON em chat** — vai pra arquivo local. Em chat so resumo executivo.
10. **Modo `--auto` sem marcar pendente** — confiar em dado de Insta sem confirmar. Tudo de fora vai como `pendente`.

---

## INTEGRACAO COM O ECOSSISTEMA TATA

A anamnese e a **camada 0** da Travessia. Tudo depende dela.

```
/anamnese-mentorada              ← VOCE ESTA AQUI (ato 0)
       ↓
/perfil-mentorada                (classifica: Construtora / Frustrada / Premium / Tecnica / etc)
       ↓
/dossie-mentorada                (cria ficha viva pra evoluir)
       ↓
/imperio-diagnostico             (FRIO + DOMINIO + PENTA)
       ↓
/celeste                         (plano estrategico de 5 passos)
       ↓
[execucao 6 meses com skills da Travessia]
```

**Skills que CONSOMEM dados da anamnese:**
- `/perfil-mentorada` — classifica a partir dos blocos 2 + 4 + 5
- `/dossie-mentorada` — copia anamnese como ponto zero do dossie
- `/imperio-diagnostico` — usa blocos 2, 4, 5, 6
- `/celeste` — usa anamnese inteira pra montar plano
- `/headline-imperatriz` — usa bloco 7 (voz/identidade)
- `/copy-conversacional-dm` — usa blocos 2, 4, 7
- `/imperatriz-bot` — usa blocos 2, 7, 8 pra calibrar
- `/skill-mentoria-tata` — usa blocos 5, 6, 8 pra montar trilha

**Skills que ALIMENTAM a anamnese (modo `--auto`):**
- `/deep-research` — busca info publica
- `/skill-persona-profunda` — pode complementar o bloco 7
- `/glossariodatata` — usado pra explicar termos pra mentorada na call

---

## EXEMPLOS DE USO

### Exemplo 1 — Mentorada nova, sem call agendada
```
Tata: "Mentorada nova fechou hoje. Manda o formulario pra Carolina Mendes, @carolmendescoach."

Skill ativa --formulario
→ slug: carolina-mendes
→ gera HTML standalone com voz Tata
→ entrega via email/WA
→ Tata pode rodar /anamnese-mentorada --validar quando ela responder
```

### Exemplo 2 — Pre-call em 24h
```
Tata: "Tenho call amanha 10h com Marina Lopes. Roteiro pra eu fazer presencial."

Skill ativa --call
→ slug: marina-lopes
→ gera roteiro markdown imprimivel: 8 blocos, 35 perguntas, cronometragem 90min
→ Tata imprime/abre no iPad e conduz
→ apos call, Tata cola transcricao em /anamnese-mentorada --validar
```

### Exemplo 3 — Mentorada conhecida do Insta
```
Tata: "Fechei com Renata Ferraz, @renataferrazpilates. Ja segue ela ha tempo. Pre-popula o que der."

Skill ativa --auto
→ slug: renata-ferraz
→ /deep-research busca @renataferrazpilates
→ extrai: nome, localizacao Curitiba, formacao Edu Fisica, audiencia ~80k Insta, nicho pilates pra gestantes
→ marca como pendente: faturamento, time, dores intimas, expectativas
→ Tata abre call ja sabendo metade
```

### Exemplo 4 — Validar anamnese antiga
```
Tata: "Camila Aguiar tinha anamnese de janeiro. Ela voltou hoje, mudou tudo. Audita."

Skill ativa --validar
→ le ~/imperio/mentoradas/camila-aguiar/00-anamnese.json
→ score por bloco
→ aponta gaps: bloco 6 desatualizado, bloco 8 sem expectativas pra 2026
→ recomenda: refazer blocos 6 e 8 em mini-call de 30min
```

---

## VOZ TATA NO FORMULARIO HTML

Quando a mentorada preenche, ela esta lendo a Tata. NAO e formulario asseptico de hospital. E provocativo, direto, intimo.

Padroes da voz Tata no formulario (ver `FORMULARIO-HTML.md` pra exemplos completos):

- **Saudacao:** "Oi, mentorada nova. Senta aqui que eu vou te conhecer de verdade."
- **Pergunta-pivo:** "Antes de qualquer plano, eu preciso entender quem voce e — nao quem voce escreve no Insta."
- **Bloco 4 abertura:** "Vamos pro pulo do gato: o que tira o seu sono. Sem polidez. Eu nao monto plano em cima de mentira educada."
- **Bloco 8 abertura:** "Ultimo bloco. O que voce ESPERA de mim em 6 meses? Vai fundo. Ninguem mais le isso alem de mim."
- **Fechamento:** "Pronto. Agora a gente nao comeca do zero — comeca do mapa."

Tom: provocativo (sem agredir), direto (sem rodeio), intimo (sem invasao). Estilo "amiga que diagnostica".

---

## VERSIONAMENTO

- **v1.0** (atual) — 8 blocos, 4 modos, 6 fases, integracao com perfil/dossie/diagnostico/celeste
- **v1.1** (planejado) — modo `--reentrar` pra mentorada que refaz Travessia
- **v1.5** (planejado) — pre-popular a partir de transcricao de webinar/call assistida
- **v2.0** (planejado) — anamnese contínua (re-coleta automatica a cada 90 dias)

---

## ARQUIVOS DE REFERENCIA (carregar sob demanda)

- `OS-8-BLOCOS.md` — perguntas literais de cada bloco + criterio de qualidade
- `FORMULARIO-HTML.md` — template HTML standalone com voz Tata
- `SCHEMA-JSON.md` — schema completo do `00-anamnese.json`
- `EXEMPLOS-PREENCHIDOS.md` — 3 anamneses completas pra perfis distintos
- `README.md` — instalacao e compartilhamento

---

## COMO COMPARTILHAR COM MENTORADAS

Esta skill e **uso interno da Tata e do time da Travessia** (Severino e quem mais entrar). NAO e distribuida pras mentoradas — elas sao **objeto** da skill, nao usuarias.

O que vai pra mentorada:
- HTML do `--formulario` (ela preenche, devolve JSON)
- Resumo executivo da anamnese (opcional, no segundo encontro, como espelho)

O que NAO vai:
- JSON cru
- Alertas detectados
- Score de completude

Ver `README.md` pra detalhes de instalacao no time.

---

**Metodo Imperatriz de Anamnese — propriedade intelectual Tata Goncalves. Travessia Imperatriz 2026.**
