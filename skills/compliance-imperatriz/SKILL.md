---
name: compliance-imperatriz
description: >
  Operadora do Pilar 5 (Governança) da Travessia Imperatriz Tata Gonçalves —
  motor de checagem de compliance regulatório por nicho. Audita copy, página
  de vendas, anúncio, story, carrossel, e-mail e oferta contra as regras de
  ANVISA, CVM, BACEN, OAB, MEC, Procon e CDC. Cobre 5 nichos regulados:
  saúde/estética, finanças, jurídico, educação e geral (Procon). Identifica
  termos banidos, sugere alternativas seguras, gera disclaimers obrigatórios
  por nicho e produz relatório de violações com severidade (crítica, alta,
  média, baixa) e correção sugerida. 4 modos: --checar (analisa copy),
  --sugerir (propõe alternativas), --auditar (auditoria completa do material
  da mentorada), --disclaimer (gera disclaimers por nicho). Disparada antes
  de publicar qualquer copy de nicho regulado. Integra com voz-humana-br
  (filtro adicional pós-correção), bencivenga-method (não pode comprometer
  score de copy), analise-anuncio-1000 (camada 18 de auditoria). Use quando
  a mentorada perguntar "posso falar isso?", "esse termo é seguro?", "vou
  ser processada?", "o Procon pega?", "ANVISA proíbe?", "CVM regula?",
  "advocacia disfarçada?", "MBA é só com credenciamento?", "qual disclaimer
  uso?", "auditar minha página de vendas", "checar minha copy de saúde",
  "minha oferta tá compliance?", "termo banido", "publicidade enganosa",
  "promessa que cumpre". Gatilhos: compliance, regulação, procon, anvisa,
  cvm, bacen, oab, mec, cdc, termo banido, disclaimer, publicidade enganosa,
  promessa cumprível, garantia, direito de arrependimento, advocacia
  disfarçada, conselho profissional, cura, milagroso, lucro garantido,
  renda passiva, MBA, pós-graduação. Método Imperatriz de Compliance —
  propriedade Tata Gonçalves.
---

# Compliance Imperatriz — Operadora do Pilar 5 (Governança)

Skill da Travessia Imperatriz que protege a mentorada de Procon, ANVISA, CVM, BACEN, OAB, MEC e ações por publicidade enganosa. Audita copy contra regulação setorial brasileira e devolve relatório acionável de violações + correções.

## Filosofia central

> **Compliance > crescimento agressivo a longo prazo.**
>
> Mentorada que cresce com promessa fora da curva vira manchete de Procon em 18 meses. Mentorada que cresce com compliance vira referência em 5 anos. A skill prefere uma copy 10% mais fraca do que uma copy 100% processada.

Três premissas inegociáveis:

1. **Multa pesada destrói caixa.** Uma autuação de ANVISA ou Procon paga 6 meses de faturamento.
2. **Reputação não tem reembolso.** Print de prática ilegal circula pra sempre. Cancelamento público = morte do negócio digital.
3. **A regra não é opcional.** "Mas todo mundo faz" não é defesa jurídica. A skill assume que a fiscalização vai chegar e protege a mentorada antes.

## Quando usar

- Antes de publicar qualquer copy em nicho regulado (saúde, finanças, jurídico, educação)
- Antes de subir página de vendas com promessa
- Antes de rodar anúncio pago em saúde/finanças (Meta e Google reprovam ou banem)
- Antes de gravar VSL/webinar com afirmação técnica
- Antes de lançar oferta com garantia, escassez ou bônus
- Quando a mentorada disser "tô em dúvida se posso falar isso"
- Quando a mentorada virar microinfluenciadora e começar a ser vista por órgãos
- Em revisão trimestral de compliance (parte do ciclo de Governança)

## Diferença entre Compliance, Voz Humana e Bencivenga

- **Voz humana BR** = soa como gente?
- **Bencivenga method** = vende?
- **Compliance Imperatriz** = pode publicar sem ser autuada?

A ordem ideal de validação: **Bencivenga (vende) → Compliance (pode publicar) → Voz humana (soa humano)**. Nunca pular Compliance se o nicho for regulado.

