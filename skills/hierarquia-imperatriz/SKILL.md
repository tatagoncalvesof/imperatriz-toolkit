---
name: hierarquia-imperatriz
description: >
  Operadora do Pilar 7 (Tribo) da Travessia Imperatriz — gerencia os 6 niveis
  hierarquicos da Corte (Aspirante, Princesa, Duquesa, Marquesa, Condessa,
  Imperatriz Plena) + 5 ritos de passagem (Investidura da Princesa, da Duquesa,
  da Marquesa, da Condessa e Coroacao Imperial). Le dossie-mentorada (perfis
  15-nivel + 14-progresso), audita criterios objetivos de subida, prepara
  cerimonia de investidura, lista mentoradas por nivel, identifica quem esta
  pronta pra subir e prepara coroacoes anuais. Aplica matriz de direitos +
  deveres por nivel. Salva mudanca em 15-nivel.json com versao. Cinco modos:
  --status, --investidura, --listar, --prontas, --coroar. Pilar 7 (Tribo) da
  Travessia Imperatriz Tata Goncalves. Use quando aparecer "qual nivel da
  fulana", "ela esta pronta pra subir?", "preparar investidura", "quem virou
  Princesa esse mes", "lista de Duquesas", "preparar Coroacao Imperial",
  "rito de passagem", "matriz de direitos", "deveres da Marquesa",
  "distribuicao da Corte", "piramide saudavel". Integra com dossie-mentorada
  (input), tatou-2.0 (gatilho de gate), gates-imperatriz (validacao porta) e
  dashboard-imperatriz (metricas).
---

# Hierarquia Imperatriz — Pilar 7 (Tribo) da Travessia Imperatriz

Esta skill e a **operadora dos 6 niveis hierarquicos da Corte e dos 5 ritos de passagem**. Sem hierarquia visivel, comunidade nao existe — vira lista de e-mail. Mentoradas precisam **se reconhecer pelo nivel** e ter **caminho claro** pra subir.

## Filosofia central

> **Marca sem ritual e logo. Marca com ritual e cultura.**

A Travessia nao termina quando a mentorada compra. Ela COMECA. E o que diferencia uma comunidade real de um grupo de WhatsApp e a presenca de **rituais de passagem com criterios objetivos, cerimonia simbolica e mudanca de status publica**.

A Corte da Imperatriz funciona assim:

1. Toda mentorada entra como **Aspirante** (nao importa quanto pagou)
2. Sobe de nivel **so com criterio objetivo cumprido** (nao tempo, nao dinheiro)
3. Cada subida tem **rito de passagem** com cerimonia, simbolo e comunicacao publica
4. Cada nivel tem **direitos crescentes** (acesso, calls, presenca da Tata)
5. Cada nivel tem **deveres crescentes** (mentorar quem esta abaixo, treinar a proxima geracao)
6. **Imperatriz Plena** e socia formal, nao aluna

Quem nao quer subir, nao sobe. Quem nao cumpre criterio, nao sobe. **Nao existe atalho. Nao existe favoritismo. Existe metodo.**

## Quando usar

- Tata pergunta "qual nivel da fulana?"
- Mentorada cumpriu criterio e precisa de rito de passagem
- Hora da Coroacao anual (evento maximo da Corte)
- Auditoria mensal: quem esta pronta pra subir?
- Comunicacao publica do novo nivel (anuncio na comunidade)
- Resposta a "quero subir, o que falta?"
- Antes de evento presencial — confirmar quem ja e Marquesa+
- Apos lancamento — quem virou Princesa nesse ciclo?

## Regra critica: nivel nao se compra, se conquista

Tata pode aceitar pagamento high-ticket (R$50k+), mas a mentorada **entra como Aspirante igual todo mundo**. Subida e por **criterio objetivo de execucao**, nao por valor pago. Isso protege a marca e a justica interna da Corte.

---

## OS 6 NIVEIS — VISAO RAPIDA

| Nivel | Emoji | Cor | Coroa | Tempo medio | Distribuicao saudavel |
|-------|-------|-----|-------|-------------|------------------------|
| 1. Aspirante | 🌱 | Verde claro + botao de rosa | (sem coroa) | 60-90 dias | 30-40% |
| 2. Princesa | 👸 | Rosa perola | 3 pontas | 6-9 meses | 25-30% |
| 3. Duquesa | 🦄 | Roxo realeza | 5 pontas | 6-12 meses | 15-20% |
| 4. Marquesa | 💎 | Azul zafira | 7 pontas | 12-18 meses | 8-12% |
| 5. Condessa | 🌟 | Dourado real | 9 pontas + pedras | 12-24 meses | 3-5% |
| 6. Imperatriz Plena | 👑 | Purpura imperial | Coroa imperial completa | (vitalicio) | 1-2% |

