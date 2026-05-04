# ANTI-PATTERNS VISUAIS — 10 Erros Fatais

A skill `/texto-em-visual` bloqueia ativamente visuais com esses 10 erros. Cada um destrui o impacto do visual inteiro, mesmo se outros elementos estiverem fortes.

---

## ANTI-PATTERN 1 — TEXTO GIGANTE SEM IMAGEM

### Exemplo que a skill recusa
Pagina de vendas com secoes inteiras de texto puro, sem visual intermediario.

### Por que e ruim
- Cansa o olho em 30 segundos
- Taxa de scroll cai dramaticamente
- Violacao do Principio Dual Coding (Paivio)
- Mobile vira muro de texto

### Dado
Usuario medio le so **20-28%** do texto de uma pagina (Nielsen Norman Group).

### Antidoto
- A cada 3 paragrafos, inserir visual (foto, diagrama, icone, infografico)
- Transformar listas em grids de icones
- Destacar dados importantes em numeros gigantes

### Exemplo corrigido
RUIM: 5 paragrafos seguidos explicando metodo
BOM: 1 paragrafo + diagrama do metodo + 1 paragrafo

---

## ANTI-PATTERN 2 — IMAGEM DECORATIVA SEM FUNCAO

### Exemplo que a skill recusa
Stock photo generica ("mulher sorrindo com laptop") ao lado de paragrafo sobre mecanismo.

### Por que e ruim
- Desperdicio de atencao
- Viola Dual Coding (imagem nao reforca mensagem)
- Reduz credibilidade (usuario percebe stock)

### Como detectar
Pergunta: "se eu remover essa imagem, o texto perde sentido?"
- Se sim: imagem tem funcao, mantem
- Se nao: imagem e decorativa, remove ou substitui

### Antidoto
- Imagem SEMPRE reforca mensagem do texto adjacente
- Se precisar de imagem por estetica, use abstrata (gradiente, textura), nao pessoa em acao falsa
- Use dados/diagrama em vez de foto decorativa

---

## ANTI-PATTERN 3 — MAIS DE 3 CORES PRIMARIAS

### Exemplo que a skill recusa
Site com azul, vermelho, verde, amarelo, roxo todos saturados.

### Por que e ruim
- Carnaval visual
- Nenhuma cor "aparece"
- Violacao da regra 60-30-10
- Percepcao de amadorismo instantanea

### Antidoto
- 1 cor primaria (marca)
- 1 cor secundaria (apoio)
- 1 cor destaque (CTA)
- 4-6 tons de neutros (cinzas)
- 2-3 cores semanticas (erro, sucesso, alerta) — usadas SO na funcao

### Teste
Olhe printscreen da pagina. Quantas cores diferentes? Se mais de 5 incluindo neutros, simplificar.

---

## ANTI-PATTERN 4 — STOCK PHOTO OBVIA

### Exemplos que a skill recusa
- Mulher classe A com blazer branco rindo com computador
- Equipe multicultural do Shutterstock
- Handshake corporativo generico
- Lightbulb como metafora de "ideia"
- Pessoa apontando pra grafico imaginario

### Por que e ruim
- Destroi credibilidade (usuario identifica em 1 segundo)
- Sinaliza "empresa sem personalidade"
- Reverte autoridade construida em outros lugares

### Antidoto
- Foto propria (voce + equipe + clientes reais)
- Ilustracao IA personalizada (Ideogram, Gemini)
- Banco de imagens autorais (Unsplash, Pexels — mas cuidado com as mais usadas)
- Fotografia profissional propria (investimento de 1 dia pra 6 meses de material)

### Recomendacao
Se orcamento permite, contratar ensaio fotografico proprio = substitui 80% do stock no site.

---

## ANTI-PATTERN 5 — ICONES DE ESTILOS DIFERENTES

### Exemplo que a skill recusa
Pagina com icones filled (preenchidos), outline (linha) e duotone (2 cores) misturados.

### Por que e ruim
- Amadorismo percebido instantaneo
- Violacao do principio de consistencia
- Cerebro nao processa como sistema unificado

### Antidoto
- Escolher UM estilo e seguir em TODO site
- Bibliotecas com sistema unico:
  - **Phosphor Icons** (6 estilos, escolha 1)
  - **Lucide** (outline consistente)
  - **Heroicons** (outline + solid consistentes)
  - **Tabler Icons** (gratuito, 4000+ icones)
  - **Iconoir** (outline moderno)

### Regra
Um projeto = um icon system. Sem excecao.

---

## ANTI-PATTERN 6 — TEXTO SOBRE IMAGEM SEM CONTRASTE

### Exemplo que a skill recusa
Texto branco sobre foto colorida clara, sem overlay escuro.

### Por que e ruim
- Ilegivel pra visitante comum
- Violacao WCAG (acessibilidade)
- 15% do publico (visao fraca, daltonicos) nao le
- Penaliza SEO

### Antidoto
- Overlay escuro (preto 40-60% transparencia) sobre a foto
- Texto com text-shadow sutil
- Caixa semi-transparente atras do texto
- Usar foto com area escura/clara contrastante intencionalmente
- Validar com WebAIM Contrast Checker

### Regra WCAG
Contraste minimo **4.5:1** texto/fundo. Texto grande (24px+) aceita 3:1.

---

## ANTI-PATTERN 7 — INFORMACAO INACESSIVEL

### Exemplos que a skill recusa
- Informacao critica SO em imagem (sem texto alt)
- Imagem de infografico complexo sem legenda textual
- Video sem legendas ou transcricao
- Grafico sem labels textuais

