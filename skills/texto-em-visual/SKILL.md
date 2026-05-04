---
name: texto-em-visual
description: >
  Motor de transformacao de texto em visual nota 1000 — converte qualquer
  copy (pagina de vendas, VSL, e-mail, carrossel, post, artigo) em
  recomendacoes visuais estruturadas: extrai ideias-ancoras do texto,
  categoriza pelos 6 tipos Dan Roam (Quem/O que, Quanto, Onde, Quando,
  Como, Por que), escolhe tipo de visualizacao ideal entre os 18
  disponiveis (diagrama, flowchart, timeline, matriz 2x2, venn, piramide,
  dashboard, heatmap, journey map, isotype, before/after, etc), gera
  briefing visual para cada ideia (incluindo prompt pra Midjourney,
  Ideogram, Gemini, Figma), aplica os 10 principios universais e valida
  contra 10 anti-patterns. Entrega versoes adaptadas por canal (site,
  Instagram feed, stories, e-mail, VSL, carrossel LinkedIn, apresentacao,
  WhatsApp). Use quando o usuario pedir "transformar texto em visual",
  "criar infografico", "visualizar minha copy", "criar diagrama do meu
  metodo", "como mostrar isso em imagem", "design para minha pagina",
  "briefing visual", "criar visual pro site", "passar isso pra imagem",
  "criar imagem explicativa", "visualizar meu mecanismo", "design do site".
  Metodo Imperatriz de Visual — propriedade Tata Goncalves.
---

# Texto em Visual — Metodo Proprietario Tata Goncalves

Este skill e o **motor de transformacao de texto em visual** nota 1000. Converte qualquer copy em recomendacoes visuais estruturadas, com briefing pronto pra cada canal.

## Filosofia central

> **Cerebro processa imagem 60.000x mais rapido que texto. Menos texto, mais hierarquia visual. 1 ideia = 1 visual.**

Essa skill nao gera a imagem final. Ela gera **o que desenhar + como desenhar + onde colocar + com que ferramenta**. O briefing pronto pra designer humano, pra IA (Midjourney/Ideogram/Gemini), ou pra voce mesma no Figma/Canva.

## Quando usar

- Tata manda copy de pagina de vendas e pede visuais
- Tata quer transformar metodo em diagrama
- Tata quer criar infografico pra Instagram
- Tata quer briefing pra Midjourney/Ideogram
- Tata quer visualizar o mecanismo unico
- Tata quer repensar estrutura visual de site existente
- Mentoranda da Tata (com skill compartilhada) pede o mesmo

## Principio da ciencia aplicada

Os 5 fatos que governam a skill:

1. **60.000x** — cerebro processa imagem mais rapido que texto (Zabisco/3M)
2. **50ms** — tempo que visitante decide se fica ou sai do site
3. **65%** — das pessoas sao aprendizes visuais
4. **6,5x** — retencao de informacao com texto + visual (Dual Coding, Paivio 1971)
5. **12 principios Mayer** — multimedia learning cientificamente validados

---

## MODOS DE OPERACAO

A skill roda em 4 modos:

- **`/texto-em-visual`** (padrao) — completo: le texto, extrai ancoras, gera briefing estruturado por canal
- **`/texto-em-visual express`** — so sugere tipo de visual + briefing rapido (sem analise profunda)
- **`/texto-em-visual por-canal [nome]`** — especifica canal (site, instagram, vsl, carrossel, email, whatsapp)
- **`/texto-em-visual mentoria`** — pedagogico pra mentoranda aprender enquanto gera

---

## PROCESSO — 9 FASES OBRIGATORIAS

### FASE 0 — Leitura do texto

Se usuario mandou copy/texto, LEIA por inteiro antes de qualquer sugestao.

Identificar:
- Tipo de documento (pagina de vendas, VSL, email, artigo)
- Objetivo principal (captar, vender, educar, engajar)
- Publico (temperatura + nivel de consciencia Schwartz se aplicavel)
- Canal de destino (se declarado)
- Mecanismo unico presente (se tem)
- Tom de marca

