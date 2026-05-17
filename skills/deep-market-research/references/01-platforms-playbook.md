# Playbook por Plataforma — Como Pesquisar de Verdade

Cada plataforma tem **lógica própria** de onde mora a voz do comprador. Pesquisar igual nas 5 é o erro nº1 de quem faz VOC superficial. Este playbook entrega queries literais e onde clicar/raspar pra cada uma.

---

## 1. Google — Reino do Intent Racional

**O que você captura aqui:** intenção declarada, dúvida explícita, comparação fria, decisão de compra avançada.

**Onde mora o ouro:**
- Caixa de busca (autocomplete) — termos que outras pessoas já digitaram
- "Pesquisas relacionadas" (rodapé) — semântica adjacente
- "Outras pessoas perguntam" — objeções implícitas em forma de pergunta
- Sugestões "About [termo]" no painel à direita — termos técnicos do nicho

### Queries-base que SEMPRE rodam

Substitua `[X]` pelo termo-raiz do nicho. Rode TODAS:

```
[X]
[X] como
[X] como fazer
[X] quanto custa
[X] vale a pena
[X] funciona
[X] não funciona
[X] tutorial
[X] passo a passo
[X] iniciante
[X] avançado
[X] erros
[X] melhor
[X] pior
[X] vs
[X] alternativa
[X] grátis
[X] pago
[X] mensal
[X] anual
[X] sem [Y comum no nicho]
[X] depois dos [idade]
[X] em [cidade ou estado se geo importa]
melhor [X]
como começar com [X]
por que [X] não funciona
como saber se [X] vale a pena
quanto tempo demora pra [resultado X]
```

### Modificadores específicos por intent

**Dor:**
- `[X] não consigo`, `[X] está difícil`, `[X] me cansei`
- `por que eu não consigo [X]`, `[X] depois de tentar tudo`

**Comparação:**
- `[A] ou [B]`, `[A] vs [B]`, `[A] melhor que [B]`
- `diferença entre [A] e [B]`

**Síndrome do impostor:**
- `tenho perfil pra [X]`, `[X] é pra mim`, `[X] depois de [idade]`
- `[X] sem experiência`, `[X] iniciante absoluto`

**Desistência:**
- `desistir de [X]`, `parar de tentar [X]`, `[X] não é pra todo mundo`

### Como capturar (passo a passo no Claude Code)

```
1. Usar WebSearch com query exata
2. Pegar top 10 títulos + meta description
3. Anotar os 5-8 termos do autocomplete (digitar query + espaço)
4. Capturar "People also ask" (4 a 8 perguntas literais)
5. Pegar "Related searches" do rodapé
6. Pra termos top, fazer segunda busca em "[termo] site:reddit.com" e "[termo] site:reclameaqui.com.br" pra achar voz literal
```

### Pegadinhas Google
- Personalização de resultado distorce — use WebSearch genérico
- Mobile autocomplete difere de desktop
- "People also ask" expande dinamicamente — clique 3 vezes pra ver as 8-12 reais
- Resultado de YouTube/TikTok no Google ≠ resultado nativo (capturar nativo na fase 2)

---

## 2. YouTube — Reino do "Como Fazer" + Comentários como Ouro

**O que você captura aqui:** dor explícita nos comentários, tutoriais que o público realmente clica, objeções pós-consumo.

**Onde mora o ouro:**
- Títulos top do nicho (linguagem que vende clique)
- **Comentários** — onde a objeção REAL aparece ("tentei isso e não funcionou porque...")
- Sugestões de autocomplete específicas do YouTube
- Vídeos sugeridos lateralmente (semântica de consumo)

### Queries-base

Mesmas do Google, mais:
```
como [X] passo a passo
[X] funciona mesmo?
testei [X] por 30 dias
revisão [X]
[X] tutorial 2025
[X] o que ninguém te conta
[X] verdade sobre
storytime [X]
[X] antes e depois
[X] erro comum
```

### Como minerar comentários

Pra cada um dos 3 vídeos mais vistos do termo-raiz:
1. Pegue os **30 comentários top** (mais curtidos)
2. Categorize cada comentário em:
   - 🔥 **Dor explícita** ("eu também sinto X")
   - 🚫 **Objeção** ("já tentei e não funcionou")
   - ❓ **Pergunta** (dúvida pós-vídeo)
   - 🎯 **Celebração** ("funcionou pra mim, fiz assim")
   - 💬 **Storytime** (caso pessoal)
3. Capture **frase literal** (não resumo)

### Pegadinhas YouTube
- Comentários de pessoas que NÃO consumiram o produto valem mais (vieram pesquisar, não compraram)
- Vídeos com >1M views já estão na "maioria consciente" — pra encontrar termo de baixa-consciência, pegue vídeos 10k-100k
- Comentários em vídeos B2B (LinkedIn-style) costumam ser mais polidos e menos verdadeiros que B2C

---

## 3. TikTok — Reino da Emoção Crua + Linguagem Gen Z

**O que você captura aqui:** hook que para o scroll, linguagem ultra-coloquial, dor expressada em <15s, hashtag-cluster.

**Onde mora o ouro:**
- Hook dos primeiros 3 segundos dos Reels virais
- Hashtags adjacentes (cluster semântico)
- Comentários com >100 likes
- Duets/Stitches do tema (críticas e endossos)

### Como pesquisar TikTok via Claude Code

