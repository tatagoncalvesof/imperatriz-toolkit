# OS 10 PRINCIPIOS UNIVERSAIS DE COMUNICACAO VISUAL

Esses 10 sao a base de todo design bom. Violar 1 fragiliza. Violar 3+ destroi. Toda recomendacao da skill passa por esses filtros.

---

## 1. HIERARQUIA VISUAL

### Definicao
O olho humano tem uma ordem de leitura. Voce controla essa ordem com tamanho, contraste, posicao e cor.

### As 4 alavancas de hierarquia

| Alavanca | Como funciona |
|---|---|
| **Tamanho** | Maior e lido primeiro |
| **Contraste** | O que contrasta mais e lido primeiro |
| **Posicao** | Topo-esquerda e lido primeiro (cultura ocidental) |
| **Cor** | Cor saturada puxa olho |

### Regra dura
Toda pagina/visual precisa ter **1 elemento dominante**, 2-3 secundarios, resto subordinado.

### Teste
Pegue um screenshot do teu visual. Desfoque. Ainda da pra ver o elemento dominante? Se nao, hierarquia fraca.

### Violacao tipica
Tudo do mesmo tamanho, mesma cor, mesmo peso. Olho nao sabe pra onde ir.

---

## 2. CONTRASTE

### Definicao
Diferenca entre elementos. Sem diferenca, cerebro ve "massa cinza" e nao processa.

### Tipos de contraste

- **Cor:** claro vs escuro, quente vs frio
- **Tamanho:** grande vs pequeno
- **Peso tipografico:** bold vs regular, fonte grossa vs fina
- **Espaco:** cheio vs vazio
- **Forma:** organica vs geometrica

### Regra WCAG (acessibilidade)
Contraste minimo **4.5:1** entre texto e fundo. Menos que isso, 15% do publico nao le + penaliza em SEO.

### Ferramenta de validacao
- WebAIM Contrast Checker (webaim.org/resources/contrastchecker)
- Figma Plugin: Stark

### Violacao tipica
Texto branco em fundo amarelo claro. Legivel pra designer com luz boa, invisivel pra usuario comum.

---

## 3. REPETICAO

### Definicao
Elementos que se repetem criam **sistema**. Sistema = identidade. Identidade = memoria.

### O que repetir
- Mesma cor de botao em todo site
- Mesmo estilo de icone (todos filled ou todos outline, nunca misturar)
- Mesma familia tipografica
- Mesma proporcao de espacamento
- Mesma curvatura de bordas (radius)

### Anti-padrao comum
Criar "sistema" diferente a cada secao. Amadorismo detectavel em 3 segundos.

### Teste
Remova as imagens e textos. Deixe so os elementos estruturais (botoes, fundos, ornamentos). Eles formam padrao reconhecivel?

---

## 4. ALINHAMENTO

### Definicao
Nada fica solto. Tudo se alinha a algo. Grid invisivel guia posicao de tudo.

### Tipos de alinhamento
- A margem (esquerda, direita, centro)
- A outro elemento (linha baseline compartilhada)
- A grid (8px, 12 colunas, etc)

### Regra profissional
**12 colunas** com gaps consistentes e um sistema de espacamento multiplicado por 4 ou 8 (4, 8, 16, 24, 32, 48, 64).

### Violacao tipica
Elementos "a olho", um 2px pra esquerda, outro 5px pra direita. Parece bagunca.

### Teste
Abra o Figma/ferramenta com regua. Todos os elementos criticos encostam em linhas imaginarias? Se sim, alinhado. Se nao, refazer.

---

## 5. PROXIMIDADE

### Definicao
Elementos relacionados ficam proximos. Elementos nao-relacionados ficam distantes.

### A lei de Gestalt
Cerebro agrupa automaticamente o que esta proximo. Se voce coloca titulo e descricao perto, leitor le como "unidade". Se coloca distante, le como "coisas separadas".

### Regra pratica
Espaco entre elementos relacionados (titulo e paragrafo): **1x**
Espaco entre secoes (grupo diferente): **2-3x**

### Exemplo
```
TITULO H2
Descricao logo abaixo
[espaco pequeno]

TITULO H2 (proxima secao)
Descricao dele
```

Vs

```
TITULO H2

Descricao isolada com espaco gigante
[parece outro bloco]
```

### Violacao tipica
Espacamento igual entre tudo — cerebro nao consegue agrupar.

---

## 6. ESPACO NEGATIVO (WHITE SPACE)

### Definicao
Espaco vazio **e elemento de design**, nao falta de conteudo.

### Por que importa
- Respiracao = sofisticacao percebida
- Aperto = barato percebido
- Apple, Stripe, Linear sao mestres em white space

### Regra Tata
Mentoranda tipica acha que precisa "preencher" o espaco. Educar: **espaco vazio valoriza** o que esta ao redor.

### Como calcular
- Titulo: pelo menos 1x altura de linha acima
- Paragrafo: pelo menos 0,5x linha entre linhas
- Secao: pelo menos 3-4x a altura do maior elemento acima

### Teste
Coloque a pagina ao lado da homepage da Apple. A tua parece "apertada demais"? Adicione 30% mais espaco.

