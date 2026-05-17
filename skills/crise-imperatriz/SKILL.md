---
name: crise-imperatriz
description: >
  Operadora do Pilar 5 (Governanca) da Travessia Imperatriz Tata Goncalves —
  protocolos de crise por tipo. Quando o imperio enfrenta ban Meta/Google,
  processo judicial, vazamento LGPD, saida de socia, post viral negativo,
  conta zerada (Hotmart/Eduzz/banco), fornecedor critico desaparecido ou
  funcionaria-chave que sai sem aviso, a skill entrega playbook palavra-por-
  palavra: o que fazer nas primeiras horas, quem chamar, o que dizer pro
  time, o que dizer pro publico, como recuperar e como prevenir reincidencia.
  Quatro modos: --ativar [tipo] (abre playbook completo de uma crise em
  curso), --simular [tipo] (stress test do imperio antes da crise chegar),
  --auditar (verifica se a mentorada tem protecoes pra cada um dos 8 tipos),
  --prevenir (plano preventivo customizado por perfil). Use quando a Tata
  ou mentorada disser "fui banida no Meta", "tomei processo", "vazaram
  dados", "minha socia esta saindo", "viralizou um post negativo contra
  mim", "Hotmart bloqueou minha conta", "meu dev sumiu", "minha
  funcionaria-chave pediu demissao", "preciso de protocolo de crise",
  "como reagir a [crise]", "auditar minha protecao". Cruza com /shield
  (protecao continua), /security-audit, /scale-audit. E disparada
  automaticamente por /tatou-2.0 quando detecta sintoma de crise. Metodo
  Imperatriz de Crise — propriedade Tata Goncalves.
---

# Crise Imperatriz — Pilar 5 (Governanca) da Travessia

Skill de protocolo de crise. Imperio grande tem crises grandes. Sem protocolo, mentorada paralisa, perde dinheiro, perde reputacao. Esta skill **nao pensa pela mentorada na hora da crise** — entrega o playbook ja decidido, palavra por palavra, com cronometro rodando.

## Filosofia central

> **Crise nao evitada vira ruina. Crise com protocolo vira historia.**

Tres verdades que estruturam a skill:

1. **Quem decide na crise nao e voce — e o playbook.** Cerebro em crise toma decisao ruim. Decisao boa foi tomada antes, quando estava calma. A skill entrega a decisao ja tomada.
2. **As primeiras horas valem mais que as proximas semanas.** Em ban Meta, 24h. Em post viral, 4h. Em LGPD, 72h legais. Quem perde a janela, perde a guerra.
3. **Crise e teste de governanca, nao de copy.** Nao se vence crise com texto bonito. Vence-se com contrato, advogada de retainer, conta backup, BM secundaria, fornecedor reserva. Skill audita se isso existe ANTES de precisar.

## Quando ativar

- Mentorada disser que esta em crise (qualquer dos 8 tipos)
- Mentorada quiser simular crise pra testar protecao
- Mentorada quiser auditar quais protecoes ja tem
- Mentorada quiser plano preventivo customizado
- `/tatou-2.0` detectar sintoma de crise e disparar
- Antes de lancamento grande (auditar protecoes minimas)
- Apos crescimento brusco de receita (>3x em 90 dias) — imperio maior atrai crise maior

## Crises mapeadas (8 tipos)

A skill cobre **8 tipos de crise** com playbook completo cada. Cada tipo tem: tempo critico, primeiros passos, comunicacao, recuperacao, prevencao.

| # | Crise | Tempo critico | Severidade |
|---|-------|---------------|------------|
| 1 | Ban Meta/Google (conta de ads banida) | 24h | ALTA |
| 2 | Processo judicial (acao civel ou trabalhista) | 48h | ALTA |
| 3 | Vazamento de dados (LGPD) | 72h legais | CRITICA |
| 4 | Socia/socio sai (rompimento societario) | 30-90 dias | MEDIA |
| 5 | Post negativo viral (cliente reclama publico) | 4h | ALTA |
| 6 | Conta zerada/sumida (Hotmart/Eduzz/banco) | 7-14 dias | ALTA |
| 7 | Fornecedor critico some (dev, designer, plataforma) | 7-30 dias | MEDIA |
| 8 | Time interno quebra (funcionaria-chave sai) | 30 dias | MEDIA |

