# 10 Validadores Anti-AI-Slop

Antes de salvar qualquer relatório, rode estes 10 checks. **Bloqueia entrega se qualquer um falhar** — corrige primeiro, entrega depois.

> Pesquisa de mercado gerada por IA é a coisa MAIS fácil de detectar e MAIS inútil. Estes validadores garantem que sua saída soe como pesquisa de campo, não como ChatGPT inventando.

---

## V1 — Literalidade dos Termos

**Regra:** Todos os 50 termos top precisam ser frases EXATAS capturadas em algum lugar, não criadas por você.

**Como validar:**
- Pra cada termo, exista pelo menos 1 fonte registrada (URL/post/comentário)
- Se você não tem a fonte do termo X, marque como "INFERIDO" e mova pro fim da lista
- Bloqueia entrega se >5 termos forem "INFERIDOS"

**Sinais de falha:**
- Termos como "Como otimizar a produtividade no nicho X" (genérico, abstrato)
- Termos perfeitos em português formal (público não fala assim)
- Termos sem nenhuma gíria/coloquialismo (50 termos formais = falso)

**Exemplo de correção:**
❌ "Como melhorar a gestão do tempo"
✅ "to enrolada com meu tempo, me ajuda"

---

## V2 — Frase-Origem em Toda Objeção

**Regra:** Cada uma das 150 objeções precisa ter `frase_origem` literal com fonte.

**Como validar:**
- Conte: quantas objeções no JSON têm `frase_origem` preenchida? Precisa ser 100%.
- Conte: quantas têm `fonte.url` válida? Precisa ser ≥80%.

**Sinais de falha:**
- Frases-origem que parecem reescritas em PT formal
- "Frase: o público costuma se preocupar com preço" ← isso é hipótese, não captura

**Exemplo de correção:**
❌ "O público demonstra preocupação com a complexidade"
✅ "que enrolação cara, eu nem entendi o vídeo todo"

---

## V3 — Cobertura Mínima de Plataformas

**Regra:** Pelo menos 3 das 5 plataformas (Google/YT/TikTok/IG/LinkedIn) representadas na coleta.

**Como validar:**
- Conte plataformas distintas em `metadata.plataformas_pesquisadas` → deve ser ≥3
- Conte queries por plataforma → cada plataforma incluída deve ter ≥4 queries

**Sinais de falha:**
- Tudo veio do Google (autocomplete não basta — falta voz literal)
- Pulou TikTok/IG "porque o público é B2B" (mesmo B2B tem IG/TikTok hoje)

---

## V4 — Anti-Abstração

**Regra:** Nenhum termo é abstração genérica sem nome próprio.

**Como validar:**
- Conte termos que contenham "ferramenta de", "estratégia de", "solução de" sem nome próprio depois → deve ser 0
- Conte termos sem nenhum nome de produto/método/pessoa → se for >30, suspeito

**Sinais de falha:**
- "Ferramenta de produtividade" ❌
- "Notion" ✅
- "Estratégia de marketing" ❌
- "Funil de 7 passos do Russell" ✅

---

## V5 — Especificidade das Sugestões

**Regra:** As 50 sugestões de conteúdo são específicas (não "fazer um post sobre X").

**Como validar:**
- Cada sugestão tem: formato definido + hook escrito + valor descrito + ponte + CTA
- Conta caracteres da `ideia_conteudo.hook` → ≥30 caracteres (1 frase real, não 3 palavras)

**Sinais de falha:**
❌ "Reel sobre como criar app"
✅ "Reel 45s — Hook: 'Você acha que precisa saber programar pra criar app. Não precisa.' — Demo Lovable 20s — Ponte: Imersão = 2 dias — CTA: link bio"

---

## V6 — Ponte Não-Genérica

**Regra:** A ponte busca→produto de cada ideia é única (não 50 vezes "compra meu curso").

**Como validar:**
- Liste todas as `ideia_conteudo.ponte` no JSON
- Conte ocorrências da string mais comum → não pode ser mais de 5x repetida
- Se >30% das pontes terminam com "link na bio", reescreva variando CTA

**Sinais de falha:**
- 50 sugestões terminando em "entre na minha mentoria"
- Pontes que não mostram o **delta** entre o conteúdo orgânico e o produto

