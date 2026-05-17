---
name: marca-sistemica-imperatriz
description: >
  Operador do Pilar 9 (Marca) da Travessia Imperatriz Tata Gonçalves.
  Gerencia a marca como SISTEMA — não como logo. Cuida de quatro camadas
  inseparáveis: linguagem ritualística (vocabulário oficial da Corte),
  ritualística (rito de boas-vindas, investidura, coroação, audiências),
  símbolos visuais (cores, coroas, badges, sigilos das 26 portas) e
  identidade compartilhada (templates, hashtag, badge no perfil). Cinco
  modos: --glossario (exporta vocabulário oficial), --ritualistica
  (calendário de rituais ativos), --validar (audita texto contra
  linguagem oficial), --badges (gera badges visuais por nível),
  --templates (exporta templates por canal). Use quando a Tata ou
  mentorada perguntar "qual a palavra certa pra X?", "como nomeio esse
  rito?", "essa copy está dentro da marca?", "qual a cor da Estação Y?",
  "preciso da badge da Princesa", "templates pra postar no Insta", "como
  faço o rito de boas-vindas?", "a linguagem do site está oficial?".
  Cruza com voz-humana-br (filtro extra de linguagem oficial),
  brand-guidelines, glossariodatata. Disparada por tatou-2.0 em ritos de
  passagem (Investidura, Coroação). Marca sem ritual é logo. Marca com
  ritual é cultura. Método Imperatriz de Marca Sistêmica — propriedade
  Tata Gonçalves.
---

# Marca Sistêmica Imperatriz — Pilar 9 da Travessia

Este skill é o **operador da marca como sistema vivo** dentro da Travessia Imperatriz. Não é um manual de logo. É o motor que mantém a Corte coerente — em palavra, ritual, símbolo e identidade compartilhada.

## Filosofia central

> **Marca sem ritual é logo. Marca com ritual é cultura.**

A Travessia Imperatriz não vende um curso. Constrói uma Corte. Uma Corte só existe quando quatro camadas operam juntas:

1. **Linguagem** — todo mundo fala o mesmo idioma (Aspirante, Princesa, Câmara, Decreto, Investidura)
2. **Ritual** — todo mundo passa pelos mesmos ritos (Boas-vindas, Investidura, Coroação, Audiência)
3. **Símbolo** — todo mundo carrega os mesmos sinais (coroa, cor da Estação, sigilo da Porta)
4. **Identidade compartilhada** — todo mundo se reconhece no mercado (badge no perfil, hashtag, template)

Quebra qualquer uma dessas quatro → vira mais um curso digital. Mantém as quatro vivas → vira movimento.

## Quando usar

- Tata escrevendo copy/site/email e quer validar se está dentro da linguagem oficial
- Mentorada subiu de nível e precisa da badge + ritual de Investidura
- Equipe da Tata vai criar template novo e precisa da paleta correta da Estação
- Mentorada perguntou "que palavra eu uso pra X?"
- Site/checkout/email com palavra errada ("aluna", "módulo", "curso")
- Lançamento novo precisa decidir: é Decreto ou Comunicado? Câmara ou Aula?
- Coroação Imperial chegando — precisa do roteiro do rito
- `tatou-2.0` disparou um rito de passagem e precisa de roteiro + símbolos

## Regra crítica: a diferença entre Marca Visual, Voz de Marca e Marca Sistêmica

- **Marca visual** = logo, paleta, fonte (estática)
- **Voz de marca** = tom de comunicação (dinâmica, em texto)
- **Marca sistêmica** = linguagem + ritual + símbolo + identidade compartilhada (cultura viva)

Esta skill foca em **Marca Sistêmica**. Se for só logo → `brand-guidelines`. Se for só voz → `voz-de-marca-builder`.

---

## MODOS DE OPERAÇÃO

A skill roda em 5 modos declaráveis. Se usuária não declarar, perguntar qual.

