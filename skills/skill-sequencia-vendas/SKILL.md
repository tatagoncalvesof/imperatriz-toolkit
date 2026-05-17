---
name: skill-sequencia-vendas
description: >
  Cria sequencias de vendas multi-canal completas: email + WhatsApp + retargeting + SMS.
  Especializada no mercado brasileiro de infoprodutos com funis de lancamento e perpetuo.
  Inclui templates por etapa do funil, timing otimizado, automacoes, e metricas de acompanhamento.
  Use quando o usuario pedir "sequencia de vendas", "automacao de email", "follow-up WhatsApp",
  "sequencia de emails", "cadencia de vendas", "nutrição de leads", "funil de email",
  "sequencia de carrinho aberto", "sequencia pos-webinar", ou qualquer fluxo de comunicacao
  multi-canal para vendas.
---

# Sequencia de Vendas Multi-Canal — Mercado BR

## Contexto
- **Canais:** Email + WhatsApp + Retargeting Ads + SMS (opcional)
- **Mercado:** Brasil — infoprodutos, mentorias, formacoes
- **Ferramentas comuns:** ActiveCampaign, RD Station, Leadlovers, Hotmart, Eduzz

## Processo

### 1. Definicao da Sequencia
Perguntar ao usuario:
- Tipo: lancamento, perpetuo, carrinho aberto, pos-webinar, onboarding
- Produto/oferta (nome, preco, beneficio)
- Duracao da sequencia (3, 7, 14, 21 dias)
- Canais disponiveis (email, WhatsApp, SMS, retargeting)
- Gatilho de entrada (inscricao, download, webinar, visita PV)

### 2. Arquiteturas de Sequencia

#### Tipo 1: Pos-Webinar (7 dias) — MAIS COMUM
```
GATILHO: Participou do webinar OU assistiu replay

DIA 0 (Imediato)
├── Email: Replay + Oferta + Bonus
├── WhatsApp: "Gostou da aula? Inscricoes abertas"
└── Retargeting: Video oferta para viewers do webinar

DIA 1
├── Email: Depoimento forte + Bonus
├── WhatsApp: Depoimento (audio ou texto)
└── Retargeting: Carrossel depoimentos

DIA 2
├── Email: Quebra de Objecao #1 ("sera que funciona?")
└── Retargeting: Video quebrando objecao

DIA 3
├── Email: Conteudo de valor + menção sutil da oferta
├── WhatsApp: Dica rapida + "ja viu a oferta?"
└── Retargeting: Imagem oferta + bonus

DIA 5
├── Email: ⚠️ Bonus expirando em 48h
├── WhatsApp: "Os bonus vencem em 48h"
└── Retargeting: Urgencia — countdown

DIA 6
├── Email: Ultimo dia + depoimento final
└── WhatsApp: "Amanha encerra"

DIA 7 (Manha)
├── Email: ULTIMO DIA
├── WhatsApp: "Hoje e o ultimo dia"
└── Retargeting: "Encerra hoje"

DIA 7 (23h)
├── Email: "Encerra a meia-noite"
├── WhatsApp: "Ultima chance"
└── Retargeting: Pausa apos meia-noite
```

#### Tipo 2: Carrinho Aberto (5 dias)
```
GATILHO: Visitou pagina de vendas OU iniciou checkout

HORA 1
├── Email: "Percebi que voce visitou..."
└── WhatsApp: "Vi que voce estava olhando [produto]"

DIA 1
├── Email: Depoimento + FAQ
└── Retargeting: Depoimento video

DIA 2
├── Email: Objecao principal respondida
└── WhatsApp: Audio da mentora respondendo duvida

DIA 3
├── Email: Bonus extra por tempo limitado
└── Retargeting: Bonus + countdown

DIA 5
├── Email: "Ultima oportunidade — encerra hoje"
├── WhatsApp: "Ultimo dia [produto] com condicao especial"
└── Retargeting: Encerra hoje
```

#### Tipo 3: Nurture de Lead (14 dias)
```
GATILHO: Baixou lead magnet ou se inscreveu na lista

DIA 0: Email de boas-vindas + entrega do material
DIA 1: Email "Conseguiu acessar? Dica para aproveitar melhor"
DIA 3: Email conteudo valor — mini-insight #1
DIA 5: Email conteudo valor — mini-insight #2 + menção da oferta
DIA 7: Email case de sucesso
DIA 9: Email conteudo valor — mini-insight #3
DIA 11: Email convite para webinar/aula gratuita
DIA 14: Email oferta direta (se nao converteu em nenhuma etapa)
```

