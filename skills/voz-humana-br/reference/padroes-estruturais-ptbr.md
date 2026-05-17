# Padrões Estruturais PT-BR que Delatam IA

Vocabulário já tá no `palavras-proibidas-ptbr.md`. Este arquivo cobre o que vai além da palavra: estrutura de frase, ritmo, parágrafo, documento. São os tiques que sobrevivem mesmo depois de trocar as palavras.

Cada padrão traz heurística de detecção com limiar quantitativo.

---

## 1. Padrões de Frase

### 1A. Paralelismo Negativo ("Não é X, é Y")

O tique mais distintivo de IA em qualquer idioma. Humano estado positivo. IA setup de negação antes de afirmar.

**Padrões em PT-BR pra detectar:**
- "Não é só X. É Y."
- "Não é apenas X. É Y."
- "Não se trata apenas de X, mas de Y."
- "Não é sobre X. É sobre Y."
- "Isso não é X. É Y."
- "A gente não vende X. A gente entrega Y."
- "IA não substitui emprego. IA redistribui emprego."
- "Não é recuo. É evolução."
- "Não é promessa. É resultado."
- "Não é mais um curso. É um método."

**Heurística:** busca "não é só", "não é apenas", "não se trata apenas", "não é sobre", "isso não é", "não é [palavra]. é [palavra]". Se 3+ no texto, IA quase certa.

**Fix:** estado positivo direto. "É Y" vence "Não é X, é Y". Corta o setup.

### 1B. Regra de Três Ascendente (Tricolon)

IA força ideia em trio com crescendo. Humano usa tricolon raramente. IA usa todo parágrafo.

**Exemplos banidos:**
- "rápido, fácil e eficiente"
- "claro, direto e prático"
- "estratégico, escalável e impactante"
- "autenticidade, confiança e verdade"
- "aprendi a persistir, a abraçar desafios e a liderar com empatia"
- "da teoria à prática, do simples ao sofisticado, do pequeno ao grande"

**Heurística:** 4+ tricolons no mesmo texto = IA certa. Conta grupos de três separados por vírgula, principalmente com ascendência de tamanho.

**Fix:** quebra o trio. Usa dois. Ou quatro. Ou um item expandido. Qualquer coisa menos o três rítmico crescente.

### 1C. Gerúndio na Cauda ("X, gerando Y")

IA pendura oração com gerúndio no fim da frase 2 a 5 vezes mais que humano. Em PT-BR é mais delator ainda, porque o gerúndio na cauda soa literalmente traduzido do inglês.

**Exemplos:**
- "A empresa lançou o produto, **gerando** milhares de empregos."
- "O estudo analisou os dados, **revelando** descobertas-chave."
- "A reforma passou em 2019, **marcando** uma mudança importante."
- "Ela abriu o negócio, **transformando** a economia local."
- "Ele publicou o paper, **destacando** a necessidade de mais pesquisa."

**Gerúndios delatadores (quase exclusivos de IA na cauda):**
gerando, criando, causando, provocando, destacando, enfatizando, sublinhando, mostrando, demonstrando, evidenciando, refletindo, simbolizando, representando, preparando (o terreno pra), pavimentando (o caminho pra), garantindo, assegurando, fomentando, incentivando, permitindo, possibilitando, impulsionando, fortalecendo.

**Heurística:** 5+ gerúndios na cauda de frase no mesmo texto = IA certa.

**Fix:** quebra em duas frases. Ou inverte. Ou reescreve.

Antes: "Lançou o produto, gerando 200 empregos."
Depois: "Lançou o produto. Criou 200 empregos."
Ou: "O lançamento do produto criou 200 empregos."

### 1D. Faixas Falsas "De X a Y"

IA cria espectro artificial que soa rico mas não entrega informação.

**Exemplos:**
- "De iniciantes a especialistas..."
- "De pequenos negócios a grandes corporações..."
- "Do simples ao sofisticado..."
- "De tradições antigas a inovações modernas..."
- "Do básico ao avançado..."
- "Do planejamento à execução..."

**Heurística:** 2+ "de X a Y" no mesmo texto, especialmente com adjetivos contrastantes (antigo/moderno, pequeno/grande, simples/complexo).

**Fix:** nomeia itens reais. "De iniciantes a especialistas usaram" vira "Beto que nunca programou usou. E a Carla, dev sênior de 10 anos, também."

### 1E. Correlativos Sobrecarregados

Humano usa correlativo de vez em quando. IA sistemático.

**Padrões:**
- "Não só X, mas também Y..."
- "Seja X, seja Y..."
- "Tanto X quanto Y..."
- "Ou X ou Y..."
- "Nem X nem Y..."