WebSearch direto no TikTok não traz comentários completos. Use:
```
site:tiktok.com [X]
[X] tiktok hashtag
[X] viral tiktok
```

Pra raspar dados mais profundos:
- WebFetch da página de hashtag `https://www.tiktok.com/tag/[hashtag]`
- Captura primeiros 20 títulos visíveis
- Pra cada Reel top, faça WebFetch do URL específico pra capturar caption + alguns comentários

### Padrões de hook a procurar

- "POV:" (point of view — virou padrão de empatia)
- "Sinal de que você [X]"
- "Coisas que ninguém te conta sobre [X]"
- "Quando você [situação]"
- "Eu fiz [X] por [Y dias] e..."
- "Storytime: [X]"
- "Red flags em [X]"
- "Green flags em [X]"
- "[idade]+ que [X]"

### Hashtag-cluster

Pra cada hashtag-raiz, capture:
- 5 hashtags que aparecem JUNTO (cluster temático)
- 3 hashtags adjacentes (semelhantes mas não iguais)
- 2 hashtags de nicho (mais específicas, menor volume)

### Pegadinhas TikTok
- Faixa etária do TikTok BR ≠ TikTok US — não importar termos americanos
- Comentário com 50k likes pode ser sarcasmo — checar contexto
- Trends mudam em 2-4 semanas — anotar **data** da pesquisa

---

## 4. Instagram — Reino do Aspiracional + Carrossel Educativo

**O que você captura aqui:** linguagem que mistura desejo + aspiração, carrosséis educativos (que viram template de copy), comentários da "tribo".

**Onde mora o ouro:**
- Carrosséis com >10k likes (educativo + salvável)
- Reels com hook similar ao TikTok mas público mais maduro (BR: 28-45)
- Comentários em posts de criadores grandes do nicho
- Stories em destaque dos perfis-referência (linguagem de bastidor)

### Como pesquisar Instagram via Claude Code

```
site:instagram.com [X]
[X] instagram hashtag
instagram [X] reel
[criador X] instagram
```

WebFetch de:
- Páginas de hashtag (limitado, IG bloqueia parcial)
- Perfis específicos dos 3-5 criadores-referência do nicho

### Padrões a capturar

- **Templates de carrossel:** "5 sinais", "3 erros", "Antes vs depois", "Tipos de [X]"
- **Hooks de Reel:** parecidos com TikTok, mas com mais "se você é..." (segmentação por identidade)
- **Comentários de "tribo":** comentários que reforçam pertencimento ("só quem é mãe entende", "todo dentista sabe disso")

### Pegadinhas Instagram
- Algoritmo penaliza link na bio → linguagem de "vá pro link" é menos comum, mais "salva esse post"
- Comentários em IG são mais polidos que TikTok (público diferente)
- Carrossel educativo = ouro pra extrair estrutura de raciocínio do público

---

## 5. LinkedIn — Reino do B2B + Linguagem Profissional

**O que você captura aqui:** dor de carreira/negócio expressada em tom profissional, linguagem de tomador de decisão, objeções de ROI/risco.

**Onde mora o ouro:**
- Posts longos com >500 reações (validação de tese)
- Comentários de quem **discorda** (revelação de objeção)
- Posts virais de critique ("não concordo com o consenso de que...")
- Newsletter LinkedIn de criadores do nicho

### Queries-base

```
[X] LinkedIn
[X] B2B
ROI [X]
como medir [X]
case de [X]
implementação [X]
desafios [X]
[X] empresa
[X] gestor
[X] diretor
[X] CEO
por que [X] falha
[X] na prática
maturidade [X]
```

### Padrões a capturar

- **Tom "honesto e contrarian":** "Vou ser direto: [X] não é o que vocês pensam"
- **Storytime profissional:** "Há 3 anos, eu [X]. Hoje, [Y]"
- **Listas de aprendizado:** "5 lições depois de [X]"
- **Carrosséis B2B:** "Framework [X]", "[N] passos pra [resultado B2B]"

### Pegadinhas LinkedIn
- Linguagem performativa — separar o que é genuíno do que é "LinkedIn-talk"
- Engagement bait ("agree?") infla número sem sinalizar dor real
- Comentários polidos escondem objeção real — buscar "ressalvas" ("ótimo post, mas...")
- B2B BR ainda é menos maduro que B2B US — não copiar termos US

---

## Quadro-resumo de profundidade por plataforma

| Plataforma | Onde está a dor explícita | Onde está o desejo | Onde está a objeção |
|---|---|---|---|
| Google | "People also ask" | Autocomplete + Related | Buscas com "não funciona" |
| YouTube | Comentários | Títulos top | Comentários "tentei e não funcionou" |
| TikTok | Hooks de Reels | Cluster de hashtags | Comentários sarcásticos |
| Instagram | Stories em destaque | Carrosséis educativos | Comentários "salvei mas ainda não fiz" |
| LinkedIn | Posts "contrarian" | Cases de sucesso | Comentários discordantes |

---

## Quanto investigar por plataforma

| Modo da skill | Queries por plataforma | Tempo estimado |
|---|---|---|
| `--full` | 8-12 queries × 5 plataformas = 40-60 buscas | 2-3h |
| `--canal=X` | 15-20 queries no canal escolhido | 1h |
| `--rapido` | 4-6 queries × 5 plataformas = 20-30 buscas | 45min |

Pare quando os termos novos pararem de aparecer (saturação semântica) — geralmente após 30-40 queries totais.