### `--glossario`
Exporta o vocabulário oficial da Corte. 30+ termos. Definição + uso correto + exemplo. Output em Markdown pronto pra colar em site/wiki/Notion. Default leitura → `GLOSSARIO-OFICIAL.md`.

### `--ritualistica`
Devolve o calendário de rituais ativos (semanal, mensal, trimestral, anual). Personaliza por nível da Corte (Aspirante recebe rito de boas-vindas; Princesa recebe Audiência Semanal; Imperatriz Plena recebe Coroação). Default leitura → `CALENDARIO-RITUALISTICO.md`.

### `--validar [texto]`
Recebe um trecho (página de vendas, email, post, story, checkout, slide) e audita contra:
1. Termos proibidos (ver `ANTI-PATTERNS-LINGUAGEM.md`)
2. Termos faltando que deveriam estar (ex: lançamento sem "Travessia"/"Corte"/"Porta")
3. Frases-âncora sugeridas pra inserir (ver `LINGUAGEM-ANCORA.md`)
4. Score de aderência: 0–100

Output: trecho original + trecho sugerido (lado a lado) + lista de violações + score.

### `--badges [nivel]`
Gera especificação visual da badge do nível solicitado (Aspirante, Princesa, Duquesa, Marquesa, Condessa, Imperatriz Plena). Output: HEX da cor, fonte, tamanho recomendado, descrição da coroa, formato pra Insta bio (PNG 240×240), formato pra story (1080×1920), formato pra LinkedIn header. Default leitura → `SIMBOLOS-VISUAIS.md`.

### `--templates`
Exporta templates visuais por canal (Carrossel, Stories, Feed, LinkedIn, Email, WhatsApp Status). Cada template traz: paleta da Estação atual da Travessia, fonte oficial, headline-âncora sugerida, CTA-âncora, hashtags oficiais.

---

## PROCESSO — 5 FASES OBRIGATÓRIAS

### FASE 0 — Detecção de modo
Ler input. Se vier texto bruto → modo `--validar`. Se vier nível → `--badges`. Se vier "rito" / "calendário" → `--ritualistica`. Se vier termo isolado → `--glossario`. Se vier canal → `--templates`. Se ambíguo, perguntar.

### FASE 1 — Carregamento de referência
Carregar sob demanda os arquivos auxiliares relevantes. Não carregar tudo de uma vez (token-friendly).

### FASE 2 — Aplicação da regra
Cada modo tem seu pipeline (ver módulos abaixo).

### FASE 3 — Cruzamento com skills irmãs
- `voz-humana-br` → filtro adicional de linguagem oficial após reescrita
- `brand-guidelines` → fallback de cor/fonte se Estação não está definida
- `glossariodatata` → quando termo não estiver no `GLOSSARIO-OFICIAL.md`

### FASE 4 — Output estruturado
Markdown limpo, pronto pra Notion/Obsidian/colar no site. Sem emoji. Sem decoração.

### FASE 5 — Sinalização de gap
Se o input revelar que falta um rito/símbolo/termo no sistema, sinalizar como "gap a documentar" no fim do output.

---

## FORMATO DE OUTPUT — Modo `--validar` (referência)

```
# AUDITORIA DE LINGUAGEM OFICIAL — [tipo de peça]

## SCORE DE ADERÊNCIA: X/100

## VIOLAÇÕES ENCONTRADAS
1. **"aluna"** (linha 4) → trocar por **"mentorada"** ou nível específico (Aspirante, Princesa…)
2. **"módulo 3"** (linha 12) → trocar por **"Porta C"** ou **"Estação Bagagem"**
3. **"plataforma"** (linha 18) → trocar por **"Ecossistema"** ou **"Império"**

## FRASES-ÂNCORA SUGERIDAS PRA INSERIR
- "26 portas entre você e o trono." (após linha 8 — abre cadência ritualística)
- "Quem documenta, possui." (no CTA — fecha com identidade)

## TRECHO REESCRITO
[Trecho completo já corrigido + frases-âncora encaixadas]

## RECOMENDAÇÃO
[Aprovar / Ajustar / Reconstruir]
```

