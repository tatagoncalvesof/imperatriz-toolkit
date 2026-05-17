# INTEGRACAO-ECOSSISTEMA — Como cada skill conversa com o Dossiê

O dossiê é a **camada de persistência** do ecossistema Tata Gonçalves. ~225 skills interagem com ele em 4 padrões:

1. **GRAVA** — skill produz output e salva em profile
2. **LÊ** — skill busca contexto antes de gerar
3. **GRAVA-E-LÊ** — skill faz ambos no mesmo ciclo
4. **OBSERVA** — skill só lê pra dashboard/auditoria, não modifica

Este documento mapeia o ecossistema em 6 grupos funcionais e detalha o fluxo de dados.

---

## ÍNDICE

1. [Grupo 1 — Skills de Onboarding e Diagnóstico (gravam o pé do dossiê)](#grupo-1)
2. [Grupo 2 — Skills de Copy e Voz (consumidoras pesadas)](#grupo-2)
3. [Grupo 3 — Skills de Oferta, Programa e Posicionamento](#grupo-3)
4. [Grupo 4 — Skills de Tráfego, Funil e Performance](#grupo-4)
5. [Grupo 5 — Skills de Infra, Deploy e Operação](#grupo-5)
6. [Grupo 6 — Skills de Orquestração, Dashboard e Auditoria](#grupo-6)
7. [Hooks automáticos](#hooks)
8. [Fluxo de dados ponta-a-ponta](#fluxo-completo)
9. [Confidencialidade entre mentoradas](#confidencialidade)

---

<a id="grupo-1"></a>
## GRUPO 1 — Skills de Onboarding e Diagnóstico

São as primeiras a rodar quando mentorada chega. Despejam o pé estrutural do dossiê.

### `anamnese-mentorada`

**Padrão:** GRAVA
**Profile destino:** `00-anamnese.json`
**Pré-requisito:** dossiê já criado (`--criar`)

**Fluxo:**
1. Skill é invocada com slug
2. Lê `00-anamnese.json` (vazio ou parcial)
3. Faz formulário interativo de 8 blocos
4. Ao concluir, chama `/dossie-mentorada --gravar [slug] 00-anamnese {output}`
5. Atualiza `14-progresso.json` (porta A0 → A1)

**Side-effects:**
- Cria entrada em `18-historico-decisoes.json` tipo `anamnese-concluida`
- Dispara `perfil-mentorada` automaticamente (próxima skill da Porta A)

### `perfil-mentorada`

**Padrão:** GRAVA-E-LÊ
**Lê:** `00-anamnese.json`
**Grava:** `01-perfil.json`

Sintetiza anamnese em perfil operacional. Calcula `arquetipo_negocio`, `estagio_carreira`, `modelo_receita_principal` baseado nas respostas brutas.

### `imperio-diagnostico`

**Padrão:** GRAVA-E-LÊ
**Lê:** `00-anamnese.json`, `01-perfil.json`
**Grava:** `02-diagnostico.json`

Aplica frameworks DOMINIO + FRIO + PENTA. Score 0-40 do FRIO determina priorização das próximas portas.

### `skill-claude-md-builder`

**Padrão:** GRAVA-E-LÊ (cross-profile)
**Lê:** TODOS os profiles preenchidos até o momento
**Grava:** `04-CLAUDE.md`

Caso especial: a cada update de QUALQUER profile crítico (03, 05, 06, 08, 09, 11), `tatou-2.0` dispara re-build automático do CLAUDE.md pra mantê-lo sincronizado.

---

<a id="grupo-2"></a>
## GRUPO 2 — Skills de Copy e Voz

São as **consumidoras mais pesadas** do dossiê. Toda skill de copy lê 4-7 profiles antes de escrever uma frase.

### `voz-de-marca-builder`

**Padrão:** GRAVA
**Lê:** `00-anamnese.json`, `01-perfil.json` (pra extrair amostras de voz natural da mentorada)
**Grava:** `03-voz-de-marca.json`

Skill especial: extrai `frases_assinatura` e `vocabulario_assinatura` analisando 5-10 amostras reais de WhatsApp/post da mentorada. NUNCA inventa termos — só extrai do que ela ESCREVEU.

### `voz-humana-br`

**Padrão:** LÊ (não modifica dossiê)
**Lê:** `03-voz-de-marca.json`

Aplica filtros de humanização usando `vocabulario_banido` e `frases_assinatura` da mentorada. Modo `--voz=maria-silva` carrega voz dela direto.

### `headline-imperatriz`

**Padrão:** LÊ
**Lê:** `03-voz`, `05-persona`, `06-mecanismo`, `08-posicionamento`, `11-oferta`

Antes de gerar headlines:
1. Lê voz pra calibrar estilo
2. Lê persona pra calibrar consciência/sofisticação
3. Lê mecanismo pra embuti-lo na headline
4. Lê posicionamento pra ângulo
5. Lê oferta pra promessa final

Sem `06-mecanismo` preenchido, skill RECUSA gerar (em mercado estágio 3+ é pré-requisito).

### `mecanismo-unico`

**Padrão:** GRAVA-E-LÊ
**Lê:** `00-anamnese`, `02-diagnostico`, `05-persona`, `08-posicionamento`, `17-cases`
**Grava:** `06-mecanismo.json`

Cases em `17-cases.json` são lidos pra montar `proof_stack` automaticamente. Se mentorada não tem cases, skill avisa e sugere coletar antes de fechar mecanismo.

### `briefing-copy-360`

**Padrão:** LÊ
**Lê:** TODOS os 19 profiles

Briefing prévio pra copy é literalmente um dump estruturado do dossiê em formato legível pra IA de copy. É a "ponte" entre dossiê e skills de escrita.

### `skill-pagina-vendas`

**Padrão:** LÊ
**Lê:** `03-voz`, `05-persona`, `06-mecanismo`, `07-historia-metodo`, `08-posicionamento`, `09-brand`, `10-programa`, `11-oferta`, `17-cases`

Skill mais "consumidora" do dossiê — lê 9 profiles. Sem dossiê preenchido, página gerada é genérica (skill avisa).

### `email-sequence`

**Padrão:** LÊ
**Lê:** `03-voz`, `05-persona`, `11-oferta`, `13-funil`

Sequência de e-mail varia conforme estágio do funil em 13-funil (lead frio vs lead quente vs carrinho abandonado).

### `copy-conversacional-dm`

**Padrão:** LÊ
**Lê:** `03-voz`, `05-persona`, `11-oferta`, `13-funil`

WhatsApp/DM precisa de voz da mentorada bem definida. Skill bloqueia se 03-voz tem `versao < 2` (significa que ainda está rascunho).

### `bestseller-book`

**Padrão:** LÊ
**Lê:** `06-mecanismo`, `07-historia-metodo`, `17-cases`

Estrutura de livro segue história do método + mecanismo central + cases ilustrativos.

### `skill-historia-metodo`

**Padrão:** GRAVA-E-LÊ
**Lê:** `00-anamnese.json` (extrai `historia.como_chegou_aqui` e `momento_decisivo`)
**Grava:** `07-historia-metodo.json`

### `criativos-mentorados` + skills filhas (`-dor-beneficio`, `-urgencia`, `-retargeting`, `-qa-instagram`)

**Padrão:** LÊ
**Lê:** `03-voz`, `05-persona`, `09-brand`, `11-oferta`

Geram criativos com identidade visual da mentorada (foto, fonte, cor) puxada de 09-brand. Foto da mentorada vem de campo específico em 09 (não está em arquivo separado).

### `analise-anuncio-1000`

**Padrão:** LÊ-E-GRAVA (parcial)
**Lê:** `06-mecanismo`, `08-posicionamento`, `13-funil`
**Grava:** entrada em `18-historico-decisoes.json` tipo `auditoria-criativo`

Audita criativos contra o mecanismo declarado. Reporta gaps.

### `bencivenga-method`

**Padrão:** LÊ
**Lê:** `03-voz`, `06-mecanismo`, `17-cases`

Score Bencivenga de copy depende de proof stack (17-cases) e mecanismo nomeável (06).

### `copy-editing`, `copywriting`, `the-rewrite-room`, `humanise-text`

**Padrão:** LÊ
**Lê:** `03-voz` (mínimo), opcionalmente `05-persona`, `06-mecanismo`

Toda skill de edição/reescrita de copy lê 03-voz como hook automático.

---

<a id="grupo-3"></a>
## GRUPO 3 — Skills de Oferta, Programa e Posicionamento

### `posicionamento-estrategico`

**Padrão:** GRAVA-E-LÊ
**Lê:** `00-anamnese`, `01-perfil`, `06-mecanismo`, `17-cases`
**Grava:** `08-posicionamento.json`

### `programa`

**Padrão:** GRAVA-E-LÊ
**Lê:** `01-perfil`, `06-mecanismo`, `08-posicionamento`
**Grava:** `10-programa.json`

### `skill-oferta-irresistivel`

**Padrão:** GRAVA-E-LÊ
**Lê:** `06-mecanismo`, `08-posicionamento`, `10-programa`, `17-cases`
**Grava:** `11-oferta.json`

Stack de valor depende de cases reais (17). Sem cases, skill sugere oferta com bônus + garantia mas avisa que conversão será baixa.

### `stack-closer`

**Padrão:** LÊ
**Lê:** `11-oferta`, `06-mecanismo`, `17-cases`

Script de fechamento usa elementos do stack já definido em 11.

### `skill-pitch-high-ticket`

**Padrão:** LÊ
**Lê:** `06-mecanismo`, `08-posicionamento`, `11-oferta`, `17-cases`

### `garantia-irresistivel`

**Padrão:** LÊ-E-GRAVA (parcial — atualiza só campo `garantia` em 11-oferta)
**Lê:** `11-oferta`, `17-cases`

### `skill-produto-entrada`

**Padrão:** LÊ-E-GRAVA
**Lê:** `01-perfil`, `05-persona`, `08-posicionamento`
**Grava:** `11-oferta.json` (campo `ofertas_complementares`)

### `pricing-strategy`

**Padrão:** LÊ
**Lê:** `08-posicionamento`, `10-programa`, `11-oferta`, `16-kpis-dashboard`

### `luxe-empire`

**Padrão:** LÊ-E-GRAVA
**Lê:** `01-perfil`, `08-posicionamento`, `09-brand`
**Grava:** atualizações em `08-posicionamento` (campos `tom_premium`, `frase_de_posicionamento`)

### `brand-guidelines`

**Padrão:** GRAVA-E-LÊ
**Lê:** `01-perfil`, `03-voz`, `08-posicionamento`
**Grava:** `09-brand.json`

### `theme-factory`, `design-page-builder`, `ui-ux-pro-max`

**Padrão:** LÊ
**Lê:** `09-brand` (paleta, tipografia, fotografia)

---

<a id="grupo-4"></a>
## GRUPO 4 — Skills de Tráfego, Funil e Performance

### `funil-completo`, `funil-novela`, `funil-registro`, `skill-funil-webinar`

**Padrão:** GRAVA-E-LÊ
**Lê:** `05-persona`, `08-posicionamento`, `11-oferta`
**Grava:** `13-funil.json`

### `maestro-trafego`

**Padrão:** GRAVA-E-LÊ
**Lê:** `01-perfil`, `05-persona`, `11-oferta`, `13-funil`
**Grava:** atualizações em `13-funil.json` (campos de tráfego)

### `ads`, `ads-meta`, `ads-google`, `ads-tiktok`, `ads-linkedin`, `ads-microsoft`, `ads-youtube`, `ads-instagram-organic`

**Padrão:** LÊ
**Lê:** `13-funil`, `16-kpis-dashboard`, `11-oferta`, `09-brand`

### `ads-creative`, `ad-creative`, `criativos-dor-beneficio`, `criativos-urgencia`, `criativos-retargeting`

**Padrão:** LÊ
**Lê:** `03-voz`, `05-persona`, `06-mecanismo`, `09-brand`, `11-oferta`

### `ads-audit`, `ads-budget`, `ads-plan`, `ads-landing`, `ads-remarketing-audit`, `ads-competitor`, `ads-audience-architect`

**Padrão:** LÊ
**Lê:** `13-funil`, `16-kpis-dashboard`

### `ab-test-setup`, `analytics-tracking`

**Padrão:** LÊ-E-GRAVA
**Lê:** `13-funil`
**Grava:** atualizações em `13-funil` (campos de experimento ativo)

### `webinario`, `webinario-perfeito`, `otimizador-webinario`, `palco-digital`

**Padrão:** LÊ
**Lê:** `06-mecanismo`, `07-historia-metodo`, `11-oferta`, `17-cases`

### `seo-audit`, `programmatic-seo`, `ai-seo`, `schema-markup`

**Padrão:** LÊ
**Lê:** `08-posicionamento`, `09-brand`, `11-oferta`

### Skills CRO (`form-cro`, `popup-cro`, `signup-flow-cro`, `paywall-upgrade-cro`, `onboarding-cro`, `page-cro`, `smart-popup`, `ads-landing`)

**Padrão:** LÊ
**Lê:** `13-funil`, `16-kpis-dashboard`, `05-persona`

---

<a id="grupo-5"></a>
## GRUPO 5 — Skills de Infra, Deploy e Operação

### `skill-deploy-vps`

**Padrão:** GRAVA-E-LÊ
**Lê:** `01-perfil`, `12-infra`
**Grava:** `12-infra.json`

Bloqueio duro: skill RECUSA gravar credenciais. Só metadados. Senhas vão pro 1Password (campo `credencial_em` aponta).

### `imperio-infra`

**Padrão:** GRAVA-E-LÊ
**Lê:** `12-infra`
**Grava:** `12-infra.json` (configs operacionais — hooks, monitoramento, backups)

### `whatsapp-connect`, `whatsapp-ai-bot`, `lara-builder`, `imperatriz-bot`

**Padrão:** LÊ-E-GRAVA
**Lê:** `03-voz`, `05-persona`, `11-oferta`, `12-infra`
**Grava:** atualizações em `12-infra` (porta + status do bot)

### `login-mentoradas`, `logindealunosporconvite`

**Padrão:** GRAVA-E-LÊ
**Lê:** `12-infra`
**Grava:** `12-infra.json` (configs de auth do projeto)

### Skills de produção/automação (`agent-orchestration`, `mcp-builder`, `imperio-multi`, `imperatriz-multiagentes`)

**Padrão:** LÊ
**Lê:** `12-infra`, `01-perfil`

---

<a id="grupo-6"></a>
## GRUPO 6 — Skills de Orquestração, Dashboard e Auditoria

### `tatou-2.0`

**Padrão:** GRAVA-E-LÊ (orquestrador supremo)
**Lê:** TODOS os profiles
**Grava:** `14-progresso.json`, `18-historico-decisoes.json`

É o cérebro orquestrador. Toda chamada de skill passa por `tatou-2.0` que:
1. Detecta mentorada-em-contexto
2. Lê `14-progresso` pra saber porta atual
3. Roda skill pedida
4. Atualiza `14-progresso` se gate concluído
5. Cria entrada em `18-historico-decisoes` se decisão crítica

### `gates-imperatriz`

**Padrão:** LÊ-E-GRAVA (parcial)
**Lê:** TODOS
**Grava:** atualizações em `14-progresso.json` (campos `gates_status`)

Valida se mentorada pode passar pra próxima porta. Critérios são lidos cross-profile (ex: porta J fechada exige `06-mecanismo.scoring.estruturais_13 == 13` E `13-funil.kpis_funil.ROAS >= 1.5`).

### `hierarquia-imperatriz`

**Padrão:** GRAVA-E-LÊ
**Lê:** `14-progresso`, `16-kpis-dashboard`
**Grava:** `15-nivel.json`

Promoção entre níveis (Aspirante → Princesa → Duquesa → Imperatriz) é automática quando critérios fecham.

### `dashboard-imperatriz`

**Padrão:** GRAVA-E-LÊ (heavy reader)
**Lê:** `13-funil`, `01-perfil` (cálculo de meta)
**Grava:** `16-kpis-dashboard.json`

Roda mensalmente (cron). Lê funil, calcula KPIs do mês, grava snapshot.

### `cases-imperatriz`

**Padrão:** GRAVA-E-LÊ
**Lê:** existing `17-cases.json`
**Grava:** `17-cases.json` (append de novos cases)

Append-only por padrão. Updates de campo `autorizacao_uso_publico` são permitidos.

### `celeste`

**Padrão:** LÊ (heavy)
**Lê:** TODOS os 19 profiles

Skill estratégica de Tata. Lê tudo, gera plano de ação, dashboard interativo, cheat sheet pra call 1:1.

### `kaizen-improvement`, `qa-expert`, `verification-gate`, `fact-checker`, `imperio-qualidade`

**Padrão:** LÊ
**Lê:** profiles relevantes pra auditoria

### `health-score`, `scale-audit`, `security-audit`, `security-review`, `guardian`, `scanner`, `shield`

**Padrão:** LÊ
**Lê:** `12-infra`, `13-funil`, `16-kpis-dashboard`

### `imperio-memoria`

**Padrão:** OBSERVA
**Lê:** todos

Skill paralela de memória de agentes IA. Não modifica dossiê — só consulta pra dar contexto a outros agentes IA do negócio.

### `glossariodatata`

**Padrão:** LÊ
**Lê:** `06-mecanismo` (pra detectar termos proprietários da mentorada)

Adiciona termos cunhados pela mentorada ao glossário público (com permissão dela).

---

<a id="hooks"></a>
## HOOKS AUTOMÁTICOS

Configurados via `update-config` em `~/.claude/settings.json`:

```json
{
  "hooks": {
    "before_skill_execute": [
      {
        "match": "*",
        "command": "/dossie-mentorada --ler {mentorada_atual} todos --modo injetar-contexto"
      }
    ],
    "after_skill_execute": [
      {
        "match": "anamnese-mentorada|perfil-mentorada|imperio-diagnostico|voz-de-marca-builder|skill-persona-profunda|mecanismo-unico|skill-historia-metodo|posicionamento-estrategico|brand-guidelines|programa|skill-oferta-irresistivel|skill-deploy-vps|funil-completo",
        "command": "/dossie-mentorada --gravar {mentorada_atual} {profile_destino} {output}"
      },
      {
        "match": "*",
        "command": "/dossie-mentorada --append-historico {mentorada_atual} {skill_nome} {acao_resumida}"
      }
    ]
  }
}
```

### Variáveis injetadas pelos hooks

- `{mentorada_atual}` — slug detectado de:
  1. argumento explícito `--mentorada [slug]`
  2. variável de ambiente `IMPERIO_MENTORADA_ATUAL`
  3. cwd contém `~/imperio/mentoradas/[slug]/`
- `{profile_destino}` — declarado pela skill em metadata (frontmatter `dossie_destino: 06-mecanismo`)
- `{output}` — JSON estruturado retornado pela skill

### Skills sem `dossie_destino` declarado

Skills puramente leitoras (copy, criativos, ads) NÃO declaram `dossie_destino`. Hook só dispara `--ler` antes, não `--gravar` depois.

---

<a id="fluxo-completo"></a>
## FLUXO DE DADOS PONTA-A-PONTA

Exemplo realístico: mentorada Maria entra na Travessia, percorre Porta A até Porta J.

### Dia 1 — Porta A (Aterrissagem)

```
1. Tata cria mentorada
   /dossie-mentorada --criar "Maria Silva"
   → ~/imperio/mentoradas/maria-silva/ criada com 19 JSONs vazios
   → 14-progresso.porta_atual = "A0"

2. Maria responde formulário
   /anamnese-mentorada --formulario maria-silva
   → grava 00-anamnese.json
   → hook: 04-CLAUDE.md atualizado (importa anamnese)
   → 14-progresso.porta_atual = "A1"

3. Sistema sintetiza perfil
   /perfil-mentorada maria-silva
   → lê 00, grava 01-perfil.json
   → 14-progresso.porta_atual = "A2"

4. Diagnóstico
   /imperio-diagnostico maria-silva
   → lê 00 + 01, grava 02-diagnostico.json
   → cria entrada em 18-historico tipo "diagnostico-inicial"
   → 14-progresso.porta_atual = "P" (Posicionamento, próxima)
```

### Dia 7 — Porta P (Posicionamento)

```
5. Voz de marca
   /voz-de-marca-builder maria-silva
   → lê 00 + 01 (extrai amostras de voz natural)
   → grava 03-voz-de-marca.json (versao 1)

6. Persona profunda
   /skill-persona-profunda maria-silva
   → lê 00 + 01 + 02
   → grava 05-persona.json

7. Mecanismo único
   /mecanismo-unico maria-silva
   → lê 00 + 02 + 05 + 17 (vazio ainda)
   → AVISA: "sem cases ainda, proof stack ficará magro"
   → grava 06-mecanismo.json
   → cria entrada em 18-historico tipo "mecanismo-v1-criado"

8. História do método
   /skill-historia-metodo maria-silva
   → lê 00 (campo historia.como_chegou_aqui)
   → grava 07-historia-metodo.json

9. Posicionamento
   /posicionamento-estrategico maria-silva
   → lê 00 + 01 + 06 + 17
   → grava 08-posicionamento.json

10. Sincronização
    /dossie-mentorada --sincronizar maria-silva
    → detecta: voz em 03 menciona "informal-respeitoso" mas
              posicionamento em 08 declara "premium-acessivel"
    → ALERTA pra Tata: revisar consistência tom premium x voz informal
    → 14-progresso.porta_atual = "E" (próxima)
```

### Dia 30 — Porta J (Jornada — copy + página)

```
20. Headline
    /headline-imperatriz maria-silva
    → hook before: lê 03 + 05 + 06 + 08 + 11
    → bloqueio: detecta que 11-oferta não foi preenchida ainda
    → AVISA: "rode /skill-oferta-irresistivel antes"

21. Oferta primeiro
    /skill-oferta-irresistivel maria-silva
    → lê 06 + 08 + 10 + 17 (3 cases coletados nas portas anteriores)
    → grava 11-oferta.json

22. Headlines
    /headline-imperatriz maria-silva
    → lê 03 + 05 + 06 + 08 + 11
    → gera 5 variações por temperatura (frio/morno/quente/hot)
    → output volta pra Tata escolher
    → quando escolhida, atualiza campo em 11-oferta.headlines_aprovadas

23. Página
    /skill-pagina-vendas maria-silva
    → lê 03 + 05 + 06 + 07 + 08 + 09 + 10 + 11 + 17
    → gera HTML completo + design + copy
    → /dossie-mentorada --gravar maria-silva 13-funil
       (registra URL da página + estrutura)

24. Auditoria Bencivenga
    /bencivenga-method maria-silva [url-da-pagina]
    → lê 03 + 06 + 17
    → score 8.7
    → cria entrada em 18-historico tipo "auditoria-pagina-bencivenga"

25. Gate da Porta J
    /gates-imperatriz validar maria-silva J
    → lê 06 + 11 + 13
    → critério: Bencivenga >= 8.0 ✓
    → critério: página live com checkout ✓
    → APROVA porta J
    → 14-progresso.porta_atual = "I" (próxima)
    → 18-historico: entrada tipo "porta-J-aprovada"

26. Verificação de promoção
    /hierarquia-imperatriz maria-silva
    → lê 14 + 16
    → critério Princesa atendido (já era)
    → critério Duquesa: precisa porta M ✗
    → mantém Princesa
    → 15-nivel.tempo_no_nivel_meses += 1
```

---

<a id="confidencialidade"></a>
## CONFIDENCIALIDADE ENTRE MENTORADAS

Cross-contamination de dados é **bloqueio crítico**. A skill garante isolamento por:

### 1. Slug = escopo

Toda operação exige slug explícito. Operação sem slug é REJEITADA.

```
/dossie-mentorada --ler 06-mecanismo
ERRO: slug obrigatório. Use /dossie-mentorada --ler [slug] 06-mecanismo
```

### 2. Cwd-detection com bloqueio

Se Claude está em cwd `~/imperio/mentoradas/maria-silva/` e chama `--ler ana-paula`, a skill ALERTA e exige confirmação dupla.

### 3. Hook de injeção de contexto isola

```python
# Pseudo-código do hook
def injetar_contexto(skill, mentorada_slug):
    contexto = dossie.ler(mentorada_slug, "todos")
    skill.contexto_disponivel = filtrar_apenas_slug(contexto, mentorada_slug)
    # qualquer dado de outro slug é descartado antes de chegar à skill
```

### 4. Logs agregados anonimizam

`dashboard-imperatriz --consolidado` mostra Corte inteira mas com dados ANONIMIZADOS quando exibe métricas comparativas (sem nomes, só slugs hash).

### 5. Skills de IA externa (LLM provider) recebem só profile da mentorada-atual

Quando uma skill envia contexto pra Claude/GPT externo, só profiles da mentorada-atual entram no payload. Nunca dump global.

### 6. Backup é por mentorada

Cada mentorada tem `.backups/` próprio. Backup global da Tata é encriptado.

### 7. Auditoria periódica

`/dossie-mentorada --auditar-confidencialidade` (mensal) varre logs em busca de cross-references suspeitas e reporta.

---

## PADRÕES DE FRONTMATTER PRA SKILLS

Toda skill que grava no dossiê DEVE declarar destino em frontmatter:

```yaml
---
name: skill-persona-profunda
description: ...
dossie_destino: 05-persona
dossie_le: [00-anamnese, 01-perfil, 02-diagnostico]
dossie_modo: GRAVA-E-LE
---
```

Skills puramente leitoras:

```yaml
---
name: copywriting
description: ...
dossie_le: [03-voz-de-marca, 05-persona, 06-mecanismo, 11-oferta]
dossie_modo: LE
---
```

`tatou-2.0` parseia frontmatter pra ativar hooks corretos.

---

## TESTES DE INTEGRAÇÃO

Toda nova skill que se conecta ao dossiê deve passar:

1. **Teste de leitura limpa** — skill rodando em dossiê vazio NÃO crasha, retorna mensagem amigável pedindo dados
2. **Teste de gravação válida** — output da skill passa schema validation
3. **Teste de re-execução** — rodar skill 2x não cria duplicatas, só incrementa `versao`
4. **Teste de slug-isolation** — skill rodando com slug A não enxerga dados de slug B
5. **Teste de hook before/after** — hooks disparam corretamente
6. **Teste de stale** — skill detecta profile com `stale: true` e avisa

Implementados em `~/.claude/skills/dossie-mentorada/tests/` (planejado v1.5).

---

## RESUMO VISUAL DO ECOSSISTEMA

```
                       [tatou-2.0 — orquestrador]
                                  │
                ┌─────────────────┼─────────────────┐
                │                 │                 │
        [GRAVAM 28+]      [LEEM TODAS ~225]   [OBSERVAM ~10]
                │                 │                 │
                └─────────► dossie-mentorada ◄──────┘
                                  │
                            ~/imperio/mentoradas/
                              ├── maria-silva/
                              │   └── 19 JSONs
                              ├── ana-paula/
                              │   └── 19 JSONs
                              └── ...
```

---

**Integração Ecossistema — Dossiê Mentorada v1.0. Propriedade intelectual Tata Gonçalves.**
