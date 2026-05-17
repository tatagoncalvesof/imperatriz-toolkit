# 06 — Boundaries Editoriais (SIM e NÃO)

## Por que boundaries existem

A maioria das marcas se define pelo que **publica**. Marca forte se define **também** pelo que **recusa publicar**.

Sem boundaries declarados:
- Toda pauta vira "vamos ver", e a marca posta tudo
- Time de conteúdo precisa pedir aprovação peça por peça
- Mentorada perde tempo decidindo o óbvio toda semana
- Marca escorrega pra opinar sobre tudo e perde foco
- Concorrente provoca → marca responde → vira novela

Com boundaries declarados:
- Pauta passa pelo filtro em 5 segundos
- Time decide sozinho 80% das vezes
- Mentorada só decide casos de fronteira
- Marca mantém posicionamento mesmo sob pressão
- Provocação de concorrente → boundary diz "não responde sob marca" → resolvido

## Estrutura: SIM / NÃO

A skill exige **mínimo 7 SIM e 7 NÃO**. Nenhum boundary é vago — cada um é regra dura.

### Padrão de um SIM bem-formado

`Marca PUBLICA SIM <o quê> [QUANDO <condição>] [, REGRA: <restrição>]`

Exemplos:

- ✅ "Marca PUBLICA SIM resultado de cliente nomeado, QUANDO houver permissão escrita, REGRA: nome real ou anônimo escolhido pela cliente."
- ✅ "Marca PUBLICA SIM bastidor de erro próprio, QUANDO houver aprendizado nomeado e ação tomada, REGRA: nunca culpar terceiro."
- ✅ "Marca PUBLICA SIM número da operação (faturamento, churn, NPS) QUANDO contextualizado com causa, REGRA: nunca solto pra impressionar."

### Padrão de um NÃO bem-formado

`Marca NÃO PUBLICA <o quê> [, EXCEÇÃO: <quando>] [, ALTERNATIVA: <onde vai]`

Exemplos:

- ❌ "Marca NÃO PUBLICA opinião política partidária, EXCEÇÃO: nenhuma, ALTERNATIVA: vai pra conta pessoal da Tata."
- ❌ "Marca NÃO PUBLICA print de DM de cliente, EXCEÇÃO: cliente que pediu pra ser citada com permissão escrita."
- ❌ "Marca NÃO PUBLICA crítica nominal a concorrente, EXCEÇÃO: nenhuma, ALTERNATIVA: post sobre o método errado, sem nome."

## Categorias de boundaries (use como checklist)

A skill cobre **mínimo** essas 8 categorias — pelo menos 1 SIM e 1 NÃO em cada:

### 1. Cliente (privacidade + uso de imagem)
- SIM: depoimento com permissão escrita, foto com permissão de uso
- NÃO: print de DM, foto de cliente sem autorização, nome de empresa cliente sem aprovação

### 2. Resultado e prova
- SIM: resultado nomeado com contexto de mecanismo, número com causa
- NÃO: número fora de contexto pra impressionar, resultado de cliente sem permissão

### 3. Concorrência
- SIM: post sobre prática errada do mercado (sem nome)
- NÃO: crítica nominal, screenshot de competidor, "diferentemente da X"

### 4. Política, religião, gênero, raça, ideologia
- SIM: posição estrutural relacionada à transformação que a marca promete (ex: "pago meu time bem porque acredito X")
- NÃO: opinião circunstancial sobre política partidária / fato do dia
- ALTERNATIVA padrão: vai pra conta pessoal, não sob marca

### 5. Vida pessoal (família, parceiro, filhos, perdas)
- SIM: aparição com integração ao posicionamento (filha aparece no story do escritório, parceiro aparece em decisão de vida que afeta marca)
- NÃO: explorar perda recente pra conteúdo, expor filho sem critério, romantizar relação só pra prova social

### 6. Time interno
- SIM: time aparecendo em ação, decisão de gente nomeada (com permissão), bastidor de cultura
- NÃO: demitir publicamente, "desabafar" sobre time, expor problema de gente em aberto

### 7. Bastidor de operação (números, parcerias, processos)
- SIM: number drop com contexto, parceria anunciada com clareza, processo descrito com método
- NÃO: número de outra empresa parceira sem aprovação, contrato confidencial, dado de cliente B2B

### 8. Resposta a crise / ataque
- SIM: comunicado oficial em canal próprio, posição clara da marca em até 24h se necessário
- NÃO: bate-boca em comentário, treplica, story raivoso, "indireta"
- PROTOCOLO: crise → silêncio de 4h → escrita → revisão por 1 pessoa do time → publicação no canal de maior alcance

## Boundaries de tom (não só de conteúdo)

Além de **o quê**, a skill registra **como**:

- ❌ Marca NÃO usa caps lock pra impacto (CAPS LOCK só pra siglas)
- ❌ Marca NÃO usa emoji em LinkedIn (exceto 1 em CTA)
- ❌ Marca NÃO usa "você" e "vc" no mesmo post
- ✅ Marca USA SEMPRE primeira pessoa do singular (mentorada fala, não "a equipe")
- ✅ Marca USA SEMPRE PT-BR (sem code-switching pra inglês desnecessário)

## Boundaries de canal (onde NÃO posta)

A skill também registra **onde** a marca não vai:

- ❌ Marca NÃO está em TikTok (decisão estratégica), EXCEÇÃO: clip de palco viralizando — vai pra IG Reels primeiro, TikTok só se demanda
- ❌ Marca NÃO está em Threads
- ❌ Marca NÃO faz Lives sem pauta declarada
- ❌ Marca NÃO faz live com convidado que não passou pelo filtro de boundaries

## O teste do "PR fail"

Pra cada boundary, fazer o teste:

> "Se essa peça vazasse pra um jornalista hostil, ela quebraria a marca?"

- Se sim → vai pra NÃO
- Se talvez → vira SIM com regra dura
- Se não → libera

## Saída JSON

```json
"boundaries": {
  "publica_sim": [
    "Resultado de cliente nomeado, QUANDO houver permissão escrita",
    "Bastidor de erro próprio com aprendizado nomeado",
    "Número da operação contextualizado com causa",
    "Posição estrutural relacionada à transformação prometida",
    "Time aparecendo em ação com nome (com permissão)",
    "Crítica a prática errada do mercado (sem nome próprio)",
    "Comunicado oficial em canal próprio em até 24h em crise"
  ],
  "publica_nao": [
    "Opinião política partidária — vai pra conta pessoal",
    "Print de DM de cliente",
    "Crítica nominal a concorrente",
    "Número fora de contexto pra impressionar",
    "Resposta a ataque em comentário (alternativa: comunicado oficial)",
    "Foto/menção a filho/parceiro sem critério",
    "Live sem pauta declarada"
  ],
  "boundaries_tom": [
    "Sempre primeira pessoa do singular",
    "Sem caps lock pra impacto",
    "Sem emoji em LinkedIn (exceto 1 em CTA)",
    "Sempre PT-BR sem code-switching"
  ],
  "boundaries_canal": [
    "NÃO está em TikTok (decisão estratégica)",
    "NÃO está em Threads",
    "NÃO faz Live sem pauta declarada"
  ],
  "protocolo_crise": "Silêncio 4h → escrita → revisão de 1 pessoa do time → publicação no canal de maior alcance"
}
```