### FASE 1 — Extracao de IDEIAS-ANCORAS

Cada paragrafo/secao tem 1 ideia central. Listar TODAS as ideias-ancoras do texto.

**Regra:** maximo 1 ancora por paragrafo. Se tem 2, paragrafo precisa ser quebrado.

**Output desta fase:** lista numerada de 8-20 ancoras (dependendo do tamanho do texto).

### FASE 2 — CATEGORIZACAO DAN ROAM (6 tipos de pergunta)

Para cada ancora, perguntar: "que pergunta essa ideia responde?"

| Pergunta | Visual ideal |
|---|---|
| Quem / O que? | Retrato / icone / foto |
| Quanto? | Grafico / dashboard / numero |
| Onde? | Mapa / diagrama espacial |
| Quando? | Timeline / calendario |
| Como? | Flowchart / diagrama de processo |
| Por que? | Diagrama causa-efeito |

### FASE 3 — ESCOLHA DO TIPO DE VISUALIZACAO (dos 18)

Baseado na categoria Dan Roam + contexto, escolher tipo especifico dos 18. Ver `OS-18-TIPOS-VISUALIZACAO.md`.

### FASE 4 — RASCUNHO ESTRUTURAL

Para cada visual, descrever em palavras:
- Elementos presentes (3-7 max)
- Relacao entre elementos (seta, sobreposicao, hierarquia)
- Layout (horizontal, vertical, circular, grid)
- Hierarquia visual (o que e dominante)

### FASE 5 — APLICACAO DOS 10 PRINCIPIOS UNIVERSAIS

Passar cada rascunho pelos 10 principios. Ver `OS-10-PRINCIPIOS.md`:
- Hierarquia visual
- Contraste
- Repeticao
- Alinhamento
- Proximidade
- Espaco negativo
- Cor intencional
- Tipografia como mensagem
- Consistencia
- Simplicidade radical

Se falhar 2+, regenerar rascunho.

### FASE 6 — VALIDACAO ANTI-PATTERNS

Rodar cada visual por `ANTI-PATTERNS-VISUAIS.md`:
- Texto gigante sem imagem
- Imagem decorativa sem funcao
- Mais de 3 cores primarias
- Stock photo obvia
- Icones de estilos diferentes
- Texto sobre imagem sem contraste
- Informacao inacessivel
- Animacao exagerada
- Infografico poluido
- Copia literal de concorrente

### FASE 7 — BRIEFING POR CANAL

Gerar versoes adaptadas ao canal:

**Site (wide):** proporcao horizontal, hierarquia f/z pattern
**Instagram post:** 1:1 quadrado, texto minimo
**Stories:** 9:16 vertical, texto curtissimo
**Email:** vertical clean, 1 imagem max
**VSL:** frame 16:9, animavel
**Carrossel LinkedIn:** 7-10 slides progressivos
**Apresentacao:** 16:9, 1 ideia por slide
**WhatsApp:** quadrado pequeno, texto minimo

### FASE 8 — GERACAO DE PROMPT PARA IA DE IMAGEM

Para visuais que precisam de IA (ilustracoes, fotos, backgrounds), gerar prompt especifico:

**Midjourney:** prompt detalhado com parametros
**Ideogram:** prompt com texto embedded
**Gemini Nano Banana:** prompt com rosto BR natural
**DALL-E:** prompt conversacional
**Adobe Firefly:** prompt + estilo vetor

Ver `BRIEFING-IA-IMAGEM.md` pra templates.

### FASE 9 — OUTPUT ESTRUTURADO

Entregar no formato abaixo.

---

## FORMATO DE OUTPUT (modo completo)

