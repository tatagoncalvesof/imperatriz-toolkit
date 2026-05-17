# 07 — Matriz Porta × Conteúdo

## O que essa matriz resolve

A linha editorial **não é estática**. Ela calibra com a Porta atual da Travessia. Sem essa matriz, a mentorada gera linha editorial uma vez e nunca mais revisa — até descobrir, três meses depois, que está postando "conteúdo de descoberta" numa Porta de venda.

Esta matriz mostra, pra cada Porta da Travessia:

1. **Foco** narrativo dominante
2. **Pilares** que ganham peso (e os que perdem)
3. **Mix TEAM** ajustado
4. **Cadência** ajustada
5. **Vocabulário** adicional que entra (e o que sai)
6. **Boundaries** específicos da Porta (ex: Porta de lançamento tem regras de comunicação diferentes)

## Mapa por Porta (resumido)

> A Travessia tem 26 Portas (A-Z). Aqui o mapa condensado por **estação** (grupos de Portas).

### Estação 1 — Portas A-D (Descoberta + Identidade + Marca + Posicionamento)

| Camada | Estado |
|---|---|
| **Foco narrativo** | "Quem eu sou + por que importo" |
| **Pilares dominantes** | Cultura (40%), Autoridade (30%), Cliente (20%), Mecanismo (10%) |
| **Mix TEAM** | T 35% / A 30% / E 20% / S 10% / M 5% |
| **Cadência** | Baixa-média (Feed 2-3, Reels 1, LinkedIn 1-2, Stories 5-7 seq/sem) |
| **Vocabulário extra ON** | Manifesto, posicionamento, bastidor de identidade |
| **Vocabulário extra OFF** | CTA de venda dura, urgência fabricada |
| **Boundary específico** | Não vender ainda — base ainda está se formando |

### Estação 2 — Portas E-H (Oferta + Promessa + Pitch + Preço)

| Camada | Estado |
|---|---|
| **Foco narrativo** | "Tem solução. E ela tem nome." |
| **Pilares dominantes** | Mecanismo (35%), Cliente (30%), Autoridade (25%), Cultura (10%) |
| **Mix TEAM** | T 25% / A 25% / E 25% / M 15% / S 10% |
| **Cadência** | Média (Feed 3, Reels 2, LinkedIn 2, Stories 7-10, Email 1-2, WhatsApp 2-3) |
| **Vocabulário extra ON** | Nome do mecanismo, nome do programa, transformação prometida |
| **Vocabulário extra OFF** | Promessa vaga, "transforme sua vida" |
| **Boundary específico** | Validar oferta com base antes de escalar — se base não responde a hint de oferta, refazer oferta |

### Estação 3 — Portas I-N (Funil + Tráfego + Lançamento + Calendário)

| Camada | Estado |
|---|---|
| **Foco narrativo** | "Tô construindo isso aqui pra te entregar X" |
| **Pilares dominantes** | Mecanismo (35%), Cliente (30%), Autoridade (20%), Cultura (15%) |
| **Mix TEAM** | M 25% / T 25% / E 25% / A 20% / S 5% |
| **Cadência** | Alta (Feed 4-5, Reels 2-3, LinkedIn 2-3, Stories 10-14, Email 2, WhatsApp 3-5) |
| **Vocabulário extra ON** | Vagas, turma, abertura, edital, pré-aquecimento |
| **Vocabulário extra OFF** | "Talvez abra", "ainda não sei se" — urgência exige clareza |
| **Boundary específico** | Calendário comanda — toda peça precisa estar conectada à narrativa do lançamento |

### Estação 4 — Portas O-R (Vendas + Operação + Atendimento)

| Camada | Estado |
|---|---|
| **Foco narrativo** | "Está aberto. Está acontecendo. Vem." |
| **Pilares dominantes** | Mecanismo (30%), Cliente (25%), Autoridade (25%), Cultura (20%) |
| **Mix TEAM** | M 30% / A 25% / T 20% / E 15% / S 10% |
| **Cadência** | Alta-intensa (Feed 4, Reels 2, LinkedIn 2, Stories 14+ pra atendimento, Email 2-3, WhatsApp 5-7) |
| **Vocabulário extra ON** | "Última semana", "X vagas", "fecha hoje", depoimento real |
| **Vocabulário extra OFF** | Genéricos — venda quente exige especificidade |
| **Boundary específico** | Stories vira canal de atendimento — voz mais próxima, mais resposta a perguntas |

