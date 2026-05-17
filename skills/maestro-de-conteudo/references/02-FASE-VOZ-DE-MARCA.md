# Fase 2 — Voz de Marca (~45min)

## O que essa fase entrega

- `~/imperio/mentoradas/[nome]/03-voz-de-marca.json`

## O que o Maestro faz

### Antes de despachar

> **Fase 2 — Voz de Marca (~45min)**
>
> Essa é a fase mais importante de todas. Aqui a gente captura O JEITO ÚNICO de você escrever — palavras que você usa, expressões que são tuas, o que você nunca diria, como você abre e fecha. Tudo vira um arquivo que TODAS as próximas skills vão usar pra produzir copy que soa exatamente como você.
>
> Vou te entrevistar em 8 blocos: tom geral, palavras-âncora, palavras banidas, ritmo de frase, gírias autorizadas, abertura padrão, fechamento padrão, exemplos canônicos.
>
> **Importante**: essa fase exige presença. Não dá pra responder no automático. Se você tá cansada, melhor pausar e voltar amanhã.
>
> Bora?

### Despacha

Invoca `/voz-de-marca-builder --entrevista` via Skill tool:

> Mentorada nova começando a Travessia. Já capturou posicionamento na Fase 1 (lê de `~/imperio/mentoradas/[nome]/01-posicionamento.json` se quiser contexto). Roda o protocolo `--entrevista` completo dos 8 blocos. Salva em `~/imperio/mentoradas/[nome]/03-voz-de-marca.json`. Quando terminar, devolve controle ao Maestro.

### Quando termina

Maestro faz **3 checks**:

1. ✅ Arquivo `03-voz-de-marca.json` existe?
2. ✅ Tem campos: `tom_geral`, `palavras_ancora` (≥10), `palavras_banidas` (≥10), `ritmo_frase`, `abertura_padrao`, `fechamento_padrao`, `exemplos_canonicos`?
3. ✅ Mínimo 3 exemplos canônicos preenchidos?

Se passa, mostra:

```
✅ Fase 2 concluída — Voz de Marca capturada

Tua voz tem:
- Tom geral: [tom]
- N palavras-âncora capturadas
- N palavras banidas capturadas
- N exemplos canônicos

Esse JSON vai ser lido por TODAS as próximas skills automaticamente.

Vamos pra Fase 3 (Porta da Travessia)?
- Sim, agora
- Pausa
```

## Erros comuns nessa fase

| Sintoma | Reação do Maestro |
|---|---|
| Mentorada não tem 3 exemplos canônicos prontos | Sugere pausa: "Pausa aqui. Pega 3 textos teus que você acha que ficou MUITO 'a tua cara' (post, áudio transcrito, e-mail). Volta com eles." |
| Mentorada copia palavras-âncora de outra pessoa | Maestro avisa: "Essas palavras parecem do mercado, não tuas. Voltar pro bloco 2 e reescrever com TEU vocabulário?" |
| Mentorada não consegue listar palavras banidas | Sugere modo --auto: "A skill consegue extrair palavras banidas analisando teus textos. Quer rodar nesse modo?" |

## Não fazer

- ❌ Pular pra Fase 3 sem `03-voz-de-marca.json` salvo com mínimo de campos
- ❌ Editar manualmente o JSON
- ❌ Ditar palavras-âncora pra mentorada ("você usa 'soberana', né?")
- ❌ Aceitar entrevista incompleta como "ok suficiente"
