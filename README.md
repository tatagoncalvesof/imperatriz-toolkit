# Imperatriz Toolkit

Toolkit proprietário da [Tata Goncalves](https://mentoriaimperioia.com) — **13 skills do Claude Code** que cobrem do briefing inicial até calendário editorial, passando por copy de alta conversão, análise de anúncio, visualização e estratégia de conteúdo multi-canal.

## O que vem dentro

### 🎯 Trio Mestre de Copy
| Skill | O que faz |
|---|---|
| `briefing-copy-360` | Framework obrigatório pré-escrita — extrai 5 níveis hierárquicos antes de qualquer copy |
| `mecanismo-unico` | 23 critérios (13 estruturais + 10 estratégicos) pra construir o Mecanismo Único |
| `headline-imperatriz` | Schwartz + Bencivenga + adaptação Brasil — 6 temperaturas, 17 fórmulas, 3 modos |

### 🎨 Visual + Análise
| Skill | O que faz |
|---|---|
| `texto-em-visual` | 18 tipos de visualização + briefing IA (Midjourney/Ideogram/Gemini) |
| `analise-anuncio-1000` | 17 camadas de análise profunda de copy/VSL/anúncio |
| `mapa-mental-imperatriz` | Mapas mentais visuais (Mermaid + Markmap + PNG + Obsidian Canvas), 8 modos |

### 📅 Estratégia de Conteúdo
| Skill | O que faz |
|---|---|
| `maestro-de-conteudo` | Orquestrador único — uma skill, cinco fases, do zero ao calendário de 30 dias |
| `linha-editorial-imperatriz` | Pilar Editorial — manifesto + pilares + matriz TEAM + cadência + vocabulário ON/OFF |
| `calendario-imperatriz` | Calendário editorial 30+ peças em 6 canais sem canibalização |
| `linkedin-empire` | Estratégia LinkedIn completa — perfil, 1.400 micro temas, 20 posts, 4 carousels, 2 newsletters |
| `stories-pergunta-resposta` | 10 stories Q&A 9:16 com identidade fechada (carro/escritório) |

### 🔬 Pesquisa + Reunião
| Skill | O que faz |
|---|---|
| `deep-market-research` | Pesquisa profunda PT-BR — voz literal do comprador em 5 plataformas, 50 termos + 150 objeções |
| `reuniao-de-resultado` | Reunião Secreta — 6 blocos do método, 14 templates Obsidian + dashboard HTML |

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

Abre o Claude Code em qualquer projeto e roda qualquer uma das skills:

```
/briefing-copy-360
/mecanismo-unico
/headline-imperatriz
/texto-em-visual
/analise-anuncio-1000
/stories-pergunta-resposta
/mapa-mental-imperatriz
/maestro-de-conteudo
/linha-editorial-imperatriz
/calendario-imperatriz
/linkedin-empire
/deep-market-research
/reuniao-de-resultado
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

## Fluxo recomendado por contexto

### Pra escrever copy (página de vendas, VSL, e-mail, anúncio)
```
1. /briefing-copy-360         (extrai contexto)
2. /deep-market-research      (captura voz literal do comprador)
3. /mecanismo-unico           (constrói o mecanismo)
4. /headline-imperatriz       (gera headlines)
5. /texto-em-visual           (transforma em visual)
6. /analise-anuncio-1000      (revisa contra 17 camadas)
```

### Pra montar estratégia de conteúdo do zero
```
/maestro-de-conteudo  (orquestra tudo em 5 fases)
       ↓
/linha-editorial-imperatriz → /calendario-imperatriz
       ↓
/linkedin-empire + /stories-pergunta-resposta + /skill-carrossel-instagram*
```

### Pra rodar reunião de resultado da empresa
```
/reuniao-de-resultado
```

### Pra organizar ideias / estruturar mentalmente
```
/mapa-mental-imperatriz
```

\* algumas skills não vêm no toolkit ainda, são instaladas separado.

## Licença

MIT — veja [LICENSE](LICENSE).

## Autoria

Criado por **Tata Goncalves** — Mentoria Império IA
🌐 [mentoriaimperioia.com](https://mentoriaimperioia.com)
