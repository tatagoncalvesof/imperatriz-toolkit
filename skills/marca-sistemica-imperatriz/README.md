# marca-sistemica-imperatriz

**Pilar 9 (Marca) da Travessia Imperatriz Tata Gonçalves.**

Marca sem ritual é logo. Marca com ritual é cultura. Esta skill mantém a Corte coerente em quatro camadas: linguagem, ritual, símbolo e identidade compartilhada.

---

## O que esta skill faz

Não é manual de logo. É operador de marca como sistema vivo. Cuida de:

1. **Linguagem ritualística** — vocabulário oficial da Corte (Aspirante, Princesa, Câmara, Decreto, Travessia, Porta, Estação)
2. **Ritualística** — calendário de ritos (boas-vindas, Investidura, Coroação, Audiências)
3. **Símbolos visuais** — cores das 6 Estações, 6 coroas progressivas, sigilos das 26 Portas, badges de nível
4. **Identidade compartilhada** — templates por canal, hashtags oficiais, badge no perfil

---

## Instalação

### Para a Tata
A skill já está em `/Users/tamiresgoncalves/Documents/travessia-imperatriz-site/skills-novas/marca-sistemica-imperatriz/`. Pra ativar, copiar pra `~/.claude/skills/marca-sistemica-imperatriz/`.

### Para mentoradas
```bash
cp -r marca-sistemica-imperatriz ~/.claude/skills/
```

Reabrir o Claude. A skill aparece como `/marca-sistemica-imperatriz`.

---

## Modos disponíveis

| Modo | Quando usar | Output |
|------|-------------|--------|
| `--glossario` | Quer ver/exportar vocabulário oficial | Markdown com 30+ termos |
| `--ritualistica` | Quer calendário de ritos ativos | Calendário semanal/mensal/trimestral/anual |
| `--validar [texto]` | Tem copy/email/site pra auditar | Score 0–100 + violações + reescrita |
| `--badges [nivel]` | Precisa de badge visual de nível | Especificação HEX + formatos por canal |
| `--templates` | Vai postar e quer template oficial | Templates por canal com paleta correta |

Sem modo declarado → skill pergunta.

---

## Exemplos de uso

### Validar uma página de vendas
```
/marca-sistemica-imperatriz --validar
[colar texto da página]
```

Skill devolve violações ("aluna" → "mentorada"; "módulo" → "Porta"), frases-âncora sugeridas e score.

### Pegar badge de Princesa pra postar no Insta
```
/marca-sistemica-imperatriz --badges Princesa
```

Skill devolve: cor HEX (#E8B4D6), descrição da coroa (3 pontas), formatos (240×240 pra bio, 1080×1920 pra story, 1584×396 pra LinkedIn), fonte oficial.

### Ver calendário de rituais da semana
```
/marca-sistemica-imperatriz --ritualistica
```

Skill devolve: Audiência Semanal (terça 19h), Câmara por nível, ritos de passagem agendados.

### Exportar glossário pra colar no Notion
```
/marca-sistemica-imperatriz --glossario
```

Skill devolve `GLOSSARIO-OFICIAL.md` formatado.

### Pegar template de carrossel da Estação Realeza
```
/marca-sistemica-imperatriz --templates
[Estação: Realeza]
[Canal: Carrossel Insta]
```

Skill devolve template com paleta roxa, fonte Cinzel + Inter, headline-âncora, CTA-âncora, hashtags.

---

## Arquivos da skill

- `SKILL.md` — filosofia + 5 modos + processo + integração
- `README.md` — este arquivo
- `GLOSSARIO-OFICIAL.md` — 30+ termos com definição + uso + exemplo
- `CALENDARIO-RITUALISTICO.md` — ritos semanais/mensais/trimestrais/anuais
- `SIMBOLOS-VISUAIS.md` — cores, coroas, badges, sigilos com HEX
- `LINGUAGEM-ANCORA.md` — 15+ frases-âncora por canal
- `ANTI-PATTERNS-LINGUAGEM.md` — termos proibidos + alternativas

---

## Integração com outras skills

| Skill | Relação |
|-------|---------|
| `voz-humana-br` | Filtro extra após reescrita (humaniza linguagem oficial sem quebrar ritual) |
| `brand-guidelines` | Fallback de cor/fonte quando Estação não declarada |
| `glossariodatata` | Glossário público externo (esta aqui é interno da Corte) |
| `voz-de-marca-builder` | Tom de comunicação (esta aqui é vocabulário ritualístico) |
| `tatou-2.0` | Dispara esta skill em ritos de passagem |
| `gates-imperatriz` | Dispara `--badges` quando Porta-marco é concluída |
| `hierarquia-imperatriz` | Dispara Investidura quando nível muda |

---

## Filosofia

A Corte só existe quando todo mundo:
- **Fala** o mesmo idioma (linguagem)
- **Passa** pelos mesmos ritos (ritual)
- **Carrega** os mesmos sinais (símbolo)
- **Se reconhece** no mercado (identidade compartilhada)

Quebrou uma dessas quatro → vira mais um curso digital.
Manteve as quatro vivas → vira movimento.

Esta skill é a guardiã das quatro.

---

**Método Imperatriz de Marca Sistêmica — propriedade Tata Gonçalves. Uso interno e mentoradas autorizadas.**