### Estação 5 — Portas S-T (Time + Receita)

| Camada | Estado |
|---|---|
| **Foco narrativo** | "Empresa de verdade. Operação de gente grande." |
| **Pilares dominantes** | Cultura (30%), Autoridade (30%), Cliente (20%), Mecanismo (20%) |
| **Mix TEAM** | A 30% / T 25% / E 20% / M 15% / S 10% |
| **Cadência** | Média-alta (Feed 4, Reels 2, LinkedIn 2-3, Stories 7-10, Email 2, WhatsApp 3-5) |
| **Vocabulário extra ON** | Time, contratamos, decisão estrutural, dado da operação |
| **Vocabulário extra OFF** | Romantização de "empreender sozinha" |
| **Boundary específico** | Time aparece com nome (com permissão) — operação invisível não é operação |

### Estação 6 — Portas U-Z (Escala + Sucessão)

| Camada | Estado |
|---|---|
| **Foco narrativo** | "Movimento, não programa. Legado, não venda do mês." |
| **Pilares dominantes** | Cultura (35%), Autoridade (30%), Cliente (20%), Mecanismo (15%) |
| **Mix TEAM** | A 30% / S 25% / T 20% / E 15% / M 10% |
| **Cadência** | Média (Feed 3, Reels 1-2, LinkedIn 3-4 — vira canal B2B principal, Stories 7-10, Email 1-2, WhatsApp 2-3) |
| **Vocabulário extra ON** | Sucessão, legado, escola, trono, conselho |
| **Vocabulário extra OFF** | Linguagem operacional ("vagas abrindo") — escala é movimento, não promo |
| **Boundary específico** | LinkedIn assume protagonismo — Imperatriz fala com pares, mídia, parceiros |

## Como a skill usa a matriz

### No `--gerar`

A skill lê a Porta atual do dossiê e:
1. Aplica a distribuição de pilares da estação correspondente
2. Aplica o mix TEAM da estação
3. Aplica a cadência da estação (multiplicada pelo fator do time)
4. Adiciona vocabulário extra ON/OFF da estação ao vocabulário base
5. Adiciona boundaries específicos da Porta aos boundaries base

### No `--evoluir`

Quando a mentorada muda de Porta:
1. Skill identifica Porta anterior + Porta nova
2. Calcula **diff** entre as duas estações
3. Apresenta pra mentorada: "vai mudar isso, isso e isso"
4. Mentorada aprova/ajusta
5. Versiona linha editorial (v2, v3...)
6. Avisa skills consumidoras (calendario, linkedin, etc) que houve mudança

### No `--auditar`

A skill checa se conteúdo recente está aderente à Porta atual:
- Mentorada na Porta J postando 70% de conteúdo de descoberta? Drift detectado.
- Mentorada na Porta U postando vagas como Porta N? Drift detectado.

## Saída JSON

```json
"matriz_porta_conteudo": {
  "porta_atual": "J",
  "estacao": "I-N — Funil/Tráfego/Lançamento/Calendário",
  "foco_narrativo": "Tô construindo isso aqui pra te entregar X",
  "pilares_pesos_ajustados": {
    "Mecanismo": 35,
    "Cliente": 30,
    "Autoridade": 20,
    "Cultura": 15
  },
  "vocabulario_extra_on": ["vagas", "turma", "abertura", "edital", "pré-aquecimento"],
  "vocabulario_extra_off": ["talvez abra", "ainda não sei se"],
  "boundary_especifico": "Calendário comanda — toda peça conectada à narrativa do lançamento",
  "porta_anterior": {
    "id": "I",
    "ajustes_feitos": ["aumentou Mecanismo de 25% pra 35%", "adicionou vocabulário de lançamento"]
  },
  "porta_proxima": {
    "id": "K",
    "preparacao": ["começar a coletar depoimentos pra Porta L (Pitch)", "preparar copy de venda"]
  }
}
```
