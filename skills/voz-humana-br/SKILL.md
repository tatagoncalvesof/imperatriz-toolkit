---
name: voz-humana-br
description: Transforma qualquer texto escrito por IA em texto que soa como pessoa real escrevendo em português brasileiro. Remove travessão, jargão corporativo, paralelismo negativo, gerúndio na cauda, nominalização, hedging, sicofancia e todos os tiques que delatam ChatGPT/Claude. Mantém intenção e voz do autor original. Aplica régua quantitativa (desvio padrão de tamanho de frase, distribuição por faixa), 12 aberturas alternativas de parágrafo, dialeto Tata/mentorada, ajuste por canal (WhatsApp, Stories, e-mail, página de vendas, post). Usa quando o usuário pedir pra humanizar texto, tirar cara de IA, deixar mais natural, soar como gente, escrever como humano, remover jargão, deixar com voz da Tata, adaptar pra WhatsApp/Stories. Gatilhos: humaniza, humanize, humanizar, tira cara de IA, deixa natural, escreve como humano, sem jargao, sem travessao, voz da Tata, parece chatGPT, parece IA, deslop, descomplica esse texto, reescreve pra parecer gente.
allowed-tools: Bash, Read, Write, Edit, Grep, Glob
---

# Voz Humana BR

Skill que transforma texto de IA em texto que soa como pessoa escrevendo em português brasileiro. Stripa todos os tiques de ChatGPT/Claude, mantém o significado intacto, respeita a voz do autor original.

Não é tradução. Não é resumo. Não é reescrita criativa. É reengenharia cirúrgica que troca palavra por palavra, quebra estrutura por estrutura, valida por régua quantitativa.

## Filosofia central

1. **Cada palavra tem que pagar o aluguel.** Se a frase funciona sem a palavra, a palavra é desnecessária. Corta.
2. **Significado é sagrado, voz é sagrada.** Toda ideia do original sobrevive. Se o autor tinha opinião, humor, raiva, hesitação, ironia, isso fica. A skill tira a camada de máquina, não a pessoa por baixo.
3. **Concreto vence genérico.** Número, nome, data, lugar específico. "Uma cliente em Curitiba pagou R$ 3.200" vence "muitos clientes investem em tráfego pago".
4. **Anglo-saxão vence latino.** "Usar" vence "utilizar". "Mostrar" vence "demonstrar". "Pra" vence "a fim de".
5. **Variação rítmica não é opcional.** Frase curta. Frase longa que respira. Corte. O desvio padrão do tamanho das frases tem que passar de 6 palavras.
6. **Quebra de regra calculada delata humano.** Começar frase com "E" ou "Mas". Fragmento sem verbo. Vírgula onde gramático puxaria orelha. Uma quebra deliberada por página assina humano.
7. **A voz do canal manda.** WhatsApp não é página de vendas. Stories não é e-mail. Cada canal tem régua própria.

## Quando usar

- Usuário cola texto e pede pra humanizar, tirar cara de IA, deixar natural
- Texto saiu de ChatGPT/Claude/Gemini e precisa virar pessoal
- Copy de venda, e-mail, post, legenda, página, artigo, qualquer prosa
- Mentorada da Tata gerou conteúdo com IA e precisa adaptar pra voz dela
- Texto pra publicar em canal específico (WhatsApp, Stories, e-mail, página)

## Quando NÃO usar

- Texto já é humano e natural (passa pelos detectores). Roda só pra confirmar.
- Ficção criativa, poesia, letra de música (regras estilísticas próprias)
- Documento técnico/jurídico que exige formalidade (avisar usuário antes)
- Usuário quer manter o estilo de IA por algum motivo

## Workflow

```
[1] Receber texto + contexto
       ↓
[2] Perguntar canal e tom (se não óbvio)
       ↓
[3] Rodar detectar_ia_ptbr.py → relatório JSON
       ↓
[4] Ler relatório + os 5 arquivos reference/
       ↓
[5] Reescrever em passada única, atacando cada flag
       ↓
[6] Subagente cego lê e aponta tiques que sobreviveram
       ↓
[7] Corrigir só o que o subagente marcou
       ↓
[8] Rodar validar_humanizado.py → score 0-100
       ↓
[9] Se passou: rodar comparar_textos.py → diff antes/depois
       ↓
[10] Entregar: texto humanizado + score + 5 mudanças mais importantes
```

## Passos de execução

### Passo 1 — Receber texto e contexto

