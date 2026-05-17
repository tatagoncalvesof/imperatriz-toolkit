# CLAUDE.md Builder

Skill interativa pro Claude Code que cria o **manual de instrucoes da sua IA** atraves de perguntas estrategicas sobre seu negocio. Voce responde 8 blocos de perguntas e o Claude gera automaticamente o arquivo `CLAUDE.md` — daquele momento em diante a IA sempre sabe quem voce e, pra quem voce vende, como voce fala e o que te diferencia.

Criada pelo **Instituto Tata Goncalves** pra mentoradas e qualquer pessoa que queira configurar o Claude Code direito desde o primeiro dia.

---

## Pre-requisitos

Ter o Claude Code instalado:

```bash
npm install -g @anthropic-ai/claude-code
```

Confirma rodando `claude --version`.

---

## Instalacao (1 comando)

Cola isso no terminal:

```bash
git clone https://github.com/tatagoncalvesof/skill-claude-md-builder.git ~/.claude/skills/skill-claude-md-builder
```

Pronto. A skill ja ta instalada.

---

## Como usar

1. Vai pra pasta do seu projeto (ou cria uma nova):

```bash
mkdir ~/meu-negocio && cd ~/meu-negocio
```

2. Abre o Claude Code:

```bash
claude
```

3. Roda a skill:

```
/skill-claude-md-builder
```

4. Responde as 8 perguntas. No final o `CLAUDE.md` e gerado automaticamente na pasta.

---

## O que a skill cobre

8 blocos de perguntas estrategicas, uma por vez, com exemplos:

1. **Identidade** — nome, negocio, o que voce faz, desde quando
2. **Publico-alvo** — perfil, dor, desejo, onde te encontram, poder aquisitivo
3. **Produtos** — principal, entrada, premium
4. **Tom de voz** — estilo, referencia, palavras banidas, palavras-marca
5. **Diferencial** — o que te torna unico, metodologia, resultado concreto
6. **Prova social** — depoimentos e numeros
7. **Canais** — Instagram, WhatsApp, site
8. **Regras pra IA** — foco do conteudo, preferencias adicionais

---

## Como atualizar (quando sair versao nova)

```bash
cd ~/.claude/skills/skill-claude-md-builder && git pull
```

---

## Teste rapido depois de criar o CLAUDE.md

Dentro do Claude Code na pasta do projeto:

```
Crie 3 ideias de post pro meu Instagram
```

Se ele responder ja sabendo seu nicho, tom de voz e publico — funcionou.

---

## Licenca

MIT. Use, copie, modifique, compartilhe.

---

Feito com carinho pelo **Instituto Tata Goncalves** — [@tatagoncalvesoficial](https://instagram.com/tatagoncalvesoficial)
