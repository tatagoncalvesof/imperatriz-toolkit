# Janelas de Aumento — Gatilhos, Cadencia, Comunicacao

> Janela de aumento e o **periodo limitado** em que a mentorada **deve** subir o preco. Nao e opcao, e gatilho. Sistema vivo de pricing **abre janela sozinho** quando indicador bate meta.

---

## A regra do sistema vivo

Preco estatico **mata margem em 4 vetores**:

1. Capacidade lotada continua cobrando preco de capacidade ociosa
2. Sazonalidade alta (alta demanda) e tratada como sazonalidade baixa
3. Reposicionamento (mais autoridade) nao e refletido no preco
4. Cliente fiel paga o mesmo que cliente novo (sem premio de retencao)

Janela de aumento corrige os 4. Cada uma com gatilho **objetivo** (nao subjetivo).

---

## Matriz mestra de gatilhos

| Gatilho | Indicador objetivo | Acao | Cadencia | Frequencia maxima |
|---------|-------------------|------|----------|-------------------|
| **G1 — Capacidade saudavel** | Slot vendido > 80% por 30 dias | +10% | Imediato (proxima venda) | A cada 90 dias |
| **G2 — Capacidade sustentada** | Slot vendido > 80% por 60 dias consecutivos | +20% (cumulativo se G1 nao foi aplicado) | Em 7 dias | A cada 90 dias |
| **G3 — Capacidade saturada** | Slot vendido > 95% (lista de espera ativa) | +30% | Em 48h | A cada 90 dias |
| **G4 — Sazonalidade alta** | Mes historicamente forte | -30% ancoragem (preco real fica, ancoragem mostra desconto) | Janela de 7 dias | 2x/ano max |
| **G5 — Black Friday/Datas | Black Friday, aniversario marca, fim de ano | -30% a -40% ancoragem | Janela de 7 dias | 2x/ano max |
| **G6 — Ex-cliente recompra** | Cliente que ja comprou ha 3+ meses retorna | -50% (recovery rate) OU manter (premium loyalty) | Imediato no contato | Sem limite |
| **G7 — Reposicionamento estrutural** | Saiu de Princesa pra Duquesa, ou Duquesa pra Marquesa | +50% a +100% | Em 30 dias com transicao publica | 1x/ano max |
| **G8 — Caso de sucesso medio** | Novo case medio entregue | +5% | Em 15 dias | A cada 3 cases medios |
| **G9 — Caso lendario** | Case publico que vira referencia (midia, palco, viral) | +10% | Em 7 dias | Por case lendario |
| **G10 — Bate meta de receita** | Faturamento mensal bate meta 12 meses | Recalibrar com novo cenario realista | Em 30 dias | Quando bate |
| **G11 — Saiu produto novo no stack** | Adicionou bonus, modulo, comunidade premium | +5% a +10% | Imediato | Por adicao |
| **G12 — Custo subiu** | Custo variavel/cliente subiu >15% | +10% (preservar margem) | Em 7 dias | Quando custo sobe |

---

## Gatilho G1 — Capacidade saudavel (>80% por 30 dias)

### Quando ativa
Slot vendido > 80% (ex: 5 de 6 vagas/mes vendidas) por **30 dias consecutivos**.

### Acao
+10% no preco. Aplica na proxima venda nova.

### Por que +10% e nao +5% ou +20%
- +5% e ruido — cliente nao percebe, nao gera reposicionamento
- +20% e cenario realista, exige comunicacao estrutural
- +10% e o **degrau certo** — cliente novo nem sente, mentorada captura margem

### Comunicacao ao cliente

**Pra lead quente que ainda nao decidiu:**

> "Oi [nome], rapidinho.
>
> Minha agenda fechou 5 das 6 vagas desse mes. Ja vou abrir as do mes
> que vem, mas com um pequeno reajuste de R$ 4.997 pra R$ 5.497.
>
> Se voce ja decidiu, fecha hoje no valor atual. Se ainda esta em duvida,
> vamos conversar?"

**Pra base de email/whatsapp morna:**