```
# VISUAIS PARA [NOME DO PROJETO/COPY]

## DIAGNOSTICO

- **Tipo de documento:** [pagina/vsl/email/etc]
- **Canal de destino:** [site/instagram/etc]
- **Publico:** [temperatura + nivel]
- **Objetivo principal:** [captar/vender/educar]
- **Ideias-ancoras identificadas:** [numero]
- **Canal principal recomendado:** [X]

---

## MAPA DE VISUAIS

### ANCORA 1 — [titulo da ideia]

**Texto original:** "[trecho do texto]"

**Pergunta Dan Roam:** [Quem/Quanto/Onde/Quando/Como/Por que?]

**Tipo de visualizacao recomendado:** [dos 18]

**Rascunho estrutural:**
- Elementos: [lista 3-7 elementos]
- Relacao entre eles: [setas, sobreposicao, etc]
- Layout: [horizontal/vertical/circular/grid]
- Dominante: [o que o olho ve primeiro]

**Hierarquia visual:**
1. [elemento mais forte]
2. [secundario]
3. [terciario]

**Cor sugerida:** [paleta baseada na marca]

**Ferramenta ideal:** [Figma/Canva/Whimsical/IA/etc]

**Briefing pra IA de imagem (se aplicavel):**
```
[prompt pronto pra Midjourney/Ideogram/Gemini]
```

**Validacao:**
- [X/10] principios universais
- [X/10] anti-patterns evitados

**Versoes por canal:**
- Site: [adaptacao]
- Instagram: [adaptacao]
- Stories: [adaptacao]

---

### ANCORA 2 — [proxima]
[mesmo formato]

[... continua ate esgotar ancoras ...]

---

## RECOMENDACAO DE PRIORIDADE

Se tempo e limitado, priorizar:
1. **CRITICO** — [ancora + razao]
2. **IMPORTANTE** — [ancora + razao]
3. **NICE TO HAVE** — [ancora + razao]

---

## RESUMO EXECUTIVO

**Total de visuais recomendados:** [X]
**Visuais criticos (impacto alto):** [Y]
**Horas estimadas de producao:** [estimativa]
**Ferramentas necessarias:** [lista]
**Investimento se terceirizar:** [R$ estimado]

---

## PROXIMOS PASSOS

1. [acao 1 - mais critica]
2. [acao 2]
3. [acao 3]

## INTEGRACAO COM ECOSSISTEMA TATA
- `/mecanismo-unico` — se precisa descobrir o COMO antes de visualizar
- `/headline-imperatriz` — se precisa de headlines pras imagens
- `/ad-creative` — se e pra ads Meta
- `/design-studio` — pra producao visual profissional
- `/skill-pagina-vendas` — se pagina completa
```

---

## MODO EXPRESS (output minimo)

Se pediu `express`:

```
## VISUAIS RAPIDOS

1. **[Ancora 1]** → [tipo de visual] → Ferramenta: [X] → Prompt IA (se aplicavel)
2. **[Ancora 2]** → [tipo de visual] → Ferramenta: [X] → Prompt IA
[... ate esgotar ...]

## PRIORIDADE: criticos numeros [X, Y, Z]
```

---

## MODO POR-CANAL

Se pediu especifico (ex: `/texto-em-visual por-canal instagram`):

- Ignora outros canais
- Foca formato, proporcao, limitacoes tecnicas do canal
- Output adaptado

### Restricoes tecnicas por canal

**Instagram feed:**
- Post 1:1 (1080x1080) ou 4:5 (1080x1350)
- Texto em 20% da imagem max (regra de alcance)
- Legibilidade mobile (texto minimo 24pt)

**Instagram stories:**
- 9:16 (1080x1920)
- Elementos criticos no centro (topo tem interface)
- Maximo 3 elementos visuais por frame

**LinkedIn carrossel:**
- 7-10 slides ideal
- Cada slide progride narrativa
- Slide 1: hook; Slide 2-N-1: valor; Slide N: CTA

**VSL / YouTube Ads:**
- 16:9 (1920x1080)
- Animavel (pensar em entrada/saida de elementos)
- Safe zone: 80% centro (bordas podem ser cortadas)

**Site hero:**
- Desktop: 1920x1080 horizontal
- Mobile: 414x896 vertical (cortar diferente)
- Dobra: 600px visivel

**Email:**
- 600px largura max
- Vertical stacking
- Imagem 1 por "tela" mobile