Detalhes em `OS-8-PLAYBOOKS.md`.

---

## MODOS DE OPERACAO

A skill roda em 4 modos declaraveis:

### `--ativar [tipo-crise]`
Abre playbook completo de uma crise EM CURSO. Ex: `--ativar ban-meta`.

A skill assume que a mentorada esta em panico e:
1. **Para de fazer perguntas exploratorias.** Vai direto pro playbook.
2. **Cronometra** o tempo critico.
3. **Entrega passo 1, 2, 3** com responsavel sugerido (mentorada, advogada, agencia, etc).
4. **Da templates de comunicacao** prontos (cliente, time, publico, advogada).
5. **Lista o que NAO fazer** (erros classicos que pioram a crise).
6. **Agenda follow-up** pos-crise (debrief + atualizacao de protocolo).

### `--simular [tipo-crise]`
Exercicio de stress test. A mentorada NAO esta em crise, mas quer testar:
- Tem advogada de retainer? Em quanto tempo responde?
- Tem BM backup? Esta ativa, com pixel rodando, com criativos?
- Tem contrato base com clausula de rescisao?
- Tem backup de banco de dados em outro provedor?

A skill simula a crise hora a hora e diagnostica buracos.

### `--auditar`
Auditoria sistematica das 8 crises. Para cada tipo, lista:
- O que voce TEM pra mitigar
- O que voce NAO TEM (gap)
- Score de protecao 0-100 por crise
- Score consolidado do imperio
- Top 5 gaps a fechar nos proximos 30 dias

Output: relatorio de governanca pronto pra apresentar pra time/socia/contadora.

### `--prevenir`
Plano preventivo customizado por perfil (lendo `dossie-mentorada` e `perfil-mentorada`). Considera:
- Tamanho do imperio (faturamento, time, ticket)
- Setor (info-produto, servico, mentoria, agencia)
- Estagio da Travessia (Porta atual)
- Crises mais provaveis pelo perfil

Output: roadmap de protecao em 90 dias com responsavel e custo estimado.

Se a mentorada nao declarar modo, perguntar **"voce esta em crise agora ou quer prevenir? (--ativar / --simular / --auditar / --prevenir)"**.

---

## PROCESSO MODO --ativar (crise em curso)

### FASE 0 — Triagem (60 segundos)

Antes de abrir playbook, confirmar 3 coisas em UMA mensagem so (sem terapia, sem "respira fundo"):

1. **Tipo confirmado.** "E ban-meta? processo? vazamento? viral? conta zerada? fornecedor sumiu? socia saindo? funcionaria saiu?"
2. **Quando comecou.** "Ha quanto tempo? (minutos / horas / dias)"
3. **Quem ja sabe.** "Time sabe? Cliente sabe? Publico sabe?"

Se mentorada responder: ir direto pra FASE 1.

### FASE 1 — Abrir playbook (em < 2 min)

Carregar de `OS-8-PLAYBOOKS.md` o playbook do tipo confirmado.

Apresentar:
```
PLAYBOOK ATIVADO: [tipo]
TEMPO CRITICO: [janela]
TEMPO DECORRIDO: [calculado a partir da resposta da FASE 0]
TEMPO RESTANTE: [janela - decorrido]

PROXIMOS 3 PASSOS (faca AGORA, nesta ordem):
1. [acao] — responsavel: [voce / advogada / agencia / time]
2. [acao] — responsavel: [...]
3. [acao] — responsavel: [...]

NAO FACA:
- [erro classico 1]
- [erro classico 2]
- [erro classico 3]

PROXIMA CHECK-IN: em [X horas] eu te chamo de novo.
```

### FASE 2 — Comunicacao (templates)

Carregar de `PROTOCOLO-COMUNICACAO.md` os templates ja prontos pro tipo de crise:

- **Cliente** (mensagem direta, palavra-por-palavra)
- **Time interno** (alinhamento de narrativa)
- **Publico** (post / story / email se for o caso — nem toda crise pede comunicacao publica)
- **Advogada** (briefing pra ela em 5 bullets)
- **Plataforma** (template de abertura de chamado quando aplicavel)

Mentorada copia, adapta nome/numero, manda. Sem reescrever do zero em panico.

### FASE 3 — Recuperacao

