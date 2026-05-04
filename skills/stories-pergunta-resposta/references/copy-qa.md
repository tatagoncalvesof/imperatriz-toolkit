---
name: copy-qa
description: Framework de extração e copy das 10 perguntas e respostas — Sexy Canvas + Bencivenga + tom da Tata
---

# Copy das Perguntas e Respostas

Como extrair os 10 melhores Q&As de uma aula da Tata e escrevê-los pra virar story que viraliza.

## Princípio fundamental

A pessoa lê e pensa:
- **"caraca, virou uma chave aqui"** (insight/transformação)
- **"quem é essa mulher?"** (curiosidade sobre a Tata)

NUNCA: "ah, ela tá vendendo algo"

## Anatomia de cada item

```json
{
  "question": "max 80 chars — soa como seguidor real escrevendo",
  "answer": "max 200 chars — tom da Tata + 2-3 **palavras** em asteriscos",
  "stickerLabel": "max 50 chars — hook contextual que substitui 'pergunte-me algo'",
  "mood": "confident | reflective | warm | empowering | thoughtful | bold",
  "scenario": "carro | escritorio",
  "scenePrompt": "ambiente + pose + iluminação (NÃO descrever rosto/corpo)",
  "colorIndex": 0
}
```

## A pergunta (max 80 caracteres)

### Como deve soar
- **Como seguidor real** escrevendo na caixinha de perguntas
- **Português coloquial brasileiro** (não institucional, não corporativo)
- Pode ter erro de digitação leve, abreviação, falta de pontuação
- **Curiosidade**: a pergunta precisa fazer querer ler a resposta

### Templates que funcionam
| Tipo | Template | Exemplo |
|---|---|---|
| Confessional | "como você [verbo pessoal]?" | "como você começou sem ninguém apoiar?" |
| Permissão | "posso [ação polêmica]?" | "posso cobrar caro mesmo começando?" |
| Curiosidade | "qual sua opinião sobre [X]?" | "qual sua opinião sobre cursos gratuitos?" |
| Insegurança | "será que eu consigo [X]?" | "será que eu consigo sem saber programar?" |
| Comparação | "vc faria [X] ou [Y]?" | "vc faria sociedade ou contrataria CLT?" |
| Tempo | "quanto tempo [X]?" | "quanto tempo até dar resultado?" |
| Erro | "qual o maior erro de quem começa?" | "qual o maior erro de quem ta começando?" |

### NÃO fazer
- ❌ Pergunta longa (> 80 chars)
- ❌ Pergunta institucional ("Quais são as estratégias para...")
- ❌ Pergunta retórica que não cabe na caixinha
- ❌ Pergunta com 3 perguntas dentro

## A resposta (max 200 caracteres)

### Tom da Tata (não-negociável)
A Tata fala:
- "você / cê / a gente"
- Pé no chão, sem rodeio
- Mistura português coloquial com termo técnico ocasional
- Tem bordões: "**porque**", "**a verdade é que**", "**ó**", "**tipo assim**"
- Confronta gentil: NÃO faz "coitadinho da audiência", joga real
- Usa números concretos (R$, dias, horas, %)

### Estrutura ideal
```
[Punchline curta direta]. [Reasoning com "porque"]. [Insight final que vira chave].
```

### Bencivenga aplicado
- **Fascination hook**: a primeira frase tem que fisgar
- **"Porque" reasoning**: explicar com "porque" deixa a frase mais persuasiva
- **SE...ENTÃO**: construção condicional cria lógica clara
- **Específico > genérico**: "R$164k em 11 minutos" > "muito dinheiro rápido"
- **Curiosidade**: terminar deixando vontade de saber mais

### Marca-texto: 2-3 palavras com `**`
Use `**palavra**` em palavras estratégicas:
- Sempre em **substantivos ou verbos principais** (NUNCA em "de", "para", "com")
- Sempre em palavras que carregam o INSIGHT (não palavras genéricas)
- 2 palavras quando a resposta é curta, 3 quando é longa
- As palavras destacadas, lidas isoladas, formam um mini-insight

### Exemplos calibrados

**Pergunta**: "como você começou sem ninguém apoiar?"
**Resposta**: "Comecei **sozinha**, sem grupo, sem palmas. A diferença é que eu **não esperei** os outros aprovarem."
**Marca-texto isolado**: "sozinha • não esperei" → mini-insight

**Pergunta**: "posso cobrar caro mesmo começando?"
**Resposta**: "Pode. Preço não é sobre tempo — é sobre **transformação**. Cobrar barato é o que mantém vc **invisível**."
**Marca-texto isolado**: "transformação • invisível"

**Pergunta**: "qual o maior erro de quem ta começando?"
**Resposta**: "**Esperar** ficar pronto. Você nunca fica. Quem **age antes** ganha vantagem injusta — e o resto fica só estudando."
**Marca-texto isolado**: "esperar • age antes"