**WhatsApp:**
- 1:1 quadrado pequeno (1080x1080)
- Texto MINIMO (app abre pequeno)
- 1 CTA visivel

---

## MODO MENTORIA

Adicionar ao output padrao:

```
## AULA EMBUTIDA

### Por que esse tipo de visual vence
[explicacao didatica]

### Como aplicar sozinha no futuro
[passo a passo pra mentoranda aplicar sem a skill]

### Os erros que 90% das pessoas cometem aqui
[lista + antidoto]

### Proximo nivel
[como evoluir dessa visualizacao simples pra versao sofisticada]
```

---

## INTEGRACAO COM ECOSSISTEMA TATA

**Fluxo ideal:**

```
/mecanismo-unico                (descobrir o COMO)
       ↓
/headline-imperatriz            (headlines por temperatura)
       ↓
/copywriting                    (corpo da copy)
       ↓
/texto-em-visual                ← VOCE ESTA AQUI
       ↓
/ad-creative ou /design-studio  (producao visual final)
       ↓
/bencivenga-method              (scoring copy)
```

**Skills adjacentes (nao canibalizar):**
- `/design-studio` — produz design completo, essa faz briefing
- `/ad-creative` — criativo de ads especifico
- `/ui-ux-pro-max` — design de interface
- `/frontend-design` — codigo de frontend
- `/skill-carrossel-instagram` — carrossel IG especifico

**Papel dessa skill no ecossistema:**
E a ponte entre texto e producao visual. Nao produz arte final, mas gera o briefing que vira arte final.

---

## REGRAS DURAS (a skill NAO negocia)

1. **Nao gera visual pra ideia vaga** — exige ideia-ancora clara
2. **Nao sugere mais de 1 ideia por visual** — 1 ancora = 1 imagem
3. **Nao recomenda stock photo obvia** — sugere alternativa especifica
4. **Nao mistura estilos de icones** em um mesmo briefing
5. **Nao sugere tipografia sem proposito** — toda fonte tem funcao
6. **Nao sugere cores sem sistema** — paleta sempre 60-30-10
7. **Nao pula teste dos 5 segundos** — todo visual passa pelo teste
8. **Nao viola acessibilidade** — contraste WCAG 4.5:1 minimo
9. **Nao sugere visual que copia concorrente literal** — diferencia
10. **Sempre oferece prompt pra IA** quando aplicavel
11. **Sempre versiona por canal** quando usuario nao especifica

---

## ARQUIVOS DE REFERENCIA (carregar sob demanda)

- `OS-10-PRINCIPIOS.md` — principios universais de design visual
- `OS-18-TIPOS-VISUALIZACAO.md` — catalogo de tipos + quando usar cada
- `FRAMEWORKS-TRANSFORMACAO.md` — Dan Roam + Mayer + Tufte + Duarte
- `APLICACAO-POR-SECAO-SITE.md` — visual por secao de site (hero, proof, etc)
- `FERRAMENTAS-E-FLUXO.md` — ferramentas por nivel + fluxo de producao
- `ANTI-PATTERNS-VISUAIS.md` — 10 erros fatais + antidoto
- `ADAPTACAO-BR-VISUAL.md` — estetica BR, cores, fontes, referencias
- `BRIEFING-IA-IMAGEM.md` — templates pra Midjourney, Ideogram, Gemini

---

## VERSIONAMENTO

- **v1.0** (atual) — 18 tipos visualizacao, 4 modos, 9 fases, briefing IA embutido
- **v1.5** (planejado) — biblioteca de visuais vencedores BR por nicho
- **v2.0** (planejado) — integracao direta com ferramentas de geracao (API)
- **v3.0** (planejado) — feedback loop com performance dos visuais produzidos

---

## COMO COMPARTILHAR COM MENTORANDAS

Copiar pasta `/Users/tamiresgoncalves/.claude/skills/texto-em-visual/` pra `~/.claude/skills/` da mentoranda.

Ver `README.md` pra instrucoes.

---

**Metodo Imperatriz de Visual — propriedade intelectual Tata Goncalves.**