#### Tipo 4: Onboarding Novo Aluno (7 dias)
```
GATILHO: Comprou o produto

DIA 0 (Imediato)
├── Email: "Bem-vinda! Acesse aqui" + primeiros passos
├── WhatsApp: "Parabens pela decisao! Acesse: [link]"

DIA 1
├── Email: "Como aproveitar ao maximo" + dica #1
└── WhatsApp: "Ja comecou? Dica: comece pelo modulo X"

DIA 3
├── Email: "Como esta indo? Estou aqui se precisar"

DIA 5
├── Email: Conteudo complementar + convite comunidade

DIA 7
├── Email: "1 semana! Como esta? + pesquisa NPS"
├── WhatsApp: "Tudo bem? Conta como ta sendo a experiencia"
```

### 3. Templates de Email Detalhados

#### Email de Boas-Vindas / Entrega
```
Assunto: ✅ [Material] pronto! Acesse aqui, [nome]

[Nome], que bom ter voce aqui!

Aqui esta o que voce pediu:
→ [Link para o material]

Como aproveitar ao maximo:
1. [Dica pratica 1]
2. [Dica pratica 2]
3. [Dica pratica 3]

Nos proximos dias, vou te enviar mais conteudos
que vao complementar isso.

Fique de olho no seu email!

[Assinatura]

PS: Me responde esse email me contando qual e o seu
maior desafio com [tema]. Eu leio todas as respostas.
```

#### Email de Conteudo (Valor)
```
Assunto: [Insight contra-intuitivo ou dado surpreendente]

[Nome], preciso te contar uma coisa...

[Abrir com dado, historia curta, ou afirmacao que gera curiosidade]

[2-3 paragrafos de conteudo valioso — insight pratico e aplicavel]

[Ponte sutil para o produto:]
"Esse e um dos [numero] pilares que ensino no [produto].
Se quiser ir mais fundo: [link]"

[Assinatura]
```

#### Email de Depoimento
```
Assunto: "[Resultado impressionante]" — [Nome da aluna]

[Nome], leia o que a [aluna] me escreveu:

"[Depoimento entre aspas — especifico, com numeros,
emocional, transformador]"

— [Nome], [profissao/cidade]

[Contexto: Ela comecou [situacao antes] e em [prazo] alcancou [resultado]]

Quer o mesmo?

→ [Link da oferta]

[Assinatura]
```

#### Email de Objecao
```
Assunto: "Sera que funciona pra mim?"

[Nome], eu sei que essa duvida esta na sua cabeca.

E eu respeito isso. Toda decisao importante merece reflexao.

Mas deixa eu te mostrar os fatos:

1️⃣ [Dado/estatistica que comprova]
2️⃣ [Depoimento de alguem "igual" ao lead]
3️⃣ [Garantia que elimina o risco]

O unico cenario onde NAO funciona:
se voce nao aplicar nada do que vai aprender.

Se voce esta disposta a se comprometer, os resultados vem.

→ [Link da oferta]

[Assinatura]

PS: Tem 7 dias de garantia. Se nao gostar, devolvo 100% do valor.
Voce nao tem nada a perder.
```

#### Email de Urgencia
```
Assunto: ⚠️ [Bonus/Preco/Vagas] encerra em [tempo]

[Nome], nao vou enrolar.

Em [tempo], [o que vai acontecer]:
→ Os bonus de R$[valor] vao ser removidos
→ O preco volta para R$[valor cheio]
→ As vagas se encerram

Se voce assistiu [webinar/aula] e sentiu que faz sentido:
→ [Link de compra]

Depois de [deadline], nao ha como voltar atras.

[Assinatura]
```

### 4. Templates de WhatsApp

#### Principios de WhatsApp para Vendas BR
- **Tom:** Pessoal, casual, como uma amiga
- **Tamanho:** Maximo 3-4 linhas (ninguem le mensagens longas)
- **Audio:** Funciona MUITO bem no BR (30-60s max)
- **Horario:** 9h-12h ou 18h-21h (evitar madrugada/almoco)
- **Frequencia:** Max 1 msg/dia durante campanha
- **LGPD:** Opt-in obrigatorio para envio