**Pergunta**: "como saber se minha ideia presta?"
**Resposta**: "Se **alguém pagou**, presta. O resto é teoria. **Validação** não é opinião do amigo, é PIX no extrato."
**Marca-texto isolado**: "alguém pagou • validação"

### NÃO fazer
- ❌ Resposta institucional ("É importante destacar que...")
- ❌ Resposta com lista (1. 2. 3. — não cabe em story)
- ❌ Resposta sem punchline (só explicação)
- ❌ Marca-texto em palavra fraca ("e", "mas", "muito")
- ❌ Bordão de outro guru ("vamos juntos!", "tamo junto!")

## A label do sticker (max 50 caracteres)

### Função
Substitui o "pergunte-me algo" padrão. Já dá o tema da pergunta antes mesmo de ler.

### Templates
| Template | Exemplo |
|---|---|
| "sobre [tema]..." | "sobre começar do zero..." |
| "respondendo [pergunta]" | "respondendo sobre preço alto" |
| "[tema] sem rodeio" | "validação sem rodeio" |
| "vc me pergunta sobre [X]" | "vc me pergunta sobre IA" |
| "[insight] na real" | "começar antes na real" |

### Regra
A label precisa **conversar** com a pergunta. Se a pergunta é sobre preço, a label fala de preço.

## Variedade nos 10 itens (CRÍTICO)

Os 10 não podem ser todos do mesmo tom. Distribuição alvo:

| Tipo | Quantidade | Característica |
|---|---|---|
| Dica prática | 3 | Tática direta, "faz X" |
| Mudança de mentalidade | 2 | Virada de chave, redefinição |
| História pessoal | 2 | "Eu fiz isso", confessional |
| Insight contraintuitivo | 2 | Vai contra o senso comum |
| Controverso | 1 | Provoca discussão saudável |

## Sexy Canvas — gatilho por Q&A

Cada um dos 10 deve ativar UM dos gatilhos abaixo (idealmente 8 diferentes nos 10):

| Gatilho | Como aparece |
|---|---|
| Ganância | dinheiro, multiplicar, economia, R$ |
| Preguiça | automático, sem esforço, IA faz por você |
| Orgulho | dominar, autonomia, ser o melhor, autoridade |
| Inveja | "outros já fazem", concorrente, ficando pra trás |
| Luxúria | desejar a vida ideal, momento depois, status |
| Ira | revolta contra sistema, gestor ruim, ferramenta cara |
| Criança interior | medo, insegurança, "será que consigo?" |
| Curiosidade | "será que tem segredo?", insight escondido |

## Frameworks de copy invisíveis

Cada Q&A puxa de UM destes universos (sem mencionar diretamente):

### Russell Brunson (funis, oferta)
- Precificação por transformação
- Stack de valor
- Funil de 3 páginas
- História antes/depois
- Empacotamento

### Gary Bencivenga (copy, persuasão)
- Fascination hooks
- "SE...ENTÃO"
- Momento depois
- Prova específica
- Curiosidade

### Alex Hormozi (valor, escala, modelo)
- R$/hora
- Informação vs implementação
- Equipe enxuta
- LTV
- Atenção qualificada

### Tata original (mentoria, IA, posicionamento)
- IA como executora, você como direção
- "Ferramenta não é problema, falta de método é"
- "Não venda hora, venda transformação"
- "App em 11 minutos no avião"

## Workflow de extração da transcrição

1. **Ler transcrição inteira** primeiro
2. **Listar TODAS as perguntas** que aparecem (do público + retóricas)
3. **Listar TODOS os bordões/frases típicas** da Tata daquela aula
4. **Listar TODOS os insights/viradas de chave** mencionados
5. **Pareiar**: cada pergunta com a melhor resposta (palavras da Tata, não suas)
6. **Reescrever** mantendo o tom mas cabendo no limite (80 + 200)
7. **Adicionar marca-texto** em 2-3 palavras-chave por resposta
8. **Atribuir cenário** (carro/escritório) por afinidade emocional
9. **Atribuir mood** que vai informar pose/expressão da foto
10. **Validar variedade** (5 cenários cada, mix de tipos, mix de gatilhos)

## Checklist final dos 10 Q&As

Antes de mandar pra geração:

- [ ] 10 perguntas, 10 respostas
- [ ] Todas perguntas ≤ 80 chars
- [ ] Todas respostas ≤ 200 chars
- [ ] Toda resposta tem 2-3 palavras com `**`
- [ ] Tom da Tata preservado (testar lendo em voz alta)
- [ ] Sem bordão de outro guru
- [ ] Sem palavra institucional
- [ ] Distribuição: ~5 carro + ~5 escritório
- [ ] Variedade: dica prática + mindset + história + contraintuitivo + controverso
- [ ] Sexy Canvas: 6+ gatilhos diferentes nos 10
- [ ] Cada Q&A funciona STANDALONE (sem precisar contexto da aula)