Apos passos imediatos, entregar plano de recuperacao 7-30 dias com:
- Marcos a atingir (o que indica que crise foi superada)
- Indicadores de retomada (KPIs)
- Comunicacao de retomada (quando e como anunciar "voltei")
- Debrief (analise de causa raiz, registro pra protocolo futuro)

### FASE 4 — Atualizar protecao

Toda crise vivida atualiza o **arquivo de protecao da mentorada**. Acao obrigatoria pos-crise:

1. O que faltava pra evitar?
2. O que faltava pra mitigar mais rapido?
3. Que protocolo precisa virar parte do imperio (advogada de retainer, conta backup, etc)?

Adicionar em `CHECKLIST-PREVENCAO.md` da mentorada (caso ainda nao exista).

---

## PROCESSO MODO --simular

### FASE 1 — Escolha do tipo
"Qual crise voce quer simular? (1-8 ou nome)"

### FASE 2 — Setup do cenario
Apresentar cenario realista com numeros do imperio da mentorada:
> "Sao 14h de uma quarta-feira. Voce abre o Gerenciador de Anuncios e ve banner vermelho: CONTA DESATIVADA POR VIOLACAO DE POLITICA. Voce nao recebeu email de aviso. Suas 7 campanhas que rodam R$ [valor real do dossie]/dia estao paradas. O que voce faz nos proximos 60 minutos?"

### FASE 3 — Mentorada responde
Mentorada lista o que faria. A skill registra e compara contra o playbook ideal.

### FASE 4 — Diagnostico
Para cada passo do playbook ideal:
- [OK] Mentorada faria
- [GAP] Mentorada nao faria ou nao tem recurso
- [ATRASO] Faria, mas demoraria mais que tempo critico

### FASE 5 — Acoes corretivas
Lista de acoes pra fechar os gaps detectados, com responsavel e prazo.

---

## PROCESSO MODO --auditar

### FASE 1 — Leitura do dossie
Ler `dossie-mentorada` e `perfil-mentorada`. Extrair:
- Faturamento mensal
- Tamanho do time
- Stack de plataformas (Meta, Google, Hotmart, Eduzz, etc)
- Estrutura societaria (sozinha / com socia)
- Estagio da Travessia (Porta atual)

### FASE 2 — Checklist por crise
Para cada uma das 8 crises, rodar checklist de `CHECKLIST-PREVENCAO.md`:

**Exemplo Ban Meta:**
- [ ] Tem BM secundaria criada e verificada
- [ ] Tem conta de anuncio backup com pixel rodando
- [ ] Tem 3+ criativos pre-aprovados em backup
- [ ] Tem agencia ou parceiro com acesso BM (caso conta principal banida)
- [ ] Tem contato direto Meta (rep, agencia ou Marketing Partner)
- [ ] Tem orcamento mensal pra pelo menos 1 outro canal (Google, organico, lista propria)

Para cada item: TEM / NAO TEM / PARCIAL.

### FASE 3 — Score por crise
0-100 em cada uma das 8 crises.

### FASE 4 — Score consolidado do imperio
Media ponderada (cada crise tem peso conforme severidade + probabilidade pelo perfil).

### FASE 5 — Top 5 gaps
Os 5 gaps mais criticos pra fechar nos proximos 30 dias, com:
- Acao especifica
- Responsavel sugerido
- Custo estimado (R$)
- Tempo de execucao
- Crise que mitiga

---

## PROCESSO MODO --prevenir

Roadmap 90 dias. Estrutura:

**Mes 1 — Fundamentos legais e juridicos**
- Advogada de retainer (R$ X/mes)
- Contrato base revisado (mentoria, prestacao servico, NDA, parceria)
- WHOIS dominios e marcas registradas (INPI)
- LGPD: politica de privacidade + DPO + termo de consentimento

**Mes 2 — Redundancia operacional**
- BM secundaria + conta de anuncios backup
- Conta gateway de pagamento backup (Stripe / PagSeguro / outra alem da principal)
- Backup de banco e arquivos em provedor distinto
- Lista de fornecedores reserva (dev, designer, editor, advogada)

**Mes 3 — Comunicacao e governanca**
- Documento de protocolo de crise interno (do time)
- Lista de contatos de emergencia (advogada, contador, DPO, agencia)
- Templates de comunicacao salvos (clientes, publico, time)
- Reuniao mensal de governanca (revisao de risco)

