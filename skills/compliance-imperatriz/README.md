# Compliance Imperatriz

Operadora do **Pilar 5 (Governança)** da Travessia Imperatriz da Tata Gonçalves. Audita copy, página de vendas, anúncio, story, carrossel, e-mail e oferta contra regulação setorial brasileira (ANVISA, CVM, BACEN, OAB, MEC, Procon, CDC) e devolve relatório de violações + correções acionáveis.

## Filosofia

> Compliance > crescimento agressivo a longo prazo.

Mentorada que cresce com promessa fora da curva vira manchete de Procon em 18 meses. Mentorada que cresce com compliance vira referência em 5 anos. A skill prefere uma copy 10% mais fraca a uma copy 100% processada.

## O que ela faz

- Identifica **termos banidos** por nicho (saúde, finanças, jurídico, educação, geral)
- Sugere **alternativas seguras** que não destroem score Bencivenga
- Gera **disclaimers obrigatórios** (curto, médio, longo) por nicho e formato
- Audita **todo o material ativo** da mentorada e gera plano de remediação priorizado
- Cruza com **voz-humana-br**, **bencivenga-method** e **analise-anuncio-1000**

## Nichos cobertos

| Nicho | Órgãos | Arquivo |
|---|---|---|
| Saúde / estética | ANVISA, CRM, CFF, CFN, Conselho Estética | `NICHO-SAUDE-ESTETICA.md` |
| Finanças | CVM, BACEN, ANBIMA, BSM | `NICHO-FINANCAS.md` |
| Jurídico | OAB | `NICHO-JURIDICO.md` |
| Educação | MEC | `NICHO-EDUCACAO.md` |
| Geral / Procon | Procon, CDC | `NICHO-GERAL-PROCON.md` |

## 4 modos

```bash
/compliance-imperatriz --checar [copy]
# analisa copy e identifica violações com severidade

/compliance-imperatriz --sugerir [copy]
# checa + sugere alternativas seguras + gera versão corrigida

/compliance-imperatriz --auditar [nome ou pasta]
# auditoria completa de TODO o material da mentorada + plano de remediação

/compliance-imperatriz --disclaimer [nicho]
# gera disclaimers prontos (curto, médio, longo) por nicho e formato
```

## 4 níveis de severidade

| Severidade | Quando | Prazo de ação |
|---|---|---|
| CRÍTICA | risco imediato de processo/multa/banimento | não publicar |
| ALTA | violação clara de norma setorial | corrigir em 24h |
| MÉDIA | zona cinza, vira ALTA com escala | corrigir em 7 dias |
| BAIXA | boa prática não cumprida | corrigir em 30 dias |

## Como instalar

```bash
# Pra a Tata (uso interno):
cp -r /Users/tamiresgoncalves/Documents/travessia-imperatriz-site/skills-novas/compliance-imperatriz ~/.claude/skills/

# Pra mentorada:
git clone <repo-quando-publicar> ~/.claude/skills/compliance-imperatriz
```

## Como usar

### Exemplo 1 — checar copy de saúde

```
/compliance-imperatriz --checar
nicho: saúde
copy:
"Tratamento revolucionário que cura ansiedade em 7 dias. Antes e depois reais.
100% garantido. Resultado milagroso comprovado por 500 alunas."
```

A skill devolve:

```
STATUS: NÃO PUBLICÁVEL
Violações: 5 críticas + 2 altas
- "cura" → banido (CFM/ANVISA)
- "milagroso" → banido (RDC ANVISA 96/2008)
- "100% garantido" → publicidade enganosa (CDC art. 37)
- "antes e depois" sem disclaimer → exige aviso "resultados variam"
- ausência de responsável técnico
```

### Exemplo 2 — gerar disclaimer pra finanças

```
/compliance-imperatriz --disclaimer
nicho: finanças
formato: VSL no YouTube
produto: curso pago de R$2.997 sobre estratégia de investimento
```

A skill devolve as 3 versões (curta, média, longa) prontas pra colar.

### Exemplo 3 — auditoria completa

```
/compliance-imperatriz --auditar
nome: Mentorada X
material:
- página de vendas: <URL>
- 5 anúncios ativos: [textos]
- 10 e-mails da sequência: [textos]
- 8 stories da semana: [transcrição]
```

A skill devolve mapa de risco + plano sprint 1/2/3.

## Integração com a Travessia

```
Pilar 5 (Governança):
  ├── compliance-imperatriz   ← VOCÊ ESTÁ AQUI
  └── crise-imperatriz        (quando compliance falha e vira crise)

Fluxo de copy:
briefing-copy-360 → mecanismo-unico → headline-imperatriz →
copywriting → bencivenga-method → COMPLIANCE-IMPERATRIZ →
voz-humana-br → analise-anuncio-1000
```

## Aviso importante

A skill **NÃO substitui consultoria jurídica**. É camada operacional de prevenção. Antes de lançamento grande ou mudança regulatória, consultar advogada especializada.

Cenário base: Brasil 2026. Regulação muda — sempre conferir a data do relatório.

---

**Método Imperatriz de Compliance — propriedade Tata Gonçalves.**
