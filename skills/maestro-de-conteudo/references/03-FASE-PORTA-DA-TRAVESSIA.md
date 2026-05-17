# Fase 3 — Porta da Travessia (~10min)

## O que essa fase entrega

- `~/imperio/mentoradas/[nome]/02-porta-atual.json` com campos `porta` (A-Z) e `nivel` (Princesa/Marquesa/Imperatriz)

## O que o Maestro faz

### Antes de despachar

> **Fase 3 — Porta da Travessia (~10min)**
>
> Rapidinha. Preciso saber em que ponto do teu negócio você está hoje. Isso muda TUDO no calendário — quem está na Porta de Lançamento posta diferente de quem está na Porta de Marca.
>
> Vou te mostrar as 26 Portas (A a Z) agrupadas em 6 estações. Você marca a tua. Se ficar em dúvida entre duas, escolhemos a mais "downstream" (mais avançada).
>
> Bora?

### Despacha (modo simplificado)

Como a Tata pediu pipeline curto, essa fase NÃO roda o `/dossie-mentorada` completo (que é grande). Em vez disso, o Maestro pergunta direto, mostrando as 26 Portas categorizadas:

```
Marca a Porta atual (A-Z) e o nível:

ESTAÇÃO 1 — Descoberta + Identidade + Marca + Posicionamento
  A — Descoberta (entender quem sou)
  B — Identidade (definir o EU)
  C — Marca (símbolos, ritual, linguagem)
  D — Posicionamento (frase + nicho + cliente ideal)

ESTAÇÃO 2 — Oferta + Promessa + Pitch + Preço
  E — Oferta (o que vendo)
  F — Promessa (qual transformação)
  G — Pitch (como apresento)
  H — Preço (quanto cobro)

ESTAÇÃO 3 — Funil + Tráfego + Lançamento + Calendário
  I — Funil (caminho do lead)
  J — Tráfego (de onde vem)
  K — Lançamento (planejar lançamento)
  L — Pré-aquecimento
  M — Aquecimento ativo
  N — Calendário editorial rodando

ESTAÇÃO 4 — Vendas + Operação + Atendimento
  O — Vendas (campanha aberta)
  P — Operação (entrega ativa)
  Q — Atendimento (suporte rodando)
  R — Pós-venda

ESTAÇÃO 5 — Time + Receita
  S — Time (contratando, gerenciando)
  T — Receita (operação financeira)

ESTAÇÃO 6 — Escala + Sucessão
  U — Escala (operação grande)
  V — Influência (mídia, palco)
  W — Movimento (vira referência)
  X — Sucessão (forma sucessoras)
  Y — Legado
  Z — Imperatriz consolidada

NÍVEL atual:
  - Princesa (até 6 meses no nicho, primeira venda)
  - Marquesa (operação rodando, time pequeno, receita previsível)
  - Imperatriz (escala estabelecida, autoridade reconhecida)

Qual a tua Porta + nível?
```

Mentorada responde (ex: "J + Marquesa"). Maestro grava direto:

```json
{
  "porta": "J",
  "porta_nome": "Tráfego",
  "estacao": 3,
  "estacao_nome": "Funil + Tráfego + Lançamento + Calendário",
  "nivel": "Marquesa",
  "registrada_em": "2026-05-09T..."
}
```

### Quando termina

```
✅ Fase 3 concluída — Porta J (Tráfego) | Marquesa

Vamos pra Fase 4 (Linha Editorial)?
- Sim, agora
- Pausa
```

## Por que essa fase é simplificada

A Tata escolheu pipeline curto. O `/dossie-mentorada` completo coleta muito mais (recursos, time, orçamento, dores específicas, etc) — útil pra outras skills, mas excessivo pra montar linha editorial + calendário. O Maestro pega só o mínimo necessário.

Se a mentorada quiser dossiê completo depois, roda `/dossie-mentorada` separadamente — esse trabalho é cumulativo, não substitui.

## Erros comuns

| Sintoma | Reação |
|---|---|
| Mentorada em dúvida entre duas Portas | "Vai na mais avançada (mais pra Z). Calendário acomoda fácil quem está adiantada; quem está atrasada se perde." |
| Mentorada não sabe a Porta | Pergunta diagnóstica: "Você já tem oferta nomeada?" → Sim → E-Z. "Já vendeu pelo menos 3x?" → Sim → I-Z. Vai afunilando. |
| Mentorada quer pular pra X (Sucessão) ambiciosamente | Maestro pede sinal: "Você já formou alguém que substitui você?" — se não, sugere voltar pra Porta real. |

## Não fazer

- ❌ Pular pra Fase 4 sem Porta + nível salvos
- ❌ Aceitar "tô em todas" — Porta é uma só, mesmo que toque várias áreas
- ❌ Sugerir Porta — mentorada decide
