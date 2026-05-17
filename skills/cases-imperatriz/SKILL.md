---
name: cases-imperatriz
description: >
  Operadora do Pilar 7 (Tribo) da Travessia Imperatriz Tata Gonçalves —
  motor de captação, validação e ativação de cases reais de mentoradas com
  proof stack auditável. Detecta mentoradas que atingiram proof point
  (mudou de nível na hierarquia, atingiu KPI verde, completou pipeline,
  destravou porta), solicita case estruturado em 8 blocos, coleta proof
  stack hierárquico (números, prints, depoimentos, vídeo, palco),
  organiza em formato reutilizável e transforma em copy pronta pra cada
  canal (página de vendas, e-mail, VSL, ad, post, capítulo de livro). 5
  modos: --captar (solicita case completo via formulário), --validar
  (audita proof stack contra hierarquia de evidência), --gerar-copy
  (transforma case em copy pra canal específico), --listar (lista cases
  do ecossistema filtrados por nicho/perfil/objeção), --biblioteca
  (exporta biblioteca de proof por objeção quebrada). Integra com
  dossie-mentorada (lê profile 17-cases), bestseller-book (case vira
  capítulo), skill-pagina-vendas (case vira seção), analise-anuncio-1000
  (case vira VSL), tatou-2.0 (dispara captação quando KPI verde é
  atingido). Use quando a Tata pedir "captar case", "case da
  [mentorada]", "validar proof", "gerar prova social pra página", "case
  pra VSL", "biblioteca de cases", "lista de cases por objeção", "termo
  de uso de imagem", "case real virou copy". Filosofia: case real >
  promessa. Sem cases, narrativa é só promessa. Método Imperatriz de
  Cases — propriedade Tata Gonçalves.
---

# Cases Imperatriz — Pilar 7 (Tribo) da Travessia

Esta skill é o **motor de captação, validação e ativação de cases reais** do ecossistema Travessia Imperatriz. No Brasil 2026 (mercado estágio 4+), prova social estruturada é o ativo #2 de copy — atrás só do mecanismo único. Sem cases, página de vendas é promessa, VSL é discurso, ad é fé.

## Filosofia central

> **Caso real > promessa. Número específico > adjetivo. Print autorizado > storytelling. Frase da mentorada > frase da Tata. Sem cases, narrativa é só fé.**

Cases não são depoimento solto. São ativos estruturais de imperio:
- Viram seção de página de vendas
- Viram capítulo de livro
- Viram VSL de 8-12 minutos
- Viram ad de retargeting
- Viram e-mail de objeção
- Viram post de palco

## Quando usar

- Tata identifica mentorada que mudou de nível na Hierarquia (Princesa → Duquesa, Duquesa → Marquesa, etc.)
- Tata identifica KPI verde atingido (faturamento dobrou, NPS > 80, recompra > 40%, time montado)
- Tata identifica pipeline completo (porta A até porta Z destravada)
- Tata precisa de proof pra quebrar objeção específica em copy nova
- Tata vai escrever página de vendas / e-mail / VSL / livro e precisa de case pronto
- Tata quer auditar se case existente tem proof stack robusto
- Tata quer biblioteca de cases organizada por objeção

## Regra crítica — o que é case e o que NÃO é

**É case:**
- Mentorada real autorizada com proof stack de 3+ tipos
- Antes/depois mensurável em número específico
- Tempo declarado entre antes e depois
- Frase original da mentorada (sem retoque)
- Termo de uso de imagem assinado

**NÃO é case:**
- Depoimento solto sem número
- Print sem contexto
- "Aluna fulana faturou 100k" sem proof
- Story narrado pela Tata sem voz da mentorada
- Caso ficcional ou inflado

Se faltar qualquer item da lista "É case", a skill NÃO entrega — sinaliza gap e devolve pra captação.

---

## MODOS DE OPERAÇÃO

A skill roda em **5 modos** declaráveis:

- **`/cases-imperatriz --captar [nome]`** — envia formulário dos 8 blocos pra mentorada preencher
- **`/cases-imperatriz --validar [nome]`** — audita proof stack contra hierarquia de evidência (7 níveis)
- **`/cases-imperatriz --gerar-copy [nome] [canal]`** — transforma case em copy pronta pra canal
- **`/cases-imperatriz --listar`** — lista todos cases do ecossistema (filtros: nicho, nível Hierarquia, objeção)
- **`/cases-imperatriz --biblioteca`** — exporta biblioteca de proof organizada por objeção quebrada

Se a Tata não declarar modo, perguntar: **"captar novo, validar existente, gerar copy de case, listar ou exportar biblioteca?"**

---

## PROCESSO — 8 FASES OBRIGATÓRIAS