### Por que e ruim
- Exclui deficientes visuais (3% da populacao ativa)
- Penaliza SEO (Google nao le texto em imagem)
- Usuario mobile com conexao ruim nao ve imagem mas le alt
- LGPD + acessibilidade estao ficando obrigatorios

### Antidoto
- Toda imagem tem alt text descritivo
- Infografico importante tem versao textual abaixo
- Video tem legendas obrigatoriamente
- Grafico tem labels + tabela textual alternativa

### Ferramentas
- Lighthouse (Chrome DevTools) — audita acessibilidade
- axe DevTools — extensao Chrome gratuita

---

## ANTI-PATTERN 8 — ANIMACAO EXAGERADA

### Exemplo que a skill recusa
Pagina com 10 elementos animando continuamente, parallax agressivo, particulas flutuando.

### Por que e ruim
- Distrai da mensagem
- Causa enjoo em alguns usuarios (LGPD brasileira tem regras pra "prefers-reduced-motion")
- Peso de pagina explode (performance mobile)
- Amadorismo "site de portfolio 2015"

### Antidoto
- Animacao intencional: so onde ajuda a comunicar (revelar dado, enfatizar CTA)
- Respeitar `prefers-reduced-motion` do usuario
- Maximo 1-2 animacoes continuas por pagina
- Animacoes de entrada (scroll trigger) sutis

### Regra
Animacao nao deve **competir** pela atencao. Deve **complementar**.

---

## ANTI-PATTERN 9 — INFOGRAFICO POLUIDO

### Exemplo que a skill recusa
Infografico com 50 elementos em 1 imagem: 20 numeros, 10 icones, 5 graficos, 8 caixas de texto, tudo colorido em cores primarias.

### Por que e ruim
- Usuario nao sabe por onde comecar
- Cerebro processa como ruido
- Nenhuma mensagem gruda
- Violacao de Tufte (data-ink ratio horrivel)

### Antidoto
- 1 infografico = 1 ideia central (no maximo 5 sub-ideias)
- Hierarquia visual forte (1 dominante + 2-3 secundarios)
- Paleta restrita (60-30-10)
- Espaco negativo generoso
- Alinhamento a grid

### Regra dura
Se voce nao consegue apontar UMA mensagem principal em 3 segundos, infografico esta poluido. Desmembrar em 2-3.

---

## ANTI-PATTERN 10 — COPIAR CONCORRENTE LITERAL

### Exemplo que a skill recusa
Pagina de vendas visualmente identica a concorrente conhecido (mesma estrutura, mesmas cores, mesmos icones).

### Por que e ruim
- Publico que ja viu o concorrente identifica
- Vira "mais um" em vez de distintivo
- Compromete marca pessoal
- Ownership zero (facil de ser substituido)

### Antidoto
- Inspirar-se em multiplas referencias, nao 1
- Identificar 3-5 sites referencia de nichos DIFERENTES
- Combinar elementos em sua propria linguagem
- Desenvolver identidade visual propria em 3-6 meses

### Teste
Mostre tua pagina pra alguem que conhece teus concorrentes. Ela fala "nossa, parece X"? Se sim, muito similar.

---

## ANTI-PATTERN BONUS #11 — FORMATACAO MOBILE QUEBRADA

### Exemplos que a skill recusa
- Texto minusculo em mobile
- Botoes pequenos demais pra dedo
- Imagem grande demais esticada
- Grid que nao colapsa em mobile (3 colunas fixas)

### Por que e ruim
- **70%+ do trafego brasileiro e mobile**
- Se nao funciona em mobile, pagina nao funciona
- Google penaliza em ranking

### Antidoto
- Design mobile-first (comecar pelo mobile, depois desktop)
- Testar em dispositivo real (nao so Chrome DevTools)
- Botao minimo 44x44px (Apple guideline)
- Fonte minima 16px corpo (prevents iOS zoom)
- Grid colapsa: 3 colunas desktop → 1 mobile; 4 colunas desktop → 2 mobile

---

## PROTOCOLO DE BLOQUEIO DA SKILL

Quando a skill detectar qualquer desses 11 anti-patterns:

1. **Nao entrega o briefing problematico**
2. **Explica ao usuario** qual anti-pattern foi detectado
3. **Mostra qual principio foi violado**
4. **Oferece contraproposta corrigida**
5. **Se usuario insistir** → entrega com warning visivel

### Exemplo de bloqueio

```
ALERTA: Visual detectado tem ANTI-PATTERN 4 (stock photo obvia).

Imagem sugerida "mulher de blazer com laptop" destroi credibilidade.

Violacao do Principio 1 (Hierarquia) + Principio 9 (Consistencia de marca).

ALTERNATIVAS:
1. Substituir por foto sua propria
2. Gerar ilustracao IA (prompt incluso abaixo)
3. Usar icone em vez de imagem (se ideia e conceitual)

[prompt IA sugerido]
```

---

## CHECKLIST ANTI-PATTERNS

Antes de entregar briefing visual, rodar:

- [ ] Texto nao esta sozinho (tem visual a cada 3 paragrafos)
- [ ] Imagem tem funcao (nao decorativa)
- [ ] Maximo 3 cores primarias
- [ ] Nao usa stock photo obvia
- [ ] Icones do mesmo sistema
- [ ] Contraste WCAG 4.5:1 em textos
- [ ] Tem versao acessivel (alt, legendas)
- [ ] Animacoes intencionais (nao exagero)
- [ ] Infografico limpo (maximo 5 sub-ideias)
- [ ] Nao copia concorrente literal
- [ ] Responsive mobile validado

Se passar todos os 11 → entrega autorizada.
Se falhar 1+ → bloqueio automatico.
