# Integração com a Stack Tata

O JSON canônico desta skill (`saida-canonica.json`) é fonte de verdade pra 8 outras skills. Esta página explica **exatamente** o que cada uma consome e como.

> Esta skill é o **motor de pesquisa** — não cria copy nem persona nem calendário. Ela alimenta quem cria.

---

## 1. `/skill-persona-profunda`

**O que consome do JSON:**
- `termos_top_50` → linguagem que a persona USA
- `expressoes_idiomaticas` → gírias e frases típicas da persona
- `metaforas` → como a persona descreve a própria dor
- `anti_termos` → o que a persona REJEITA
- `objecoes` (agrupadas por eixo PADC) → 4 dimensões: "Medos", "Resistências", "Síndrome do impostor", "Histórico de fracassos"

**Como conectar:**
Quando rodar `/skill-persona-profunda`, mencione: "Use o JSON em `~/Documents/Obsidian Vault/05 - Pesquisa de Mercado/[nicho-slug]/saida-canonica.json` como fonte primária."

A skill de persona vai preencher as 30 dimensões usando linguagem EXATA do JSON (não inventando).

---

## 2. `/briefing-copy-360`

**O que consome:**
- Bloco "Voz do Cliente" → preenchido por `expressoes_idiomaticas` + `metaforas`
- Bloco "Anti-vocabulário" → preenchido por `anti_termos`
- Bloco "Estágio Schwartz" → `metadata.schwartz_dominante`
- Bloco "Eixo PADC dominante" → `metadata.padc_dominante`
- Bloco "Plataforma principal" → analisa onde mais termos apareceram

**Como conectar:**
`/briefing-copy-360` é **obrigatório antes de escrever copy**. Se já existe pesquisa de mercado pro nicho, o briefing fica 60% pronto automaticamente.

---

## 3. `/headline-imperatriz`

**O que consome:**
- Top 10 termos por `schwartz` (10 termos por nível) → vira matéria-prima de hook
- Objeção #1 de cada termo → modifica o ângulo Bencivenga (4U + Believable + Beneficial)
- `anti_termos` → exclui da geração de variações

**Como conectar:**
Roda assim: "Gera headlines pra produto X usando como base os termos top do nicho do JSON em [path]"

A headline-imperatriz vai gerar 5-10 variações por temperatura (frio, morno, quente, retargeting) usando termo literal no hook.

---

## 4. `/mecanismo-unico`

**O que consome:**
- Objeções recorrentes por eixo → revelam **vilão externo** do mecanismo
- `metaforas` → matéria-prima pra metáfora explicativa do mecanismo
- Termos top → revelam o que o público ACHA que é o problema (causa-percebida)

**Como conectar:**
Antes de criar mecanismo único, leia a pesquisa de mercado. O vilão externo precisa ser:
1. **Real** (não inventado por copywriter)
2. **Externo ao cliente** (algo que VENCE ele, não a culpa dele)
3. **Reconhecível na linguagem do nicho**

Pesquisa de mercado prova quais vilões o público já reconhece.

---

## 5. `/calendario-imperatriz`

**O que consome:**
- `ideias_conteudo` (50 ideias) → vira pauta de 30-60 dias
- `metadata.plataformas_pesquisadas` → distribui formatos por canal

**Como conectar:**
```
/calendario-imperatriz --base=~/Documents/Obsidian Vault/05 - Pesquisa de Mercado/[nicho-slug]/saida-canonica.json
```

O calendário aplica:
- Matriz TEAM da `/linha-editorial-imperatriz`
- Cadência por canal (regra editorial)
- Distribui ideias por temperatura (frio → meio → quente)

---

## 6. `/linha-editorial-imperatriz`

**O que consome:**
- `anti_termos` → preenche vocabulário OFF
- `expressoes_idiomaticas` → preenche vocabulário ON (palavras-âncora)
- `metadata.padc_dominante` → escolhe pilares temáticos prioritários
- Padrões de hook → escolhe tom dominante

