# LÓGICA DE CLASSIFICAÇÃO — Algoritmo de 12 Sinais + Scoring

> Esse documento descreve **como** a skill `/perfil-mentorada` decide o perfil. Cada decisão tem que ser auditável: a Tata precisa conseguir abrir o `01-perfil.json` e ver QUAL sinal puxou pra QUAL perfil e POR QUE.

---

## VISÃO GERAL DO ALGORITMO

```
ENTRADA:
  - 00-anamnese.json (preenchido pela mentorada)
  - dados de deep-research público (Insta, site, LinkedIn, Google)

PROCESSO:
  FASE 1: extrair os 12 sinais (cada um vira valor categórico)
  FASE 2: para cada um dos 8 perfis, calcular score 0-100
  FASE 3: identificar top 1, top 2 e gap (Δ)
  FASE 4: aplicar regras de desempate e híbrido
  FASE 5: gerar justificativa em sinais concretos

SAÍDA:
  - perfil principal + score
  - perfil secundário (se híbrido) + score
  - sinais decisivos
  - rota A-Z customizada
  - kit + NÃO usar + tempo + nível
```

---

## OS 12 SINAIS — CARTÕES DETALHADOS

Cada sinal tem:
- **Nome**
- **Pergunta-chave** que extrai do `00-anamnese.json` ou da pesquisa
- **Valores possíveis** (categorias)
- **Peso no score final** (em %)
- **Tabela de pontuação por perfil** (0-100 por perfil)

---

### SINAL 1 — Faixa de faturamento mensal

**Peso:** 15%

**Pergunta-chave:** "Qual o faturamento médio mensal da mentorada nos últimos 6 meses?"

**Valores possíveis:**
- `zero` — R$ 0 a R$ 1.500
- `baixo` — R$ 1.500 a R$ 5.000
- `medio` — R$ 5.000 a R$ 30.000
- `alto` — R$ 30.000 a R$ 100.000
- `muito_alto` — R$ 100.000 a R$ 500.000
- `empresarial` — R$ 500.000+

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| zero | 95 | 10 | 0 | 0 | 5 | 30 | 0 | 40 |
| baixo | 70 | 40 | 5 | 5 | 10 | 35 | 0 | 60 |
| medio | 15 | 90 | 30 | 20 | 35 | 50 | 5 | 80 |
| alto | 0 | 30 | 95 | 70 | 70 | 60 | 30 | 50 |
| muito_alto | 0 | 5 | 70 | 95 | 95 | 70 | 80 | 20 |
| empresarial | 0 | 0 | 20 | 70 | 70 | 80 | 100 | 5 |

---

### SINAL 2 — Tipo de produto/oferta atual

**Peso:** 15%

**Pergunta-chave:** "O que ela vende HOJE? (atendimento 1:1 / mentoria em grupo / curso digital / serviço B2B / produto físico / SaaS / processo terapêutico / nada)"

**Valores possíveis:**
- `nenhum`
- `1_a_1` — atendimento individual (consultoria, sessão, projeto avulso)
- `mentoria_grupo` — mentoria em grupo, programa de imersão
- `curso_digital` — curso digital pré-gravado, lançamentos
- `servico_b2b` — serviço pra outras empresas
- `produto_fisico` — clínica, loja, restaurante
- `saas_app` — SaaS, app, software
- `processo_transformacao` — processo terapêutico/coaching de 8-12 semanas

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| nenhum | 95 | 5 | 0 | 0 | 0 | 20 | 0 | 30 |
| 1_a_1 | 25 | 95 | 40 | 5 | 50 | 30 | 5 | 70 |
| mentoria_grupo | 5 | 30 | 95 | 60 | 50 | 20 | 5 | 60 |
| curso_digital | 0 | 5 | 70 | 95 | 30 | 30 | 5 | 30 |
| servico_b2b | 0 | 30 | 10 | 5 | 20 | 60 | 95 | 5 |
| produto_fisico | 0 | 30 | 5 | 0 | 95 | 5 | 30 | 5 |
| saas_app | 0 | 5 | 5 | 5 | 0 | 95 | 70 | 0 |
| processo_transformacao | 10 | 50 | 40 | 5 | 20 | 5 | 0 | 95 |

---

### SINAL 3 — Formato de venda predominante

**Peso:** 12%

**Pergunta-chave:** "Como entra venda hoje? (DM 1:1 / call diagnóstico / página de vendas + ads / lançamento / proposta comercial B2B / pacote presencial / agenda de atendimento)"

