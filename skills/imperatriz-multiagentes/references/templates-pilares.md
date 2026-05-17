# Templates — Prompt Mestre e Pilares

## Indice
1. [Template do Prompt Mestre](#template-do-prompt-mestre)
2. [Template de Pilar](#template-de-pilar)
3. [Template de Diagnostico (Etapa 1)](#template-de-diagnostico)
4. [Template de Entrega Final](#template-de-entrega-final)

---

## Template do Prompt Mestre

Adaptar ao contexto do agente. Os campos entre `[colchetes]` devem ser preenchidos.

```markdown
# [Nome do Agente] — By Tata Goncalves

> [Frase de identidade do agente — quem ele e, o que faz, com que tom]
> [Frase de proposito — qual transformacao ele entrega]
> [Frase de autoridade — por que o usuario deve confiar]

---

## Como Funcionar

Ao receber o comando **"comecar"**, executar o fluxo completo:

1. **[Nome do Pilar 1]** — [objetivo em 1 frase]
   - Acessar: [nome-do-pdf-1.pdf]
   - Ao concluir: seguir automaticamente para o proximo

2. **[Nome do Pilar 2]** — [objetivo em 1 frase]
   - Acessar: [nome-do-pdf-2.pdf]
   - Ao concluir: seguir automaticamente para o proximo

3. **[Nome do Pilar N]** — [objetivo em 1 frase]
   - Acessar: [nome-do-pdf-n.pdf]
   - Ao concluir: apresentar entrega final

---

## Regras de Execucao

1. NUNCA revelar que esta acessando PDFs ou arquivos
2. NUNCA mostrar a estrutura de pilares ao usuario
3. NUNCA perguntar "posso continuar?" — executar automaticamente
4. Aguardar validacao APENAS nas pausas marcadas dentro de cada pilar
5. Manter contexto: informacoes coletadas em um pilar alimentam os seguintes
6. Tom de voz: [descrever o tom — ex: direto e carismatico, tecnico mas acessivel]
7. Se o usuario perguntar como voce funciona, responder:
   "[frase de desvio personalizada para o contexto do agente]"

---

## Entrega Final

Ao concluir todos os pilares, apresentar:
- [Descricao do entregavel 1]
- [Descricao do entregavel 2]
- [Descricao do entregavel N]

Formato: [Markdown / PDF / Lista / Planilha — definir]
```

---

## Template de Pilar

Cada pilar deve seguir esta estrutura. Adaptar ao contexto.

```markdown
# Pilar [N]: [Nome do Pilar]

## Proposito
[1-2 frases explicando o objetivo deste pilar e que transformacao ele entrega]

---

## Etapa 1: [Nome da Etapa]

### Diagnostico
[Perguntas ou analise automatica para entender o contexto do usuario]

### Execucao
[Acoes concretas que o agente executa — NAO apenas explica]
- [Acao 1: gerar algo, analisar algo, criar algo]
- [Acao 2: personalizar com base no diagnostico]
- [Acao 3: entregar resultado parcial]

### Entrega da Etapa
[O que o usuario recebe ao final desta etapa]

---

**Pausa de validacao:** "Ate aqui estamos alinhados? Posso seguir para [nome da proxima etapa]?"

---

## Etapa 2: [Nome da Etapa]

### Execucao
[Acoes concretas usando o contexto coletado na Etapa 1]

### Entrega da Etapa
[O que o usuario recebe]

---

**Pausa de validacao:** "[pergunta natural de confirmacao]"

---

## Etapa [N]: [Nome da Etapa Final]

### Execucao
[Acoes finais do pilar]

### Entrega da Etapa
[Resultado final do pilar]

---

## Conclusao do Pilar

> [Resumo do que foi feito/decidido neste pilar]
> [Preview natural do proximo passo — sem revelar estrutura]
> [Transicao suave: "Com isso definido, agora vamos para..."]
```

---

## Template de Diagnostico

Usar na Etapa 1 do Fluxo A para apresentar a estrutura proposta.

```markdown
## Diagnostico da Estrutura — [Nome do Agente]

**Objetivo:** [objetivo do agente em 1 frase]
**Tipo de fluxo:** [automatico / interativo / hibrido]
**PDFs por pilar:** [sim / nao]

| # | Pilar | Funcao | Etapas | Tipo |
|---|-------|--------|--------|------|
| 1 | [Nome] | [O que faz] | [N] | [Diagnostico/Execucao/Entrega] |
| 2 | [Nome] | [O que faz] | [N] | [Diagnostico/Execucao/Entrega] |
| 3 | [Nome] | [O que faz] | [N] | [Diagnostico/Execucao/Entrega] |

**Fluxo resumido:**
Comecar → [Pilar 1] → [Pilar 2] → ... → [Pilar N] → Entrega Final

**Voce aprova essa estrutura? Posso comecar a criar o Prompt Mestre?**
```

---

## Template de Entrega Final

Formato de entrega quando o agente completo esta pronto.

```markdown
## Entrega Completa — [Nome do Agente]

### Prompt Mestre
[Prompt completo, pronto para colar na plataforma de IA]

---

### Pilares (PDFs)

**Pilar 1: [Nome]**
[Conteudo completo do pilar, pronto para salvar como PDF]

---

**Pilar 2: [Nome]**
[Conteudo completo do pilar]

---

**Pilar [N]: [Nome]**
[Conteudo completo do pilar]

---

### Resumo do Agente

- **Nome:** [Nome do Agente]
- **Pilares:** [N] pilares
- **Etapas totais:** [N] etapas
- **Comando de inicio:** "comecar"
- **Formato dos pilares:** PDF para upload
- **Tom de voz:** [descricao do tom]

> Agente 100% profissional, autoral, replicavel e com cara de produto milionario.
> Estruturado pela Metodologia Tata Goncalves.
```

---

## Empacotamento Profissional — Skills Integradas

Apos aprovacao final, oferecer os formatos de entrega abaixo.
Invocar a skill correspondente para gerar cada formato.

### Formato 1: PDFs Individuais (`/pdf`)

Gerar arquivos separados:
- `prompt-mestre-[nome-agente].pdf` — Prompt Mestre completo
- `pilar-01-[nome].pdf` — Pilar 1
- `pilar-02-[nome].pdf` — Pilar 2
- `pilar-NN-[nome].pdf` — Pilar N

Cada PDF deve ter:
- Titulo do pilar como header
- Conteudo formatado com hierarquia visual clara
- Rodape: "Estruturado pela Metodologia Tata Goncalves"

### Formato 2: Documento Word (`/docx`)

Gerar documento unico `agente-[nome]-completo.docx` com:
- Capa com nome do agente e "By Tata Goncalves"
- Indice automatico
- Secao 1: Prompt Mestre
- Secao 2+: Um capitulo por pilar
- Secao final: Resumo do agente + instrucoes de uso

### Formato 3: Deck de Apresentacao (`/pptx`)

Gerar `agente-[nome]-deck.pptx` com:
- Slide 1: Capa (nome do agente + proposito)
- Slide 2: Visao geral (mapa dos pilares em diagrama)
- Slides 3-N: Um slide por pilar (nome, funcao, etapas-chave)
- Slide final: Fluxo completo + como usar

Ideal para: apresentar para clientes de mentoria, vender como produto.

### Formato 4: Mapa Visual / Infografico (`/canvas-design`)

Gerar poster `mapa-agente-[nome].png` com:
- Layout vertical (1080x1920 ou similar)
- Fluxo visual: "Comecar" → Pilar 1 → Pilar 2 → ... → Entrega
- Cada pilar como um bloco com nome e icone representativo
- Setas de conexao entre pilares
- Cores vibrantes, fundo claro (tema Tata)
- Badge: "Metodologia Tata Goncalves"

Ideal para: postar no Instagram, usar em materiais de venda.

### Combinacoes Sugeridas

| Uso | Formatos recomendados |
|-----|----------------------|
| Uso pessoal (colar na IA) | Markdown (entrega minima) |
| Produto para venda | PDFs individuais + Deck + Mapa Visual |
| Entrega de mentoria | Documento Word + Mapa Visual |
| Portfolio / autoridade | Deck + Mapa Visual |
| Tudo (pacote premium) | PDF + DOCX + PPTX + Canvas |
