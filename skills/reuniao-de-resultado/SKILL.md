---
name: reuniao-de-resultado
description: Constrói o sistema completo de Reunião de Resultado (Reunião Secreta) pra qualquer empresária — entrega 14 arquivos no Obsidian Vault + dashboard HTML interativo cobrindo os 6 blocos do método (diagnóstico dos 7 sintomas, indicadores que importam, agenda sagrada, checklist 6 passos, ata, FCA/UFCA, 5 porquês, plano de ação pra meta em risco, feedback, cobrança não-tóxica, EFEITO BRIO, daily x mensal, 7 erros, comunicado pro grupo, roteiro da 1ª reunião). Dois modos — MODO TRANSCRIÇÃO (cola reunião existente, diagnostica) ou MODO DO ZERO (entrevista + monta personalizado). Use quando pedir reunião de resultado, reunião secreta, reunião gerencial, reunião do time, estruturar reunião, dashboard de reunião, ata, plano de ação meta em risco, FCA, 5 porquês, EFEITO BRIO, ou disser "minhas reuniões não decidem nada", "ninguém apresenta números", "o time não cumpre o que foi combinado".
---

# Reunião de Resultado — Skill Imperatriz

> Skill proprietária da Tata Gonçalves. Constrói o sistema completo de Reunião de Resultado pra qualquer negócio — diagnóstico, estrutura, condução, implementação e primeira reunião — em pacote pronto pra usar (HTML + arquivos no vault).

## Overview

Reunião de Resultado é o ritual gerencial que transforma reunião que não decide nada em reunião que faz dinheiro. O método tem 6 blocos sequenciais (diagnóstico → estrutura → core → condução → implementação → primeira reunião) e essa skill empacota TUDO em entregáveis prontos pra uma empresária implementar na semana que vem.

**Dois modos de uso** — escolha um no início da conversa:

- **Modo Transcrição** — a usuária cola transcrição de uma reunião que já faz hoje. A skill diagnostica os 7 sintomas, mapeia os erros do bloco 5, e entrega plano de transformação personalizado.
- **Modo Do Zero** — a usuária ainda não tem reunião estruturada. A skill faz entrevista curta (5 perguntas) e monta o sistema completo do zero.

Em ambos os modos, o output final é o mesmo: **HTML standalone + 14 arquivos no Obsidian Vault**.

## Workflow Decision Tree

```
1. Detectar modo (perguntar se ainda não está claro)
   ├── Modo A: TRANSCRIÇÃO
   │   ├── Aceitar transcrição
   │   ├── (opcional) sugerir /transcript-fixer se vier crua de STT
   │   ├── Diagnosticar 7 sintomas (references/bloco-1-diagnostico.md)
   │   ├── Mapear contra 7 erros (references/bloco-5-implementacao.md)
   │   ├── Resumir gaps em 1 página
   │   └── Seguir pra construção do pacote
   │
   └── Modo B: DO ZERO
       ├── 5 perguntas de briefing (ver "Briefing Mínimo" abaixo)
       ├── (opcional) sugerir /mecanismo-unico se a usuária não souber
       │   o que diferencia o negócio dela — ajuda a escolher os 2-3
       │   indicadores que importam
       └── Seguir pra construção do pacote

2. Construir pacote (sempre igual nos dois modos)
   ├── Ler os 6 references/ pra absorver método
   ├── Personalizar templates de assets/vault-templates/ com dados do briefing/diagnóstico
   ├── Personalizar assets/dashboard-template.html
   ├── Passar comunicado pro grupo + roteiro 1ª reunião por /voz-humana-br
   │   (obrigatório — não entregar texto sem humanizar)
   └── Salvar tudo no destino

3. Entregar
   ├── Vault: ~/Documents/Obsidian Vault/03 - Projetos/Reuniao-Resultado-{NEGOCIO}/
   ├── HTML: mesma pasta, arquivo dashboard.html
   └── Resumo final no chat: lista dos 15 arquivos + próxima ação

4. Modo pós-construção (se a usuária voltar depois)
   ├── "Auditar minha reunião de ontem" → roda diagnóstico em transcrição nova
   ├── "Refazer ata" → atualiza só o template de ata
   ├── "Plano de ação pra meta X em risco" → gera só o plano (bloco 3)
   └── "Roteiro pra próxima reunião" → gera só o roteiro
```