**Heurística:** 3+ correlativos num texto = sinal forte. "Não só, mas também" aparecendo mais de 1 vez já é sinal.

**Fix:** coordenação simples. "Não só redesenharam a UI, mas também melhoraram a performance" vira "Redesenharam a UI e melhoraram a performance."

### 1F. Gangorra do Hedge

Balanceamento covarde que não compromete com nada. Autor em cima do muro.

**Exemplos:**
- "Embora X tenha benefícios, é importante notar que Y..."
- "Se por um lado X, por outro lado Y..."
- "Apesar de X, também existe Y..."
- "Ainda que X apresente desafios, também oferece oportunidades..."
- "X tem pontos fortes e áreas de melhoria..."

**Heurística:** procura par concessão-e-contra em todo parágrafo. Se toda seção tem "embora/apesar [positivo], [negativo]" ou vice-versa, é IA sentada no muro.

**Fix:** compromete com posição. "A interface melhorou. O onboarding ainda confunde." Não "Embora a interface tenha melhorado, desafios permanecem no onboarding."

### 1G. Tamanho Uniforme de Frase

IA média 15 a 25 palavras por frase com variância muito baixa (SD 2 a 3). Humano tem "explosão": fragmento curto ao lado de frase complexa longa.

**Heurística:**
- Calcula desvio padrão do tamanho das frases no parágrafo
- IA: SD menor que 4 (ritmo metrônomo)
- Humano: SD maior que 6 (ritmo variado)
- Se toda frase no parágrafo tem entre 14 e 22 palavras, parece IA

**Fix:** ver `principios-reescrita-ptbr.md` (padrão 1-1-3 e distribuição alvo).

### 1H. Ciclagem de Sinônimos (Variação Elegante)

A penalidade de repetição da IA faz ela ciclar sinônimo que ninguém usaria.

**Padrão exemplo:**
- 1ª menção: "o protagonista"
- 2ª menção: "o personagem principal"
- 3ª menção: "a figura central"
- 4ª menção: "o herói"
- 5ª menção: "o epônimo da obra"
- 6ª menção: "o ator-chave da narrativa"

Exemplo em contexto de mentoria:
- 1ª menção: "a cliente"
- 2ª menção: "a mentorada"
- 3ª menção: "a aluna"
- 4ª menção: "a empreendedora"
- 5ª menção: "a profissional"

**Heurística:** se o texto usa 4+ termos diferentes pra mesma entidade num trecho, e nenhum adiciona informação, é IA.

**Fix:** humano escolhe um ou dois e repete. Repetição é natural. Variação forçada não é.

---

## 2. Padrões de Parágrafo

### 2A. Estrutura Formulaica

Todo parágrafo de IA segue o mesmo template:
1. Frase-tópico (declara o ponto)
2. Evidência ou elaboração (1 a 3 frases)
3. Frase-síntese (repete o ponto e liga pro próximo parágrafo)

**Heurística:** lê a primeira e a última frase de cada parágrafo. Se a última é restatement da primeira, template IA. Se 3+ parágrafos seguidos repetem esse padrão, sinal forte.

**Fix:** humano varia. Parágrafo de uma frase. Parágrafo de dez. Alguns começam pela evidência e param seco. Outros vão direto pra conclusão. Nenhum tem a mesma arquitetura interna.

### 2B. Tamanho Uniforme

IA gera parágrafo com tamanho parecido (3 a 5 frases cada). Ritmo visual da página é simétrico.

**Heurística:** conta frases por parágrafo no doc todo. Se a faixa é estreita (todos entre 3 e 5 frases), é IA. Humano tem parágrafo de uma frase misturado com parágrafo denso de oito.

**Fix:** varia de propósito. Conteúdo dita tamanho. Ponto afiado merece uma frase sozinha. Argumento complexo precisa de oito.

### 2C. Lista Pra Tudo

IA default:
- Bullet point pra tudo
- Lista numerada pra sequência
- **Negrito-label:** descrição, padrão pra categoria
- Inline-header ("**Nome da categoria:** texto da descrição")

**Heurística:** o formato "**Termo em negrito:** Explicação" em texto corrido (não em doc de referência) é quase 100% IA. Conta bullets: se texto em prosa tem mais de 2 listas, provavelmente saiu de IA.

**Fix:** converte lista em parágrafo fluido. Enumeração embutida na frase: "Três coisas importaram: o custo, o tempo e a reação do público."

### 2D. Subtítulo em Excesso

IA aplica subtítulo formulaico:
- "Entendendo [X]"
- "A importância de [Y]"
- "Principais benefícios de [Z]"
- "Desafios e perspectivas futuras"
- "Conclusão"