Pede o texto. Se o usuário não disse, pergunta:

- **Canal**: WhatsApp, Stories, post de feed, legenda, e-mail, página de vendas, artigo, outro?
- **Tom**: amiga falando com amiga, especialista falando com aluno, vendedor falando com lead frio, autoridade falando com pares?
- **Voz de quem**: voz da Tata, voz da própria mentorada, voz neutra-natural?

Se o usuário não souber responder, assume defaults:
- Canal: post de feed
- Tom: especialista falando com aluno
- Voz: natural brasileira, sem ser específica

### Passo 2 — Salvar input pra processamento

```bash
cat > /tmp/voz_input.txt << 'INPUTEOF'
[texto do usuário aqui]
INPUTEOF
```

### Passo 3 — Detectar padrões de IA

```bash
python3 ~/.claude/skills/voz-humana-br/scripts/detectar_ia_ptbr.py /tmp/voz_input.txt --formato json > /tmp/voz_relatorio.json
```

Lê o JSON e nota:

- `densidade_ia` (0-100): grau de contaminação. Acima de 40 já é sinal forte.
- `palavras_flagadas`: cada palavra vermelha/amarela com posição
- `frases_flagadas`: aberturas vazias, fechamentos vazios, hedging, sicofancia, hype
- `padroes_estruturais`: paralelismo negativo, regra de três, gerúndio na cauda, faixas falsas, correlativos
- `ritmo`: desvio padrão do tamanho das frases, distribuição por faixa, parágrafos uniformes
- `pontuacao`: quantidade de travessão, dois-pontos, negrito, emoji
- `tom`: nominalização, voz passiva, hedging

### Passo 4 — Ler os reference

Antes de reescrever, lê (na ordem):

1. `reference/palavras-proibidas-ptbr.md` — dicionário completo PT-BR de palavras vermelhas/amarelas com alternativas humanas
2. `reference/frases-proibidas-ptbr.md` — aberturas, fechamentos, hedging, hype, sicofancia, conversacional fake, atribuição vaga
3. `reference/padroes-estruturais-ptbr.md` — paralelismo negativo, regra de três, gerúndio na cauda, faixas falsas, correlativos, gangorra do hedge, ritmo uniforme, ciclagem de sinônimos
4. `reference/principios-reescrita-ptbr.md` — régua quantitativa, 12 aberturas alternativas, padrão 1-1-3, anglo-saxão vs latino, de-nominalização, voz ativa, transições naturais
5. `reference/dialeto-tata.md` — voz da Tata, vocabulário específico, frases assinatura (usar só se contexto pedir voz da Tata)
6. `reference/regua-por-canal.md` — limites e ajustes por WhatsApp/Stories/feed/e-mail/página/artigo

### Passo 5 — Reescrever

**Regras inegociáveis na reescrita:**

**Palavras:**
- Substitui TODA palavra vermelha. Tolerância zero. Usa a alternativa do dicionário PT-BR.
- Palavra amarela: máximo 1 por documento. Se aparecer mais, mantém só onde for mais precisa.
- Mata cópula camuflada: "serve como" → "é"; "apresenta" (no sentido de ter) → "tem"; "constitui" → "é".
- De-nominaliza: substantivos terminados em -ção, -mento, -ância, -ência + verbo "ser/estar/haver". Liberta o verbo, nomeia quem fez.
- Prefere anglo-saxão: "usar" não "utilizar"; "fazer" não "realizar"; "mostrar" não "demonstrar"; "começar" não "iniciar"; "pra" não "a fim de".

**Frases:**
- Apaga toda abertura vazia ("No mundo atual", "Nos dias de hoje", "Vamos mergulhar", "Vamos lá"). Começa direto.
- Apaga todo fechamento vazio ("Em conclusão", "Em resumo", "O futuro é promissor"). Termina seco ou com ponto novo.
- Apaga todo hedging ("É importante notar que", "Vale ressaltar que"). Fala a coisa.
- Apaga editorialização ("Não daria pra falar de X sem mencionar Y").
- Apaga sicofancia ("Ótima pergunta", "Espero que isso ajude").
- Substitui inflação de significância: "se apresenta como prova de" → "prova" ou "mostra".

