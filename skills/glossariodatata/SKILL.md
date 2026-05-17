---
name: glossariodatata
description: Gerencia o Glossário da Tata (https://mentoriaimperioia.com/glossariodatata). Adiciona termos novos, escaneia conversas pra detectar termos faltando, regenera Markdown e faz deploy pro site. Ativa com /glossariodatata ou quando usuário disser "adiciona ao glossário", "glossário tata", "atualiza o glossário".
---

# Glossariodatata — Gerenciador do Glossário Tech da Tata

## Sobre

O Glossário é um sistema de 3 camadas com **fonte única de verdade**:

```
glossario.json  ◄── FONTE ÚNICA DE VERDADE (edita só aqui)
    ↓
    ├─→ index.html (site — lê JSON via fetch)
    └─→ Glossario-Imperatriz-Tech.md (vault — gerado por script)
```

**Paths:**
- Projeto local: `~/Documents/Obsidian Vault/03 - Projetos/Glossario-Tata-Site/`
  - `glossario.json` — dados
  - `index.html` — site
  - `generate-md.mjs` — regenera MD
  - `deploy.sh` — upload pra VPS
- MD gerado: `~/Documents/Obsidian Vault/08 - Recursos/Glossario-Imperatriz-Tech.md`
- VPS path: `/var/www/apps/glossariodatata/` (acesso via `ssh -i ~/.ssh/id_ed25519_hostinger root@76.13.175.161`)
- URL pública: `https://mentoriaimperioia.com/glossariodatata/`

## Ações suportadas

### 1. `/glossariodatata add <termo>` — Adicionar termo novo

Quando usuária pedir pra adicionar um termo (ex: "adiciona 'Kubernetes' no glossário"):

1. **Ler** `~/Documents/Obsidian Vault/03 - Projetos/Glossario-Tata-Site/glossario.json`
2. **Verificar** se o termo já existe (case-insensitive em `name`)
3. Se já existe, confirmar com usuária se quer **atualizar** ou abortar
4. Se novo, **decidir a categoria** certa entre as 17 existentes baseado no conceito
5. **Escrever os 4 campos** seguindo o padrão:
   - `name`: nome canônico do termo
   - `tag`: tag curta (ex: "Conceito", "Ferramenta", "Erro", "React")
   - `what`: definição técnica em 1-2 frases (linguagem simples)
   - `analogy`: analogia do mundo real, preferencialmente de restaurante/casa/vida cotidiana
   - `uses`: conexão com o ecossistema REAL da Tata (projetos: Marketing Command, Escritório Império, Ana Lazarotto, VPS Hostinger, skills Claude Code, etc). Se não se aplica ao stack dela, dizer "potencial" ou "não aplica ao seu stack atual".
6. **Inserir** no array `terms` da categoria escolhida
7. **Atualizar** `updatedAt` para a data de hoje
8. **Rodar** `cd "~/Documents/Obsidian Vault/03 - Projetos/Glossario-Tata-Site" && ./deploy.sh`
9. **Confirmar** deploy com URL + contagem nova

**Qualidade do texto:**
- Português BR, tom direto e acolhedor
- Evitar "é uma ferramenta que" — ir direto ao ponto
- Analogias concretas (não abstratas)
- Sempre conectar com o ecossistema Tata em `uses`

### 2. `/glossariodatata scan` — Escanear conversa recente

Quando a usuária pedir pra "escanear termos que usamos" ou "ver o que falta":

1. **Ler** `~/Documents/Obsidian Vault/03 - Projetos/Glossario-Tata-Site/glossario.json`
2. Extrair **todos os `name`** de todas as categorias (lowercase) como set de termos conhecidos
3. **Pegar os últimos ~20 turnos** da conversa atual (usar contexto disponível)
4. **Identificar termos técnicos** que apareceram (heurística: palavras que parecem jargão — CamelCase, siglas 2-4 letras, nomes de ferramentas, comandos Linux, padrões de código)
5. **Filtrar** os que NÃO estão no set conhecido
6. Apresentar lista à usuária com:
   - Termo
   - Contexto em que apareceu
   - Categoria sugerida
   - Recomendação (adicionar/pular)
7. Perguntar quais ela quer adicionar
8. Pra cada aprovado, usar o fluxo `add`

### 3. `/glossariodatata sync` — Forçar redeploy

Quando a usuária só pedir pra "atualizar o site" ou "redeploy":

1. Rodar `cd "~/Documents/Obsidian Vault/03 - Projetos/Glossario-Tata-Site" && ./deploy.sh`
2. Confirmar com URL

### 4. `/glossariodatata list [categoria]` — Listar termos

Quando a usuária perguntar "quantos termos tem?" ou "mostra os termos de IA":

1. Ler JSON
2. Se categoria especificada, listar só dela
3. Senão, mostrar resumo: total + contagem por categoria

### 5. `/glossariodatata edit <termo>` — Editar termo existente

1. Achar o termo no JSON
2. Perguntar qual campo editar (what/analogy/uses/tag/name)
3. Fazer edit
4. Rodar deploy

## Regras importantes

- **NUNCA** edite o Markdown (`Glossario-Imperatriz-Tech.md`) direto — ele é gerado
- **NUNCA** edite o `index.html` direto pra adicionar termos — sempre via JSON
- **Sempre** rode o deploy após alterar JSON (ou avise usuária que precisa sincronizar)
- **Preserve** a ordem: mudanças no JSON devem respeitar a categoria onde fazem sentido
- **Termos novos** devem seguir o estilo dos existentes: analogia concreta + conexão com Tata
- **Ecossistema Tata** pra referência em `uses`:
  - VPS Hostinger (76.13.175.161, 27 apps PM2)
  - Marketing Command (comando.iacomtata.com.br, Express 5 + TS + SQLite + React 19)
  - Escritório Império (SPEC v1.1, Node+TS, Redis Streams, event sourcing)
  - Ana Lazarotto Meta Ads (act_217134671443090)
  - Stack default: Node + TypeScript + SQLite + JWT + Express + React
  - 200+ skills Claude Code
  - Obsidian Vault como fonte primária

## Não fazer

- Não adicionar termos random sem valor (ex: gírias, termos de moda, acrônimos obscuros)
- Não duplicar termos com nomes parecidos (ex: se já tem "Container", não criar "Docker Container")
- Não usar analogias abstratas ou acadêmicas — sempre concreto
- Não expandir `uses` com info que a Tata não usa (evitar "potencial" demais — seja honesto se ela NÃO usa)

## ANONIMIZAÇÃO OBRIGATÓRIA (o site é público pra mentoradas!)

**NUNCA escreva** dados pessoais da Tata no campo `uses`:
- ❌ IPs reais (76.13.175.161) → ✅ `SEU_IP` ou `***.***.***.***`
- ❌ act_217134671443090 → ✅ `act_***`
- ❌ Pixel 1463261344941570 → ✅ `Pixel ****`
- ❌ Ana Lazarotto → ✅ `campanhas de clientes` ou `seus clientes`
- ❌ Marketing Command, Escritório Império, Ebook Império → ✅ `apps backend`, `projetos com event sourcing`, `apps builder`
- ❌ comando.iacomtata.com.br → ✅ `seuapp.exemplo.com`
- ❌ iacomtata.com.br → ✅ `seudominio.com`
- ❌ "ssh hostinger-vps" → ✅ "ssh seu-vps"

**Manter OK:**
- Nomes de ferramentas públicas (Node, React, Express, PM2, Nginx, SQLite, Redis)
- "sua VPS", "seu app", "seu stack" — referências genéricas
- Domínios de fornecedores (Anthropic, Gemini, ElevenLabs, Hostinger)
- Tom de voz pessoal nas Quick Answers (é intencional)

## Exemplos de interação

**Usuária:** "adiciona o termo 'worktree' no glossário"
**Claude:** Analisa → categoria "Git e Versionamento" → escreve 4 campos → insere → deploy → "✓ Adicionado. 286 termos agora. Link: https://..."

**Usuária:** "escaneia o que falta do que a gente conversou"
**Claude:** Lê JSON → analisa últimos turnos → "encontrei 5 termos que mencionamos e não estão: ENOENT, sshpass, known_hosts, expect, scp". → "Quer que eu adicione todos ou escolhe quais?"

**Usuária:** "atualiza o site"
**Claude:** `./deploy.sh` → "Redeploy feito, 285 termos."