Detalhamento completo em `OS-6-NIVEIS-DETALHADO.md`.

---

## MODOS DE OPERACAO

A skill roda em 5 modos declaraveis:

- **`/hierarquia-imperatriz --status [nome]`** — qual nivel atual + criterios pendentes pra proximo
- **`/hierarquia-imperatriz --investidura [nome]`** — preparar rito de passagem
- **`/hierarquia-imperatriz --listar [nivel]`** — todas mentoradas em determinado nivel
- **`/hierarquia-imperatriz --prontas`** — quem esta pronta pra subir agora
- **`/hierarquia-imperatriz --coroar [nome]`** — preparar Coroacao Imperial anual

Se a Tata nao declarar modo, perguntar **"e status, investidura, listar, prontas ou coroar?"**.

---

## PROCESSO POR MODO

### MODO `--status [nome]`

1. Le `dossie-mentorada` perfis **15-nivel** + **14-progresso** da mentorada citada
2. Confirma nivel atual (1-6)
3. Lista os **criterios objetivos** do proximo nivel
4. Marca cada criterio: **[X] cumprido / [ ] pendente / [~] em andamento**
5. Estima **tempo estimado** pra completar pendentes (com base em ritmo historico)
6. Identifica **bloqueio principal** (qual criterio esta segurando?)
7. Sugere **proxima acao concreta** pra desbloquear
8. Output: status card de 1 pagina

**Output do --status:**

```
# STATUS — [Nome da Mentorada]

## Nivel atual: [Nivel] [Emoji]
- Tempo no nivel: [X meses]
- Direitos ativos: [lista resumida]
- Deveres em aberto: [lista]

## Proximo nivel: [Nivel +1] [Emoji]

### Criterios objetivos (X de Y cumpridos)
- [X] [criterio 1] — cumprido em [data]
- [ ] [criterio 2] — PENDENTE — [estimativa]
- [~] [criterio 3] — em andamento — [% completo]

### Bloqueio principal
[Qual criterio esta segurando + por que]

### Proxima acao recomendada
[Acao concreta com prazo]

### Estimativa de subida
[Pessimista / Realista / Otimista] — [X semanas/meses]
```

---

### MODO `--investidura [nome]`

Quando mentorada cumpriu **todos** os criterios de subida, prepara o **rito de passagem**.

1. Confirma nivel-de + nivel-pra
2. Identifica qual rito aplicar (5 opcoes — ver `OS-5-RITOS.md`)
3. Gera **roteiro da cerimonia** (preparacao + ato + comunicacao)
4. Gera **comunicacao publica** (anuncio Stories + grupo + email)
5. Gera **kit de boas-vindas** do novo nivel (simbolo + acesso + onboarding)
6. Gera **briefing pra Tata** (o que falar na cerimonia, o que entregar)
7. Atualiza `15-nivel.json` da mentorada com versao + data + Tata como autorizadora
8. Notifica **dashboard-imperatriz** (metrica de subida)
9. Notifica **tatou-2.0** (handoff de jornada — proxima porta a destravar)

**Output do --investidura:**

```
# INVESTIDURA — [Nome] — [Nivel-de] → [Nivel-pra]

## RITO APLICAVEL
[Investidura da Princesa / Duquesa / Marquesa / Condessa / Coroacao]

## CRITERIOS CONFIRMADOS
- [X] [criterio 1] — evidencia: [link/print]
- [X] [criterio 2] — evidencia: [link/print]
- [X] [criterio 3] — evidencia: [link/print]

## CERIMONIA — [tipo: call mensal / imersao / presencial / evento aberto / anual]
- **Data sugerida:** [proxima ocorrencia]
- **Local/canal:** [Zoom / sala fisica / palco]
- **Duracao do rito:** [X minutos]

### Preparacao (T-7 dias)
1. [acao]
2. [acao]
3. [acao]

### Roteiro do ato (script da Tata)
**Abertura (2 min):**
"[falas literais]"

**Reconhecimento (3 min):**
"[falas + leitura dos criterios cumpridos]"

**Investidura simbolica (2 min):**
"[gesto + entrega do simbolo: coroa/colar/cetro]"

**Encerramento (1 min):**
"[falas + abracos + foto]"

### Comunicacao publica (T+0 a T+3)
- **Story Tata (T+0):** [copy pronto]
- **Anuncio comunidade (T+0):** [copy pronto]
- **Email base (T+1):** [copy pronto]
- **Post feed (T+2):** [copy pronto]

### Kit de boas-vindas do novo nivel
- Simbolo fisico: [item — coroa/colar/cetro/anel]
- Acesso liberado: [grupo/canal/dashboard]
- Onboarding: [doc + call de orientacao]
- Atualizacao no perfil: [novo emoji + cor + titulo]

## ATUALIZACAO NO DOSSIE
- 15-nivel.json — versao [Vx → Vx+1]
- Data: [YYYY-MM-DD]
- Autorizadora: Tata Goncalves
- Evidencia arquivada: [path]

## HANDOFF
- tatou-2.0: notificar nova porta destravada
- dashboard-imperatriz: incrementar contador
- gates-imperatriz: revalidar dependencias
```

