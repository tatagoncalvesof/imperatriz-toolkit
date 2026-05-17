# Output Final (entrega ao terminar Fase 5)

## O pacote entregue

Ao concluir as 5 fases, Maestro consolida TUDO em duas pastas:

### Pasta técnica (JSONs canônicos)

```
~/imperio/mentoradas/[nome]/
├── 01-posicionamento.json          (Fase 1)
├── 02-porta-atual.json              (Fase 3)
├── 03-voz-de-marca.json             (Fase 2)
├── 04-linha-editorial.json          (Fase 4)
├── 05-calendario-30-dias.md         (Fase 5)
├── _progresso.json                  (estado de execução)
└── 99-pacote-completo.html          ← dashboard único que junta TUDO
```

### Pasta amigável (Obsidian Vault)

```
~/Documents/Obsidian Vault/03 - Projetos/Pacote-Conteudo-[Nome]/
├── README.md                        ← como usar o pacote
├── manifesto-editorial.md           ← 1 página A4 pra parede
├── linha-editorial-dashboard.html   ← interativo
├── calendario-30-dias-dashboard.html ← interativo
└── _resumo-da-construcao.md         ← log das 5 fases
```

## O dashboard final (`99-pacote-completo.html`)

Um arquivo HTML standalone que abre no navegador e mostra TUDO num lugar só:

### Seção 1 — Identidade
- Nome da mentorada + Porta atual + nível
- Frase de posicionamento (em destaque)
- Cliente ideal

### Seção 2 — Voz
- Top 10 palavras-âncora (chips verdes)
- Top 10 palavras banidas (chips vermelhos)
- Abertura padrão + fechamento padrão
- 1 exemplo canônico em destaque

### Seção 3 — Linha Editorial
- Pilares com proporção (gráfico pizza)
- Matriz TEAM (gráfico barras)
- Cadência por canal (mini-calendário visual)
- Boundaries SIM/NÃO (lista lado a lado)

### Seção 4 — Calendário 30 Dias
- Calendário visual mês inteiro
- Cada peça clicável mostra: tema, formato, canal, dia, horário, intenção TEAM, "qual skill produz"

### Seção 5 — Próximos Passos
- 5 botões grandes: "Produzir LinkedIn da semana", "Produzir Carrossel", "Produzir Stories Q&A", "Produzir Mensagens DM", "Produzir E-mails da semana"
- Cada botão mostra qual skill rodar + o que ela vai entregar

### Seção 6 — Manifesto
- O manifesto editorial completo (8 blocos)
- Botão "copiar" + botão "imprimir"

## Mensagem de entrega

Maestro mostra:

```
✅ PACOTE COMPLETO — [Nome da Mentorada]

Tempo total: [X horas em Y sessões]

Você tem agora:
✓ Posicionamento capturado e nomeado
✓ Voz de marca em arquivo canônico
✓ Porta da Travessia identificada ([X] | [nível])
✓ Linha editorial completa
✓ Manifesto editorial pra colar na parede
✓ Calendário de 30 dias com [N] peças

📁 Tudo salvo em:
   • Técnico:  ~/imperio/mentoradas/[nome]/
   • Amigável: ~/Documents/Obsidian Vault/03 - Projetos/Pacote-Conteudo-[Nome]/

🌐 Abre o dashboard final agora:
   ~/imperio/mentoradas/[nome]/99-pacote-completo.html

────────────────────────────────────

PRÓXIMOS PASSOS

A partir de agora, sempre que você quiser PRODUZIR uma peça, roda a skill da peça. Todas elas LEEM automaticamente teu pacote — você não precisa contar de novo quem você é, nem qual a tua voz.

Pra produzir LinkedIn da semana:
→ /linkedin-empire

Pra produzir um carrossel Instagram:
→ /skill-carrossel-instagram

Pra produzir 10 stories de Q&A:
→ /stories-pergunta-resposta

Pra produzir mensagens de DM (WhatsApp/IG):
→ /copy-conversacional-dm

Pra produzir e-mails da semana:
→ /email-sequence

Pra produzir página de vendas:
→ /skill-pagina-vendas

DICA: o calendário já te diz QUAL peça produzir QUANDO. Abre o dashboard e clica na peça do dia.

────────────────────────────────────

Daqui a 30 dias, quando o calendário acabar, roda /calendario-imperatriz --gerar de novo (ou /linha-editorial-imperatriz --auditar se quiser revisar a linha antes).

Bora postar.
```

## O que Maestro NÃO faz no fim

- ❌ Oferecer pra continuar produzindo peças (escopo separado)
- ❌ Vender outra skill ou outro programa
- ❌ Pedir feedback sobre a experiência (vira ruído)
- ❌ Sugerir "compartilhe no Instagram que você usou" (cringe)
- ❌ Resumir as 5 fases de novo (já mostrou na entrega)

## Arquivo `README.md` da pasta amigável

Maestro escreve esse arquivo automaticamente:

```markdown
# Pacote de Conteúdo — [Nome]
**Construído em [data] | Porta atual: [X] | Nível: [Princesa/Marquesa/Imperatriz]**

## Como usar essa pasta

### Pra ver tudo num lugar só
Abre `99-pacote-completo.html` no navegador.

### Pra colar manifesto na parede
`manifesto-editorial.md` — uma página A4. Imprime e cola.

### Pra ver tua linha editorial visualmente
`linha-editorial-dashboard.html` — pilares + TEAM + cadência + vocabulário + boundaries.

### Pra ver teu calendário
`calendario-30-dias-dashboard.html` — mês inteiro visual.

### Pra produzir peças
Roda as skills filhas (lista no dashboard final).

## Quando atualizar

- **Mensalmente**: roda `/calendario-imperatriz --gerar` pra próximo mês
- **Trimestralmente**: roda `/linha-editorial-imperatriz --auditar`
- **Quando mudar de Porta**: roda `/linha-editorial-imperatriz --evoluir`

---

Pacote gerado pelo `/maestro-de-conteudo` — Travessia Imperatriz Tata Gonçalves.
```
