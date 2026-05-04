# Texto em Visual — Skill Proprietaria Tata Goncalves

Motor de transformacao de texto em visual nota 1000 baseado no **Metodo Imperatriz de Visual** — combinacao proprietaria de:

- **Dan Roam** (6x6 + SQVID — categorizacao de ideias)
- **Paivio** (Dual Coding — texto + imagem)
- **Tufte** (Data-Ink Ratio — simplicidade)
- **Mayer** (12 principios de multimedia learning)
- **Nancy Duarte** (Forma S narrativa)
- **Gestalt + F/Z patterns** (psicologia visual)
- **Adaptacao Brasil** (estetica BR, paletas, tipografia)

---

## O QUE ELA FAZ

Recebe texto (copy, VSL, pagina, artigo) e entrega **briefing visual estruturado**:

- Extrai ideias-ancoras do texto
- Categoriza cada uma pelos 6 tipos Dan Roam
- Escolhe tipo de visualizacao ideal entre 18 disponiveis
- Aplica os 10 principios universais de design
- Valida contra 11 anti-patterns visuais
- Gera **prompt pronto pra IA de imagem** (Midjourney, Ideogram, Gemini, DALL-E, Firefly)
- Adapta por canal (site, Instagram, stories, VSL, e-mail, carrossel, apresentacao, WhatsApp)
- Indica ferramenta ideal pra cada visual
- Estima tempo e orcamento de producao

---

## COMO USAR

### Modo padrao (completo)
```
/texto-em-visual

[cola copy/texto aqui]
```
Analise completa + briefing por canal + prompts IA.

### Modo express
```
/texto-em-visual express

[texto]
```
So tipo de visual + briefing rapido.

### Modo por canal
```
/texto-em-visual por-canal instagram

[texto]
```
So briefing pro canal especifico.

Canais suportados: `site`, `instagram`, `stories`, `vsl`, `email`, `carrossel-linkedin`, `apresentacao`, `whatsapp`.

### Modo mentoria
```
/texto-em-visual mentoria

[texto]
```
Explica cada decisao com profundidade didatica.

---

## ESTRUTURA DE ARQUIVOS

```
texto-em-visual/
├── SKILL.md                      ← Cerebro (sempre carregado)
├── OS-10-PRINCIPIOS.md           ← Principios universais de design
├── OS-18-TIPOS-VISUALIZACAO.md   ← Catalogo de tipos + quando usar
├── FRAMEWORKS-TRANSFORMACAO.md   ← Dan Roam, Mayer, Tufte, Duarte
├── APLICACAO-POR-SECAO-SITE.md   ← Visual por secao de site
├── FERRAMENTAS-E-FLUXO.md        ← Ferramentas por nivel + fluxo 9 fases
├── ANTI-PATTERNS-VISUAIS.md      ← 11 erros fatais + antidoto
├── ADAPTACAO-BR-VISUAL.md        ← Paletas BR, tipografia, referencias
├── BRIEFING-IA-IMAGEM.md         ← Templates pra Midjourney, Ideogram, Gemini
└── README.md                     ← Este arquivo
```

---

## OS 18 TIPOS DE VISUALIZACAO SUPORTADOS

### Explicar conceito
1. Diagrama simples (SVO)
2. Venn
3. Piramide
4. Matriz 2x2

### Contar processo
5. Flowchart
6. Timeline
7. Journey Map
8. Stepper

### Comparar
9. Before/After
10. Tabela comparativa
11. Pros/Cons

### Mostrar dados / prova
12. Dashboard de numeros
13. Grafico de barras
14. Grafico de linha
15. Isotype

### Storytelling
16. Carrossel de slides
17. Ilustracao narrativa
18. Mood board

---

## INTEGRACAO COM O ECOSSISTEMA TATA

**Fluxo ideal:**

```
/briefing-copy-360              (briefing)
       ↓
/mecanismo-unico                (o COMO)
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
       ↓
/analise-anuncio-1000           (pos-lancamento)
```

**Papel dessa skill:** ponte entre texto e producao visual. Nao produz arte final, gera o briefing que vira arte final.

---

## TRIO PROPRIETARIO TATA

Essa skill forma o **trio completo** de copy nota 1000:

| Skill | Responsabilidade |
|---|---|
| `/mecanismo-unico` | O COMO (mecanismo) |
| `/headline-imperatriz` | Como apresentar (headlines por temperatura) |
| `/texto-em-visual` | Como **visualizar** (visuais do mecanismo e das headlines) |

Juntas: motor completo de copy + visual nota 1000.

---

## REGRAS DURAS (a skill nao negocia)

1. Nao gera visual pra ideia vaga — exige ancora clara
2. Nao sugere mais de 1 ideia por visual
3. Nao recomenda stock photo obvia
4. Nao mistura estilos de icones
5. Nao sugere tipografia sem proposito
6. Nao sugere cores sem sistema (60-30-10)
7. Nao pula teste dos 5 segundos
8. Nao viola acessibilidade (WCAG 4.5:1)
9. Nao copia concorrente literal
10. Sempre oferece prompt pra IA quando aplicavel
11. Sempre versiona por canal

---

## COMO COMPARTILHAR COM MENTORANDAS

### Opcao 1 — Copiar pasta
```bash
cp -r ~/.claude/skills/texto-em-visual /caminho/da/mentoranda/.claude/skills/
```

### Opcao 2 — Zipar e enviar
```bash
cd ~/.claude/skills/
zip -r texto-em-visual.zip texto-em-visual/
```

### Opcao 3 — Git repo privado

---

## CANAIS SUPORTADOS

- Site / Landing page (hero, proof, metodo, beneficios, oferta, FAQ, CTA)
- Instagram feed (1:1 ou 4:5)
- Instagram stories (9:16)
- LinkedIn carrossel (7-10 slides)
- VSL / YouTube Ads (16:9)
- E-mail marketing (vertical 600px)
- WhatsApp (quadrado pequeno)
- Apresentacao / Webinar (16:9)
- Ebook / PDF

---

## FERRAMENTAS RECOMENDADAS (stack Tata)

1. **Figma** — montagem final profissional
2. **Whimsical** — diagramas e wireframes
3. **Ideogram 2.0** — criativos com frases
4. **Gemini Nano Banana** — ilustracoes com rosto BR
5. **Midjourney** — estetica premium
6. **Flourish.studio** — graficos de dados
7. **Canva Pro** — emergencia ou iniciantes

Custo total: ~R$ 300-400/mes pra stack completa.

---

## VERSIONAMENTO

- **v1.0** (atual) — 18 tipos visualizacao, 4 modos, 9 fases, briefing IA embutido
- **v1.5** (planejado) — biblioteca de visuais vencedores BR por nicho
- **v2.0** (planejado) — integracao direta com ferramentas de geracao (API)
- **v3.0** (planejado) — feedback loop com performance dos visuais

---

## FILOSOFIA DA SKILL

> **Cerebro processa imagem 60.000x mais rapido que texto. Menos texto, mais hierarquia visual. 1 ideia = 1 visual.**

Visual nao e decoracao. Visual e **comunicacao acelerada**. Pagina com visual certo converte 3-5x mais que pagina igualmente boa em texto. E em mercado BR saturado, visual diferenciado = vantagem mensuravel em CPA.

Metodo Imperatriz de Visual — propriedade intelectual Tata Goncalves.
