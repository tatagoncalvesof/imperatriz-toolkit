# Os 3 Cenarios — Conservador, Realista, Agressivo

> Toda recomendacao de pricing-dinamico apresenta os 3 cenarios. Nunca um so. A mentorada precisa **ver as opcoes lado a lado pra decidir consciente**.

---

## Por que 3 cenarios (e nao 1, nem 5)

- **1 cenario** = decisao imposta. Mentorada nao internaliza, nao defende.
- **5 cenarios** = paralisia de analise. Mentorada nao decide.
- **3 cenarios** = espelho de risco/retorno. Cada um serve um momento da Travessia.

A mentorada **escolhe o cenario que combina com onde ela esta agora**, nao onde ela quer estar em 12 meses.

---

## Cenario 1 — CONSERVADOR

### Filosofia
"Subir o que da pra subir sem perder ninguem."

### Formula

```
Preco_conservador = Preco_atual x (1.10 a 1.20)
```

Variacao absoluta entre +10% e +20%. Nunca menos (nao vale a pena rodar). Nunca mais (entra no realista).

### Quando usar

- Primeira subida de preco da mentorada
- Posicionamento atual: **Princesa** ou **Duquesa**
- Autoridade ainda em construcao (< 6 meses de prova social)
- Mentorada com aversao a risco alta
- Base de clientes ativa que precisa ser preservada
- Antes de campanha sazonal (subir base pra dar desconto depois)

### Risco esperado

- Perda de volume: **< 5%**
- Perda de clientes existentes: **0-3%**
- Margem ganha: **+3 a +6 pp**
- Receita ganha: **+5 a +15%**

### Calculo de impacto (exemplo)

```
Preco atual: R$ 4.997
Slots/mes: 6
Receita atual: R$ 29.982/mes
Margem atual: 70% (R$ 800 custo variavel)

Preco conservador: R$ 5.497 (+10%)
Slots projetados: 6 (sem perda — elasticidade -0.5 nao age em variacao tao pequena)
Receita projetada: R$ 32.982/mes (+10%)
Margem projetada: 73% (custo continua R$ 800)
```

### Comunicacao ao cliente

Reajuste leve, comunicado com 7-15 dias de antecedencia:

> "Estou ajustando o investimento da mentoria pra R$ 5.497 a partir do mes que vem.
> Quem fechar essa semana ainda entra no valor atual de R$ 4.997."

---

## Cenario 2 — REALISTA

### Filosofia
"Cobrar o que voce vale hoje, calibrado por quem ja te paga e por quem cobra na concorrencia."

### Formula

```
Preco_realista = max(
    Preco_atual x (1.30 a 1.50),
    Mediana_concorrencia x 1.10,
    Custo_variavel / (1 - margem_alvo_70%)
)
```

Pega o **maior** entre 3 referencias:
1. Preco atual + 30 a 50%
2. Mediana da concorrencia + 10% (acima do meio do mercado)
3. Preco que garante margem de 70% no minimo

### Quando usar

- Mentorada tem **6+ meses de operacao** com prova social solida
- Posicionamento: **Duquesa** consolidada ou em **transicao pra Marquesa**
- Tem 5+ cases medios OU 1+ case lendario
- Slot vendido entre 70-90% (saudavel)
- Concorrencia ja precificou alto e validou mercado
- Quer destravar Revenue Gap de 30-50%

### Risco esperado

- Perda de volume: **10-20%** (compensada por margem)
- Perda de clientes existentes: **5-15%** (mas atrai melhor publico)
- Margem ganha: **+7 a +12 pp**
- Receita ganha: **+15 a +35%**

### Calculo de impacto (exemplo)

```
Preco atual: R$ 4.997
Mediana concorrencia: R$ 6.500 -> R$ 6.500 x 1.10 = R$ 7.150
Preco com margem 70%: R$ 800 / 0.30 = R$ 2.667 (nao binda)
Preco_realista = max(R$ 6.996, R$ 7.150, R$ 2.667) = R$ 7.150

Aplicando elasticidade -0.75:
Variacao preco: +43%
Variacao volume: -32%
Slots novos: 6 x 0.68 = 4 slots/mes

Receita projetada: 4 x R$ 7.150 = R$ 28.600/mes (-5% receita)
Margem projetada: (R$ 7.150 - R$ 800) / R$ 7.150 = 89%
```