**Como conectar:**
Roda na ordem:
1. Posicionamento estratégico
2. Voz de marca
3. **Pesquisa de mercado** (esta skill) ← fundação
4. Linha editorial (consome pesquisa)
5. Calendário (consome linha + pesquisa)

---

## 7. `/copy-conversacional-dm`

**O que consome:**
- Banco de 150 objeções → roteiro de quebra em DM
- `metadata.schwartz_dominante` → calibra sequência fria/morna/quente
- `expressoes_idiomaticas` → linguagem das mensagens (não inventar)

**Como conectar:**
Quando rodar `/copy-conversacional-dm`, ela vai usar o banco de objeções como **fonte primária**. Cada objeção do JSON vira 1 entrada do banco de 15 objeções da skill conversacional.

---

## 8. `/analise-anuncio-1000`

**O que consome:**
- Termos top → benchmark pra avaliar se o anúncio analisado usa linguagem do público
- Objeções → checagem de quais foram quebradas no anúncio

**Como conectar:**
Quando analisar anúncio de competidor, cruze com a pesquisa: "Esse anúncio usa [N] dos top 10 termos do nicho? Quebra quais objeções?"

---

## 9. `/skill-pagina-vendas`

**O que consome:**
- `termos_top_50` → headline, sub-heads, bullet points
- 150 objeções → seção FAQ
- `metadata.schwartz_dominante` → estrutura geral (PASTOR pra dor-consciente, AIDA pra solução-consciente)

**Como conectar:**
Antes de gerar página de vendas, **sempre** verificar se existe pesquisa de mercado do nicho. Se não existe, rodar esta skill primeiro.

---

## 10. `/maestro-de-conteudo`

**O que consome:**
- TUDO. A maestro é orquestradora — roda esta skill como uma das 5 fases obrigatórias pra mentorada iniciante.

**Como conectar:**
A maestro chama na sequência:
1. `/posicionamento-estrategico`
2. `/voz-de-marca-builder`
3. **`/deep-market-research`** ← preenche linguagem real
4. `/linha-editorial-imperatriz`
5. `/calendario-imperatriz`

---

## Ordem de execução recomendada (workflow inteiro)

```
DIA 1: /posicionamento-estrategico  (define nicho + cliente ideal)
DIA 2: /voz-de-marca-builder        (captura voz da pessoa)
DIA 3-4: /deep-market-research      (esta skill — captura voz do público)
DIA 5: /skill-persona-profunda      (persona com linguagem real)
DIA 6: /mecanismo-unico             (com vilão validado pela pesquisa)
DIA 7: /linha-editorial-imperatriz  (vocabulário ON/OFF baseado em pesquisa)
DIA 8: /calendario-imperatriz       (50 ideias da pesquisa viram pauta)
DIA 9+: /headline + /briefing + /skill-pagina-vendas (criação de copy)
```

A pesquisa de mercado é fundação. Sem ela, tudo depois é chute.

---

## Como passar o JSON pra próxima skill

Se a skill aceita arquivo de input, passe o caminho:
```
/skill-persona-profunda --pesquisa=~/Documents/Obsidian Vault/05 - Pesquisa de Mercado/[nicho-slug]/saida-canonica.json
```

Se a skill não aceita arquivo, mencione no prompt:
```
"Use como referência principal o JSON em [path]. Não invente — extraia linguagem desse arquivo."
```

---

## Quando ATUALIZAR a pesquisa

Re-rode esta skill quando:
- **A cada 6 meses** (linguagem do nicho muda)
- Mudou o produto/oferta significativamente
- Entrou em nicho adjacente (não basta atualizar — refaz)
- Detecta drift nas métricas de copy (CTR caindo = linguagem desalinhada)
- Vai entrar em novo canal (LinkedIn pela primeira vez? rode `--canal=linkedin`)

Use `--atualizar=<arquivo>` pra gerar diff e ver o que mudou desde a última pesquisa.