**Estrutura:**
- Quebra paralelismo negativo. "Não é só X, é Y" vira "É Y" e ponto. Estado positivo direto.
- Quebra regra de três. Não toda lista precisa ter três itens. Usa dois. Quatro. Um.
- Tira gerúndio na cauda. "Lançou o produto, gerando empregos" vira "Lançou o produto. Gerou 200 empregos." Ou rearranja.
- Substitui travessão (—) por vírgula, parênteses ou ponto. Mantém no máximo 1 a cada 500 palavras, e só se for spontaneidade real.
- Quebra estrutura uniforme de parágrafo. Varia. Parágrafo de uma frase é ok. Parágrafo de dez frases é ok. Conteúdo dita tamanho.
- Varia abertura de parágrafo. Nunca mais de 2 em 5 parágrafos consecutivos começando com "O/A/Esse/Essa/Isso".
- Para de ciclar sinônimo. Escolhe uma palavra pra cada conceito e repete.

**Ritmo:**
- Mira desvio padrão de tamanho de frase maior que 6 palavras.
- Mistura fragmento (2-5 palavras) com frase complexa (25-35 palavras).
- Padrão 1-1-3 frouxo: duas curtas, uma longa. Depois quebra o padrão.
- Lê em voz alta mentalmente. Se toda frase pega a mesma respiração, reescreve.

**Transições:**
- Apaga "Ademais", "Outrossim", "Além disso" (no início), "Notadamente", "Por conseguinte", "Em síntese".
- Usa "Mas", "E", "Então", "Aí", "Daí", "Só que", "Acontece que" — ou nenhuma transição. A quebra de parágrafo já é a transição.

**Tom e voz:**
- Detecta o registro do input e mantém. Casual fica casual. Formal fica formal.
- Casual: contração ("pra", "tá", "tô", "dá pra"), frase curta, endereçamento direto.
- Formal: mantém formalidade mas tira o inchaço. Formal não significa inflado.
- Se o original tem opinião, mantém. "Isso não funciona" é humano. "Há aspectos a considerar" é IA.
- Se tem humor, tangente, comentário lateral, mantém. É exatamente isso que separa humano de máquina.
- Sentimento misto é humano. "Gostei da interface mas o onboarding me confundiu" vence "O produto tem pontos fortes e oportunidades de melhoria".

### Passo 6 — Subagente cego

Depois de reescrever, dispara um subagente Opus que recebe SÓ o texto reescrito. Não vê o original. Não vê o relatório. A única missão dele é apontar tiques que sobreviveram.

**Prompt do subagente (literal):**

```
Lê o texto abaixo. Ele soa como pessoa escrevendo ou ainda parece IA?

Aponta SÓ as frases ou trechos específicos que ainda parecem máquina. Pra cada um, fala o que delata e sugere alternativa mais enxuta.

Regras:
- NÃO reorganiza, reestrutura, nem muda significado.
- NÃO adiciona conteúdo, expande ideia, muda o argumento.
- NÃO mexe em frase que já soa humana. Deixa em paz.
- Foco estreito: ritmo robótico, vocabulário inflado, transição formulaica, tom achatado, paralelismo negativo, gerúndio na cauda, hedging.
- Se o texto já lê como humano, fala isso e para.

Texto:
[TEXTO REESCRITO AQUI]
```

Lê a resposta. Corrige só o que o subagente apontou. Se ele falar que tá bom, pula pro Passo 7.

### Passo 7 — Validar

```bash
python3 ~/.claude/skills/voz-humana-br/scripts/validar_humanizado.py /tmp/voz_input.txt /tmp/voz_output.txt
```

Critérios de aprovação (todos têm que passar):

- Densidade IA caiu pra menos de 15
- Zero palavras vermelhas
- Máximo 1 palavra amarela
- Desvio padrão de tamanho de frase maior que 5
- Travessão menor que 1 por 500 palavras
- Pelo menos 1 frase com menos de 8 palavras a cada parágrafo de 5+ frases
- Variação de abertura de parágrafo: nenhuma palavra inicial repete em 3 parágrafos seguidos

Se falhou: lê o relatório, corrige falha por falha, revalida. Máximo 3 iterações.

### Passo 8 — Comparar e entregar

```bash
python3 ~/.claude/skills/voz-humana-br/scripts/comparar_textos.py /tmp/voz_input.txt /tmp/voz_output.txt
```

Apresenta pro usuário:

1. **Texto humanizado** (em bloco, pronto pra copiar)
2. **Score**: densidade IA antes → depois (ex: 78 → 9)
3. **5 mudanças mais importantes** que você fez (em bullet curto)
4. **Diff de palavras**: quantas trocadas, padrões removidos
5. **Aviso**: se algum trecho ficou ambíguo ou se o significado pode ter mudado, marca