**Valores possíveis:**
- `nenhuma_estrutura`
- `dm_1a1`
- `call_diagnostico`
- `pagina_ads`
- `lancamento`
- `proposta_b2b`
- `presencial_loja_clinica`
- `agenda_atendimento`

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| nenhuma_estrutura | 95 | 30 | 0 | 0 | 5 | 40 | 0 | 50 |
| dm_1a1 | 30 | 90 | 30 | 10 | 30 | 20 | 5 | 80 |
| call_diagnostico | 5 | 70 | 80 | 30 | 50 | 30 | 30 | 70 |
| pagina_ads | 0 | 10 | 80 | 95 | 30 | 30 | 30 | 20 |
| lancamento | 0 | 5 | 60 | 95 | 20 | 5 | 5 | 20 |
| proposta_b2b | 0 | 20 | 5 | 5 | 30 | 70 | 95 | 0 |
| presencial_loja_clinica | 0 | 30 | 5 | 0 | 95 | 5 | 50 | 30 |
| agenda_atendimento | 5 | 80 | 30 | 0 | 70 | 10 | 5 | 90 |

---

### SINAL 4 — Origem do cliente

**Peso:** 8%

**Pergunta-chave:** "De onde vêm os clientes hoje? (indicação / orgânico digital / ads pago / cold outreach / passagem física / network corporativo)"

**Valores possíveis:**
- `indicacao`
- `organico_digital`
- `ads_pago`
- `cold_outreach`
- `passagem_fisica`
- `network_corporativo`
- `nenhum_cliente_ainda`

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| indicacao | 30 | 95 | 30 | 5 | 60 | 50 | 40 | 70 |
| organico_digital | 50 | 30 | 80 | 70 | 30 | 50 | 20 | 80 |
| ads_pago | 5 | 10 | 90 | 95 | 30 | 30 | 30 | 20 |
| cold_outreach | 0 | 30 | 5 | 5 | 5 | 70 | 95 | 5 |
| passagem_fisica | 5 | 30 | 5 | 0 | 95 | 5 | 30 | 30 |
| network_corporativo | 5 | 60 | 5 | 5 | 30 | 50 | 90 | 20 |
| nenhum_cliente_ainda | 95 | 5 | 0 | 0 | 5 | 30 | 0 | 30 |

---

### SINAL 5 — Tempo no mercado

**Peso:** 6%

**Pergunta-chave:** "Há quanto tempo a mentorada vende o que vende hoje?"

**Valores possíveis:**
- `menos_6m`
- `6m_a_1ano`
- `1_a_3_anos`
- `3_a_7_anos`
- `mais_7_anos`

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| menos_6m | 95 | 50 | 5 | 5 | 30 | 50 | 5 | 50 |
| 6m_a_1ano | 60 | 80 | 30 | 30 | 50 | 60 | 30 | 60 |
| 1_a_3_anos | 10 | 70 | 90 | 80 | 70 | 60 | 50 | 70 |
| 3_a_7_anos | 0 | 30 | 80 | 90 | 90 | 50 | 80 | 70 |
| mais_7_anos | 0 | 30 | 60 | 60 | 95 | 50 | 95 | 50 |

---

### SINAL 6 — Audiência digital (tamanho + qualidade)

**Peso:** 8%

**Pergunta-chave:** "Quantos seguidores no Instagram + qualidade do engajamento + lista de e-mail?"

**Valores possíveis:**
- `inexistente` — < 500 seguidores
- `pequena_engajada` — 500-3k engajados
- `media` — 3k-30k
- `grande_engajada` — 30k-100k engajados
- `gigante` — 100k+
- `linkedin_dominante` — pequena no Insta, forte no LinkedIn (sinal técnico/B2B)

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| inexistente | 95 | 30 | 0 | 0 | 30 | 50 | 30 | 30 |
| pequena_engajada | 70 | 80 | 30 | 10 | 50 | 60 | 50 | 80 |
| media | 30 | 70 | 80 | 60 | 60 | 30 | 30 | 70 |
| grande_engajada | 5 | 30 | 90 | 90 | 50 | 30 | 30 | 60 |
| gigante | 0 | 5 | 70 | 95 | 30 | 10 | 30 | 30 |
| linkedin_dominante | 5 | 30 | 30 | 30 | 30 | 90 | 90 | 30 |

---

### SINAL 7 — Maturidade de mecanismo único

**Peso:** 6%

**Pergunta-chave:** "Tem mecanismo único nomeado e usado em copy?"

