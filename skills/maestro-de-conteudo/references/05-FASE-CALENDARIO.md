# Fase 5 — Calendário 30 Dias (~30min)

## O que essa fase entrega

- `~/imperio/mentoradas/[nome]/05-calendario-30-dias.md`
- `~/Documents/Obsidian Vault/03 - Projetos/Pacote-Conteudo-[Nome]/calendario-30-dias-dashboard.html`

## O que o Maestro faz

### Antes de despachar

> **Fase 5 — Calendário 30 Dias (~30min — última!)**
>
> Última fase. Vou pegar tua linha editorial e gerar o calendário dos próximos 30 dias: 4 ideias macro × 5 adaptações por canal + 10 peças de engajamento = **30+ peças** distribuídas em IG Feed, IG Stories, IG Reels, LinkedIn, E-mail e WhatsApp Status, espaçadas 2-3 dias pra evitar canibalização.
>
> Importante: o calendário é o **plano**, não as peças prontas. Cada peça do calendário aparece com tema, formato, canal, dia, horário, intenção (TEAM) e link de qual skill produzir.
>
> Bora?

### Despacha

Invoca `/calendario-imperatriz --gerar`:

> Mentorada nova, primeira execução. Pré-requisito JÁ atendido pelo Maestro:
> - `~/imperio/mentoradas/[nome]/04-linha-editorial.json` ✓
>
> Roda o protocolo `--gerar` completo (30 dias). Cruza com lançamento atual (lê Porta de `02-porta-atual.json` — se Porta J/K/L/M/N, ativa modo lançamento). Sazonalidade do mês corrente considerada se aplicável. Salva em `~/imperio/mentoradas/[nome]/05-calendario-30-dias.md` + dashboard HTML em `~/Documents/Obsidian Vault/03 - Projetos/Pacote-Conteudo-[Nome]/calendario-30-dias-dashboard.html`. Devolve controle ao Maestro.

### Quando termina

Maestro faz **4 checks**:

1. ✅ `05-calendario-30-dias.md` existe?
2. ✅ Tem ≥30 peças listadas?
3. ✅ Distribui entre os canais ativos da linha editorial (não inventa canal)?
4. ✅ `calendario-30-dias-dashboard.html` foi salvo?

Se passa, Maestro chama o **Output Final** (próximo arquivo: `07-OUTPUT-FINAL.md`).

## Erros comuns

| Sintoma | Reação |
|---|---|
| Calendário sai com canais que a mentorada não opera | Falha da skill filha — Maestro pede regenerar lendo cadência da linha editorial |
| Calendário sai canibalizado (mesma peça 2 canais no mesmo dia) | Falha — pede regenerar |
| Mentorada acha calendário muito apertado | Maestro sugere `/calendario-imperatriz --auditar` em 30 dias pra recalibrar — não muda agora, deixa rodar |

## Não fazer

- ❌ Encerrar Fase 5 sem dashboard salvo
- ❌ Aceitar calendário com < 30 peças
- ❌ Aceitar calendário sem espaçamento (peças no mesmo dia em vários canais)
- ❌ Sugerir que mentorada já produza as peças nesse momento — produção é trabalho separado
