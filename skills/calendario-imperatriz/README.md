# Calendário Imperatriz

> Skill da **Porta N (Narrativa)** da Travessia Imperatriz — Tata Gonçalves.
> Calendário editorial UNIFICADO que cruza 6 canais sem canibalização.

---

## O que essa skill faz

Você (mentoranda) tem 1 ideia/aula/insight e precisa transformar em conteúdo pra:
- Instagram Carrossel (feed)
- Instagram Stories
- Instagram Reels
- LinkedIn
- Email
- WhatsApp Status

Em vez de copiar e colar o mesmo texto em todos os canais (canibalização) ou ficar travada sem saber o que postar, essa skill aplica a fórmula **1 ideia central por semana × 5 adaptações por canal** e gera 30 peças/mês prontas pra produção.

## O que essa skill NÃO faz

- **Não produz a peça final.** Ela monta o briefing e despacha pras skills produtoras (`/skill-carrossel-instagram`, `/stories-pergunta-resposta`, `/linkedin-empire`, `/email-sequence`, `/skill-copy-ads-ptbr`).
- **Não posta nada.** Só gera o calendário. Você usa Metricool / Later / Buffer / mLabs pra agendar.
- **Não inventa voz de marca.** Lê `~/imperio/mentoradas/[nome]/03-voz-de-marca.json` antes de gerar.
- **Não força os 6 canais.** Se você não usa LinkedIn, ela respeita.

## A lógica em 1 frase

> **Não posta tudo em todo lugar. Adapta uma ideia única em 5 formatos pra 5 canais — e espaça 2-3 dias entre cada peça.**

## Os 4 modos

| Modo | Quando usar | Comando |
|------|------------|---------|
| **Gerar** | Planejar mês inteiro | `/calendario-imperatriz --gerar [nome]` |
| **Semanal** | Só a próxima semana | `/calendario-imperatriz --semanal [nome]` |
| **Reaproveitar** | Já tem 1 conteúdo, quer adaptar pros 5 outros canais | `/calendario-imperatriz --reaproveitar [nome] [conteudo]` |
| **Auditar** | Analisar calendário existente, achar gaps e canibalização | `/calendario-imperatriz --auditar [nome]` |

## Pré-requisitos (instalação)

Antes de rodar a skill, sua mentoranda precisa ter:

### 1. Voz de marca preenchida

Arquivo obrigatório: `~/imperio/mentoradas/[nome-mentoranda]/03-voz-de-marca.json`

Se não existe, rodar antes:
```
/voz-de-marca-builder
```

### 2. Skills filhas instaladas

A skill despacha pra:
- `/skill-carrossel-instagram` (carrossel)
- `/stories-pergunta-resposta` (stories Q&A)
- `/linkedin-empire` (LinkedIn)
- `/email-sequence` (email)
- `/skill-copy-ads-ptbr` (WhatsApp + ads)
- `/voz-humana-br` (validação obrigatória)

Se alguma não está instalada, a skill pula a recomendação de despacho mas ainda gera o briefing.

### 3. Pasta da mentoranda

Estrutura esperada:
```
~/imperio/mentoradas/[nome]/
├── 02-perfil.json              (nicho, ticket, ICP)
├── 03-voz-de-marca.json        (OBRIGATÓRIO — filtro)
├── 04-mecanismo-unico.json     (opcional — se já rodou /mecanismo-unico)
├── 05-porta-atual.json         (opcional — porta vigente)
└── calendario-[mes].json       (output da skill)
```

## Instalação rápida

### Pra Tata (origem)

A skill vive em:
```
/Users/tamiresgoncalves/Documents/travessia-imperatriz-site/skills-novas/calendario-imperatriz/
```

Quando estiver finalizada, copiar pra:
```bash
cp -r /Users/tamiresgoncalves/Documents/travessia-imperatriz-site/skills-novas/calendario-imperatriz \
      ~/.claude/skills/
```

### Pra mentoranda (destino)

```bash
# Copiar a pasta inteira pra ~/.claude/skills/
cp -r calendario-imperatriz ~/.claude/skills/

# Verificar
ls ~/.claude/skills/calendario-imperatriz/

# Rodar
# (no Claude Code)
/calendario-imperatriz --gerar [seu-nome]
```

## Uso típico (passo a passo)

### Cenário 1 — "Quero planejar junho inteiro"

1. Mentoranda abre Claude Code
2. Roda `/calendario-imperatriz --gerar maria`
3. Skill pergunta:
   - Mês alvo? → `2026-06`
   - Porta atual? → `L (Lançamento)`
   - Lançamento ativo? → `sim, fase de aquecimento`
   - Sazonalidade? → `Festa Junina + Dia dos Namorados`
   - Objetivos? → `vender Mentoria 2.0 com meta de 30 vagas`
4. Skill gera 8 ideias macro candidatas
5. Mentoranda escolhe 4
6. Skill gera as 20 peças adaptadas + 10 extras
7. Skill valida tudo em `voz-humana-br`
8. Skill salva em `~/imperio/mentoradas/maria/calendario-2026-06.json` + `.md`
9. Mentoranda lê o markdown, ajusta, aprova
10. Mentoranda começa a despachar pras skills filhas semana a semana

