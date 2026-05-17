# 03 — Matriz TEAM (Mix de Formatos)

## O que é TEAM

Sistema de classificação de conteúdo por **intenção comunicacional** — não por formato (post/story/reels) e não por canal (IG/LinkedIn). Toda peça publicada cabe em uma e só uma das cinco caixas:

| Letra | Categoria | Pergunta que responde | Métrica natural |
|---|---|---|---|
| **T** | **Teach** (Ensina) | "O que aprendi?" | Save / compartilhamento |
| **E** | **Engage** (Engaja) | "O que você acha?" | Comentário / DM |
| **A** | **Authority** (Autoridade) | "Por que ela?" | Nova seguida / mensagem qualificada |
| **M** | **Monetize** (Vende) | "Quero. Como compro?" | Click / DM de venda |
| **S** | **Story** (Humaniza) | "Quem é ela?" | Reply de story / DM íntima |

> Sim, o acrônimo deveria ser TEAMS — mas TEAM é o nome consagrado e a quinta letra (S) entrou depois. A skill respeita.

## Distribuição padrão (e por que ela existe)

A distribuição **default** é:

| Categoria | % | Lógica |
|---|---|---|
| Teach | 30% | Massa do conteúdo. Constrói reputação técnica. |
| Engage | 25% | Constrói relacionamento e dá sinal pro algoritmo. |
| Authority | 25% | Diferencia de competidor. Sem isso, vira professora. |
| Monetize | 15% | Vende sem cansar. Mais que isso, queima base. |
| Story | 5% | Cola a marca à pessoa. Menos que isso, vira corporate. |

**Soma: 100%.** Sempre.

## Distribuição por Porta da Travessia

A skill **não usa o default** — calibra pela Porta:

### Portas A-D (Descoberta / Identidade / Marca / Posicionamento)
**Foco: construir reputação, ser descoberta**
- Teach: 35%
- Authority: 30%
- Engage: 20%
- Story: 10%
- Monetize: 5%

### Portas E-H (Oferta / Promessa / Pitch / Preço)
**Foco: validar oferta, criar desejo**
- Teach: 25%
- Authority: 25%
- Engage: 25%
- Monetize: 15%
- Story: 10%

### Portas I-N (Funil / Tráfego / Lançamento / Calendário)
**Foco: aquecer base, preparar venda**
- Teach: 25%
- Engage: 25%
- Authority: 20%
- Monetize: 25%
- Story: 5%

### Portas O-R (Vendas / Operação / Atendimento)
**Foco: vender, atender, reter**
- Monetize: 30%
- Authority: 25%
- Teach: 20%
- Engage: 15%
- Story: 10%

### Portas S-T (Time / Receita)
**Foco: profissionalizar, mostrar operação**
- Authority: 30%
- Teach: 25%
- Engage: 20%
- Monetize: 15%
- Story: 10%

### Portas U-Z (Escala / Sucessão)
**Foco: virar movimento, formar legado**
- Authority: 30%
- Story: 25%
- Teach: 20%
- Engage: 15%
- Monetize: 10%

## O que cabe em cada categoria

### T — Teach
- Tutorial passo-a-passo de algo que a mentorada faz no negócio dela
- Quebra de paradigma técnico ("você está fazendo X errado, faça Y")
- Carrossel didático de método/framework
- Mini-aula de 60s (Reels)
- Newsletter explicativa
- Post LinkedIn de "como funciona X"

❌ NÃO é Teach: post motivacional disfarçado de ensino

### E — Engage
- Pergunta direta sobre dilema do cliente ideal
- Story com caixinha de pergunta/enquete
- Post "qual sua experiência com X?"
- Provocação editorial sobre tema do nicho ("opinião impopular: X")
- Pedido de feedback público
- Comentário quente em post de competidor (cuidado, ver boundaries)

❌ NÃO é Engage: pergunta retórica que ninguém responde ("vocês concordam?")

### A — Authority
- Resultado de cliente nomeado (com permissão) com mecanismo explicado
- Bastidor de decisão estratégica com aprendizado nomeado
- Posicionamento claro contra prática comum do nicho
- Anúncio de palco, mídia, parceria
- Number drop (KPI da operação com contexto)
- Carrossel "por dentro do nosso método"

❌ NÃO é Authority: foto na frente de carro / hotel / cenário

### M — Monetize
- CTA direto pra produto/programa
- Página de vendas linkada
- Story com link de checkout
- Anúncio de turma abrindo, vaga abrindo, edital
- Depoimento de cliente com call pra ação
- Post de "tem 3 vagas" / "fecha amanhã"

❌ NÃO é Monetize: post de vibe que termina com "DM se quiser saber mais"

### S — Story
- Decisão pessoal que afeta a marca
- Bastidor de vida com aprendizado relacionado ao negócio
- Marco pessoal (aniversário, casamento, perda) tratado com cuidado
- Story "dia comum no escritório" com pessoa, não com setup
- Post sobre filho/parceiro/família **se** integra com posicionamento

❌ NÃO é Story: foto de café com legenda "bom dia" sem nada por baixo

## Regras de execução do mix

1. **Mix é semanal, não diário.** Não precisa de todas as 5 categorias por dia. Precisa bater % na semana.
2. **Cadência por canal redistribui.** Stories pode rodar mais Story+Engage. LinkedIn mais Teach+Authority. E-mail mais Monetize. A skill calibra.
3. **Monetize concentrado funciona melhor.** Em vez de 1 Monetize por dia, fazer 3-4 num mesmo dia de campanha (efeito enxurrada).
4. **Story raro vale mais.** 5% é pouco mas precioso — quando aparece, marca o mês.
5. **Authority precisa de prova.** Sem print, número, nome, depoimento, foto — não é Authority, é só promessa.

## Como a skill audita o mix

No modo `--auditar`, a skill:

1. Pede 10-30 peças recentes
2. Classifica cada uma em uma categoria TEAM
3. Compara distribuição real vs ideal (pra Porta atual)
4. Sinaliza desvios > 10 pontos percentuais
5. Recomenda redistribuição

Exemplo de saída:

```
Mix declarado (Porta J):    T 25% | E 25% | A 20% | M 25% | S 5%
Mix executado (últimos 30d): T 60% | E 10% | A 15% | M 10% | S 5%

⚠️ Drift de 35 pontos em Teach (sobreoferta)
⚠️ Drift de -15 pontos em Engage (subexposição)
⚠️ Drift de -15 pontos em Monetize (subexposição — perigoso, em Porta de venda)

Recomendação: parar de postar mais 1 carrossel didático por semana, substituir por 1 post de pergunta + 2 posts com CTA pra programa.
```

## Saída JSON

```json
"matriz_team": {
  "teach_pct": 25,
  "engage_pct": 25,
  "authority_pct": 20,
  "monetize_pct": 25,
  "story_pct": 5,
  "porta_referencia": "J",
  "redistribuicao_por_canal": {
    "instagram_stories": {"engage": 50, "story": 30, "teach": 10, "monetize": 10},
    "linkedin": {"teach": 40, "authority": 35, "engage": 20, "monetize": 5},
    "email": {"monetize": 50, "authority": 30, "teach": 20}
  }
}
```