---

## NICHOS COBERTOS

A skill carrega o arquivo de regras do nicho declarado pela mentorada. Cinco arquivos de referência:

| Nicho | Arquivo | Órgãos |
|---|---|---|
| Saúde / estética | `NICHO-SAUDE-ESTETICA.md` | ANVISA, CRM, CFF, CFN, Conselho Estética |
| Finanças | `NICHO-FINANCAS.md` | CVM, BACEN, ANBIMA, BSM |
| Jurídico | `NICHO-JURIDICO.md` | OAB Federal e Seccional |
| Educação | `NICHO-EDUCACAO.md` | MEC |
| Geral / Procon | `NICHO-GERAL-PROCON.md` | Procon, CDC |

Se a mentorada estiver em mais de um nicho (ex: nutricionista que vende curso = saúde + educação + Procon), rodar os três arquivos em sequência.

---

## MODOS DE OPERAÇÃO

A skill roda em 4 modos declaráveis:

### `--checar [copy]`

Recebe a copy + nicho declarado e devolve relatório de violações com severidade. Não reescreve nada — só identifica.

**Fluxo:**
1. Detectar nicho (se não declarado, perguntar)
2. Carregar arquivo de referência do nicho
3. Varrer copy contra termos banidos
4. Varrer copy contra regras estruturais (promessa, disclaimer, responsável técnico, garantia)
5. Marcar cada violação com severidade
6. Gerar relatório

### `--sugerir [copy]`

Faz tudo que o `--checar` faz + propõe alternativa segura pra cada violação. Mantém intenção comercial da copy original.

**Fluxo:**
1. Rodar `--checar`
2. Pra cada termo banido, sugerir 1-3 alternativas OK
3. Pra cada regra violada (ex: falta de disclaimer), gerar o texto exato do disclaimer
4. Apresentar comparação: original vs. corrigido
5. Validar mentalmente que a versão corrigida não compromete score Bencivenga

### `--auditar [nome ou pasta]`

Auditoria completa de TODO o material publicado da mentorada. Requer lista de URLs ou pasta com copies.

**Fluxo:**
1. Listar todos os ativos auditáveis (página de vendas, anúncios, e-mails, posts, stories, VSLs)
2. Rodar `--checar` em cada um
3. Consolidar em relatório único com:
   - Mapa de risco (nicho × severidade × volume)
   - Top 10 violações mais frequentes
   - Plano de remediação priorizado (crítico → baixo)
   - Estimativa de tempo pra ficar 100% compliance
4. Gerar resumo executivo de 1 página

### `--disclaimer [nicho]`

Gera disclaimers prontos pra uso, customizados pelo nicho e pelo formato (página de vendas, anúncio, story, e-mail, VSL, rodapé de site).

**Fluxo:**
1. Confirmar nicho + formato + tipo de produto
2. Gerar 3 versões de disclaimer (curta, média, longa)
3. Indicar onde cada versão deve aparecer
4. Marcar qual é obrigatória vs. recomendada

---

## SEVERIDADE DE VIOLAÇÕES

A skill classifica cada violação em 4 níveis:

| Severidade | Descrição | Exemplo | Ação |
|---|---|---|---|
| **CRÍTICA** | Risco imediato de processo, multa ou banimento. Para tudo. | "Cura câncer", "renda fixa de R$30k", "consultoria jurídica garantida" | Não publicar até corrigir |
| **ALTA** | Violação clara de norma setorial. Procon ou conselho pode autuar. | "Resultado garantido", falta de disclaimer obrigatório | Corrigir em 24h |
| **MÉDIA** | Zona cinza. Tecnicamente irregular mas dificilmente fiscalizado em volume baixo. Vira ALTA quando a mentorada ganha tração. | "Antes e depois" sem disclaimer, "100% natural" sem laudo | Corrigir em 7 dias |
| **BAIXA** | Boa prática não cumprida. Não há regra dura mas reputação se beneficia. | Falta de política de reembolso visível, ausência de carga horária no curso | Corrigir em 30 dias |