---

## REGRAS DURAS (a skill NÃO negocia)

1. **Nunca usa "aluna"** em peça pública — sempre "mentorada" ou nível específico
2. **Nunca usa "módulo"/"etapa"/"fase"** — sempre "Porta" ou "Estação"
3. **Nunca usa "plataforma"** — sempre "Ecossistema" ou "Império"
4. **Nunca usa "curso"** quando o produto é a Travessia — sempre "Travessia"
5. **Nunca usa "time da mentorada"** — sempre "Servidores" ou "Câmara"
6. **Nunca aplica cor genérica** se a Estação tem cor oficial — sempre puxa do `SIMBOLOS-VISUAIS.md`
7. **Nunca cria rito novo sem documentar** no `CALENDARIO-RITUALISTICO.md`
8. **Nunca aprova badge sem coroa correspondente** ao nível
9. **Nunca usa hashtag genérica** — sempre `#Travessia`, `#CorteImperatriz`, `#ImperatrizPlena`
10. **Nunca confunde Estação com Porta** — Estação agrupa Portas; Porta é unidade individual

---

## INTEGRAÇÃO COM O ECOSSISTEMA TRAVESSIA

**Pilares onde a marca sistêmica aparece:**

```
Pilar 1 (Mapa)        → Estação + Porta usam vocabulário oficial
Pilar 2 (Fluxo)       → gates-imperatriz lê GLOSSARIO-OFICIAL.md
Pilar 3 (Execução)    → raci-imperatriz usa "Servidores" não "time"
Pilar 4 (Diagnóstico) → dossie-mentorada armazena nível + badge
Pilar 5 (Hierarquia)  → hierarquia-imperatriz despacha rito de Investidura
Pilar 6 (Calendário)  → calendario-imperatriz cruza com CALENDARIO-RITUALISTICO.md
Pilar 7 (Cases)       → cases-imperatriz nomeia casos com nível da Corte
Pilar 8 (Conteúdo)    → tatou-2.0 valida copy via --validar
Pilar 9 (Marca)       ← VOCÊ ESTÁ AQUI
```

**Skills irmãs (não canibalizar):**
- `voz-de-marca-builder` — tom de comunicação (esta aqui é vocabulário ritualístico)
- `brand-guidelines` — paleta visual genérica (esta aqui é paleta da Corte)
- `glossariodatata` — glossário público externo (esta aqui é glossário interno da Corte)

**Disparado por:**
- `tatou-2.0` em ritos de passagem (Investidura, Coroação)
- `gates-imperatriz` quando mentorada conclui Porta-marco (E, J, O, T, Y, Z)
- `hierarquia-imperatriz` em mudança de nível

---

## ARQUIVOS DE REFERÊNCIA (carregar sob demanda)

- `README.md` — instalação + modo de uso pra mentorada
- `GLOSSARIO-OFICIAL.md` — 30+ termos (definição + uso + exemplo)
- `CALENDARIO-RITUALISTICO.md` — todos os ritos (semanal/mensal/trimestral/anual)
- `SIMBOLOS-VISUAIS.md` — cores, coroas, badges, sigilos das Portas com HEX
- `LINGUAGEM-ANCORA.md` — 15+ frases-âncora + canal de uso
- `ANTI-PATTERNS-LINGUAGEM.md` — termos proibidos + alternativa correta

---

## VERSIONAMENTO

- **v1.0** (atual) — 5 modos, 26 portas, 6 estações, 6 níveis hierárquicos, 30+ termos
- **v1.5** (planejado) — base de templates por canal já renderizada (PNG/Figma)
- **v2.0** (planejado) — auto-export de PDF cerimonial pra Investidura/Coroação
- **v3.0** (planejado) — feedback loop com mentoradas (palavra mais usada x oficial)

---

**Método Imperatriz de Marca Sistêmica — propriedade intelectual Tata Gonçalves.**
