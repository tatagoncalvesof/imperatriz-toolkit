# 01 — Fundação da Linha Editorial

## O que é (e o que não é)

**Linha editorial é a régua que decide se um conteúdo PODE existir sob essa marca.**

Não é:
- ❌ Calendário (calendário é o **quando** — linha é o **se**)
- ❌ Voz de marca (voz é o **como soa** — linha é o **sobre o quê e por quê**)
- ❌ Posicionamento (posicionamento é o **lugar no mercado** — linha é o **filtro editorial diário**)
- ❌ Briefing de copy (briefing é por peça — linha é o sistema)
- ❌ Manifesto bonito de site (manifesto é 1 dos artefatos — não é a linha inteira)

É:
- ✅ Um **contrato editorial** assinado entre a marca e ela mesma
- ✅ Uma **régua dura** que cabe num post-it: 3-5 pilares, mix TEAM, vocabulário ON/OFF, boundaries SIM/NÃO
- ✅ Um **filtro** que qualquer pessoa do time consegue aplicar antes de publicar
- ✅ Um **documento vivo** que muda quando a Porta da Travessia muda

## Os 5 ativos que compõem a linha

Toda linha editorial gerada pela skill carrega cinco peças não-negociáveis:

### 1. Pilares temáticos (3-5)
Os territórios sobre os quais a marca tem direito de falar — porque domina, porque o cliente precisa, porque ninguém mais fala daquele jeito. Cada pilar com:
- Nome curto (1-3 palavras)
- Descrição (1 frase)
- Proporção sugerida (%)
- 5 micro-temas exemplo

### 2. Matriz TEAM (mix de formatos)
Distribuição entre **T**each (ensina), **E**ngage (provoca conversa), **A**uthority (mostra autoridade), **M**onetize (vende), **S**tory (humaniza). Proporção varia por Porta da Travessia.

### 3. Cadência por canal
Frequência semanal + horário padrão + voz calibrada por canal. Só pra canais que a mentorada **já opera** ou pediu pra entrar.

### 4. Vocabulário ON/OFF
- **Palavras-âncora** (30+): vocabulário próprio da marca, puxado da voz-de-marca + marca-sistemica + pilares
- **Palavras banidas** (30+): tudo que delata IA, jargão genérico, vícios de copy

### 5. Boundaries (SIM/NÃO)
Mínimo 7 SIM e 7 NÃO. Exemplos de SIM: "publica bastidor de erro com aprendizado nomeado". Exemplos de NÃO: "não publica opinião política sob a marca, só sob conta pessoal".

## Por que linha editorial é Pilar (não Porta)

Na arquitetura da Travessia:

- **Portas A-Z** são etapas sequenciais (uma vez concluída, você passa pra próxima)
- **Pilares** são camadas permanentes (rodam em paralelo, atravessando todas as Portas)

Linha editorial é Pilar porque:

1. Não tem "concluiu a linha editorial e foi pra próxima" — ela é revisitada toda Porta
2. Atravessa Porta A (descoberta) até Porta Z (sucessão)
3. Toda Porta nova **recalibra** a linha (modo `--evoluir`), mas não substitui
4. Sem ela ativa, o calendário (Porta N) não funciona
5. Sem ela ativa, a página de vendas (Porta L) escapa da voz
6. Sem ela ativa, o e-mail de venda (Porta R) parece outra empresa

## Quando rodar a primeira vez

A primeira execução acontece **depois das três fundações**:

```
Porta A (Descoberta) → posicionamento-estrategico
Porta B (Identidade) → voz-de-marca-builder
Porta C (Marca)      → marca-sistemica-imperatriz (opcional, mas recomendado)
                    ↓
              [LINHA EDITORIAL — gerar pela primeira vez aqui]
                    ↓
Porta N (Narrativa)  → calendario-imperatriz começa a consumir a linha
```

Se a mentorada chegou na Porta N sem linha editorial declarada, **rollback obrigatório** pra Porta de fundação. Calendário sem linha é planilha.

## Quando rodar de novo

| Gatilho | Modo | Quem dispara |
|---|---|---|
| Mudança de Porta na Travessia | `--evoluir` | `gates-imperatriz` ao validar saída de Porta |
| Salto de nível (Princesa→Marquesa→Imperatriz) | `--evoluir` | `dossie-mentorada` ao registrar promoção |
| Mentorada relata "tô perdida no que postar" | `--auditar` (depois `--evoluir` se drift > 30%) | Tata na sessão 1:1 |
| Time de conteúdo mudou | `--auditar` | Mentorada após onboarding de nova pessoa |
| Trimestre fechado | `--auditar` | Cron mensal/trimestral via `evolucao-imperatriz` |

## Anti-patterns desta fundação

- ❌ Tratar linha editorial como "manifesto bonito" pra colar no site
- ❌ Criar linha sem ter rodado posicionamento + voz primeiro
- ❌ Copiar linha de outra mentorada (linha é impressão digital)
- ❌ Gerar e nunca mais revisitar (linha congelada vira museu)
- ❌ Documentar e não usar como filtro real antes de publicar