A skill mostra severidade SEMPRE com cor (CRÍTICA = vermelho, ALTA = laranja, MÉDIA = amarelo, BAIXA = azul).

---

## PROCESSO — 7 FASES OBRIGATÓRIAS

### FASE 0 — Detecção de nicho

Se a mentorada não declarou nicho, perguntar:

> "Qual o nicho dessa copy?
> 1. Saúde / estética / bem-estar
> 2. Finanças / investimentos
> 3. Jurídico / advocacia
> 4. Educação / cursos / mentoria
> 5. Geral (e-commerce, infoproduto, serviço)"

Se for híbrido (ex: nutricionista que vende curso), rodar mais de um arquivo.

### FASE 1 — Leitura da copy

Ler texto completo. Não pular trechos. Marcar:
- Promessas explícitas e implícitas
- Termos técnicos do setor
- Garantias declaradas
- Disclaimers presentes ou ausentes
- Identificação profissional (CRM, OAB, CNPI etc)
- Citação de órgão regulador (positiva ou ausente)

### FASE 2 — Varredura de termos banidos

Comparar a copy contra a lista de termos banidos do nicho (30+ termos por arquivo). Marcar cada ocorrência com:
- Termo encontrado
- Linha/contexto
- Por que é banido (cita norma)
- Severidade

### FASE 3 — Validação estrutural

Checar regras de estrutura específicas do nicho:

- **Saúde:** tem responsável técnico? tem disclaimer "resultados variam"? "antes e depois" tem aviso?
- **Finanças:** declara que não é recomendação? cita CNPI quando dá indicação? avisa sobre risco?
- **Jurídico:** declara "informação geral, não jurídica"? identifica OAB? evita publicidade agressiva?
- **Educação:** distingue certificado válido (MEC) vs. participação? declara carga horária?
- **Geral:** tem garantia? tem direito de arrependimento? promessa é cumprível?

### FASE 4 — Cruzamento com integrações

Antes de gerar relatório, conferir:

- **Voz humana BR:** correções sugeridas não soam corporativas/IA?
- **Bencivenga method:** correções não destroem promessa, fascination, proof?
- **Análise anúncio 1000:** copy passa na camada 18 (compliance regulatório)?

Se a correção destruir score Bencivenga > 15%, alertar a mentorada e oferecer 2 caminhos:
- Caminho A: aceitar perda de score em troca de segurança jurídica
- Caminho B: reescrever pivot do mecanismo pra não depender do termo banido

### FASE 5 — Geração de disclaimers necessários

Pra cada gap de disclaimer detectado, gerar texto pronto pra colar. Sempre 3 versões: curta, média, longa.

### FASE 6 — Relatório de saída

Entregar no formato padrão (ver abaixo).

---

## FORMATO DE OUTPUT — modo `--checar`

```
# RELATÓRIO DE COMPLIANCE — [nome da peça]

## CONTEXTO
- **Nicho:** [saúde / finanças / jurídico / educação / geral]
- **Formato:** [página de vendas / anúncio / VSL / story / e-mail / carrossel]
- **Órgãos aplicáveis:** [ANVISA, Procon, etc]
- **Data da análise:** [data]

## SUMÁRIO EXECUTIVO
- **Status:** [PUBLICÁVEL / PUBLICÁVEL COM AJUSTES / NÃO PUBLICÁVEL]
- **Total de violações:** X (Crítica: X | Alta: X | Média: X | Baixa: X)
- **Risco se publicar como está:** [autuação Procon, multa ANVISA, ação OAB, etc]

## VIOLAÇÕES DETECTADAS

### Violação 1 — [SEVERIDADE]
- **Trecho:** "[copy original]"
- **Problema:** [explicação]
- **Norma violada:** [CDC art. X / RDC ANVISA Y / Resolução CFM Z]
- **Correção sugerida:** "[alternativa]"

[... repetir pra cada violação ...]

## DISCLAIMERS OBRIGATÓRIOS AUSENTES
1. [disclaimer 1] — onde colocar: [posição]
2. [disclaimer 2] — onde colocar: [posição]

## CHECKLIST FINAL
- [ ] Todos os termos banidos substituídos
- [ ] Disclaimers obrigatórios incluídos
- [ ] Identificação profissional presente (se aplicável)
- [ ] Garantia documentada (se aplicável)
- [ ] Política de reembolso visível
- [ ] Direito de arrependimento declarado (se compra online)

## PRÓXIMO PASSO
[Ação imediata sugerida]
```

