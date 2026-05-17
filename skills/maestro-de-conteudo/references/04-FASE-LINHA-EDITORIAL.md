# Fase 4 — Linha Editorial (~45min)

## O que essa fase entrega

- `~/imperio/mentoradas/[nome]/04-linha-editorial.json`
- `~/Documents/Obsidian Vault/03 - Projetos/Pacote-Conteudo-[Nome]/manifesto-editorial.md`
- `~/Documents/Obsidian Vault/03 - Projetos/Pacote-Conteudo-[Nome]/linha-editorial-dashboard.html`

## O que o Maestro faz

### Antes de despachar

> **Fase 4 — Linha Editorial (~45min)**
>
> Agora a mágica. Vou cruzar tudo que você me deu (posicionamento + voz + Porta) e construir a tua RÉGUA EDITORIAL — sobre o quê você posta, em que proporção, com que palavras, com quais limites.
>
> No fim você sai com:
> - 3 a 5 pilares temáticos com proporção declarada
> - Matriz TEAM (mix Teach/Engage/Authority/Monetize/Story)
> - Cadência por canal (frequência + horário + voz por canal)
> - Vocabulário ON/OFF (palavras-âncora e banidas)
> - Boundaries (mínimo 7 SIM e 7 NÃO)
> - **Manifesto editorial** (1 página A4 pra colar na parede)
> - **Dashboard HTML** interativo
>
> Vai ter UMA pausa de validação no meio (depois que eu propor os pilares). O resto eu rodo direto.
>
> Bora?

### Despacha

Invoca `/linha-editorial-imperatriz --gerar`:

> Mentorada nova, primeira execução. Pré-requisitos JÁ atendidos pelo Maestro:
> - `~/imperio/mentoradas/[nome]/01-posicionamento.json` ✓
> - `~/imperio/mentoradas/[nome]/03-voz-de-marca.json` ✓
> - `~/imperio/mentoradas/[nome]/02-porta-atual.json` ✓
>
> Roda o protocolo `--gerar` completo (10 etapas). Pausa obrigatória depois de propor pilares (etapa 3) — mentorada precisa aprovar antes de seguir. Ao terminar, exporta automaticamente em `--exportar` (JSON + manifesto + dashboard). Devolve controle ao Maestro.

### Quando termina

Maestro faz **5 checks**:

1. ✅ `04-linha-editorial.json` existe?
2. ✅ Tem 3-5 pilares (não menos, não mais)?
3. ✅ Soma das proporções dos pilares = 100%?
4. ✅ Vocabulário tem ≥30 palavras-âncora e ≥30 banidas?
5. ✅ Manifesto.md e dashboard.html foram salvos no Obsidian Vault?

Se passa:

```
✅ Fase 4 concluída — Linha Editorial completa

Você agora tem:
- N pilares temáticos
- Mix TEAM definido pra Porta [X]
- Cadência calibrada pra teus canais ativos
- N palavras-âncora + N banidas
- N boundaries SIM + N NÃO
- Manifesto editorial pronto

📁 Manifesto: ~/Documents/Obsidian Vault/03 - Projetos/Pacote-Conteudo-[Nome]/manifesto-editorial.md
📊 Dashboard: ~/Documents/Obsidian Vault/03 - Projetos/Pacote-Conteudo-[Nome]/linha-editorial-dashboard.html

Última fase agora — Calendário de 30 dias.
- Sim, bora pra Fase 5
- Pausa (quero respirar antes da última)
```

## Erros comuns

| Sintoma | Reação |
|---|---|
| `/linha-editorial-imperatriz` reclama de pré-requisito faltando | Erro de pipeline — Maestro NUNCA deveria deixar isso acontecer. Refaz a fase faltante (1, 2 ou 3). |
| Mentorada não aprova os pilares propostos | Skill filha pede ajustes — Maestro respeita, espera os pilares revisados saírem |
| Linha editorial sai com palavras banidas no próprio manifesto | Falha da skill filha. Maestro pede regenerar o manifesto. |

## Não fazer

- ❌ Pular pra Fase 5 sem dashboard.html gerado
- ❌ Editar manualmente os pilares
- ❌ Aceitar 2 pilares (mínimo 3) ou 6 pilares (máximo 5)
- ❌ Pular a pausa de validação dos pilares
