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

### Mac / Linux

Copia e cola no terminal:

```bash
git clone https://github.com/tatagoncalvesof/imperatriz-toolkit ~/imperatriz-toolkit && cd ~/imperatriz-toolkit && bash install.sh
```

### Windows (PowerShell)

```powershell
git clone https://github.com/tatagoncalvesof/imperatriz-toolkit $HOME\imperatriz-toolkit
cd $HOME\imperatriz-toolkit
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

### Instalação manual (qualquer sistema)

Se preferir copiar à mão:

```bash
git clone https://github.com/tatagoncalvesof/imperatriz-toolkit
cp -R imperatriz-toolkit/skills/* ~/.claude/skills/
```

No Windows:
```powershell
git clone https://github.com/tatagoncalvesof/imperatriz-toolkit
Copy-Item -Path imperatriz-toolkit\skills\* -Destination $HOME\.claude\skills\ -Recurse
```

## Uso

Abre o Claude Code em qualquer projeto e roda:

```
/briefing-copy-360
/mecanismo-unico
/headline-imperatriz
/texto-em-visual
/analise-anuncio-1000
/stories-pergunta-resposta
```

## Atualização

Pra pegar as últimas versões das skills:

```bash
cd ~/imperatriz-toolkit
git pull
bash install.sh    # ou .\install.ps1 no Windows
```

## Pré-requisitos

- [Claude Code](https://claude.com/claude-code) instalado (`claude` no terminal)
- `git` instalado
- Algumas skills usam Python 3 e ferramentas externas (Midjourney, Ideogram, Gemini) — leia o `SKILL.md` de cada uma

## Fluxo recomendado

```
1. /briefing-copy-360         (extrai contexto)
2. /mecanismo-unico           (constrói o mecanismo)
3. /headline-imperatriz       (gera headlines)
4. /texto-em-visual           (transforma em visual)
5. /analise-anuncio-1000      (revisa contra 17 camadas)
6. /stories-pergunta-resposta (gera Q&A pra Instagram)
```

## Licença

MIT — veja [LICENSE](LICENSE).

## Autoria

Criado por **Tata Goncalves** — Mentoria Império IA
🌐 [mentoriaimperioia.com](https://mentoriaimperioia.com)