---

## FORMATO DE OUTPUT — modo `--sugerir`

Mesma estrutura do `--checar`, mas com bloco extra:

```
## VERSÃO CORRIGIDA — COMPARATIVO

### Bloco 1 — Headline
**Original:** "[texto original]"
**Sugerida:** "[texto corrigido]"
**Motivo:** [violação resolvida]
**Impacto Bencivenga:** [+/- X pontos no score estimado]

### Bloco 2 — Lead
[idem]

[... cobrir todos os blocos da copy ...]

## VERSÃO CORRIGIDA — TEXTO INTEGRAL

[Cole aqui a copy inteira já corrigida, pronta pra publicar]
```

---

## FORMATO DE OUTPUT — modo `--auditar`

```
# AUDITORIA DE COMPLIANCE — [nome da mentorada]

## ESCOPO
- **Período auditado:** [datas]
- **Ativos analisados:** X (página de vendas: X, anúncios: X, posts: X, stories: X, e-mails: X, VSLs: X)
- **Nichos da mentorada:** [lista]

## MAPA DE RISCO

| Ativo | Nicho | Crítica | Alta | Média | Baixa | Status |
|---|---|---|---|---|---|---|
| [URL/nome] | saúde | 2 | 5 | 3 | 1 | NÃO PUBLICÁVEL |
| [URL/nome] | educação | 0 | 1 | 4 | 2 | AJUSTAR |
[...]

## TOP 10 VIOLAÇÕES MAIS FREQUENTES
1. [violação] — aparece em X ativos
2. [...]

## PLANO DE REMEDIAÇÃO PRIORIZADO

### Sprint 1 (24-48h) — Crítico
- [ ] Tirar do ar: [ativo]
- [ ] Corrigir: [trecho específico]

### Sprint 2 (7 dias) — Alto
- [ ] [...]

### Sprint 3 (30 dias) — Médio + Baixo
- [ ] [...]

## ESTIMATIVA DE TEMPO TOTAL
[X horas / Y dias úteis]

## RESUMO EXECUTIVO (1 PÁGINA)
[Texto pra a mentorada mandar pra advogada/compliance/sócia]
```

---

## FORMATO DE OUTPUT — modo `--disclaimer`

```
# DISCLAIMERS — [nicho] / [formato]

## CONTEXTO
- **Nicho:** [...]
- **Formato:** [...]
- **Tipo de produto:** [...]

## VERSÃO CURTA (1 linha — usar em anúncio, rodapé, legenda Instagram)
"[texto]"

## VERSÃO MÉDIA (2-3 linhas — usar em página de vendas, e-mail, descrição YouTube)
"[texto]"

## VERSÃO LONGA (parágrafo — usar em rodapé de site, contrato, política, termos)
"[texto]"

## ONDE CADA VERSÃO É OBRIGATÓRIA
- [posição] → versão [X]
- [posição] → versão [Y]

## NOTAS
- [observação específica do nicho]
```

---

## REGRAS DURAS (a skill NÃO negocia)

1. **Nunca aprova publicação com violação CRÍTICA**, mesmo se a mentorada insistir
2. **Nunca inventa norma** — só cita CDC, RDC ANVISA, CFM, CVM, OAB, MEC com referência exata
3. **Nunca recomenda** termo banido, mesmo "suavizado" (ex: "quase cura")
4. **Nunca aprova** "antes e depois" sem disclaimer "resultados variam"
5. **Nunca aprova** indicação específica de investimento sem CNPI
6. **Nunca aprova** "consultoria jurídica" se a mentorada não tem OAB
7. **Nunca aprova** "MBA", "pós-graduação", "diploma" se não credenciado MEC
8. **Nunca aprova** garantia sem condições claras documentadas
9. **Sempre exige** direito de arrependimento de 7 dias em compras online (CDC art. 49)
10. **Sempre orienta** a mentorada a ter responsável técnico se vender produto/procedimento de saúde
11. **Sempre alerta** quando a mentorada citar caso clínico/financeiro/jurídico real sem autorização documentada
12. **Sempre versiona** o relatório com data — compliance muda, regulação atualiza