### Cenário 2 — "Acabei de gravar uma aula, quero virar conteúdo"

1. Mentoranda salva transcrição em `/tmp/aula-mecanismo.txt`
2. Roda `/calendario-imperatriz --reaproveitar maria /tmp/aula-mecanismo.txt`
3. Skill lê a transcrição, extrai 3-5 insights principais
4. Skill gera 5 peças (carrossel + reels + stories + LinkedIn + email) baseadas nos insights
5. Skill sugere espaçamento de 7 dias pra publicar
6. Skill salva no `calendario-[mes].json`

### Cenário 3 — "Tô achando que tô postando demais e ninguém engaja"

1. Mentoranda manda link/screenshot do calendário atual
2. Roda `/calendario-imperatriz --auditar maria`
3. Skill detecta:
   - 3 canibalizações temporais (mesma ideia em 2 canais no mesmo dia)
   - 2 vácuos de canal (LinkedIn parado há 18 dias)
   - 1 descolamento da Porta (conteúdo de Porta D mas mentoranda está em Porta L)
4. Skill entrega plano de correção 7 dias

## Anatomia de uma peça gerada

Cada uma das 5 peças adaptadas vem com:

```yaml
canal: Carrossel Instagram
tema: Os 3 erros que travam mentora high-ticket
hook: "Você tá vendendo barato e nem percebe."
estrutura:
  slide_1: Hook
  slide_2-6: 3 erros + 3 antídotos
  slide_7: CTA salvar
caption: "[texto pronto da legenda]"
hashtags: ["#mentoriahighticket", "#imperioia", ...]
horario_sugerido: 2ª-feira 19h
despacha_pra: /skill-carrossel-instagram
voz_marca_aprovada: true
voz_humana_br_aprovada: true
```

## O que está em cada arquivo

| Arquivo | O que tem |
|---------|-----------|
| `SKILL.md` | Instruções executáveis (lido pela IA) |
| `README.md` | Esse arquivo (lido por humana) |
| `ESTRUTURA-30-DIAS.md` | Template visual + schema JSON + tabela de sazonalidade BR |
| `LOGICA-REAPROVEITAMENTO.md` | Fórmula 1→5 + extração de ângulos por canal |
| `FORMATOS-POR-CANAL.md` | Spec técnica + criativa de cada canal (carrossel slide a slide, stories Q&A, etc) |
| `EXEMPLOS-CALENDARIOS.md` | 3 calendários reais (Porta L / Porta D / Porta M) |
| `ANTI-PATTERNS.md` | 12 erros típicos + antídoto + checklist 8 itens |

## Validação obrigatória

Toda peça gerada passa por:

1. **Filtro voz-de-marca** — palavras banidas removidas, palavras-âncora preservadas
2. **Filtro voz-humana-br** — sem travessão, sem jargão, sem cara de IA
3. **Filtro anti-canibalização** — espaçamento + adaptação de tom
4. **Filtro Porta** — conteúdo serve a porta vigente

Se alguma peça reprovar, a skill regera ANTES de salvar o calendário.

## FAQ

**P: Eu tenho que usar todos os 6 canais?**
R: Não. A skill respeita o que você usa. Se só usa Instagram + Email, gera só essas peças.

**P: E se eu já uso outra ferramenta de calendário (Notion, Trello)?**
R: A skill exporta JSON + Markdown. Você cola onde quiser.

**P: Posso editar o que a skill gerou?**
R: Sim. Editar diretamente no `.md` ou pedir pra skill regenerar uma peça específica.

**P: A skill agenda automaticamente?**
R: Não. Ela só gera o briefing. Você usa Metricool/Later/Buffer pra agendar.

**P: 30 peças/mês não é demais?**
R: É o mínimo de quem quer escala. Se sua estratégia é menos volume, peça `--semanal` em vez de `--gerar` e produza 5 peças por semana.

**P: Como é a integração com a Porta L (Lançamento)?**
R: Quando você declara que tem lançamento ativo, a skill calibra os temas e CTAs pra servir o funil. Aquecimento prepara, abertura promove, urgência pressiona, fechamento converte, pós-venda fideliza.

**P: A skill funciona em inglês?**
R: Não. Foi calibrada pra português brasileiro com voz-humana-br. Se precisar em inglês, use `/social-content`.

## Suporte

- Tata: `tatamentoriafluxo@gmail.com`
- Mentoria Imperio IA: [mentoriaimperioia.com](https://mentoriaimperioia.com)
- Glossário da Tata: [mentoriaimperioia.com/glossariodatata](https://mentoriaimperioia.com/glossariodatata)

## Licença

Método Imperatriz de Calendário Editorial — propriedade intelectual Tata Gonçalves.
Distribuição autorizada apenas pra mentorandas ativas da Mentoria Imperio IA.