**Ler o resultado:** receita CAI 5% mas margem SOBE 19pp. Lucro liquido sobe (R$ 25.400 vs R$ 21.000 atuais). Mentorada trabalha menos com cada cliente, atende com mais qualidade, e ainda libera capacidade pra crescer outro vetor.

### Comunicacao ao cliente

Reajuste estrutural — comunicado com 30 dias de antecedencia + janela de "ultima chamada":

> "A partir de [data], a mentoria passa a ter o investimento de R$ 7.150.
> Esse ajuste reflete os 8 cases que entregamos nos ultimos 6 meses,
> a evolucao do metodo e a inclusao de [bonus novo].
>
> Quem fecha ate [data-1] entra no valor de R$ 4.997 ainda.
> A partir de [data], R$ 7.150 e o novo investimento oficial."

---

## Cenario 3 — AGRESSIVO

### Filosofia
"Reposicionar pra premium e cobrar como premium."

### Formula

```
Preco_agressivo = max(
    Preco_atual x (2.0 a 3.0),
    Concorrente_topo x (1.20 a 1.50)
)
```

Pega o **maior** entre:
1. Preco atual x 2 a 3
2. Concorrente do topo do mercado x 1.20 a 1.50 (acima do mais caro)

### Pre-requisitos OBRIGATORIOS

A skill **nao recomenda agressivo sem isso instalado**:

- [ ] **Reposicionamento Luxe completo** (rodar `/luxe-empire` antes — Pilares 1, 2, 4)
- [ ] **3+ cases lendarios publicos** (nao basta caso bom — precisa ser referencia de mercado)
- [ ] **Autoridade midiatica** (entrevista, palco, podcast, livro, coluna)
- [ ] **Posicionamento Marquesa ou Condessa** (nao roda em Princesa ou Duquesa)
- [ ] **Oferta reformulada com `/skill-oferta-irresistivel`** (stack premium ancorado em R$Y)
- [ ] **Mecanismo unico instalado** (rodar `/mecanismo-unico` se ainda nao tem)
- [ ] **Margem operacional alta** (>75% atual — nao da pra fazer agressivo com margem fraca)

Se faltar 2+ desses, **bloqueia o cenario agressivo** e sinaliza pra mentorada o que precisa instalar antes.

### Quando usar

- Mentorada chegou em **Marquesa** ou **Condessa** consolidada
- Quer **mudar de tier** (sair de mentorada media pra referencia de mercado)
- Tem capacidade de **trabalhar com 50% menos clientes** sem quebrar margem
- Quer **filtrar publico** (eliminar perfil de cliente que da trabalho e nao paga premium)
- Esta entrando em **mercado de luxo de fato** (publico C+, B, A)
- Bateu **teto de elasticidade** no realista

### Risco esperado

- Perda de volume: **30-50%**
- Perda de clientes existentes: **40-70%** (parte VAI sair — e desejado)
- Margem ganha: **+15 a +25 pp**
- Receita ganha: **+10 a +50%** (depende do quanto reduz volume)
- Tempo de implementacao: **6-12 meses** (com transicao de publico)

### Calculo de impacto (exemplo)

```
Preco atual: R$ 4.997
Concorrente_topo: R$ 12.000
Preco_agressivo = max(R$ 14.991, R$ 14.400) = R$ 14.991, arredonda R$ 15.000

Aplicando elasticidade -0.75 + reposicionamento Luxe:
Sem Luxe: variacao preco +200% -> volume -150% (impossivel — vira 0)
Com Luxe instalado: elasticidade muda pra -0.4 (publico premium e menos sensivel a preco)
Variacao volume: -80%
Slots novos: 6 x 0.20 = 1-2 slots/mes (boutique)

Receita projetada (cenario otimista): 2 x R$ 15.000 = R$ 30.000/mes
Margem projetada: (R$ 15.000 - R$ 1.500 custo premium) / R$ 15.000 = 90%

OBS: assume custo variavel sobe pra R$ 1.500 (atendimento mais qualificado, brindes, experiencia premium).
```

