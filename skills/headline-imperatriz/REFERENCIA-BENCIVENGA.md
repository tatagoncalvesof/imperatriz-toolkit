# REFERENCIA BENCIVENGA — Scoring 4U + Believable + Beneficial

Gary Bencivenga e considerado o maior copywriter vivo. Cobrava $50k + royalties por uma carta. Em Bencivenga Bullets ele sistematizou o que separa headline que converte de headline que morre.

## A LEI BENCIVENGA

> **A maior headline e aquela que e simultaneamente mais ACREDITAVEL e mais BENEFICA.**

Curiosidade sozinha nao converte em publico frio cetico. Ela precisa vir acoplada a credibilidade. Em mercado brasileiro — que e um dos mais ceticos do mundo — isso e lei absoluta.

---

## OS 6 CRITERIOS DE SCORING (0-100 cada)

### 1. USEFUL (util)
**Pergunta:** o prospect ve beneficio CLARO e DESEJADO?

| Nota | Significado |
|---|---|
| 0-40 | Beneficio vago ou inexistente ("descubra o segredo") |
| 41-70 | Beneficio presente mas nao desejado por ESSE publico |
| 71-90 | Beneficio claro e desejado |
| 91-100 | Beneficio claro + especifico + conectado a dor central do publico |

### 2. URGENT (urgente)
**Pergunta:** tem urgencia implicita ou explicita legitima?

| Nota | Significado |
|---|---|
| 0-40 | Nenhuma urgencia, parece eterno |
| 41-70 | Urgencia fake ("nao perca", "aja agora") |
| 71-90 | Urgencia implicita pela relevancia do momento |
| 91-100 | Urgencia legitima ancorada em razao real (evento, janela, escassez verdadeira) |

### 3. UNIQUE (unico)
**Pergunta:** e diferente do que o mercado ja grita 1000 vezes?

| Nota | Significado |
|---|---|
| 0-40 | Copia literal do que todo mundo fala |
| 41-70 | Variacao pequena do padrao |
| 71-90 | Angulo diferente reconhecivel |
| 91-100 | Pattern interrupt real, mecanismo unico declarado |

### 4. ULTRA-SPECIFIC (ultra-especifico)
**Pergunta:** tem numero, tempo, caso especifico, local?

| Nota | Significado |
|---|---|
| 0-40 | Generico total ("muito", "rapido", "facil") |
| 41-70 | Especificidade fraca ("em poucas semanas") |
| 71-90 | 1 elemento especifico (numero OU tempo OU caso) |
| 91-100 | 2+ elementos especificos (ex: "8kg em 60 dias, caso de Ana, 42 anos") |

### 5. BELIEVABLE (acreditavel) — VETO BENCIVENGA
**Pergunta:** o prospect frio CETICO acredita?

| Nota | Significado |
|---|---|
| 0-40 | Parece mentira, scam, impossivel |
| 41-59 | Duvidoso sem proof correspondente |
| 60-75 | Acreditavel com proof implicito |
| 76-100 | Acreditavel com proof explicito embedded |

**REGRA DE VETO:** headlines com `believable < 60` sao **descartadas automaticamente**. Nao importa quao criativas sejam.

### 6. BENEFICIAL (benefico)
**Pergunta:** o beneficio e desejado por ESSE publico especifico? (nao publico em geral)

| Nota | Significado |
|---|---|
| 0-40 | Beneficio que nao importa pra esse publico |
| 41-70 | Beneficio generico que atinge o publico tangencialmente |
| 71-90 | Beneficio relevante pra dor central do publico |
| 91-100 | Beneficio hiper-conectado a dor + desejo secreto do publico |

---

## SCORING CONSOLIDADO

**Media final** = (U + U + U + U + B + B) / 6

| Media | Classificacao | Acao |
|---|---|---|
| 0-49 | Morta | Reescrever do zero |
| 50-69 | Fraca | Reforcar 2 criterios mais baixos |
| 70-84 | Competitiva | Boa pra testar |
| 85-94 | Forte | Priorizar em A/B |
| 95-100 | Excelencia | Candidata a vencedora |

**Regra dura:** mesmo com media 85+, se `believable < 60` → descarta.

---

## EXEMPLOS DE SCORING APLICADO

### Exemplo 1: Headline fraca

> "Transforme sua vida com meu metodo revolucionario"

| Criterio | Nota | Por que |
|---|---|---|
| Useful | 25 | "Transforme sua vida" e generico |
| Urgent | 20 | Nenhuma urgencia |
| Unique | 15 | Frase usada em 1 milhao de ads |
| Ultra-specific | 10 | Zero especificidade |
| Believable | 30 | "Revolucionario" cheira scam |
| Beneficial | 30 | Sem publico definido |
| **Media** | **22** | **MORTA** |

### Exemplo 2: Headline forte

> "Como mulheres 40+ estao perdendo 8kg em 60 dias sem dieta usando a enzima que o ginecologista nao menciona"

| Criterio | Nota | Por que |
|---|---|---|
| Useful | 95 | Beneficio claro + desejado |
| Urgent | 75 | "Estao" = movimento atual |
| Unique | 90 | Enzima + ginecologista = angulo novo |
| Ultra-specific | 95 | "8kg + 60 dias + 40+" |
| Believable | 82 | Tem mecanismo + autoridade implicita |
| Beneficial | 95 | Dor central direto |
| **Media** | **89** | **FORTE** |

### Exemplo 3: Headline curiosa mas NAO acreditavel (descartada)

> "O truque bizarro de 3 segundos que derrete 15kg em 7 dias"

| Criterio | Nota | Por que |
|---|---|---|
| Useful | 60 | Beneficio, mas suspeito |
| Urgent | 85 | "7 dias" tem urgencia forte |
| Unique | 80 | "3 segundos" e contrarian |
| Ultra-specific | 90 | Muitos numeros |
| Believable | **25** | **15kg em 7 dias = impossivel cetico** |
| Beneficial | 70 | Beneficio exagerado |
| **Media** | **68** | **DESCARTADA (believable < 60)** |

---

## COMO APLICAR O SCORING NA SKILL

Para cada variacao gerada, a skill calcula internamente os 6 criterios e entrega no output:

```
Scoring Bencivenga:
- Useful: 92
- Urgent: 75
- Unique: 88
- Ultra-specific: 95
- Believable: 82
- Beneficial: 95
Media: 88 — FORTE
```

Se `believable < 60` → regenera antes de mostrar ao usuario.

---

## COMO ELEVAR SCORE BAIXO

| Criterio fraco | Como elevar |
|---|---|
| Useful | Nomear o beneficio explicitamente em termos concretos |
| Urgent | Ancorar em razao real (evento, data, janela) |
| Unique | Apresentar mecanismo unico ou angulo contrarian |
| Ultra-specific | Adicionar numero, tempo, caso, local |
| Believable | Adicionar proof (caso, numero, autoridade, mecanismo cientifico) |
| Beneficial | Voltar ao briefing e confirmar dor central real |

---

## FRASE DE BENCIVENGA PRA LEMBRAR

> "Every word in your headline should be doing a specific job. If it's not pulling its weight, kill it."

Cada palavra da headline precisa ter funcao. Palavra sem funcao = desperdicio de atencao.