## Variantes (modos de uso)

A skill aceita modificadores no pedido. Detecta pela frase do usuário e ajusta:

### Modo `--canal=whatsapp`
Frases mais curtas (média 8-12 palavras), uso intenso de "pra/tá/né", emoji raro, quebra de linha frequente, sem formatação de mercado.

### Modo `--canal=stories`
Texto curtíssimo (máximo 50 palavras por slide), uma ideia por frase, gancho na primeira linha, CTA implícita ou explícita no final.

### Modo `--canal=feed`
Hook poderoso na primeira linha, parágrafos curtos (2-3 frases), espaçamento visual, CTA no final, hashtag opcional separada.

### Modo `--canal=email`
Assunto separado, abertura direta sem "espero que esteja bem", uma ideia por parágrafo, CTA único e claro.

### Modo `--canal=pagina-vendas`
Pode usar mais retórica de copy (sem cair em hype IA), depoimentos vão em primeira pessoa do cliente, sem palavras de inflação ("transformador", "revolucionário").

### Modo `--canal=artigo`
Tolera frases mais longas, parágrafos maiores, transições mais elaboradas (mas ainda banidas as IA).

### Modo `--voz=tata`
Aplica `reference/dialeto-tata.md`. Vocabulário, frases assinatura, jeito de cortar, opiniões fortes da Tata.

### Modo `--voz=mentorada`
Pede ao usuário 1 parágrafo escrito por ela mesma como exemplo de voz. Imita esse padrão.

### Modo `--so-detecta`
Não reescreve. Roda só o detector e devolve o relatório. Útil pra mentorada saber onde tá errando.

## Para textos longos (mais de 2000 palavras)

Divide em seções lógicas. Despacha agentes paralelos (Opus) com:
- Sua seção de texto
- O relatório de detecção dessa seção
- Os arquivos reference
- O parágrafo anterior (pra continuidade) e o próximo (pra transição)

Um agente coordenador costura, checa consistência de costura, roda validação final.

## Integração com ecossistema Tata

Esta skill conversa com outras do arsenal:

- **`/copy-editing`**: chama esta skill ANTES de revisar copy. Texto de IA mascara erros de copy. Humaniza primeiro, edita depois.
- **`/headline-imperatriz`**: gera headlines. Esta skill humaniza o resultado se necessário.
- **`/mecanismo-unico`**: gera nome de mecanismo. Esta skill checa se a explicação do mecanismo não tá inflada.
- **`/texto-em-visual`**: pega copy humanizado pra transformar em visual.
- **`/briefing-copy-360`**: faz briefing antes da escrita. Esta skill é PASSO PÓS-ESCRITA.
- **`/skill-copy-ads-ptbr`**: gera copy de ads. Esta skill humaniza o output se passar do detector.
- **`/analise-anuncio-1000`**: analisa anúncios. Esta skill ajuda a entender por que copy de IA não converte.
- **`/skill-pagina-vendas`**: gera página de vendas. Esta skill humaniza o output em modo `--canal=pagina-vendas`.

## Reference

- `reference/palavras-proibidas-ptbr.md` — Dicionário completo PT-BR de palavras vermelhas/amarelas
- `reference/frases-proibidas-ptbr.md` — Aberturas, fechamentos, hedging, hype, sicofancia
- `reference/padroes-estruturais-ptbr.md` — Padrões de estrutura que delatam IA em PT-BR
- `reference/principios-reescrita-ptbr.md` — Régua quantitativa e técnicas positivas
- `reference/dialeto-tata.md` — Voz da Tata pra modo `--voz=tata`
- `reference/regua-por-canal.md` — Ajustes por canal de publicação

## Scripts

- `scripts/detectar_ia_ptbr.py` — Detector de padrões IA em PT-BR, devolve JSON com score
- `scripts/validar_humanizado.py` — Verifica se output passa nos critérios
- `scripts/comparar_textos.py` — Diff antes/depois com métricas

## Examples

- `examples/copy-vendas-antes-depois.md` — Página de vendas reescrita
- `examples/email-antes-depois.md` — E-mail de venda reescrito
- `examples/post-instagram-antes-depois.md` — Legenda de post reescrita
- `examples/whatsapp-antes-depois.md` — Mensagem de WhatsApp reescrita
