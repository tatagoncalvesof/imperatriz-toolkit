# RACI Imperatriz — Skill Proprietaria Tata Goncalves

Motor de execucao da **Travessia Imperatriz** — define quem faz cada skill em cada porta, quanto tempo demora e quanto custa.

Pilar 3 (Execucao) do sistema da Tata Goncalves. Nao decide ESTRATEGIA (isso e tatou-2.0). Decide **OPERACAO**: quem coloca a mao, quem aprova, quem opina, quem fica sabendo, em quanto tempo, por quanto.

---

## O QUE ELA FAZ

Recebe nome da mentorada + porta(s) e gera:

- **Matriz RACI customizada** — 1 R, 1 A, N C, N I por skill
- **Tempo estimado** — Iniciante x Avancada por porta + breakdown por skill
- **Custo estimado** — 3 cenarios (Mochila / Realista / Premium)
- **Cronograma** — timeline visual com dependencias e marcos
- **Alertas de gargalo** — sobrecarga da mentorada, custo > 30% faturamento, etc.
- **Plano de realocacao** — quando muda recursos (mais time, mais agente, menos orcamento)

---

## OS 5 ATORES

| Ator | O que faz | Quando aparece |
|------|-----------|----------------|
| **Mentorada** | Decisao estrategica + voz de marca + validacao final | Sempre como A em decisoes de oferta/preco/voz |
| **Time da mentorada** | Operacional humano com julgamento | A partir de 30k+/mes |
| **Agente IA** | Tarefa repetitiva, padronizavel, escalavel | Sempre — backbone de copy/conteudo |
| **Tata + time** | Suporte estrategico via mentoria | Como C em skills proprietarias |
| **Terceirizado** | Habilidade tecnica especializada | Quando custo/hora dela > custo terceiro |

---

## RACI — DEFINICOES

- **R = Responsavel** — coloca a mao na massa
- **A = Aprovador** — assina embaixo (sempre 1 unico)
- **C = Consultado** — opina ANTES (bidirecional)
- **I = Informado** — sabe DEPOIS (unidirecional)

Regra de ouro: 1 R principal + 1 A unico por skill. C e I podem ser 0, 1 ou varios.

---

## COMO USAR

### Modo padrao: gerar RACI de uma porta

```
/raci-imperatriz --gerar Tata J
```

Le o dossie da Tata, identifica skills da Porta J (Jornada de Copy), gera matriz RACI customizada + tempo + custo.

### Modo orcamento

```
/raci-imperatriz --orcamento Tata
```

Soma custos das proximas 3-6 portas no roadmap dela.

### Modo cronograma

```
/raci-imperatriz --cronograma Tata
```

Timeline visual das proximas portas com tempo + dependencias + marcos de validacao.

### Modo ajustar

```
/raci-imperatriz --ajustar Tata "contratei social media + R$ 5k extra/mes"
```

Recalcula tudo com os novos recursos. Mostra antes/depois e o que muda.

---

## EXEMPLO RAPIDO — Porta J (Jornada de Copy)

| Skill | R | A | C | I |
|-------|---|---|---|---|
| briefing-copy-360 | Mentorada | Mentorada | Tata | — |
| mecanismo-unico | Agente IA + Mentorada | Mentorada | Tata | Time |
| headline-imperatriz | Agente IA | Mentorada | — | Time |
| voz-humana-br | Agente IA | Time | — | Mentorada |
| design-page-builder | Designer freelancer | Mentorada | Time | Tata |
| skill-pagina-vendas | Designer + Mentorada | Mentorada | Tata | Time |
| bencivenga-method | Agente IA | Mentorada | Tata | — |

**Tempo:** 2 semanas (Iniciante) | 1 semana (Avancada)
**Custo realista:** R$ 2.500-3.000 one-shot + R$ 100/mes ferramentas

---

## ARQUIVOS DA SKILL

- `SKILL.md` — manifesto + processo + regras duras
- `README.md` — este arquivo
- `MATRIZES-RACI-26-PORTAS.md` — RACI base de todas as 26 portas A-Z
- `TEMPO-ESTIMADO-DETALHADO.md` — tabela completa Iniciante x Avancada
- `CUSTO-ESTIMADO-DETALHADO.md` — faixas de custo por porta + cenarios
- `EXEMPLOS-CASOS.md` — 3 casos completos (Iniciante / Intermediaria / Avancada)

---

## INTEGRACAO

Roda no fluxo completo da Travessia:

```
dossie-mentorada (perfil)
        ↓
tatou-2.0 (estrategia)
        ↓
raci-imperatriz (execucao)  ← AQUI
        ↓
execucao real
        ↓
reuniao-de-resultado (revisao)
```

---

## INSTALACAO PRA MENTORADA

1. Copiar pasta inteira `raci-imperatriz/` pra `~/.claude/skills/` da mentorada
2. Conferir que `dossie-mentorada` ja esta instalado (pre-requisito)
3. Rodar `/raci-imperatriz --gerar [nome] [porta]` na primeira porta dela

Pronto. Skill compartilhavel sem dependencia de servico externo.

---

**Metodo Imperatriz de Execucao — propriedade intelectual Tata Goncalves.**