> "Aviso rapido: a partir de [data], o investimento da mentoria passa
> de R$ 4.997 pra R$ 5.497 (10% de reajuste).
>
> Quem ja estava considerando: ate [data-1] o valor antigo continua.
> Depois disso, novo valor pra todo mundo."

**Pra cliente atual que vai renovar:**

> "Voce que ja e cliente nao tem reajuste agora. Continua R$ 4.997 na
> renovacao. Esse reajuste vale so pra cliente novo a partir de [data]."

### Anti-pattern

NAO comunicar como "promocao acabando" se nao tem promocao real. **Sistema vivo de pricing nao usa falsa escassez.** O gatilho real e: "agenda esta cheia, preco sobe pra calibrar demanda."

---

## Gatilho G2 — Capacidade sustentada (>80% por 60 dias)

### Quando ativa
Slot continua > 80% por 60 dias consecutivos. Se G1 ja foi aplicado, aplica +10% adicional. Se nao foi, aplica +20%.

### Acao
+20% (cumulativo) ou aplicar G1+G2 sequencial.

### Por que dispara em 60 dias
Capacidade sustentada por 2 meses **prova que demanda nao foi acidente**. Eh tendencia. Sistema cobra a tendencia, nao a media historica antiga.

### Comunicacao ao cliente

Comunicado mais formal que G1, com 7 dias de antecedencia:

> "Querida lista, preciso comunicar uma decisao importante.
>
> Minha agenda esta operando entre 90-100% ha 2 meses consecutivos.
> Isso significa que a demanda pelo metodo cresceu, e pra continuar
> entregando com qualidade, preciso ajustar o investimento.
>
> A partir de [data + 7 dias], a mentoria passa de R$ 4.997 pra R$ 5.997.
>
> Se voce ja estava considerando, [data + 7 dias] e o ultimo dia no
> valor atual. A partir disso, R$ 5.997 e o novo investimento oficial."

---

## Gatilho G3 — Capacidade saturada (>95% + lista de espera)

### Quando ativa
Slot >95% **E** existe lista de espera com 3+ pessoas qualificadas.

### Acao
+30% em 48h. Sem janela de transicao (lista de espera ja aceitou esperar — aceita o novo preco).

### Por que e tao rapido
Lista de espera e **demanda nao atendida** — mercado sinalizando que preco esta abaixo do valor percebido. Sistema responde rapido: sobe ate normalizar lista de espera.

### Comunicacao ao cliente

**Pra lista de espera (pessoas que pediram pra entrar quando abrir):**

> "Oi [nome], abriu vaga pra [mes]. Atualizo voce em 2 coisas:
>
> 1. Voce e a [posicao] da minha lista de espera, prioridade na vaga
> 2. O investimento atualizou pra R$ 6.497 (de R$ 4.997)
>
> Se ainda faz sentido, te mando o link. Se nao, sem problema, libera
> a vaga pro proximo da fila."

### Importante
Mantem o **respeito** com a lista. Quem aceitou esperar ja indicou alta intencao. Se nao aceitar o novo preco, libera a vaga sem ressentimento.

---

## Gatilho G4 — Sazonalidade alta

### Quando ativa
Mes historicamente forte do nicho (ex: janeiro pra mentoria, novembro pra Black Friday, abril pra produtos academicos).

### Acao
**Nao sobe preco real.** Em vez disso, ancora o preco real como **"valor com desconto"**.

### Por que nao sobe
Sazonalidade alta = demanda alta de pessoas em **pico emocional de decisao**. Subir preco aqui e suicidio comercial. O movimento certo e:
- Manter o preco real
- Ancorar como desconto sobre **R$Y** (valor real do stack)
- Criar urgencia legitima de janela de 7 dias

### Estrutura da janela sazonal

```
Dia 1 (segunda) — Comunicar abertura da janela
Dia 2-3 — Conteudo de aquecimento (cases, depoimentos)
Dia 4-5 — Pico de oferta (lives, q&a)
Dia 6 — Lembrete urgencia
Dia 7 (domingo 23h) — Encerramento
```

### Comunicacao ao cliente

> "Janeiro e mes de virar a chave. Por isso, ate domingo 23h voce entra
> na mentoria com o investimento de R$ 4.997 (valor real do stack:
> R$ 49.970 — voce paga 10x menos).
>
> A partir de segunda, o valor volta pra R$ 5.997 (preco oficial 2026)
> e ai voce vai precisar esperar a proxima janela em [data futura]."