**Ler o resultado:** receita praticamente igual com 2 clientes em vez de 6. Mentorada libera 67% do tempo. Liberacao de tempo abre espaco pra produto digital escalavel, palestras pagas, livro, palco premium. **A receita real do agressivo nao esta no 1:1 — esta no que a mentorada constroi com o tempo liberado.**

### Comunicacao ao cliente

NAO se comunica como reajuste. Se comunica como **mudanca de tier**.

Estrutura:
1. **Anuncio publico** de novo tier (post + email + video)
2. **Comunicacao individual** pros clientes atuais sobre transicao
3. **Janela de ultima oportunidade** no preco antigo (60-90 dias)
4. **Lancamento oficial** do novo tier com nova oferta

Exemplo:

> "Esse e um anuncio importante. A partir de [data], minha mentoria sai do
> formato atual de R$ 4.997 e passa a ser oferecida em formato boutique:
> 2 vagas/mes, R$ 15.000, com [bonus exclusivos premium].
>
> Pra quem ja era cliente: voce mantem o investimento de R$ 4.997 nas
> renovacoes em 2026 (loyalty rate). Pra quem ainda nao entrou: ate
> [data-1], voce ainda pode entrar no formato atual. A partir de [data],
> apenas o formato boutique."

---

## Tabela comparativa rapida

| Dimensao | Conservador | Realista | Agressivo |
|----------|-------------|----------|-----------|
| **Variacao** | +10 a +20% | +30 a +50% | +100 a +300% |
| **Risco volume** | < 5% | 10-20% | 30-50% |
| **Margem ganha** | +3-6pp | +7-12pp | +15-25pp |
| **Receita ganha** | +5-15% | +15-35% | +10-50% |
| **Posicionamento exigido** | Princesa+ | Duquesa+ | Marquesa+ |
| **Pre-requisitos** | 0 | 6m operacao + 5 cases | Luxe + 3 cases lendarios + autoridade midiatica |
| **Tempo implementacao** | 7-15 dias | 30 dias | 6-12 meses |
| **Comunicacao** | Reajuste leve | Reajuste estrutural | Mudanca de tier |

---

## Regras de decisao entre cenarios

### Escolha CONSERVADOR quando:
- Primeira subida da mentorada
- Aversao a risco alta
- Base de clientes ativa critica
- Slot 60-80%
- Posicionamento ainda em construcao

### Escolha REALISTA quando:
- 6+ meses de operacao
- Slot >80% por 30+ dias
- 5+ cases solidos
- Concorrencia ja validou preco mais alto
- Quer destravar Revenue Gap em 30-50%
- Margem atual <75%

### Escolha AGRESSIVO quando:
- Bateu teto de receita do realista
- Marquesa+ consolidada
- 3+ cases lendarios publicos
- Capacidade saturada (>95%)
- Quer filtrar publico
- Tem tempo/dinheiro pra reposicionamento de 6-12 meses
- Margem atual >75%

---

## Erros comuns na escolha (anti-patterns)

1. **Escolher agressivo sem Luxe** — vira preco fora do mercado, nao vende
2. **Escolher conservador quando da pra realista** — deixa dinheiro na mesa
3. **Pular conservador e ir direto pra agressivo** — perde 80% da base de uma vez
4. **Mexer em preco sem mecanismo unico instalado** — concorrencia copia o preco, nao copia o mecanismo
5. **Aplicar agressivo em mercado de baixa elasticidade** (saude regulada, B2B governo) — sem flexibilidade

---

## Frequencia de re-execucao

- **Conservador:** pode rodar a cada 90 dias
- **Realista:** pode rodar a cada 6 meses
- **Agressivo:** maximo 1x por ano (e exige toda a jornada de Luxe Empire)

Nunca aplicar 2 cenarios consecutivos sem janela de respiro de **90 dias minimo**.

---

**Os 3 Cenarios — propriedade intelectual Tata Goncalves.**