## Briefing Mínimo (Modo Do Zero)

Pergunte UMA por vez, em conversa fluida — não como formulário. Se a usuária der respostas curtas, peça expansão; se já trouxer informação extra na resposta, pule a próxima pergunta correspondente.

1. **Negócio em uma frase** — o que vende, pra quem, faturamento médio mensal, tamanho do time
2. **Cargo de quem participa** — quem na empresa toma decisão sobre números (ex: dono + gerente comercial + financeiro), quantas pessoas no total
3. **O que dói hoje na reunião** (ou na falta dela) — escolha múltipla dos 7 sintomas (bloco 1) ou texto livre
4. **Os 2-3 indicadores que mais importam** — se ela souber, anote. Se não souber, ofereça os 5 motores universais (faturamento, conversão, ticket médio, recorrência, custo) e ajude a escolher
5. **Frequência desejada** — semanal, quinzenal, mensal, daily? (Padrão recomendado: semanal de 60 min)

Se a usuária travar na pergunta 4 ("não sei quais números olhar"), ofereça rodar `/mecanismo-unico` antes — define o que diferencia o negócio dela e isso clareia os indicadores.

## Os 6 Blocos do Método

Os 6 references/ contêm o conhecimento detalhado. **Leia o bloco correspondente ANTES de gerar o entregável dele** — não responda de cor.

1. **[Bloco 1 — Diagnóstico e Mentalidade](references/bloco-1-diagnostico.md)** — 7 sintomas, mentalidade da grande empresa, o que parar de fazer
2. **[Bloco 2 — A Estrutura](references/bloco-2-estrutura.md)** — 5 motores, agenda sagrada, checklist 6 passos
3. **[Bloco 3 — O Core do Método](references/bloco-3-core.md)** — ata, 3 visualizações, regra de ouro, FCA/UFCA, 5 porquês, plano de ação
4. **[Bloco 4 — A Condução](references/bloco-4-conducao.md)** — feedback, cobrança não-tóxica, desculpa repetida, EFEITO BRIO
5. **[Bloco 5 — Implementação](references/bloco-5-implementacao.md)** — daily × mensal, 7 erros, engajamento, ritual sem o dono
6. **[Bloco 6 — Primeira Reunião](references/bloco-6-primeira-reuniao.md)** — comunicado, roteiro frase por frase, compromisso público

## Entregáveis (sempre os 15 arquivos)

### Pasta no Obsidian Vault

Salvar em `~/Documents/Obsidian Vault/03 - Projetos/Reuniao-Resultado-{NEGOCIO}/`:

| # | Arquivo | Origem do template | Personalização |
|---|---|---|---|
| 00 | `00-Overview.md` | gerar do zero | nome do negócio, time, frequência escolhida |
| 01 | `01-Diagnostico-7-Sintomas.md` | `assets/vault-templates/01-...md` | marcar sintomas do diagnóstico |
| 02 | `02-Os-2-3-Indicadores.md` | `assets/vault-templates/02-...md` | indicadores escolhidos no briefing |
| 03 | `03-Agenda-Sagrada.md` | `assets/vault-templates/03-...md` | dia/hora/duração/quem participa |
| 04 | `04-Checklist-6-Passos.md` | `assets/vault-templates/04-...md` | adaptar nomes dos responsáveis |
| 05 | `05-Template-Ata.md` | `assets/vault-templates/05-...md` | colocar nomes do time + indicadores |
| 06 | `06-FCA-5-Porques.md` | `assets/vault-templates/06-...md` | 2 exemplos vivos do nicho dela |
| 07 | `07-Plano-Acao-Meta-Risco.md` | `assets/vault-templates/07-...md` | nada — template universal |
| 08 | `08-Feedback-Sem-Destruir.md` | `assets/vault-templates/08-...md` | nada — template universal |
| 09 | `09-Cobrar-Sem-Ser-Toxico.md` | `assets/vault-templates/09-...md` | nada — template universal |
| 10 | `10-Efeito-Brio.md` | `assets/vault-templates/10-...md` | nada — template universal |
| 11 | `11-7-Erros-Que-Arruinam.md` | `assets/vault-templates/11-...md` | marcar erros que ela faz hoje (se modo transcrição) |
| 12 | `12-Comunicado-Grupo-Hoje.md` | `assets/vault-templates/12-...md` | personalizar nome empresa + dia/hora 1ª reunião + passar por /voz-humana-br |
| 13 | `13-Roteiro-Primeira-Reuniao.md` | `assets/vault-templates/13-...md` | personalizar nomes + indicadores + passar por /voz-humana-br |