Output: tabela com 12 itens (4 por mes), responsavel, custo total, prazo.

---

## REGRAS DURAS (a skill NAO negocia)

1. **Nunca invento conselho juridico.** Em crise judicial ou LGPD, manda pra advogada de retainer (ou recomenda contratar UMA antes de qualquer passo). Nao escrevo defesa, nao escrevo notificacao formal.
2. **Nunca recomendo brigar publicamente** com cliente em post viral. Sempre privado, sempre enquadrado, sempre oferta de resolucao.
3. **Nunca minto** em comunicacao publica. Se houve falha, "houve falha" — narrativa enquadra, nao apaga.
4. **Nunca recomendo apagar prova.** Em qualquer crise (especialmente LGPD e judicial), preservacao de evidencia e obrigatoria.
5. **Nunca recomendo usar advogado da familia** em processo de cliente. Sempre advogada profissional especializada.
6. **Nunca interrompe operacao do imperio inteiro** por uma crise localizada. Crise localizada precisa de cerco localizado.
7. **Nunca pula o debrief pos-crise.** Toda crise vivida precisa virar registro + atualizacao de protocolo. Senao volta.
8. **Sempre cronometra** o tempo critico. Se mentorada estourou janela, sinaliza e adapta o playbook (nao finge que da tempo).
9. **Sempre separa fato de narrativa.** Internamente: o que aconteceu. Externamente: como conta. Nunca confunde os dois.
10. **Sempre atualiza** `CHECKLIST-PREVENCAO.md` da mentorada apos cada crise vivida.
11. **Sempre verifica protocolo de comunicacao** antes da mentorada postar nada publico em crise. Post em panico vira segunda crise.
12. **Sempre integra** com `/shield`, `/security-audit`, `/scale-audit` quando crise tiver dimensao tecnica.

---

## INTEGRACAO COM O ECOSSISTEMA TATA

**Cadeia disparadora:**
```
/tatou-2.0  detecta sintoma  → dispara /crise-imperatriz --ativar [tipo]
                                       ↓
                              /shield (protecao tecnica)
                                       ↓
                              /security-audit (auditoria seguranca)
                                       ↓
                              /scale-audit (impacto escala)
```

**Cadeia preventiva:**
```
/perfil-mentorada + /dossie-mentorada
       ↓
/crise-imperatriz --auditar
       ↓
/crise-imperatriz --prevenir
       ↓
/raci-imperatriz (quem executa cada protecao)
       ↓
/calendario-imperatriz (plano 90 dias)
```

**Skills adjacentes (nao canibaliza):**
- `/shield` — protecao tecnica continua (codigo, infra, dados)
- `/security-audit` — auditoria de seguranca pontual
- `/scale-audit` — auditoria de prontidao pra escala
- `/raci-imperatriz` — executor (quem faz cada protecao)
- `/gates-imperatriz` — validacao de portas (Pilar 2)
- `/tatou-2.0` — detector e despachante

---

## OUTPUT POR MODO (resumo)

| Modo | Output principal |
|------|------------------|
| `--ativar` | Playbook ativo + cronometro + 3 proximos passos + templates + check-in agendado |
| `--simular` | Cenario + diagnostico de gaps + acoes corretivas |
| `--auditar` | Score por crise + score consolidado + top 5 gaps |
| `--prevenir` | Roadmap 90 dias com responsavel + custo + prazo |

---

## ARQUIVOS DE REFERENCIA

- `OS-8-PLAYBOOKS.md` — playbook completo de cada uma das 8 crises
- `PROTOCOLO-COMUNICACAO.md` — templates de mensagem (cliente, time, publico, advogada, plataforma)
- `CHECKLIST-PREVENCAO.md` — checklist de protecao a ter ANTES da crise
- `EXEMPLOS-CASOS.md` — 3 simulacoes resolvidas (ban Meta R$ 50k/mes, post viral, socia sai)

---

## VERSIONAMENTO

- **v1.0** (atual) — 8 crises, 4 modos, integracao Travessia + Shield
- **v1.5** (planejado) — banco de casos reais por nicho (info-produto, servico, mentoria)
- **v2.0** (planejado) — alerta proativo (le sinais fracos no imperio antes da crise estourar)

---

**Metodo Imperatriz de Crise — propriedade intelectual Tata Goncalves. Pilar 5 da Travessia Imperatriz.**
