---
name: identidade-tata
description: Identidade visual fechada da Tata para geração de fotos com IA — joias, maquiagem, pele, corpo, cabelo
---

# Identidade Visual — Tata Gonçalves (Fechada)

Toda foto gerada por essa skill DEVE preservar TODOS os elementos abaixo. Sem exceção.

## Joias (obrigatórias em todas as fotos)

### Colar
- **Tipo**: corrente fina de ouro amarelo
- **Pingente**: pedra de esmeralda **pequenina** (não dramática — sutil, elegante)
- **Posição**: na altura da clavícula, visível mesmo em selfie de perto
- **EN para prompt**: `gold thin chain necklace with small delicate emerald pendant at collarbone`

### Outras joias douradas
- **Brincos**: ouro amarelo, pequenos a médios (não maximalistas)
- **Anéis**: ouro amarelo, podem ser empilhados em uma mão
- **Pulseira/relógio**: ouro amarelo OU rose gold
- **EN para prompt**: `gold yellow stacked rings on fingers, small to medium gold earrings, gold-toned wristwatch or bracelet`

### Regra de ouro
- **NUNCA** prata
- **NUNCA** acessório colorido brilhante
- **NUNCA** bijuteria visivelmente fake (sem cor brilhosa de tinta)
- O ouro precisa **brilhar com a luz** — golden hour ou luz quente realça as peças

## Maquiagem

### Estilo: leve, "quietly expensive"
Não é maquiagem de festa. É a maquiagem do dia a dia da Tata, com produtos premium.

### Componentes
| Item | Detalhe | EN para prompt |
|---|---|---|
| Base | cobertura média natural, dewy finish | `medium-coverage dewy foundation` |
| Blush | **Dior** (rosado quente / pêssego), aplicado **alto nas maçãs** | `Dior peachy-pink blush high on cheekbones` |
| Iluminador | dourado discreto nas maçãs e topo da bochecha | `subtle gold highlighter on cheekbones, golden glow` |
| Olhos | sombra neutra/marrom, **eyeliner marrom** (não preto) | `brown eyeliner, soft brown eyeshadow` |
| Cílios | máscara marrom, espessos e definidos | `brown mascara, thick defined lashes` |
| Lápis | **marrom** na linha d'água | `brown waterline pencil` |
| Sobrancelha | natural, preenchida com lápis marrom claro | `natural full brows, light brown pencil fill` |
| Lábios | gloss nude / rosa amadeirado | `nude pinkish-brown lip gloss` |

### Iluminação dourada na pele
- Pele **dewy** com brilho dourado nas áreas altas (testa, maçãs, ponta do nariz)
- Efeito final: pele que parece tocada pelo sol
- **EN**: `dewy skin with golden glow on high points (forehead, cheekbones, nose bridge)`

## Pele e textura (CRÍTICO — anti-IA-plástico)

A pele NUNCA pode parecer perfeita/idealizada. Sempre realista.

| Elemento | Manter | NUNCA |
|---|---|---|
| Poros | visíveis em close | apagar/borrar |
| Linhas de expressão | leves, naturais ao redor dos olhos | suavizar todas |
| Sardas/marcas naturais | preservar | retocar |
| Brilho/oleosidade | leve em zona T | secar completamente |
| Textura geral | realista, não-plástica | filtro Instagram beleza pesado |

### EN para prompt (anti-plastic)
```
visible skin pores, natural expression lines, slight shine in T-zone, realistic skin texture, NOT smooth/plastic, real iPhone photo quality, no beauty filter
```

## Corpo

### Regra absoluta
**NUNCA** alterar o corpo da Tata. Manter fidelidade total às fotos de referência.

| Aspecto | Regra |
|---|---|
| Tipo corporal | plus size — preservar TODAS as curvas |
| Cintura | NUNCA afinar |
| Braços/ombros | NUNCA afinar |
| Rosto | NUNCA emagrecer / afinar mandíbula |
| Pescoço | manter natural |

### EN para prompt
```
plus size body type, NEVER slim down, preserve real body proportions from reference photos, body identical to reference, full natural curves
```

## Cabelo

### Características fixas
- **Cor**: castanho (brown shoulder-length)
- **Comprimento**: na altura dos ombros
- **Textura**: natural, com **frizz** e flyaways
- **Movimento**: nunca penteado de salão / chapinha pesada

### EN para prompt
```
brown shoulder-length hair with natural frizz and flyaways, slight wave, hair with movement and texture, NOT salon-perfect, NOT straightened flat
```

### Variações permitidas
- Solto (default)
- Atrás da orelha de um lado (mostrando brinco)
- Levemente preso atrás (rabo baixo descontraído)

### NUNCA
- Coque alto formal
- Penteado tipo "casamento"
- Cabelo molhado/úmido
- Cabelo extremamente liso

## Olhos e expressão

| Elemento | Detalhe |
|---|---|
| Cor | castanho quente (warm brown eyes) |
| Expressão default | sorriso suave amigável (friendly soft smile) |
| Variações | reflexivo, contemplativo, rindo natural, focado |
| NUNCA | sorriso forçado de banco de imagem, pose "modelo" |

## Roupas

### Estilo: casual elegante brasileiro
- Blusas básicas em cores quentes (cream, off-white, terracotta, marrom, preto sóbrio)
- Tecidos bons: linho, algodão de qualidade, malha fina
- Decote em V ou redondo (deixa o colar visível)
- **NUNCA**: roupa estampada chamativa, cores neon, logos visíveis

### EN para prompt
```
casual elegant Brazilian outfit, neutral warm tones (cream, terracotta, brown, soft black), good quality fabric (linen, cotton, fine knit), V-neck or crew neck (necklace visible), no loud prints, no logos
```

## Cara/rosto livre (REGRA CRÍTICA DA SKILL)

A caixinha de pergunta JAMAIS pode estar sobre o rosto da Tata.

- **Rosto da Tata**: deve ocupar 30-50% superiores do frame
- **Caixinha**: começa em 60% da altura do frame
- **Margem de segurança**: 10% entre o queixo e a caixinha
- Se a foto gerada tiver o rosto muito baixo, **regerar** com prompt mais explícito sobre framing

### EN para prompt (framing)
```
face positioned in upper 30-50% of vertical 9:16 frame, leaving entire bottom half clear for text overlay, head shot composition with breathing room above and below face
```

## Resumo do prompt final (template)

Use este template em CADA `scenePrompt` do JSON:

```
[CENÁRIO base do references/cenarios.md], 
Brazilian woman with brown shoulder-length hair with natural frizz, 
warm brown eyes, friendly soft smile, plus size body type (preserve curves identically), 
gold thin chain necklace with small delicate emerald pendant visible at collarbone, 
gold rings, gold earrings, gold-toned wristwatch, 
medium-coverage dewy foundation with golden glow, Dior peachy blush high on cheekbones, 
subtle gold highlighter, brown eyeliner, brown mascara, brown waterline pencil, 
nude lip gloss, visible skin pores and natural texture, 
casual elegant outfit in warm neutral tones with V-neck (necklace visible), 
face positioned in upper 30-50% of vertical 9:16 frame, 
leave entire bottom half clear for text overlay, 
candid iPhone photo quality, NOT plastic, NOT studio, real and natural
```