---

### MODO `--listar [nivel]`

Lista todas mentoradas de determinado nivel.

1. Filtra dossies por `15-nivel.atual = [nivel]`
2. Ordena por **tempo no nivel** (mais antiga primeiro)
3. Marca quem esta **proxima de subir** (3+ criterios cumpridos)
4. Marca quem esta **estagnada** (>120% do tempo medio)
5. Output: tabela + sinalizadores

**Output:**

```
# CORTE — [Nivel] [Emoji]

Total: [N] mentoradas
Distribuicao saudavel: [%] (atual: [%])
Status: [equilibrado / inflando / minguando]

## Lista
| Nome | Tempo no nivel | Criterios pra subir | Sinal |
|------|---------------|---------------------|-------|
| [nome] | [X meses] | [Y/Z] | 🟢 pronta |
| [nome] | [X meses] | [Y/Z] | 🟡 caminhando |
| [nome] | [X meses] | [Y/Z] | 🔴 estagnada |

## Acoes recomendadas
- [N] mentoradas prontas pra investidura — agendar rito
- [N] mentoradas estagnadas — acionar /tatou-2.0 ou 1:1
```

---

### MODO `--prontas`

Auditoria global da Corte — quem cumpriu **todos** criterios e esta pronta pra subir.

1. Varre todos dossies
2. Filtra por **criterios 100% cumpridos** mas **nivel ainda nao atualizado**
3. Agrupa por rito de passagem aplicavel
4. Sugere **calendario de investiduras** dos proximos 30-90 dias
5. Sinaliza casos urgentes (cumprido ha >30 dias sem rito)

**Output:**

```
# PRONTAS PRA SUBIR — Corte da Imperatriz

Total prontas: [N]
Atrasadas (>30d sem rito): [N] 🚨

## Por rito

### Investidura da Princesa (proxima call mensal)
- [nome] — pronta ha [X dias]
- [nome] — pronta ha [X dias]

### Investidura da Duquesa (proxima imersao trimestral)
- [nome] — pronta ha [X dias]

### Investidura da Marquesa (proximo encontro presencial)
- [nome] — pronta ha [X dias]

### Investidura da Condessa (proximo evento aberto)
- [nome] — pronta ha [X dias]

### Coroacao Imperial (evento anual)
- [nome] — pronta ha [X dias]

## Calendario sugerido
- [data] — [tipo de cerimonia] — [N candidatas]
- [data] — [tipo de cerimonia] — [N candidatas]
```

---

### MODO `--coroar [nome]`

Cerimonia maxima da Corte — Condessa → Imperatriz Plena.

E **diferente** das outras investiduras:

- E uma vez por ano, em evento anual
- A mentorada vira **socia formal** (% receita ou white label ou royalty)
- Tem **contrato societario** assinado, nao so simbolico
- Cerimonia tem **publico amplo** (toda comunidade convidada)
- E **vitalicia** (so sai por escolha propria)

Processo:

1. Confirma todos criterios de Condessa cumpridos
2. **Adiciona criterios extras de Imperatriz**: imperio autonomo + sucessao definida
3. Prepara **contrato societario** (briefing pro juridico)
4. Define **modelo de socia** (% receita / white label / royalty / advisory)
5. Roteiro da Coroacao (cerimonia mais longa, ~30 min)
6. Comunicacao **maxima**: video institucional + matetia em midia + post na imprensa
7. Atualiza dossie + dashboard + lista publica de Imperatrizes Plenas