**Valores possíveis:**
- `inexistente` — não tem nem ideia
- `embrionario` — tem na cabeça, não nomeou
- `nomeado_fraco` — tem nome mas pouco diferenciado
- `nomeado_forte` — tem nome forte, usa em todo lugar
- `proprietario_consolidado` — registrado, articulado, é a base do funil

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| inexistente | 95 | 70 | 30 | 5 | 60 | 50 | 30 | 50 |
| embrionario | 70 | 90 | 60 | 30 | 70 | 60 | 30 | 70 |
| nomeado_fraco | 30 | 60 | 80 | 70 | 50 | 50 | 50 | 60 |
| nomeado_forte | 5 | 30 | 90 | 95 | 50 | 50 | 60 | 50 |
| proprietario_consolidado | 0 | 5 | 70 | 95 | 30 | 70 | 80 | 30 |

---

### SINAL 8 — Estrutura de time

**Peso:** 6%

**Pergunta-chave:** "Quantas pessoas no time? (sozinha / 1-2 ajuda / 3-5 / 6-15 / 16-50 / 50+)"

**Valores possíveis:**
- `sozinha`
- `1_a_2`
- `3_a_5`
- `6_a_15`
- `16_a_50`
- `mais_50`

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| sozinha | 95 | 80 | 20 | 5 | 30 | 80 | 5 | 80 |
| 1_a_2 | 60 | 90 | 60 | 30 | 60 | 70 | 30 | 70 |
| 3_a_5 | 5 | 60 | 90 | 70 | 70 | 60 | 50 | 50 |
| 6_a_15 | 0 | 30 | 70 | 95 | 90 | 50 | 80 | 30 |
| 16_a_50 | 0 | 5 | 30 | 70 | 95 | 30 | 95 | 5 |
| mais_50 | 0 | 0 | 5 | 30 | 70 | 30 | 95 | 0 |

---

### SINAL 9 — Origem do conhecimento que vende

**Peso:** 6%

**Pergunta-chave:** "De onde veio a expertise que ela ensina? (vivência pessoal / profissão prática longa / formação acadêmica / construção técnica) — usado pra desempatar"

**Valores possíveis:**
- `vivencia_pessoal_transformacao`
- `profissao_pratica_longa`
- `formacao_academica`
- `construcao_tecnica`
- `experiencia_corporativa`
- `nao_definido`

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| vivencia_pessoal_transformacao | 50 | 60 | 50 | 30 | 30 | 5 | 5 | 95 |
| profissao_pratica_longa | 30 | 80 | 70 | 50 | 95 | 30 | 70 | 60 |
| formacao_academica | 30 | 60 | 80 | 70 | 60 | 50 | 60 | 70 |
| construcao_tecnica | 5 | 20 | 30 | 30 | 5 | 95 | 70 | 5 |
| experiencia_corporativa | 30 | 50 | 50 | 50 | 60 | 60 | 90 | 30 |
| nao_definido | 70 | 50 | 30 | 30 | 30 | 30 | 30 | 30 |

---

### SINAL 10 — Tom/linguagem dominante

**Peso:** 6%

**Pergunta-chave:** "Como é o tom dela em conteúdo + bio + venda? (terapêutico/poético / comercial direto / técnico / corporativo / íntimo amigo / autoridade objetiva)"

**Valores possíveis:**
- `terapeutico_poetico`
- `comercial_direto`
- `tecnico`
- `corporativo`
- `intimo_amigo`
- `autoridade_objetiva`
- `confuso_misturado`

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| terapeutico_poetico | 30 | 50 | 30 | 5 | 30 | 5 | 5 | 95 |
| comercial_direto | 30 | 70 | 90 | 95 | 50 | 30 | 60 | 5 |
| tecnico | 5 | 20 | 30 | 30 | 30 | 95 | 80 | 5 |
| corporativo | 5 | 30 | 30 | 50 | 70 | 60 | 95 | 10 |
| intimo_amigo | 70 | 90 | 70 | 50 | 50 | 30 | 5 | 80 |
| autoridade_objetiva | 30 | 50 | 80 | 80 | 80 | 70 | 80 | 50 |
| confuso_misturado | 80 | 60 | 30 | 5 | 70 | 30 | 30 | 50 |

---

### SINAL 11 — Sensibilidade a copy agressivo

**Peso:** 6%

**Pergunta-chave:** "Ela aceita copy de urgência/escassez/'ÚLTIMAS VAGAS'? (rejeita totalmente / desconfortável / aceita com filtro / aceita / abraça)"

