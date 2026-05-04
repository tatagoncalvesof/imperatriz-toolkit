# Imperatriz Toolkit

Toolkit proprietário da [Tata Goncalves](https://mentoriaimperioia.com) — 6 skills do Claude Code que constroem copy de alta conversão do briefing ao visual final.

## O que vem dentro

| Skill | O que faz |
|---|---|
| `briefing-copy-360` | Framework obrigatório pré-escrita — extrai 5 níveis hierárquicos antes de qualquer copy |
| `mecanismo-unico` | 23 critérios (13 estruturais + 10 estratégicos) pra construir o Mecanismo Único |
| `headline-imperatriz` | Schwartz + Bencivenga + adaptação Brasil — 6 temperaturas, 17 fórmulas, 3 modos |
| `texto-em-visual` | 18 tipos de visualização + briefing IA (Midjourney/Ideogram/Gemini) |
| `analise-anuncio-1000` | 17 camadas de análise profunda de copy/VSL/anúncio |
| `stories-pergunta-resposta` | 10 stories Q&A 9:16 com identidade fechada (carro/escritório) |

**Trio mestre:** `mecanismo-unico` → `headline-imperatriz` → `texto-em-visual` (mecanismo vira headline vira visual).

## Instalação

No Claude Code, dentro de qualquer projeto:

```bash
/plugin marketplace add tatagoncalvesof/imperatriz-toolkit
/plugin install imperatriz-toolkit@tatagoncalvesof-imperatriz-toolkit
```

Reinicia ou roda `/reload-plugins` e usa as skills com namespace:

```bash
/imperatriz-toolkit:briefing-copy-360
/imperatriz-toolkit:mecanismo-unico
/imperatriz-toolkit:headline-imperatriz
/imperatriz-toolkit:texto-em-visual
/imperatriz-toolkit:analise-anuncio-1000
/imperatriz-toolkit:stories-pergunta-resposta
```

## Atualização

```bash
/plugin update imperatriz-toolkit
```

## Pré-requisitos

- Claude Code instalado (`claude` no terminal)
- Conta Claude ativa
- Algumas skills usam Python 3 e ferramentas externas (Midjourney, Ideogram, Gemini) — leia o `SKILL.md` de cada uma

## Fluxo recomendado

```
1. /imperatriz-toolkit:briefing-copy-360       (extrai contexto)
2. /imperatriz-toolkit:mecanismo-unico         (constrói o mecanismo)
3. /imperatriz-toolkit:headline-imperatriz     (gera headlines)
4. /imperatriz-toolkit:texto-em-visual         (transforma em visual)
5. /imperatriz-toolkit:analise-anuncio-1000    (revisa contra 17 camadas)
6. /imperatriz-toolkit:stories-pergunta-resposta (gera Q&A pra Instagram)
```

## Licença

MIT — veja [LICENSE](LICENSE).

## Autoria

Criado por **Tata Goncalves** — Mentoria Império IA
🌐 [mentoriaimperioia.com](https://mentoriaimperioia.com)
