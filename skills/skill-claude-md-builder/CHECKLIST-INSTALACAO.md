# Como Instalar a Skill "CLAUDE.md Builder" no Seu Claude Code

## O que e essa skill?

E um assistente interativo que te faz perguntas estrategicas sobre seu negocio e, no final, cria automaticamente um arquivo CLAUDE.md — o "manual de instrucoes" que faz a IA entender quem voce e, o que faz e como deve trabalhar pra voce. Voce configura uma vez e a IA lembra pra sempre.

---

## Pre-requisitos

1. Ter o **Claude Code** instalado no computador (Mac ou Linux)
2. Ter o **Claude Code funcionando** — abrir o terminal e digitar `claude` pra confirmar

Se ainda nao instalou, rode no terminal:
```
npm install -g @anthropic-ai/claude-code
```

---

## Passo a Passo da Instalacao

### Passo 1: Criar a pasta da skill

Abra o terminal e cole esses comandos (um por um):

```bash
mkdir -p ~/.claude/skills/skill-claude-md-builder
```

### Passo 2: Criar o arquivo da skill

Cole esse comando no terminal para abrir o editor:

```bash
nano ~/.claude/skills/skill-claude-md-builder/SKILL.md
```

### Passo 3: Colar o conteudo

1. Abra o arquivo **SKILL.md** que a Tata te enviou
2. Copie TODO o conteudo (Ctrl+A ou Cmd+A, depois Ctrl+C ou Cmd+C)
3. Cole no editor do terminal (Ctrl+V ou Cmd+V)
4. Salve: aperte **Ctrl+O**, depois **Enter**, depois **Ctrl+X** para sair

### Passo 4: Confirmar que deu certo

Cole no terminal:

```bash
cat ~/.claude/skills/skill-claude-md-builder/SKILL.md
```

Deve aparecer o conteudo da skill na tela. Se apareceu, deu certo!

---

## Como Usar

### Passo 5: Abrir o Claude Code na pasta do seu projeto

Va ate a pasta onde voce quer criar o CLAUDE.md. Por exemplo:

```bash
cd ~/meu-projeto
claude
```

> **Dica:** Se voce ainda nao tem uma pasta de projeto, crie uma:
> ```bash
> mkdir ~/meu-negocio && cd ~/meu-negocio
> claude
> ```

### Passo 6: Ativar a skill

Dentro do Claude Code, digite:

```
/skill-claude-md-builder
```

A IA vai comecar a te fazer perguntas sobre seu negocio, uma por vez. Responda com calma — quanto mais detalhes voce der, melhor!

### Passo 7: Responder as perguntas

Sao 8 blocos de perguntas:

1. **Identidade** — Seu nome, negocio, o que faz
2. **Publico-alvo** — Quem e seu cliente ideal
3. **Produtos** — O que voce vende e por quanto
4. **Tom de voz** — Como voce fala e se comunica
5. **Diferencial** — O que te torna unico
6. **Prova social** — Depoimentos e numeros
7. **Canais** — Instagram, WhatsApp, site
8. **Regras** — O que a IA deve sempre fazer

### Passo 8: Pronto!

Ao final, a IA gera automaticamente o arquivo `CLAUDE.md` na sua pasta. A partir de agora, toda vez que voce abrir o Claude Code nessa pasta, a IA ja sabe tudo sobre voce e seu negocio.

---

## Teste Rapido

Depois de criar o CLAUDE.md, teste pedindo algo:

```
Crie 3 ideias de post pro meu Instagram
```

A IA vai responder ja sabendo seu nicho, tom de voz e publico. Magico, ne?

---

## Duvidas Frequentes

**P: Posso editar o CLAUDE.md depois?**
R: Sim! E so abrir o arquivo e editar manualmente, ou pedir pro Claude Code atualizar.

**P: Funciona em qualquer pasta?**
R: O CLAUDE.md so funciona na pasta onde ele foi criado. Se voce tiver varios projetos, pode ter um CLAUDE.md diferente em cada pasta.

**P: E se eu errar uma resposta?**
R: Sem problema. Voce pode editar o CLAUDE.md depois ou rodar a skill de novo.

**P: Preciso pagar algo a mais?**
R: Nao. A skill e gratuita e funciona com qualquer plano do Claude Code.

---

## Resumo Visual

```
1. Abrir Terminal
2. mkdir -p ~/.claude/skills/skill-claude-md-builder
3. Colar o SKILL.md na pasta
4. cd ~/sua-pasta-de-projeto
5. claude
6. /skill-claude-md-builder
7. Responder as perguntas
8. CLAUDE.md criado automaticamente!
```

---

Feito com carinho pelo Instituto Tata Goncalves