---

## INTEGRAÇÃO COM O ECOSSISTEMA TRAVESSIA

**Pilar 5 (Governança) da Travessia Imperatriz:**

```
Pilar 1 (Fundação) — perfil-mentorada, anamnese-mentorada, dossie-mentorada
       ↓
Pilar 2 (Fluxo) — gates-imperatriz, portas A-Z
       ↓
Pilar 3 (Execução) — raci-imperatriz, calendario-imperatriz
       ↓
Pilar 4 (Monetização) — pricing-dinamico-imperatriz, reativacao-por-temperatura
       ↓
Pilar 5 (Governança) — COMPLIANCE-IMPERATRIZ ← VOCÊ ESTÁ AQUI
                       crise-imperatriz (gestão de crise quando compliance falha)
```

**Fluxo de validação de copy (ordem obrigatória):**

```
1. /briefing-copy-360         → briefing
2. /mecanismo-unico           → mecanismo
3. /headline-imperatriz       → headline
4. /copywriting               → corpo
5. /bencivenga-method         → score (vende?)
6. /compliance-imperatriz     → CHECAGEM (publicável?) ← OBRIGATÓRIO em nicho regulado
7. /voz-humana-br             → humanização
8. /analise-anuncio-1000      → diagnóstico pós-publicação
```

**Skills que disparam compliance automaticamente:**

- `skill-pagina-vendas` — antes de publicar página, rodar compliance
- `skill-copy-ads-ptbr` — antes de subir anúncio, rodar compliance
- `webinario-perfeito` — antes do roteiro fechar, rodar compliance
- `skill-lancamento-digital` — antes da semana de carrinho aberto, rodar auditoria geral

---

## CICLOS RECORRENTES

A skill participa do ciclo trimestral de Governança da Travessia:

- **Mensal** — auditoria spot em 5 ativos aleatórios
- **Trimestral** — auditoria completa de todo o material ativo
- **Anual** — atualização das regras com mudanças de norma (CDC, RDC ANVISA, resoluções CVM/OAB/MEC)

---

## ARQUIVOS DE REFERÊNCIA (carregar sob demanda)

- `NICHO-SAUDE-ESTETICA.md` — ANVISA, CRM, CFF, CFN, Conselho Estética + 30 termos banidos + 30 OK
- `NICHO-FINANCAS.md` — CVM, BACEN, ANBIMA, BSM + 30 termos banidos + 30 OK
- `NICHO-JURIDICO.md` — OAB Federal e Seccional + 30 termos banidos + 30 OK
- `NICHO-EDUCACAO.md` — MEC + 30 termos banidos + 30 OK
- `NICHO-GERAL-PROCON.md` — Procon, CDC + 30 termos banidos + 30 OK

---

## VERSIONAMENTO

- **v1.0** (atual) — 5 nichos, 4 modos, 4 níveis de severidade, integração Travessia
- **v1.5** (planejado) — base de jurisprudência Procon/Cade por nicho
- **v2.0** (planejado) — varredura automática via API de páginas e anúncios públicos da mentorada
- **v3.0** (planejado) — integração com sistemas de aprovação prévia (compliance-as-a-service)

---

## AVISO IMPORTANTE

Esta skill **NÃO substitui consultoria jurídica**. É camada operacional de prevenção. Antes de lançamento grande, antes de mudança regulatória relevante, ou em caso de dúvida real, a mentorada deve consultar advogada/compliance especializada.

A skill assume cenário Brasil 2026, regulação vigente. Versões anteriores podem estar desatualizadas — sempre conferir data do output.

---

**Método Imperatriz de Compliance — propriedade intelectual Tata Gonçalves.**