Detalhe completo em `OS-5-RITOS.md` (rito #5).

---

## INTEGRACAO COM O ECOSSISTEMA

### Inputs (le de)

- **`dossie-mentorada`** — perfil **15-nivel** (nivel atual + historico) + perfil **14-progresso** (criterios cumpridos)
- **`gates-imperatriz`** — confirma quais portas A-Z foram destravadas
- **`tatou-2.0`** — gatilho automatico quando mentorada atinge gate critico
- **`dashboard-imperatriz`** — historico de eventos, calls, vendas

### Outputs (escreve em)

- **`15-nivel.json`** — atualiza nivel + data + autorizadora + versao
- **`dashboard-imperatriz`** — metrica de subida + distribuicao da Corte
- **Comunicacao**: Stories + grupo + email + feed (gera copy pronto)
- **Kit fisico**: lista de envio (coroa/colar/cetro do novo nivel)

### Skills adjacentes (nao canibalizar)

- `/dossie-mentorada` — fonte de verdade do perfil completo
- `/perfil-mentorada` — perfil resumido publico
- `/calendario-imperatriz` — agenda quando Tata fara as cerimonias
- `/tatou-2.0` — operadora geral da jornada (puxa hierarquia-imperatriz quando gate atinge)

---

## REGRAS DURAS (a skill NAO negocia)

1. **Nao sobe ninguem sem criterio objetivo cumprido** — nao importa relacao com a Tata
2. **Nao pula nivel** — Aspirante nao vira Duquesa direto, nem Marquesa vira Imperatriz
3. **Nao baixa nivel publicamente** — se mentorada regredir, conversa privada
4. **Nao sobe sem rito de passagem** — subida silenciosa nao existe na Corte
5. **Nao distribui simbolo (coroa/colar) antes da cerimonia** — simbolo sem ritual e merchandising
6. **Nao anuncia subida sem evidencia arquivada** — print, link ou caso documentado
7. **Nao confunde tempo com merito** — 5 anos de Aspirante nao vira Princesa por antiguidade
8. **Sempre versiona mudanca** em 15-nivel.json (V1 → V2 com data + autorizadora)
9. **Sempre notifica** dashboard-imperatriz e tatou-2.0 apos subida
10. **Sempre arquiva** evidencia (1a venda, primeiro funil 30d autonomo, mencao midia, etc)
11. **Imperatriz Plena exige contrato societario** — simbolico nao basta
12. **Coroacao e anual** — nao acontece em call mensal

---

## ARQUIVOS DE REFERENCIA (carregar sob demanda)

- `OS-6-NIVEIS-DETALHADO.md` — cada nivel com criterios, simbolos, direitos, deveres, tempo medio
- `OS-5-RITOS.md` — cada rito de passagem (preparacao, cerimonia, comunicacao)
- `DIREITOS-DEVERES.md` — matriz completa por nivel
- `DISTRIBUICAO-ESPERADA.md` — piramide saudavel + sinais de desbalanceamento
- `EXEMPLOS-INVESTIDURAS.md` — 3 casos reais (Aspirante→Princesa, Duquesa→Marquesa, Condessa→Imperatriz)

---

## FILOSOFIA OPERACIONAL

> **A coroa nao e premio. E responsabilidade.**

Cada subida na Corte aumenta:
- Acesso (mais Tata, mais comunidade)
- Visibilidade (mais palco, mais autoridade)
- **Dever** (mais responsabilidade pelas que estao abaixo)

Imperatriz Plena nao manda. Imperatriz Plena **sustenta a Corte**. Por isso so 1-2% chega la — e por isso a cerimonia de Coroacao e anual e publica.

---

## VERSIONAMENTO

- **v1.0** (atual) — 6 niveis, 5 ritos, 5 modos, integracao Travessia
- **v1.5** (planejado) — automacao de criterios via dashboard-imperatriz
- **v2.0** (planejado) — Corte distribuida (mentoradas em paises diferentes)
- **v3.0** (planejado) — sucessao de Imperatriz Plena (modelo de saida)

---

## COMO COMPARTILHAR COM TIME DA TATA

Skill PRIVADA — uso interno Tata + time RH/Comunidade. NAO compartilhar com mentoradas (elas sao objeto da skill, nao operadoras).

Pasta: `/Users/tamiresgoncalves/Documents/travessia-imperatriz-site/skills-novas/hierarquia-imperatriz/`

---

**Pilar 7 (Tribo) da Travessia Imperatriz — propriedade intelectual Tata Goncalves.**