**Heurística:** se subtítulos seguem padrão previsível (Entendendo/Importância/Benefícios/Desafios/Conclusão), é IA. Se todo bloco de 2 a 3 parágrafos tem subtítulo, é IA. Humano usa subtítulo com moderação.

**Fix:** corta metade dos subtítulos. Renomeia os restantes pra serem específicos. "Entendendo machine learning" vira "Como o modelo classifica tumor." Subtítulo tem que trabalhar.

### 2E. Meta-comentário

IA narra a própria estrutura, falando pro leitor o que vai acontecer.

**Exemplos:**
- "Nesta seção vamos falar sobre..."
- "Como mencionado anteriormente..."
- "Agora que exploramos X, vamos para Y..."
- "Mais adiante, veremos..."
- "Antes de prosseguir..."

**Heurística:** 3+ meta-comentários no texto = sinal de IA. Qualquer frase que descreve a estrutura do doc em vez de avançar o conteúdo é meta-comentário.

**Fix:** apaga tudo. Vai pro próximo ponto direto. Leitor não precisa de índice a cada parágrafo.

### 2F. Efeito Esteira

Texto passa por cima das mesmas ideias sem avançar. Leitor sente movimento mas não progride. IA autoregressiva sabe a próxima palavra, não sabe o destino.

**Heurística:** lê 3 parágrafos seguidos. Se dá pra resumir os três numa frase só, tá na esteira. Cada parágrafo tem que ter pelo menos uma ideia que os outros não têm.

**Fix:** depois de escrever, escreve resumo de uma linha por parágrafo. Se dois resumos são iguais, funde ou corta um.

### 2G. Tamanho em vez de Substância

IA enche com restatement e contexto desnecessário. 2.500 palavras pra dizer o que cabe em 500. Ela otimiza "completude" em vez de comunicação.

**Heurística:** pergunta "o que leitor aprende aqui que ele não pegaria no primeiro resultado do Google?". Se nada, o texto precisa de ângulo específico, dado concreto, experiência vivida. Conta também: quantas vezes o ponto principal é repetido?

**Fix:** corta 30 a 50% na revisão. Cada frase tem que pagar o aluguel.

---

## 3. Pontuação e Formatação

### 3A. Travessão em Excesso

IA usa travessão longo (—) onde humano em português usa vírgula, parênteses ou dois-pontos.

**Padrões de travessão IA:**
- Revelação dramática: "A resposta — surpreendentemente — foi não."
- Aposição (onde humano usa parênteses)
- Introdução de lista (onde humano usa dois-pontos)
- Ênfase (onde humano usa vírgula)

**Heurística:** 3+ travessões por parágrafo = sinal forte. Mais de 1 travessão a cada 100 palavras é elevado.

**Fix:** substitui maioria por vírgula, parênteses ou ponto. Mantém no máximo 1 a cada 500 palavras pra efeito dramático real.

### 3B. Negrito em Excesso

IA aplica negrito mecanicamente em "termos-chave", produtos, marcadores de seção ao longo da prosa.

**Heurística:** negrito no meio de parágrafo pra destacar "conceito-chave" (não título, não label de UI) é padrão IA. Mais de 3 frases em negrito por página de prosa é sinal.

**Fix:** tira todo negrito de prosa corrente. Negrito é pra título e elemento de UI, não pra ênfase em parágrafo. Usa estrutura da frase pra dar ênfase.

### 3C. Dois-pontos em Excesso

IA começa parágrafo com declaração seguida de dois-pontos e salta pra lista ou explicação.

**Heurística:** 10+ dois-pontos em texto em prosa (sem contar título) é sinal forte.

**Fix:** substitui maioria por ponto ou vírgula. Usa dois-pontos pra introdução de lista real ou punchline: "O resultado foi claro: falha."

### 3D. Título em Caixa Alta em Todas as Palavras

IA capitaliza "Todas As Palavras Principais Do Título" (Title Case). Em português, a norma é só primeira palavra e nomes próprios ("Todas as palavras principais do título").

**Heurística:** se todo título usa Title Case, checa outros sinais. Title Case sozinho não é conclusivo, mas correlaciona.

**Fix:** usa só primeira palavra maiúscula pra título, a não ser que o estilo da publicação peça outra coisa.

### 3E. Aspas Curvas (" ")