### Dashboard HTML

`dashboard.html` na mesma pasta. Origem: `assets/dashboard-template.html`. Substituir placeholders: `{{NEGOCIO}}`, `{{INDICADORES}}`, `{{AGENDA}}`, `{{TIME}}`, `{{DATA_PRIMEIRA_REUNIAO}}`.

## Integrações com outras skills

**Obrigatórias:**
- `/voz-humana-br` — comunicado (arquivo 12) e roteiro 1ª reunião (arquivo 13) DEVEM passar por essa skill antes de salvar. Sem isso o texto sai com cara de IA e a usuária perde credibilidade no grupo.

**Opcionais (sugerir, não forçar):**
- `/transcript-fixer` — se no modo transcrição a usuária colar texto cru de STT (com erros tipo "vc", "vamo", marcadores de speaker quebrados), ofereça rodar antes do diagnóstico
- `/mecanismo-unico` — se a usuária travar na escolha dos 2-3 indicadores no modo do zero, ofereça rodar antes pra clarificar o que diferencia o negócio dela

## Regras de qualidade

- **Não responder de cor** — sempre ler o bloco em references/ antes de gerar o entregável correspondente
- **Não simplificar a regra de ouro** — quem apresenta os números NUNCA é o dono. Isso é inegociável. Se a usuária resistir, mostrar bloco 3.
- **Não inventar indicadores** — usar APENAS o que veio no briefing ou os 5 motores universais
- **Não pular humanização** — comunicado e roteiro sem `/voz-humana-br` é defeito de fábrica
- **Não criar mais do que 15 arquivos** — exatamente 14 .md + 1 .html. Mais que isso vira ruído.
- **Não colocar emoji em arquivo gerado** — mesmo que a usuária goste de emoji em conversa, os arquivos do vault e do dashboard devem ser limpos pra ela poder reaproveitar como manual da empresa.

## Modos pós-construção

Depois que o pacote foi entregue uma vez, a usuária pode voltar pra modos específicos. Detecte e roteie:

| Pedido da usuária | Ação |
|---|---|
| "Auditar minha reunião de ontem" | Aceitar transcrição, rodar diagnóstico (bloco 1 + bloco 5), entregar relatório de gaps |
| "Refazer a ata" ou "Atualizar o template" | Regerar só o arquivo 05, com mudanças solicitadas |
| "Tenho uma meta em risco — preciso de plano de ação" | Gerar só o arquivo 07 personalizado pra essa meta específica, aplicando FCA + 5 porquês |
| "Roteiro pra próxima reunião" | Gerar versão customizada do arquivo 13 pra reunião específica (não a primeira) |
| "Funcionário X repete a mesma desculpa" | Aplicar protocolo do bloco 4 — gerar script de conversa 1:1 |

## Exemplos de uso

**Exemplo 1 — Modo Do Zero:**
> Usuária: "Quero estruturar uma reunião gerencial pro meu time, hoje é uma bagunça, ninguém apresenta nada, fica todo mundo discutindo opinião"

Ação: detectar modo do zero. Fazer briefing curto. Construir pacote completo.

**Exemplo 2 — Modo Transcrição:**
> Usuária: "Olha minha reunião de ontem, dura 2h e não decide nada [cola transcrição]"

Ação: detectar modo transcrição. Rodar diagnóstico. Mapear sintomas + erros. Construir pacote com plano de transformação.

**Exemplo 3 — Pós-construção:**
> Usuária: "Tenho meta de fechar 30 contratos esse mês e tô em 12 — preciso do plano de ação"

Ação: detectar modo pós-construção. Gerar só o arquivo 07. Aplicar FCA + 5 porquês com a meta específica dela.