---

## Gatilho G5 — Black Friday / Datas Comemorativas

### Quando ativa
Black Friday, aniversario da marca, fim de ano, dia da mae/dos pais (se relevante pro nicho).

### Acao
-30% a -40% ancoragem sobre preco realista. **NUNCA sobre preco conservador** (perde margem real).

### Estrutura

```
Preco realista (base): R$ 7.150
"Desconto Black Friday 40%": R$ 4.290
Comunicado: "voce economiza R$ 2.860"
```

### Regra dura
Se a mentorada nunca subiu o preco pro realista (ainda esta em R$ 4.997), **nao tem margem pra dar 40% de desconto**. Solucao: subir pra realista 60 dias antes da Black Friday, depois ancorar desconto. Nunca improvisar.

---

## Gatilho G6 — Ex-cliente recompra

### Quando ativa
Cliente que ja comprou ha 3+ meses entra em contato pra reativar/renovar.

### Acao (decisao por contexto)

**Opcao A — Recovery rate (-50%):**
- Cliente nao consumiu 100% do programa
- Saiu insatisfeito
- Mentorada quer reconquistar
- Preco: 50% do atual (R$ 4.997 -> R$ 2.498)

**Opcao B — Loyalty premium (manter ou +5%):**
- Cliente concluiu programa anterior
- Esta em momento de evolucao (proximo nivel)
- Mentorada quer renovacao premium
- Preco: igual ao atual ou +5% como upgrade

**Opcao C — Bonus de loyalty (mesmo preco + bonus exclusivo):**
- Cliente ativo, satisfeito, indica
- Preco: mantido + bonus de fidelidade (acesso comunidade vitalicio, sessao 1:1 extra, etc)

### Como decidir

Pergunta pra mentorada:
1. Cliente saiu satisfeito? -> Opcao B ou C
2. Cliente saiu insatisfeito ou sumiu? -> Opcao A
3. Cliente eh embaixador ativo (indica, divulga)? -> Opcao C

### Comunicacao

**Opcao A:**
> "[Nome], que bom que voltou. Eu queria te dar uma chance especial de
> retomar: R$ 2.498 (50% do valor atual) pra voce voltar pro programa
> e finalizar o que comecou. Vale ate [data]. Topa?"

**Opcao C:**
> "[Nome], como voce ja foi cliente, voce nao paga reajuste. Continua
> R$ 4.997. E como bonus de fidelidade, voce ganha [bonus]. Quando voce
> quer comecar?"

---

## Gatilho G7 — Reposicionamento estrutural

### Quando ativa
Mentorada sobe de tier de posicionamento (ver `luxe-empire`):
- Princesa -> Duquesa
- Duquesa -> Marquesa
- Marquesa -> Condessa

### Acao
+50% a +100% de uma vez. **Comunicado como mudanca de tier, nao como reajuste.**

### Janela
30 dias com transicao publica. Estrutura:

```
Dia 1 — Anuncio do novo tier (post + email + video)
Dia 1-15 — Janela "ultimo mes do preco antigo"
Dia 16-30 — Janela "ultima semana do preco antigo"
Dia 31 — Novo tier oficial
```

### Comunicacao

Comunicado em formato de **carta**, nao em formato de email frio:

> "Hoje eu quero te contar uma decisao que demorou 2 anos pra acontecer.
>
> [Historia de evolucao do metodo, 3-5 paragrafos]
>
> A partir de [data + 30 dias], minha mentoria passa a operar em formato
> [novo formato]: [N] vagas/mes, R$ [novo preco], [novos bonus exclusivos].
>
> Pra quem ja era cliente: voce mantem [politica de loyalty].
> Pra quem ainda nao entrou: voce tem ate [data] no valor atual de
> R$ [valor atual]. Depois, novo tier."

---

## Gatilho G8/G9 — Cases (medio e lendario)

### Quando ativa

**G8 (medio):** mentorada acumula 3 cases novos com resultado validavel (numero, prazo, depoimento)
**G9 (lendario):** 1 case que vira referencia publica (midia, palco grande, viral, contrato com marca grande)