IA usa aspas curvas/smart. Humano em plain text e mobile digita aspa reta ("). Sinal menor mas correlaciona.

### 3F. Gramática Perfeita (Paradoxalmente Delata)

IA evita fragmento, frase longa sem pontuação certa, começar com "E" ou "Mas", toda forma de quebra de regra proposital. Frase sempre gramaticalmente completa.

**Heurística:** zero fragmentos, zero frase iniciada por "E" ou "Mas", zero pensamento interrompido num texto longo = sinal de IA. Texto humano profissional tem fragmento proposital, pensamento cortado, conjunção no início.

**Fix:** quebra regra de propósito. Um fragmento a cada página. Começa alguma frase com "E" ou "Mas". Escrita humana é imperfeita de propósito.

### 3G. Padrão de Emoji

IA adiciona emoji decorativo em contexto profissional onde humano não usaria. Emoji simétrico (um por bullet, enquadrando título) é IA.

**Heurística:** emoji no início de cada bullet ou em cima e em baixo de título = IA. Um emoji por seção, perfeitamente posicionado, é IA. Humano usa emoji irregular ou nenhum.

**Fix:** tira todo emoji de texto profissional. Se emoji é apropriado (contexto casual), usa de forma irregular e com moderação.

### 3H. Inglês Americano Consistente em Texto em PT

IA ocasionalmente solta anglicismo ou ortografia americana em texto em português. "Optimize", "analyze", "technology-driven", "startup-like". Mais delator em texto formal.

**Fix:** traduz ou remove. Manter "startup" se for o termo de mercado. Traduzir "leveraging" pra "aproveitando" ou melhor "usando".

---

## 4. Padrões de Documento

### 4A. Ensaio de Cinco Parágrafos

IA default: Introdução, Corpo 1, Corpo 2, Corpo 3, Conclusão. Cada seção com tamanho parecido.

**Heurística:** conta seções. Se tem exatamente 5 seções com word count parecido, é template IA. Humano tem seção com tamanho desigual, porque certos tópicos precisam de mais espaço.

**Fix:** conteúdo dita estrutura. Tópico pode precisar de um parágrafo. Outro pode precisar de quinze. Cinco-parágrafos é formato de redação de escola, não escrita profissional.

### 4B. Template Introdução-Lista-Conclusão

Parágrafo de contexto, lista com bullets, parágrafo de fechamento. Repete no doc inteiro.

**Heurística:** se 3+ seções seguem esse padrão, é estrutura IA.

**Fix:** integra conteúdo da lista em parágrafo fluido. Varia estrutura por seção. Algumas são só prosa. Outras são um exemplo único estendido.

### 4C. Conclusão que Repete Tudo

Conclusão IA repete o que foi dito, em vez de avançar o argumento. Último parágrafo adiciona zero informação nova.

**Heurística:** compara conclusão com introdução. Se 60%+ das ideias da conclusão já tão na introdução, é resumo IA.

**Fix:** última parte pode avançar o argumento pro final (algo novo), terminar com pergunta provocativa, apontar o que vem depois, ou simplesmente parar. Nunca repete a introdução.

### 4D. Seções Simétricas

Toda seção com o mesmo número de parágrafos, mesma estrutura, mesmo tamanho aproximado. Nenhuma seção notavelmente maior ou menor.

**Heurística:** calcula word count por seção. Se o coeficiente de variação é menor que 0,15 (todas dentro de 15% uma da outra), simetria é IA.

**Fix:** deixa tópico importante maior. Tópico menor, menor. Assimetria é natural.

### 4E. Nomes Genéricos em Exemplos

IA usa "Maria", "João", "Ana", "Pedro" em 60-70% dos exemplos gerados em português. Em inglês é "Emily" e "Sarah".

**Heurística:** checa nomes de exemplo. Se todos são nomes comuns brasileiros genéricos (Maria, Ana, João, Pedro, Carla, Roberto), flagga como potencial IA.

**Fix:** usa nome específico, incomum, ou real do seu domínio. "Cristiane da agência de Londrina" vence "Maria da agência". Melhor ainda: cliente real com permissão.

### 4F. Falta de Nome Próprio Específico

IA gera referência vaga em vez de nome, data, lugar, figura específica.

**Heurística:** procura "um estudo importante" em vez de citar o estudo. "Especialistas dizem" em vez de citar. "Uma empresa de destaque" em vez de nomear. Atribuição vaga onde específico seria fácil = IA.

**Fix:** nomeia o estudo, o especialista, a empresa, a cidade, a data. Específico é humano.

### 4G. Ausência de Reflexão Metacognitiva

IA nunca fala "mudei de ideia sobre isso", "eu achava que X mas agora penso Y", "não tenho certeza sobre isso mas".

**Heurística:** se o texto toma posição firme sem nenhuma autocorreção, incerteza ou jornada intelectual, pode ser IA. Especialista humano rotineiramente nota onde mudou a visão ou onde permanece incerto.

**Fix:** inclui momento de incerteza real, posição mudada, honestidade intelectual sobre o que não sabe.

---

*Este arquivo cobre padrão estrutural, formatação e documento. Use as heurísticas pra varrer texto sistematicamente. O detector automatiza a maioria.*