#### Mensagem Tipo 1: Convite Suave
```
Oi [nome]! 👋

A Tata vai fazer uma aula ao vivo especial sobre [tema].

📅 [Data] às [hora]
🔗 [Link inscricao]

E gratuita. Acho que voce vai gostar!
```

#### Mensagem Tipo 2: Follow-up Pos-Evento
```
[Nome], gostou da aula de ontem? 🔥

As inscricoes do [produto] estão abertas com bonus especial.

Se tiver interesse, posso te mandar os detalhes?
```

#### Mensagem Tipo 3: Urgencia
```
Oi [nome]! As inscricoes do [produto] encerram hoje às 23:59.

Depois disso, sem bonus e preco normal.

Se tiver duvida, me manda aqui que respondo rapido! 💛
```

#### Mensagem Tipo 4: Audio Pessoal (ALTA CONVERSAO)
```
[TRANSCRICAO DO AUDIO — 30-60s]

"Oi [nome], aqui e a Tata! Queria te falar pessoalmente...
Vi que voce se inscreveu na aula e queria saber se
gostou. Se tiver alguma duvida sobre o [produto],
pode me mandar aqui que eu mesma respondo. Beijo!"
```

### 5. Retargeting Complementar

#### Audiencias para Retargeting por Etapa
| Etapa da Sequencia | Audiencia | Criativo |
|--------------------|-----------|----------|
| Dia 0-1 | Webinar viewers | Video replay + oferta |
| Dia 2-3 | PV visitors sem compra | Depoimento + bonus |
| Dia 4-5 | Checkout abandonado | Urgencia + bonus extra |
| Dia 6-7 | Engajados sem conversao | Countdown + ultimo dia |

### 6. Automacoes e Condicoes

```
LOGICA DE AUTOMACAO:

SE lead COMPROU → Mover para sequencia ONBOARDING
SE lead ABRIU email objecao → Enviar email especifico
SE lead NAO ABRIU 3 emails seguidos → Reenviar com assunto diferente
SE lead CLICOU no link da oferta → Tag "interesse_alto" → WhatsApp priorizado
SE lead ASSISTIU webinar completo → Prioridade maxima no retargeting
SE lead ABANDONOU checkout → Sequencia checkout em 1 hora
```

### 7. Metricas por Canal

| Canal | Metrica | Meta | Bom | Otimo |
|-------|---------|------|-----|-------|
| Email | Taxa abertura | > 25% | 30-40% | > 45% |
| Email | Taxa clique | > 3% | 4-6% | > 8% |
| Email | Taxa conversao | > 1% | 2-3% | > 5% |
| WhatsApp | Taxa leitura | > 80% | 85-90% | > 95% |
| WhatsApp | Taxa resposta | > 15% | 20-30% | > 40% |
| Retargeting | CTR | > 1% | 1.5-2.5% | > 3% |
| Retargeting | ROAS | > 3x | 5-8x | > 10x |

### 8. Timing Otimizado (Brasil)

| Canal | Melhor Horario | Pior Horario |
|-------|---------------|-------------|
| Email | Ter-Qui 9h-10h ou 19h-20h | Seg manha, Sex tarde, fim de semana |
| WhatsApp | 9h-11h ou 18h-20h | Madrugada, horario de almoco |
| SMS | 10h ou 17h | Depois das 20h |
| Retargeting | Sempre ativo (algoritmo otimiza) | — |

## Output

Entregar os seguintes arquivos por sequencia:
- `SEQUENCIA-[TIPO]-[PRODUTO]-OVERVIEW.md` — Mapa da sequencia completa
- `SEQUENCIA-[TIPO]-[PRODUTO]-EMAILS.md` — Todos os emails com assunto + corpo
- `SEQUENCIA-[TIPO]-[PRODUTO]-WHATSAPP.md` — Mensagens de WhatsApp + audios
- `SEQUENCIA-[TIPO]-[PRODUTO]-RETARGETING.md` — Criativos de retargeting por etapa
- `SEQUENCIA-[TIPO]-[PRODUTO]-AUTOMACAO.md` — Logica de automacao