---

## V7 — Score com Racional

**Regra:** Todo `score_oportunidade` (1-10) tem justificativa, não é chutado.

**Como validar:**
- Pra cada termo top-10, exija no relatório markdown 1 frase explicando o score
- Exemplo bom: "Score 9: termo aparece em 18 fontes, objeção é PADC-Dúvida (mais fácil quebrar), volume estimado alto pelo autocomplete"

**Sinais de falha:**
- Todos os termos com score 7-9 (escala não usada de verdade)
- Scores sem nenhum racional documentado

---

## V8 — Registro Linguístico Adequado

**Regra:** Output respeita o registro do nicho (não "leverage synergies" pra esteticista, não "mano vibe" pra advogado).

**Como validar:**
- Pegue 3 amostras aleatórias do relatório
- Lê em voz alta — soa coerente com o nicho?
- Se nicho é B2C feminino: tem coloquialismos, gírias? ✅
- Se nicho é B2B corporativo: tem termos técnicos sem soar gringo? ✅

**Sinais de falha:**
- Tradução literal de termos US ("alavancar sinergias", "frictionless experience")
- Linguagem ChatGPT padrão (palavras tipo "abordagem holística", "ecossistema vibrante")

**Cross-check obrigatório:** rode o output final por `/voz-humana-br` antes de fechar. Se voz-humana detectar palavras-banidas, volta pra correção.

---

## V9 — Anti-termos Listados

**Regra:** Os 10 anti-termos (o que NÃO falar) estão preenchidos.

**Como validar:**
- `anti_termos.length === 10` no JSON
- Cada anti-termo tem `razao` preenchida

**Sinais de falha:**
- Lista vazia ("não identificamos anti-termos") ← isso é preguiça
- Anti-termos sem razão ← inútil pra próxima skill consumir

**Tipos válidos de anti-termo:**
- Jargão gringo que o nicho rejeita ("hustle culture")
- Palavras que público associa a vendedor chato ("imperdível", "última chance")
- Termos técnicos que confundem ("ROI" pra B2C que não sabe o que é)
- Gatilhos negativos do nicho ("rico", "milionário" pode afastar nicho terapeuta)

---

## V10 — Output Passou pela Voz-Humana

**Regra:** O relatório-mestre.md e os recortes foram rodados via `/voz-humana-br` antes de salvar.

**Como validar:**
- Verifique que não tem travessão em texto corrido (só em diálogo direto)
- Sem "no entanto", "ademais", "portanto" (jargão IA)
- Sem paralelismo negativo ("não apenas X mas também Y")
- Sem gerúndio na cauda ("estando você procurando...")
- Sem sicofancia ("excelente pergunta!", "ótima observação!")
- Sem hedging ("talvez possa ser interessante considerar")
- Frases de tamanhos variados (desvio padrão saudável)

**Sinais de falha:**
- Texto que parece traduzido do inglês
- Frases todas iguais em tamanho
- Vocabulário "ChatGPT-2024" (insights acionáveis, jornada, mindset, etc)

---

## Checklist final antes de salvar

Cole isso no fim de cada relatório-mestre como evidência de validação:

```markdown
## Validação Anti-AI-Slop

- [x] V1: 50 termos literais, com fonte
- [x] V2: 150 objeções com frase-origem
- [x] V3: 5 plataformas representadas
- [x] V4: Zero termos abstratos
- [x] V5: Sugestões específicas (hook + valor + ponte + CTA)
- [x] V6: Pontes variadas (sem repetir CTA >5x)
- [x] V7: Scores com racional
- [x] V8: Registro coerente com nicho
- [x] V9: 10 anti-termos com razão
- [x] V10: Passou por /voz-humana-br em [data]

Validado em: 2026-05-13
```

Se algum item estiver [ ] (não checked), NÃO entregue. Corrija primeiro.

---

## Bonus: Smell test final

Antes de fechar, leia 3 termos aleatórios do top-50 em voz alta, e pergunte:

> **"Eu, como cliente desse nicho, digitaria exatamente isso?"**

Se a resposta é "talvez não, soa robótico", marque o termo pra correção. A pesquisa só vale se passa nesse smell test.