### FASE 0 — Detecção do proof point

A skill é disparada por `tatou-2.0` quando uma das 4 condições aciona:

1. **Mudança de nível na Hierarquia Imperatriz** — mentorada subiu de Princesa → Duquesa, Duquesa → Marquesa, Marquesa → Imperatriz
2. **KPI verde atingido** — faturamento ≥ meta declarada, NPS ≥ 80, recompra ≥ 40%, churn ≤ 10%, time ≥ 3 pessoas
3. **Pipeline completo** — porta A até a porta declarada como objetivo destravada (validado por `gates-imperatriz`)
4. **Proof point qualitativo** — saiu em palco, virou capa de revista, foi citada por autoridade do nicho, fechou contrato grande

Se nenhuma condição acionou, perguntar à Tata: **"qual o proof point dessa mentorada que justifica captação de case agora?"**

### FASE 1 — Leitura do dossiê 17-cases

Antes de captar, ler `dossie-mentorada` profile 17-cases:
- Já tem case anterior dessa mentorada?
- Versão v1 ou v2 do case?
- Termo de uso já assinado?
- Histórico de evolução (Princesa → Duquesa → Marquesa)?
- Cases de mentoradas do mesmo nicho pra evitar repetição

Se já existe case v1, decidir: **atualizar v1** ou **criar v2** (evolução).

### FASE 2 — Captação dos 8 blocos

Disparar formulário (ver `ESTRUTURA-CASE-PADRAO.md`) pela mentorada. 8 blocos obrigatórios:

1. Apresentação
2. Ponto de partida (ANTES)
3. Virada
4. Resultados objetivos (DEPOIS)
5. Proof stack
6. Frase-pegada
7. Aplicação
8. Autorização

Se mentorada deixar bloco em branco → skill recusa publicar e devolve pedindo preenchimento.

### FASE 3 — Validação dos números

Para cada número declarado em ANTES/DEPOIS:
- Há print/dado que comprova?
- Print é da fonte oficial (Stripe, Hotmart, Kiwify, banco, planilha de gestão)?
- Datas conferem com tempo declarado?
- Multiplicador (X vezes) bate matematicamente?

Se número não confere ou não tem proof → não publica. Sinaliza gap.

**Regra dura:** nunca arredondar pra cima. Nunca inferir. Se mentorada disse "subiu uns 5x", cobra número exato.

### FASE 4 — Hierarquia de proof stack

Aplicar os **7 níveis de proof** (ver `PROOF-STACK-HIERARQUIA.md`):

1. Texto puro (mais fraco)
2. Texto + número
3. Texto + número + data
4. Print autorizado da fonte oficial
5. Vídeo depoimento curto (15-60s)
6. Vídeo longo + storytelling (3-10min)
7. Reconhecimento público externo (palco, mídia, citação)

Case nota 1000 tem **3+ níveis simultâneos**, sendo pelo menos 1 do nível 4+.

Se case só tem nível 1-2 → skill rebaixa pra "depoimento" e recusa rotular como case.

### FASE 5 — Frase-pegada (extração)

Da resposta da mentorada no Bloco 6, extrair **1 frase original**:
- Sem retoque
- Sem reescrita
- Sem polimento de gramática (corrige só se erro grosseiro impede leitura)
- Tem que soar como ELA, não como a Tata

Aplicar `voz-humana-br` em modo validador, NÃO em modo reescritor — só checa se voz está preservada.

Se frase soar genérica ("a Tata mudou minha vida") → pedir reformulação específica ("a Tata me ensinou a parar de cobrar por hora — em 90 dias passei de R$8k pra R$45k/mês").

### FASE 6 — Aplicação por canal (categorização)

Decidir em qual copy esse case vira proof. Aplicar matriz canal × objeção (ver `APLICACAO-POR-CANAL.md`):

| Canal | Tipo de case ideal | Tamanho |
|-------|-------------------|---------|
| Página de vendas | Antes/depois com números + print + frase | 1 bloco visual + 100 palavras |
| E-mail | 1 case por e-mail focado em 1 objeção | 200-400 palavras |
| VSL | Case completo narrado + vídeo da mentorada | 2-4 minutos |
| Ad estático | Print + 1 frase + nome | 1 imagem |
| Ad vídeo | Vídeo depoimento 15-30s | 15-30s |
| Post Instagram | Carrossel antes/depois 8-10 slides | 8-10 slides |
| Capítulo de livro | Storytelling completo + dados + reflexão | 1500-3000 palavras |
| Stories | Depoimento direto da mentorada | 3-5 stories |
| Palco | Case oral + slide com print | 5-8 minutos |
| Webinar | Case ao vivo + entrevista mentorada | 8-15 minutos |