**Valores possíveis:**
- `rejeita_totalmente` — coach pura
- `desconfortavel` — alguma reserva
- `aceita_com_filtro` — usa mas adapta
- `aceita`
- `abraca` — gosta e usa em escala

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| rejeita_totalmente | 30 | 30 | 5 | 0 | 30 | 50 | 30 | 95 |
| desconfortavel | 50 | 50 | 30 | 10 | 50 | 60 | 60 | 80 |
| aceita_com_filtro | 70 | 70 | 70 | 70 | 70 | 70 | 70 | 30 |
| aceita | 50 | 70 | 90 | 90 | 70 | 50 | 70 | 5 |
| abraca | 30 | 70 | 80 | 95 | 50 | 30 | 30 | 0 |

---

### SINAL 12 — Trilha desejada declarada na anamnese

**Peso:** 6%

**Pergunta-chave:** "Na anamnese, o que ela disse que quer construir nos próximos 6-12 meses?"

**Valores possíveis:**
- `comecar_do_zero`
- `produtizar_atendimento_1a1`
- `escalar_mentoria_existente`
- `automatizar_lancamentos`
- `monetizar_expertise_fisica`
- `criar_skills_agentes_apps`
- `estruturar_comercial_b2b`
- `monetizar_processo_transformacao`
- `nao_sabe_ainda`

**Tabela de pontuação:**

| Valor | Iniciante | Vendedora | Mentora Est. | Infoprod | Emp. Física | Esp. Técnica | Emp. B2B | Coach |
|-------|-----------|-----------|--------------|----------|-------------|--------------|----------|-------|
| comecar_do_zero | 95 | 30 | 5 | 5 | 30 | 30 | 5 | 50 |
| produtizar_atendimento_1a1 | 30 | 95 | 60 | 30 | 50 | 30 | 30 | 70 |
| escalar_mentoria_existente | 5 | 50 | 95 | 70 | 30 | 30 | 30 | 50 |
| automatizar_lancamentos | 0 | 30 | 70 | 95 | 30 | 30 | 30 | 30 |
| monetizar_expertise_fisica | 5 | 30 | 30 | 30 | 95 | 5 | 30 | 30 |
| criar_skills_agentes_apps | 5 | 5 | 30 | 30 | 5 | 95 | 70 | 5 |
| estruturar_comercial_b2b | 0 | 30 | 30 | 30 | 30 | 60 | 95 | 5 |
| monetizar_processo_transformacao | 30 | 50 | 60 | 30 | 30 | 5 | 5 | 95 |
| nao_sabe_ainda | 80 | 50 | 30 | 30 | 30 | 30 | 30 | 50 |

---

## FÓRMULA DE SCORING FINAL

Para cada um dos 8 perfis:

```
score_perfil = Σ (pontuacao_sinal_X × peso_sinal_X)
```

Onde:
- `pontuacao_sinal_X` = valor 0-100 da tabela do sinal X pra esse perfil
- `peso_sinal_X` = peso percentual do sinal (0.15 pra Sinal 1, etc.)

Resultado: número 0-100 por perfil.

### Exemplo numérico — mentorada Vendedora Avulsa típica

| # | Sinal | Valor | Pontuação Vendedora | × Peso |
|---|-------|-------|---------------------|--------|
| 1 | Faturamento | medio (8k/mês) | 90 | 90 × 0.15 = 13.5 |
| 2 | Produto | 1_a_1 | 95 | 95 × 0.15 = 14.25 |
| 3 | Formato venda | dm_1a1 | 90 | 90 × 0.12 = 10.8 |
| 4 | Origem cliente | indicacao | 95 | 95 × 0.08 = 7.6 |
| 5 | Tempo mercado | 1_a_3_anos | 70 | 70 × 0.06 = 4.2 |
| 6 | Audiência | pequena_engajada | 80 | 80 × 0.08 = 6.4 |
| 7 | Mecanismo | embrionario | 90 | 90 × 0.06 = 5.4 |
| 8 | Time | sozinha | 80 | 80 × 0.06 = 4.8 |
| 9 | Origem conhec. | profissao_pratica | 80 | 80 × 0.06 = 4.8 |
| 10 | Tom | intimo_amigo | 90 | 90 × 0.06 = 5.4 |
| 11 | Copy agressivo | aceita_com_filtro | 70 | 70 × 0.06 = 4.2 |
| 12 | Trilha desejada | produtizar_1a1 | 95 | 95 × 0.06 = 5.7 |

**Total Vendedora Avulsa: 87.05/100**

A skill calcula isso pros 8 perfis. O com maior score é o principal.

---

## REGRA DE HÍBRIDO

```
Δ = score_top1 - score_top2

SE Δ < 15:
  declarar HÍBRIDO
  apresentar combinação (ver CASOS-HIBRIDOS.md)

SE Δ >= 15:
  perfil único confirmado
```