### Acao
- G8: +5% (cumulativo a cada 3 cases)
- G9: +10% (por case lendario)

### Estrutura
Atualizacao de pagina de vendas + email de comunicado:

> "Acabei de fechar [resultado lendario] com [cliente lendario]. Por
> conta dessa evolucao, atualizei o investimento pra R$ [novo preco]
> a partir de [data + 7 dias]. Se voce ja estava decidindo, ate [data]
> voce pega no valor atual."

---

## Gatilho G10 — Bate meta de receita

### Quando ativa
Mentorada bate meta de faturamento de 12 meses **antes** do prazo.

### Acao
**Nao sobe preco automaticamente.** Em vez disso, **roda novo `/pricing-dinamico-imperatriz --gerar`** com nova realidade pra recalibrar todos os 3 cenarios.

### Por que nao automatico
Bater meta antes do prazo pode significar:
- Demanda real cresceu (sinal pra subir)
- Mercado entrou em momento bom (sinal pra subir mas com sazonalidade)
- Mentorada otimizou conversao (nao necessariamente pricing)
- Mix de produtos mudou (precisa recalibrar tudo)

A skill **roda novamente** pra ver onde encaixa o cenario novo.

---

## Gatilho G11 — Stack cresceu

### Quando ativa
Mentorada adicionou item novo no stack (modulo, bonus, comunidade premium, sessao extra, etc).

### Acao
+5% a +10% imediato. Ancoragem na pagina de vendas atualizada.

### Estrutura

> "Adicionei [novo bonus] no stack. Por conta disso, o investimento
> ajustou pra R$ [novo preco] a partir de hoje. Quem ja entrou no
> valor antigo: voce ganha o bonus de cortesia."

---

## Gatilho G12 — Custo subiu

### Quando ativa
Custo variavel por cliente subiu >15% (plataforma cara, time novo, comissao maior).

### Acao
+10% pra preservar margem. Nao mais que isso (e gatilho de manutencao, nao de upgrade).

---

## Cadencia anual recomendada

Sequencia ideal pra mentorada **estavel** (sem evento extraordinario):

```
Q1 (jan-mar): Janela sazonal alta (G4) — manter preco, ancorar desconto
Q2 (abr-jun): Possivel G1/G2 se capacidade >80% — +10% a +20%
Q3 (jul-set): Janela aniversario marca (G5) — preco realista + ancoragem
Q4 (out-dez): Black Friday (G5) + recalibracao Q1 do ano seguinte
```

A cada **12 meses**: rodar Porta Y (revisita anual) com `/pricing-dinamico-imperatriz --gerar` completo.

---

## Anti-patterns (o que NAO fazer)

1. **Subir preco sem comunicar** — base se sente traida, churn alto
2. **Comunicar reajuste e nao aplicar** — perde credibilidade
3. **Aplicar G7 (reposicionamento) sem rodar Luxe Empire antes** — vira preco fora do mercado
4. **Acumular gatilhos sem executar** (G1+G2+G3 ao mesmo tempo) — choque de preco
5. **Aplicar G3 (capacidade saturada) sem ter lista de espera real** — falsa escassez
6. **Dar G6 (ex-cliente -50%) pra cliente que NAO concluiu por culpa propria** — vicia o publico
7. **Subir preco em mes de sazonalidade baixa** — perde volume e perde percepcao
8. **Aumentar mais de 1 gatilho por mes** — confunde o publico, churn alto

---

## Como a skill detecta gatilho ativo

Modo `--janela [nome]` consulta:

1. `dossie/profile-16-kpis.json` -> taxa de ocupacao + datas
2. `dossie/profile-04-posicionamento.json` -> tier atual
3. `dossie/profile-09-concorrencia.json` -> posicao de mercado
4. Calendario sazonal do nicho (interno da skill)
5. Historico de cases adicionados desde ultima execucao
6. Historico de aumentos previos (controle de cumulatividade)

Output: lista de gatilhos ativos + acao recomendada + comunicacao sugerida.

---

**Janelas de Aumento — propriedade intelectual Tata Goncalves.**