### FASE 7 — Cruzamento com objeção quebrada

Cada case quebra objeções específicas. Categorizar:

**Objeções de tempo:**
- "Não tenho tempo pra mais isso"
- "Vou demorar muito pra ver resultado"

**Objeções de dinheiro:**
- "Não tenho como investir"
- "Não dá retorno"

**Objeções de identidade:**
- "Pra mim não funciona, meu nicho é diferente"
- "Eu não tenho perfil"
- "Sou tímida demais"

**Objeções de capacidade:**
- "Não sei tecnologia"
- "Não tenho time"
- "Não sei vender"

**Objeções de timing:**
- "Não é o momento certo"
- "O mercado está ruim"

Para cada case, marcar 2-4 objeções que ele quebra com mais força. Vai pra biblioteca de proof por objeção.

### FASE 8 — Autorização legal

Antes de publicar em qualquer canal, validar:

1. Termo de uso de imagem assinado (ver `FORMULARIO-AUTORIZACAO.md`)
2. Canais autorizados declarados (Instagram, e-mail, página, livro, palco, ads pagos)
3. Prazo de uso declarado (1 ano, 3 anos, perpétuo)
4. Direito à imagem em vídeo separado de imagem em foto
5. Possibilidade de versão anônima (sim/não)
6. Limites declarados (não pode aparecer em ad de remarketing? Não pode em palco?)

**Regra dura:** sem termo assinado físico ou digital com data → não publica em canal nenhum.

Se case foi captado pré-termo, retroautorizar antes de qualquer uso.

---

## FORMATO DE OUTPUT — MODO `--captar`

```
# CASE IMPERATRIZ — CAPTAÇÃO INICIADA

## MENTORADA: [nome]
- Nível atual na Hierarquia: [Princesa / Duquesa / Marquesa / Imperatriz]
- Proof point detectado: [descrição]
- Disparado por: [tatou-2.0 / Tata manual / gates-imperatriz]
- Versão do case: [v1 nova / v2 evolução]

## FORMULÁRIO ENVIADO

[8 blocos do template padrão — ver ESTRUTURA-CASE-PADRAO.md]

## CHECKLIST DE COMPLETUDE

- [ ] Bloco 1 (Apresentação)
- [ ] Bloco 2 (ANTES)
- [ ] Bloco 3 (Virada)
- [ ] Bloco 4 (DEPOIS)
- [ ] Bloco 5 (Proof stack — mínimo 3 itens)
- [ ] Bloco 6 (Frase-pegada)
- [ ] Bloco 7 (Aplicação)
- [ ] Bloco 8 (Autorização — termo assinado)

## PRÓXIMO PASSO
Após mentorada preencher → rodar `/cases-imperatriz --validar [nome]`
```

---

## FORMATO DE OUTPUT — MODO `--validar`

```
# AUDITORIA DE CASE — [nome da mentorada]

## SCORE GERAL
- Proof stack: X/7 níveis presentes
- Completude dos 8 blocos: X/8
- Termo de uso assinado: [sim / não]
- Classificação: [Bronze / Prata / Ouro / Diamante]

## NÍVEIS DE PROOF PRESENTES
1. [X] Texto puro
2. [X] Texto + número
3. [X] Texto + número + data
4. [X] Print autorizado
5. [ ] Vídeo curto
6. [ ] Vídeo longo
7. [ ] Reconhecimento público

## GAPS IDENTIFICADOS
### Gap 1: [descrição]
**O que falta:** [item específico]
**Como resolver:** [ação]
**Impacto se não resolver:** [onde não pode ser usado]

## RECOMENDAÇÃO
- [ ] Pronto pra publicar em todos canais
- [ ] Pronto pra publicar em [canais X, Y]
- [ ] Precisa retorno à captação antes de publicar
- [ ] Rebaixar pra "depoimento" (não atinge nível de case)

## OBJEÇÕES QUEBRADAS
1. [objeção] — força: alta/média/baixa
2. [objeção] — força: alta/média/baixa
```

---

## FORMATO DE OUTPUT — MODO `--gerar-copy [nome] [canal]`

Output adapta ao canal escolhido. Ver `APLICACAO-POR-CANAL.md` pra templates.

Sempre entrega:
1. Versão pronta da copy (sem placeholders)
2. Briefing visual (qual print, qual foto, qual vídeo usar)
3. Checklist de uso (termo assinado? canal autorizado?)
4. Variação A/B opcional pra testar

---

## FORMATO DE OUTPUT — MODO `--listar`

