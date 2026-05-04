# BRIEFING PARA IA DE IMAGEM — Templates Prontos

Como escrever prompts que geram imagem de alta qualidade em cada IA (Midjourney, Ideogram, Gemini, DALL-E, Firefly).

---

## ESTRUTURA UNIVERSAL DE UM PROMPT FORTE

Todo prompt potente tem 7 elementos:

1. **Sujeito** — quem/o que
2. **Acao** — o que esta fazendo
3. **Cenario** — onde
4. **Estilo visual** — estetica
5. **Iluminacao** — qualidade da luz
6. **Composicao** — angulo, enquadramento
7. **Parametros tecnicos** — aspect ratio, qualidade, estilo (especifico da ferramenta)

---

## MIDJOURNEY v6 / v7

### Anatomia do prompt Midjourney

```
[Sujeito detalhado], [acao], [cenario], [estilo], [iluminacao], [composicao] --ar [proporcao] --v [versao] --style [estilo]
```

### Template 1 — Retrato de avatar BR

```
Professional brazilian woman in her 40s, wearing beige blazer, confident expression, 
working on laptop in sunlit home office with plants, natural warm lighting, 
golden hour, shot on 50mm lens, shallow depth of field, editorial style, 
warm color palette terracotta and cream, clean minimal aesthetic 
--ar 16:9 --v 6 --style raw
```

### Template 2 — Ilustracao de conceito abstrato

```
Abstract illustration of transformation journey, flowing organic shapes, 
gradient from warm terracotta to deep burgundy, soft curves, minimalist, 
editorial magazine style, premium aesthetic, clean composition, negative space 
--ar 4:5 --v 6
```

### Template 3 — Hero de landing page

```
Elegant brazilian entrepreneur woman smiling softly, 45 years old, 
wearing cream silk shirt, holding cup of coffee, seated at wooden table 
with notebook and plants, natural window light, cozy warm home aesthetic, 
editorial photography style, shallow depth of field, muted color palette, 
terracotta and beige tones, sophisticated 
--ar 16:9 --v 6 --style raw --q 2
```

### Parametros uteis Midjourney

- `--ar 16:9` horizontal (site hero, video)
- `--ar 1:1` quadrado (Instagram post)
- `--ar 9:16` vertical (stories, reels)
- `--ar 4:5` Instagram post alto
- `--v 6` versao atual
- `--style raw` reduz "arte MJ" padrao, mais realista
- `--q 2` qualidade maxima (custa mais creditos)
- `--chaos 10-30` adiciona variacao
- `--stylize 50-200` controla estilizacao (100 default)

---

## IDEOGRAM 2.0

### Especialidade
Texto DENTRO da imagem com qualidade (logos, posts, criativos).

### Anatomia do prompt Ideogram

```
[Descricao da cena], with text that says "[TEXTO EXATO]", [estilo], [cor], [composicao]
```

### Template 1 — Post Instagram com frase

```
Modern minimalist Instagram post design, cream background with terracotta accents,
with text that says "Mulher 40+, seu momento e agora",
elegant serif typography, professional editorial layout,
soft gradient, subtle shadow, premium aesthetic, 1:1 square format
```

### Template 2 — Criativo de ads

```
Professional ad creative, split layout with photo on left and text on right,
with text that says "Perca 8kg em 60 dias sem dieta",
warm color palette, brazilian woman 45 years old smiling,
modern serif + sans-serif typography combination, high converting ad design,
clean minimal style
```

### Template 3 — Capa de e-book / carrossel

```
Ebook cover design, elegant and premium,
with text that says "METODO IMPERATRIZ" as main title,
with text that says "Como transformar sua copy em maquina de vendas" as subtitle,
editorial magazine aesthetic, serif typography, 
cream and gold color palette, professional layout
```

### Parametros Ideogram

- Aspect ratio selecionavel na interface
- "Style" options: Auto, General, Realistic, Design, 3D, Anime
- "Magic Prompt" on/off (expande teu prompt automaticamente)

---

## GOOGLE GEMINI NANO BANANA / IMAGEN

### Especialidade
Rostos brasileiros naturais, ilustracoes cotidianas, fotos realistas BR.

### Anatomia do prompt Gemini

Mais conversacional que Midjourney. Pode descrever em portugues.

### Template 1 — Rosto BR autentico

```
Fotografia profissional de uma mulher brasileira de 45 anos, 
tracos suaves, pele morena clara, cabelo castanho, 
sorrindo de forma natural, olhando pra camera, 
vestindo camisa branca, sentada em casa com plantas ao fundo, 
luz natural quente, estilo editorial, 
composicao 3/4, foco nos olhos, 
proporcao 16:9, alta qualidade
```

### Template 2 — Cena cotidiana brasileira

```
Ilustracao de uma mulher empresaria brasileira trabalhando em casa, 
notebook aberto, xicara de cafe, caderno com anotacoes, 
plantas no peitoril da janela, luz dourada do final de tarde, 
estilo editorial moderno, cores quentes (terracota, creme, dourado),
proporcao quadrada 1:1
```

### Template 3 — Grupo diverso BR

```
Grupo de 4 mulheres brasileiras empresarias, idades entre 35 e 55 anos, 
diversidade etnica genuina, todas sorrindo em conversa descontraida, 
sentadas em mesa com cafe e notebooks, ambiente de coworking moderno 
com plantas e luz natural, estilo fotografia editorial, 
cores quentes e terrosas, proporcao 16:9
```