**Exemplos:**
- top1 = 87 (Vendedora) | top2 = 61 (Coach) → Δ = 26 → **único: Vendedora**
- top1 = 72 (Vendedora) | top2 = 65 (Mentora Est.) → Δ = 7 → **híbrido: Vendedora + Mentora**
- top1 = 78 (Coach) | top2 = 70 (Vendedora) → Δ = 8 → **híbrido: Coach + Vendedora**

---

## CONFIANÇA DA CLASSIFICAÇÃO

| Score top 1 | Δ top1-top2 | Confiança |
|-------------|-------------|-----------|
| ≥ 80 | ≥ 20 | **Alta** |
| 65-79 | ≥ 15 | **Média** |
| < 65 OU Δ < 15 | — | **Baixa** (sinaliza pra Tata revisar) |

Se confiança = Baixa, a skill **DEVE** alertar:

> "Atenção, Tata: a classificação ficou em zona cinza (score X, Δ Y). Recomendo abrir uma call rápida com a mentorada pra confirmar manualmente antes de gravar `01-perfil.json`."

---

## TRATAMENTO DE SINAL FALTANTE

Se a anamnese não traz dado pro Sinal X e o deep-research não conseguiu inferir:

1. Marcar sinal como `desconhecido`
2. **Redistribuir o peso** desse sinal proporcionalmente entre os outros 11
3. Sinalizar no output: "Sinal X não disponível — peso redistribuído"
4. Recomendar follow-up pra completar dado

---

## REGRAS DE OURO DO ALGORITMO

1. **Auditável:** todo score precisa ter trilha (qual sinal puxou pra qual perfil)
2. **Honesto:** se confiança é baixa, diz que é baixa
3. **Não força encaixe perfeito:** cada mentorada é única, perfil é arquétipo
4. **Híbrido > forçar único:** quando Δ < 15, declara híbrido sem hesitar
5. **Sensibilidade ao tom (Sinal 11) é decisivo pra Coach:** se rejeita totalmente copy agressivo, **boost +20** no score Coach (regra fundadora)
6. **Cliente B2B (Sinal 4 = network_corporativo + Sinal 2 = servico_b2b) é decisivo pra Empresa B2B:** boost +15
7. **Construção técnica (Sinal 9 = construcao_tecnica + Sinal 12 = criar_skills) é decisivo pra Especialista Técnica:** boost +15
8. **Quando dúvida entre Mentora Estabelecida e Infoprodutora:** olhar ritmo de lançamento (Sinal 3 = lancamento → Infoprodutora; Sinal 3 = call_diagnostico OU pagina_ads contínuo → Mentora Estabelecida)
9. **Vendedora Avulsa vs Iniciante Zero:** Sinal 1 (faturamento) é o juiz — `medio` (5-30k) confirma Vendedora, `zero/baixo` confirma Iniciante
10. **Empresa Física vs outros:** Sinal 2 = produto_fisico **trava** classificação em Empresa Física (a não ser que esteja em transição completa)

---

## PSEUDOCÓDIGO DE REFERÊNCIA

```python
def classificar_mentorada(anamnese_json, deep_research):
    sinais = extrair_sinais(anamnese_json, deep_research)  # 12 valores

    scores = {}
    for perfil in OS_8_PERFIS:
        score = 0
        for sinal in sinais:
            pontuacao = TABELA[sinal.nome][sinal.valor][perfil]
            score += pontuacao * sinal.peso
        scores[perfil] = score

    # boosts especiais
    if sinais['copy_agressivo'].valor == 'rejeita_totalmente':
        scores['coach'] += 20
    if sinais['cliente'].valor == 'network_corporativo' and sinais['produto'].valor == 'servico_b2b':
        scores['empresa_b2b'] += 15
    if sinais['origem_conhec'].valor == 'construcao_tecnica' and sinais['trilha'].valor == 'criar_skills_agentes_apps':
        scores['especialista_tecnica'] += 15

    # ranking
    ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top1, top2 = ranking[0], ranking[1]
    delta = top1[1] - top2[1]

    hibrido = delta < 15
    confianca = calcular_confianca(top1[1], delta)

    return {
        'perfil_principal': top1[0],
        'score_principal': top1[1],
        'perfil_secundario': top2[0] if hibrido else None,
        'score_secundario': top2[1] if hibrido else None,
        'hibrido': hibrido,
        'confianca': confianca,
        'sinais_decisivos': top_3_sinais_que_puxaram(sinais, top1[0])
    }
```

---

**Algoritmo Travessia Imperatriz — versão 1.0 — propriedade Tata Gonçalves.**