```
# BIBLIOTECA DE CASES — TRAVESSIA IMPERATRIZ

## TOTAL: X cases ativos
- Princesa: X
- Duquesa: X
- Marquesa: X
- Imperatriz: X

## POR NICHO
- Mentora high-ticket: X
- Coach: X
- Esteticista: X
- ...

## POR OBJEÇÃO QUEBRADA (top 5)
- "Não tenho tempo": X cases
- "Pra mim não funciona": X cases
- ...

## LISTA DETALHADA
[Tabela: nome | nível | nicho | proof score | canais autorizados | última atualização]
```

---

## FORMATO DE OUTPUT — MODO `--biblioteca`

```
# BIBLIOTECA DE PROOF POR OBJEÇÃO

## OBJEÇÃO: "Não tenho tempo pra mais isso"
### Cases que quebram (3+):
1. [nome] — [resumo em 1 linha + número]
2. [nome] — [resumo em 1 linha + número]
3. [nome] — [resumo em 1 linha + número]

### Trecho pronto pra copy:
"[parágrafo de 80 palavras combinando os 3 cases]"

### Frases-pegada disponíveis:
- "[frase 1]"
- "[frase 2]"

[... repetir pra cada objeção ...]
```

---

## INTEGRAÇÃO COM O ECOSSISTEMA

```
gates-imperatriz / tatou-2.0
       ↓ (detecta proof point)
cases-imperatriz --captar
       ↓
cases-imperatriz --validar
       ↓
dossie-mentorada (atualiza profile 17-cases)
       ↓
       ├── bestseller-book (case vira capítulo)
       ├── skill-pagina-vendas (case vira seção de prova social)
       ├── analise-anuncio-1000 (case vira VSL de retargeting)
       ├── email-sequence (case vira e-mail de objeção)
       ├── linkedin-empire (case vira post de autoridade)
       └── palco-digital (case vira slide de palco)
```

**Skills adjacentes (não canibalizar):**
- `dossie-mentorada` — armazena cases (cases-imperatriz LÊ dali)
- `tatou-2.0` — dispara captação (cases-imperatriz EXECUTA)
- `gates-imperatriz` — valida pipeline (cases-imperatriz CONFIRMA proof point)
- `analise-anuncio-1000` — analisa VSL pronta com case já incluído
- `headline-imperatriz` — gera headline usando frase-pegada do case

---

## REGRAS DURAS (a skill NÃO negocia)

1. **Nunca inventa case** — se não existe, sinaliza ausência
2. **Nunca arredonda número** pra cima
3. **Nunca publica sem termo assinado** — bloqueia output
4. **Nunca retoca frase-pegada** — voz da mentorada é sagrada
5. **Nunca rotula depoimento como case** — exige proof stack 3+ níveis
6. **Nunca mistura cases** ("uma aluna minha…") — sempre nominal e autorizado
7. **Nunca usa case fora do canal autorizado** no termo
8. **Nunca extrapola prazo** declarado no termo
9. **Sempre cruza** cases por nicho pra evitar repetição
10. **Sempre marca** objeções quebradas pra biblioteca
11. **Sempre versiona** (v1, v2, v3) quando case evolui
12. **Sempre confirma** proof point antes de captar

---

## ARQUIVOS DE REFERÊNCIA (carregar sob demanda)

- `ESTRUTURA-CASE-PADRAO.md` — os 8 blocos detalhados com perguntas
- `PROOF-STACK-HIERARQUIA.md` — os 7 níveis de proof do mais fraco ao mais forte
- `APLICACAO-POR-CANAL.md` — case vira copy pra cada canal (templates)
- `FORMULARIO-AUTORIZACAO.md` — termo de uso de imagem completo
- `EXEMPLOS-CASES-COMPLETOS.md` — 3 cases ficcionais nota 1000 (Princesa/Duquesa/Marquesa)

---

## VERSIONAMENTO

- **v1.0** (atual) — 8 blocos, 7 níveis de proof, 5 modos, integração ecossistema
- **v1.5** (planejado) — auto-deteção de KPI verde via integração com dashboard-imperatriz
- **v2.0** (planejado) — biblioteca cruzada por mecanismo único + temperatura
- **v3.0** (planejado) — tracking de qual case converteu em qual canal (loop ROI por case)

---

## COMO COMPARTILHAR COM MENTORADAS

Esta skill é de uso interno do escritório Tata. Mentoradas NÃO recebem cópia — mas **resultam** dela como protagonistas dos cases. Cases prontos podem ser entregues à mentorada como ativo dela (presente do programa) pra ela usar nas próprias copys.

---

**Método Imperatriz de Cases — propriedade intelectual Tata Gonçalves.**

> Caso real > promessa. Sem cases, narrativa é fé. Com cases, narrativa é convicção.