---

## DALL-E 3 (via ChatGPT)

### Especialidade
Conversacional, interativo, itera rapido.

### Dica
Melhor usar via ChatGPT em conversa — pede revisoes e refina.

### Template base

```
Crie uma imagem de [descricao detalhada]. 
Estilo: [editorial/minimalista/etc].
Cores: [paleta especifica].
Composicao: [angulo/enquadramento].
Mood: [atmosfera emocional].
Proporcao: [formato].
```

### Exemplo aplicado

```
Crie uma imagem editorial de uma empresaria brasileira sorrindo,
de 40 anos, usando blazer bege, sentada em home office com plantas.
Luz natural quente, estilo fotografia magazine, paleta terracota e creme,
composicao 3/4, foco no rosto com fundo desfocado, proporcao 16:9.
```

---

## ADOBE FIREFLY

### Especialidade
Direitos comerciais seguros (treinado em imagens licenciadas).

### Template 1 — Vetor / ilustracao comercial

```
Vector illustration of [sujeito], flat design style,
color palette: warm terracotta, cream, gold,
clean minimal composition, professional business aesthetic,
suitable for web and print, editorial style
```

### Template 2 — Textura / background

```
Abstract texture background, organic flowing shapes,
gradient from cream to warm terracotta,
subtle noise, premium magazine quality, 
suitable for landing page hero overlay
```

---

## RUNWAY (IMAGEM + VIDEO)

### Especialidade
Animar imagem estatica, gerar video de 5-10 segundos.

### Fluxo
1. Gerar imagem em Midjourney/Gemini
2. Trazer pra Runway
3. Prompt de animacao: "slow zoom in, warm light shift, subtle breathing"

### Use casos
- VSL backgrounds animados
- Hero video de landing
- Instagram Reels de teste

---

## TEMPLATES POR TIPO DE VISUAL

### Tipo 1 — Hero de landing page (pessoa)

**Midjourney:**
```
Brazilian entrepreneur woman 45 years old smiling, cream silk blouse,
professional home office setting, plants and warm lighting, 
natural window light from left, editorial photography style, 
soft depth of field, muted warm color palette, sophisticated
--ar 16:9 --v 6 --style raw
```

**Gemini Nano Banana:**
```
Fotografia profissional de empresaria brasileira 45 anos sorrindo,
blusa cor creme, home office moderno com plantas,
luz natural de manha, estilo editorial, cores quentes,
composicao 3/4, proporcao 16:9
```

### Tipo 2 — Diagrama de mecanismo (ilustracao)

**Firefly (vetor):**
```
Vector infographic illustration of 3-step process,
clean minimalist style, arrows connecting 3 circular icons,
warm terracotta + cream color palette,
professional business aesthetic, flat design
--ar 16:9
```

### Tipo 3 — Post Instagram com frase

**Ideogram:**
```
Minimal Instagram post design, cream background,
with text that says "Promessa fala o QUE. Mecanismo fala o COMO.",
elegant serif typography centered,
subtle texture, premium editorial aesthetic, 1:1 square
```

### Tipo 4 — Ilustracao conceitual abstrata

**Midjourney:**
```
Abstract concept illustration of business growth and transformation,
flowing organic shapes, upward trajectory,
gradient from deep burgundy to warm gold,
minimalist editorial aesthetic, premium magazine style,
clean composition with negative space
--ar 4:5 --v 6
```

### Tipo 5 — Fotografia de produto / mockup

**Midjourney:**
```
Premium notebook and coffee on wooden desk, soft morning light,
plants in blurred background, warm tones, 
editorial lifestyle photography, top-down angle,
muted cream and terracotta palette, premium aesthetic
--ar 4:5 --v 6 --style raw
```

---

## DICAS GERAIS DE PROMPT ENGINEERING

### 1. Seja especifico, nao vago
RUIM: "woman working"
BOM: "brazilian woman 45, beige blazer, laptop on wooden desk, morning light"

### 2. Descreva emocao/mood
RUIM: "elegant"
BOM: "sophisticated, quiet confidence, warm inviting atmosphere"

### 3. Cite estilos visuais conhecidos
- "editorial magazine style"
- "minimalist scandinavian"
- "premium lifestyle photography"
- "warm cinematic aesthetic"

### 4. Iluminacao importa
- "natural window light"
- "golden hour soft light"
- "diffused studio lighting"
- "dramatic side light"

### 5. Aspect ratio primeiro
Sempre declare proporcao no prompt. Muda tudo.

### 6. Itere, nao aceite o primeiro
Gere 4-6 variacoes. Escolha melhor. Refine.

### 7. Use seeds pra consistencia
Se ja tem imagem vencedora, use seed dela pra gerar variacoes no mesmo estilo.

---

## CHECKLIST DE PROMPT APROVADO

Antes de gerar:

- [ ] Sujeito claro
- [ ] Acao definida
- [ ] Cenario especifico
- [ ] Estilo visual citado
- [ ] Iluminacao descrita
- [ ] Composicao/angulo indicado
- [ ] Aspect ratio correto
- [ ] Paleta de cores da marca
- [ ] Estilo combina com identidade do projeto
- [ ] Nao tem clichês (handshake, lightbulb, etc)

Se passar todos → gerar. 

Se resultado nao agradar → refinar prompt (nao tentar outra ferramenta imediatamente).
