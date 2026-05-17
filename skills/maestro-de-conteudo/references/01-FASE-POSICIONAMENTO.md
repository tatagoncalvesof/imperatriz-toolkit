# Fase 1 — Posicionamento (~30min)

## O que essa fase entrega

- `~/imperio/mentoradas/[nome]/01-posicionamento.json`

## O que o Maestro faz

### Antes de despachar

Anuncia pra mentorada:

> **Fase 1 — Posicionamento (~30min)**
>
> Vou te perguntar 5 coisas: o que você ama fazer, o que você sabe fazer, qual nicho você ocupa, quem é o teu cliente perfeito e como você atrai ele.
>
> No fim dessa fase a gente vai ter UMA frase que diz exatamente o que você faz, pra quem e por quê. Essa frase vira a coluna vertebral de tudo que a gente vai construir depois.
>
> Posso começar?

Aguarda confirmação da mentorada (sim/agora/bora).

### Despacha

Invoca `/posicionamento-estrategico` via Skill tool, passando contexto mínimo:

> Mentorada nova começando a Travessia. Roda o protocolo completo dos 5 pilares (Paixões, Competências, Posicionamento e Nicho, Cliente Perfeito, Estratégia de Atração). Salva o output em `~/imperio/mentoradas/[nome-da-mentorada]/01-posicionamento.json`. Quando terminar, devolve controle ao Maestro de Conteúdo.

### Durante a execução da skill filha

Maestro fica em silêncio. Skill filha conduz a entrevista. Mentorada interage diretamente com a filha.

### Quando a skill filha termina

Maestro retoma o controle. Faz **3 checks**:

1. ✅ Arquivo `01-posicionamento.json` existe?
2. ✅ Tem campos: `nicho`, `cliente_ideal`, `transformacao_prometida`, `frase_posicionamento`, `estrategia_atracao`?
3. ✅ Frase de posicionamento está preenchida (não em branco)?

Se algum check falha, Maestro avisa e pede pra mentorada revisar:

> Faltou capturar [X] na Fase 1. Vamos rodar de novo a parte que ficou em aberto?

Se todos os checks passam, Maestro mostra:

```
✅ Fase 1 concluída — Posicionamento capturado

Tua frase de posicionamento:
"[frase capturada]"

Tudo certo? Vamos pra Fase 2 (Voz de Marca)?
- Sim, agora — bora pra Fase 2
- Pausa — eu volto mais tarde
```

Se a mentorada escolheu modo **maratona** no início, oferece pausa de 5min antes da Fase 2.
Se a mentorada escolheu modo **sessão por sessão**, espera ela combinar quando volta.

## Erros comuns nessa fase (e como o Maestro reage)

| Sintoma | Reação do Maestro |
|---|---|
| Mentorada não sabe responder pilar 4 (Cliente Perfeito) | Convida pausa: "Tudo bem não saber ainda. Pensa esse fim de semana e volta segunda. Cliente vago é raiz de problema depois — vale pensar com calma." |
| Frase de posicionamento sai genérica | Pede 1 reformulação: "Essa frase serviria pra muita mentora. Vamos especificar o nicho e a transformação?" |
| Skill filha não termina (mentorada desistiu no meio) | Salva progresso parcial, marca fase como `incompleta` no `_progresso.json`, fecha sessão sem culpar a mentorada |

## Não fazer

- ❌ Pular pra Fase 2 sem `01-posicionamento.json` salvo
- ❌ Editar manualmente o JSON pra "completar" o que faltou
- ❌ Sugerir frase de posicionamento ("que tal '...'?") — Maestro não escreve copy
- ❌ Apressar a mentorada se ela trava
