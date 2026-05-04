# Headline Imperatriz — Skill Proprietaria Tata Goncalves

Motor decisional de headlines nota 1000 baseado em **Metodo Imperatriz de Headline** — combinacao proprietaria de:

- **Schwartz** (5 niveis de consciencia + 5 estagios de sofisticacao)
- **Bencivenga** (scoring 4U + believable + beneficial)
- **Adaptacao Brasil** (gatilhos culturais + fraseologia nativa + regulacao)

---

## O QUE ELA FAZ

Le sua copy (VSL, pagina de vendas, anuncio, email, carrossel) e gera **5-10 variacoes de headline por TEMPERATURA DE PUBLICO**, com ficha pedagogica completa:

- **FRIO** — publico que nao te conhece
- **MORNO** — engajou seu conteudo organico
- **QUENTE** — visitou sua pagina de vendas
- **HOT / CARRINHO** — quase comprou
- **BASE COMPRADORA** — ja e cliente (reativacao/upsell)
- **RETARGETING GENERICO** — viu anuncio, nao clicou

Cada variacao vem com:
- Formula aplicada (das 17)
- Racional pedagogico
- Scoring Bencivenga (0-100)
- Gatilho emocional primario
- Mecanismo unico embedded
- Proof embedded
- Direcao visual sugerida

---

## COMO USAR

### Modo padrao (ensino)
```
/headline-imperatriz

[cola sua copy aqui]
```
A skill le, diagnostica, entrevista se precisar, gera variacoes com ficha completa.

### Modo express
```
/headline-imperatriz express

[sua copy]
```
So as headlines + scoring. Sem racional extenso.

### Modo mentoria (pra aluna)
```
/headline-imperatriz mentoria

[copy]
```
Explica CADA decisao com profundidade pedagogica.

---

## PRE-REQUISITOS IDEAIS

Nao obrigatorios, mas elevam qualidade:

1. **Briefing 360 preenchido** — rodar `/briefing-copy-360` antes
2. **Copy existente** — a skill le e extrai contexto
3. **Declaracao de temperatura(s)** desejada(s)

Se nada disso existir, a skill entra em **modo entrevista** e pergunta o minimo necessario antes de gerar.

---

## INTEGRACAO COM O ECOSSISTEMA TATA

**Fluxo ideal:**

```
/briefing-copy-360
       ↓
/headline-imperatriz  ← VOCE ESTA AQUI
       ↓
/copywriting ou /skill-copy-ads-ptbr   (corpo da copy)
       ↓
/bencivenga-method                     (scoring final)
       ↓
/analise-anuncio-1000                  (pos-lancamento)
```

---

## ESTRUTURA DE ARQUIVOS

```
headline-imperatriz/
├── SKILL.md                  ← O cerebro (sempre carregado)
├── REFERENCIA-SCHWARTZ.md    ← Niveis + estagios
├── REFERENCIA-BENCIVENGA.md  ← Scoring 4U + believable + beneficial
├── 17-FORMULAS.md            ← Catalogo de formulas com exemplos BR
├── ADAPTACAO-BR.md           ← Filtros culturais + nicho regulado
├── ANTI-PATTERNS.md          ← O que a skill recusa
└── README.md                 ← Este arquivo
```

---

## COMO COMPARTILHAR COM MENTORADAS

### Opcao 1 — Copiar pasta
A mentoranda instala copiando a pasta inteira pra `~/.claude/skills/`:

```bash
cp -r /caminho/pra/headline-imperatriz ~/.claude/skills/
```

Depois do proximo `/` a skill aparece disponivel via `/headline-imperatriz`.

### Opcao 2 — Zipar e enviar
```bash
cd ~/.claude/skills/
zip -r headline-imperatriz.zip headline-imperatriz/
```
Envia o zip, mentoranda extrai em `~/.claude/skills/`.

### Opcao 3 — Git repo privado
Subir a skill num repo privado, mentorandas clonam com permissao.

---

## REGRAS DURAS (a skill nao negocia)

1. Nao gera headline generica
2. Nao gera claim sem proof correspondente
3. Nao copia headline gringa literal
4. Nao mistura promessas (1 emocao dominante)
5. Nao entrega sem scoring Bencivenga
6. Nao gera estagio errado de sofisticacao
7. Nao gera nivel errado de consciencia pro publico
8. Em nicho regulado — alerta claims problematicas
9. Sempre le copy existente antes de pedir briefing
10. Curiosidade sem credibilidade = automaticamente descartada (regra Bencivenga)

---

## VERSIONAMENTO

- **v1.0** (atual) — motor Schwartz + Bencivenga + adaptacao BR, 6 temperaturas, 3 modos
- **v1.5** (planejado) — feedback loop com CTR/CPC real
- **v2.0** (planejado) — multi-canal com restricoes tecnicas automaticas por plataforma
- **v3.0** (planejado) — swipe files BR alimentados por resultados do ecossistema Tata

---

## FILOSOFIA DA SKILL

> **Headline e 80% do resultado.** Nao existe copy boa com headline fraca. Essa skill forca pensar antes de escrever — Schwartz decide formula, Bencivenga decide se passa, Brasil decide se ressoa. E depois disso, escreve.

Metodo Imperatriz de Headline — propriedade intelectual Tata Goncalves.
