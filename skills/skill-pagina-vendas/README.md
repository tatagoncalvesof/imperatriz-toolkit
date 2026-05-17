# PageCraft — Sales Page Factory

Skill do Claude Code que gera páginas de vendas completas de A a Z: estratégia, copy, fotos com IA, design e HTML pronto pra publicar.

Combina 8 frameworks de copywriting (AIDA, PASTOR, QUEST, FAB, ACCA, SSS, 4Ps, 1-2-3-4) com as metodologias de Russell Brunson, Alex Hormozi, Sexy Canvas, Gary Bencivenga e 70+ modelos mentais de marketing.

Por **Tata Goncalves** — Mentoria Império IA.

---

## Instalação (1 comando)

```bash
curl -fsSL https://raw.githubusercontent.com/tatagoncalvesof/skill-pagina-vendas/main/install.sh | bash
```

Pré-requisitos:
- Claude Code instalado
- `git` disponível no terminal (no Mac: `xcode-select --install`)

O instalador:
1. Baixa a skill mais recente
2. Faz backup automático se você já tinha uma versão instalada
3. Coloca em `~/.claude/skills/skill-pagina-vendas/`

---

## Como usar

Abra o Claude Code em qualquer projeto e digite:

```
/skill-pagina-vendas
```

A skill vai te guiar por 5 fases:

1. **Briefing inteligente** — perguntas sobre produto, público, provas, tom de voz
2. **Estratégia + framework** — escolhe o melhor framework pro seu caso
3. **Copy completa** — gera 3 variações do hero + todas as seções
4. **Análise + score** — avalia persuasão, objeções, mapa de emoções
5. **Design + build** — gera fotos com IA, monta HTML responsivo, abre no browser

---

## Atualização

Roda o mesmo comando de instalação. Sua versão antiga vira backup automático.

---

## Estrutura

```
skill-pagina-vendas/
├── SKILL.md                  # prompt principal da skill
├── frameworks/               # 8 frameworks de copywriting
├── metodologias/             # Russell, Hormozi, Sexy Canvas, Bencivenga, modelos mentais
├── scoring/                  # analisador de copy
├── fotos/                    # regras pra fotos realistas com IA
└── design/                   # construtor de páginas
```

---

## Suporte

Mentoradas da Imersão Imperatriz IA: tira dúvidas no grupo do Telegram.