---

## 7. COR INTENCIONAL

### Definicao
Cor nao e estetica. Cor e **funcao**.

### Sistema de cor profissional

| Tipo | Funcao | Quantidade |
|---|---|---|
| **Primaria** | Marca, identidade principal | 1-2 tons |
| **Secundaria** | Apoio, variedade | 2-3 tons |
| **Destaque / CTA** | Acao critica | 1 cor unica |
| **Neutros** | Estrutura (fundo, texto, bordas) | 4-6 tons de cinza |
| **Semantica** | Erro (vermelho), sucesso (verde), alerta (amarelo), info (azul) | 4 cores |

### Regra dos 60-30-10
- 60% neutro (fundo, texto)
- 30% primaria (elementos de marca)
- 10% destaque (CTAs)

Violar isso vira carnaval.

### Violacao tipica
3-4 cores primarias diferentes. Site parece infantil / amador.

---

## 8. TIPOGRAFIA COMO MENSAGEM

### Definicao
Fonte comunica antes das palavras. A escolha de fonte E mensagem.

### Familias e o que transmitem

| Familia | Transmite | Uso tipico BR |
|---|---|---|
| **Serif (Playfair, Georgia, Fraunces)** | Tradicional, autoridade, luxo, elegancia | Marcas high ticket, mentoria, financas |
| **Sans-serif (Inter, Helvetica, Manrope)** | Moderno, tech, limpo, neutro | Startups, SaaS, produto digital |
| **Script (Playlist, Caveat, Dancing)** | Feminino, artesanal, pessoal | Mentoria feminina, artesanato |
| **Display (Bebas, Oswald, Anton)** | Impacto, atencao, poder | Headlines, hero, manifestos |
| **Monospace (JetBrains, Fira Code)** | Tecnico, preciso, codigo | Tech, tools, devs |

### Regra
**Maximo 2 familias** em um projeto. Uma pra titulos, outra pra corpo.

### Combinacoes BR que funcionam

1. **Playfair (titulos) + Inter (corpo)** — high ticket feminino
2. **Manrope (titulos) + Inter (corpo)** — SaaS moderno
3. **Fraunces (titulos) + Inter (corpo)** — editorial + tech
4. **Bebas (display) + Manrope (corpo)** — impacto + limpeza

### Tamanhos
- H1: 48-72px desktop / 32-40px mobile
- H2: 32-40px desktop / 24-28px mobile
- H3: 24-28px desktop / 18-22px mobile
- Corpo: 16-18px desktop / 14-16px mobile

Texto menor que 14px em mobile e ilegivel.

---

## 9. CONSISTENCIA

### Definicao
Regras definidas e seguidas em TODO lugar do projeto.

### O que precisa ser consistente

- Todos os botoes tem mesma aparencia
- Todos os H1 tem mesma fonte e tamanho
- Todos os icones tem mesmo estilo
- Todas as imagens tem mesmo tratamento
- Todos os espacamentos seguem mesmo sistema

### Por que importa
Inconsistencia = amadorismo percebido. Usuario nao "vai notar" conscientemente, mas vai sentir que algo "nao bate" — e vai desconfiar.

### Como construir
Criar **design system** minimo:
- 1 paleta de cores
- 1 escala tipografica
- 1 sistema de espacamento
- 1 conjunto de icones
- 1 estilo de botao (com estados: normal, hover, pressed, disabled)

### Teste
Print de 5 paginas diferentes do teu site. Elas parecem da mesma marca? Se sim, consistente. Se cada uma parece site diferente, incoerente.

---

## 10. SIMPLICIDADE RADICAL

### Definicao
A melhor pergunta antes de finalizar: **"o que eu posso remover sem perder o sentido?"**

### Algoritmo de simplicidade

1. Olhe seu visual
2. Remova o elemento menos importante
3. Ainda comunica? Se sim, deixe removido
4. Repita ate nao poder mais remover sem perder mensagem

### Frase-ancora
> "Perfeicao nao e quando nao ha mais nada para adicionar, mas quando nao ha mais nada para remover." — Antoine de Saint-Exupery

### Aplicacoes
- Remover textos redundantes
- Remover ornamentos decorativos sem funcao
- Remover linhas/fundos/boxes desnecessarios
- Consolidar 3 CTAs em 1

### Violacao tipica
"Eu queria mostrar X, Y e Z num so visual." Nao. 1 visual = 1 ideia. Se tem 3 ideias, faca 3 visuais.

---

## CHECKLIST FINAL DOS 10 PRINCIPIOS

Antes de aprovar qualquer visual:

- [ ] Hierarquia clara (1 dominante + 2-3 secundarios)
- [ ] Contraste minimo 4.5:1
- [ ] Repeticao de elementos consistente
- [ ] Alinhamento a grid
- [ ] Proximidade respeitando relacoes
- [ ] White space respirando
- [ ] Paleta 60-30-10 respeitada
- [ ] Maximo 2 familias tipograficas
- [ ] Design system consistente
- [ ] Simplicidade — nada removivel restante

Se passar todos → aprovado.
Se falhar 1-2 → ajustar.
Se falhar 3+ → refazer.
