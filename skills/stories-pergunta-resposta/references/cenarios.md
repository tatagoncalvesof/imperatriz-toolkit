---
name: cenarios
description: Descrições visuais completas dos 2 cenários permitidos (carro + escritório) com prompts prontos pra IA de imagem
---

# Cenários — Stories Pergunta e Resposta da Tata

Apenas DOIS cenários são permitidos. Cada Q&A precisa do campo `scenario: "carro"` ou `scenario: "escritorio"`.

---

## Cenário 1 — Dentro do carro

### Visual base (sempre presente)
- **Banco**: couro caramelo (caramel leather, cognac tan)
- **Iluminação**: golden hour atravessando vidro (warm golden window light, lens flare sutil)
- **Volante**: visível parcialmente quando faz sentido na composição
- **Background**: levemente desfocado (bokeh natural de cidade ou árvores)

### Poses possíveis
1. **Mão no volante, olhando pra câmera** — clássica, autoridade calma
2. **Olhando pelo espelho retrovisor** — pose introspectiva
3. **Sentada de lado no banco, porta aberta** — descontraída
4. **Selfie ângulo alto, cinto de segurança visível** — íntima, confessional
5. **Mãos no volante, olhar pra frente, perfil** — pensativa
6. **Apoiada na janela aberta, vento no cabelo** — leve, livre

### Quando usar carro
- Q&A confessional ("deixa eu te contar...")
- Reflexões ("eu pensava nisso outro dia...")
- Mindset/virada de chave íntima
- Resposta com tom emocional
- Resposta curta/punchline (selfie de perto cabe)

### ScenePrompts prontos (copy-paste no JSON)

```
"sitting in driver's seat, hands on caramel leather steering wheel, golden hour light streaming through windshield, soft lens flare, looking at camera with warm smile, gold necklace with emerald pendant visible at neckline, light Dior blush, dewy golden-lit skin, candid iPhone selfie quality, slight motion blur"
```

```
"sitting sideways on caramel leather car seat with door open, golden hour, urban background blurred, looking at camera over shoulder, gold necklace catching light, gold rings on hand resting on knee, natural hair with light frizz, casual elegant outfit"
```

```
"car interior shot, looking through rearview mirror reflection, warm caramel leather visible, golden window light on face, gold earrings and necklace with small emerald, contemplative expression, light makeup, real iPhone candid photo"
```

```
"close-up selfie inside car, seatbelt visible, caramel leather seat in background, golden hour glow on face, dewy skin with golden highlight, gold necklace with emerald pendant clearly visible, blush Dior on cheekbones, brown eyeliner, smiling at camera, hair with natural frizz"
```

```
"hands on steering wheel, profile view, looking forward at road through windshield, golden afternoon light, caramel leather interior, gold rings on fingers, gold necklace silhouette visible, contemplative confident expression"
```

```
"leaning on open car window, wind in hair, caramel leather seat behind, urban golden hour light, candid laughing moment, gold jewelry catching sunlight, light dewy makeup, iPhone vertical orientation"
```

---

## Cenário 2 — Escritório

### Visual base (sempre presente)
- **Mesa**: madeira ipê (deep warm wood, ipê hardwood, rich brown grain)
- **Estante**: nichos decorativos com plantas + livros + objetos curados
- **Iluminação**: amarela/quente (warm yellow tungsten, ambient golden light, lamp glow)
- **Plantas**: presentes visivelmente (folhagem verde, vasos elegantes)
- **Background**: estante e plantas levemente desfocadas (bokeh suave)

### Poses possíveis
1. **Sentada na mesa de ipê, laptop fechado** — autoridade calma
2. **Apoiada na mesa, pé apoiado, plantas no fundo** — casual confiante
3. **Sentada na cadeira virada de lado pra mesa** — explicando
4. **Em pé encostada na estante, livros visíveis** — expert
5. **Plano médio, estante e plantas atrás** — ensinando, mãos gesticulando
6. **Olhando pelo lado, mão no rosto, pensativa** — mestria

### Quando usar escritório
- Q&A estratégica ("vou te explicar...")
- Conteúdo técnico ou de ensino
- Resposta densa/longa (sobra espaço pra texto)
- Posicionamento de autoridade
- Insight contraintuitivo

### ScenePrompts prontos (copy-paste no JSON)

```
"sitting at ipê wood desk in warm-lit home office, decorative shelf with plants and books in background slightly blurred, warm yellow tungsten lighting, leaning on elbow looking at camera, gold necklace with small emerald pendant, gold rings, dewy makeup with Dior blush, hair with natural texture and frizz, candid working photo"
```

```
"medium shot in home office, standing in front of decorative shelf with green plants and books, warm yellow ambient light, looking at camera with confident smile, gold jewelry visible (necklace with emerald, rings, earrings), light golden-lit skin, casual elegant outfit, real iPhone photo quality"
```

```
"casual pose leaning against ipê desk edge, decorative niches with plants behind, warm tungsten light from lamp, golden hour through window mixing with interior light, gold necklace catching light, hand resting near MacBook, light makeup, friendly natural expression"
```

```
"sitting on desk corner with plants and shelf in background, warm yellow office light, gold necklace with emerald and gold rings visible, dewy golden skin, looking at camera over shoulder, hair with natural frizz, candid moment"
```

```
"in front of shelf with plants and curated decorative objects, warm interior lighting, soft bokeh background, hands gesturing while explaining, gold jewelry catching warm light, light Dior blush, brown eyeliner, hair down with natural movement"
```

```
"close-up at ipê desk, plants in soft-focus background, warm ambient light from desk lamp, looking thoughtfully off-camera, hand near face showing gold ring, gold necklace with emerald clearly visible, dewy skin, mascara on lashes"
```

---

## Distribuição sugerida (10 stories)

Para variedade visual ao longo dos 10 stories, distribua aproximadamente 5 carro + 5 escritório, alternando.

Exemplo de ordem por colorIndex:
| # | Cenário | Pose sugerida |
|---|---|---|
| 01 | Carro | Mão no volante, olhar câmera |
| 02 | Escritório | Sentada na mesa de ipê |
| 03 | Carro | Selfie ângulo alto |
| 04 | Escritório | Em pé na estante |
| 05 | Carro | Olhando pelo retrovisor |
| 06 | Escritório | Plano médio gesticulando |
| 07 | Carro | Apoiada na janela aberta |
| 08 | Escritório | Apoiada na mesa, pé apoiado |
| 09 | Carro | Sentada de lado, porta aberta |
| 10 | Escritório | Olhando pelo lado, pensativa |

## Regras visuais para AMBOS os cenários

- **Rosto**: SEMPRE nos 30-50% superiores do frame (deixa 50%+ inferior pra caixinha)
- **Joias**: colar de ouro com esmeralda + outras peças douradas SEMPRE visíveis
- **Pele**: textura real (poros, linhas), iluminação dourada, blush nas maçãs
- **Cabelo**: solto, com frizz natural, NÃO penteado de salão
- **Maquiagem**: leve, brown eyeliner, mascara, blush Dior alto, gloss labial
- **Vibe**: foto de iPhone, não estúdio. Levemente granulada, candid.
- **NUNCA**: foto de banco de imagem, pose corporativa, fundo branco infinito, iluminação de estúdio
