# Dossiê Mentorada — Sistema de Memória da Travessia Imperatriz

> *"Quem não tem dossiê não tem mentorada — tem desconhecida pagando."*

Sistema de memória persistente do ecossistema Tata Gonçalves. **Pilar 1 (Dados)** da Travessia Imperatriz: estrutura única em `~/imperio/mentoradas/[slug]/` com 19 arquivos JSON que abastecem automaticamente as ~225 skills do ecossistema.

Sem essa skill, cada skill pergunta tudo de novo. Mentorada cansa, fica inconsistente, e o ecossistema esquece quem ela é. Com essa skill, o ecossistema TEM MEMÓRIA — uma vez gravado, toda skill posterior lê dali antes de gerar.

---

## O QUE ELA FAZ

A `dossie-mentorada` é a **espinha dorsal** do ecossistema. Em uma frase: **lê e grava JSON estruturado de cada mentorada e injeta contexto automaticamente nas skills**.

Concretamente, ela:

- **Cria** dossiê completo (19 JSONs com schema válido) em uma chamada
- **Grava** output de qualquer skill no profile correto, validando schema
- **Lê** qualquer profile e injeta contexto na skill seguinte (hook automático)
- **Sincroniza** profiles cruzando informações pra detectar inconsistências
- **Versiona** cada update (campo `versao` incrementa, histórico fica)
- **Audita** decisões críticas em `18-historico-decisoes.json`
- **Exporta** dossiê completo em markdown denso pra apresentação 1:1
- **Lista** todas as mentoradas da Corte com status resumido (visão Tata)

Ela NÃO escreve copy. Ela NÃO gera persona. Ela é a **camada de persistência** que sustenta as skills que fazem isso.

---

## QUANDO USAR

| Situação | Modo |
|----------|------|
| Mentorada nova entra na Travessia (Porta A) | `--criar` |
| Skill terminou e precisa salvar output | `--gravar` (hook automático) |
| Skill vai começar e precisa ler contexto | `--ler` (hook automático) |
| Tata quer ver status de mentorada | `--status` |
| Auditoria periódica de consistência | `--sincronizar` |
| Tata quer ver Corte inteira | `--listar` |
| Preparar call 1:1 com mentorada | `--exportar` |

**Regra crítica:** antes de QUALQUER skill operar pela primeira vez na mentorada, o dossiê DEVE estar criado. Se não existe, o orquestrador `tatou-2.0` força criação automática antes de prosseguir.

---

## INSTALAÇÃO

### Onde mora

```
~/.claude/skills/dossie-mentorada/
├── SKILL.md                      ← cérebro (sempre carregado)
├── README.md                     ← este arquivo
├── SCHEMAS-JSON.md               ← schemas dos 19 JSONs
├── INTEGRACAO-ECOSSISTEMA.md     ← como cada skill interage
├── EXEMPLOS-USO.md               ← 5 exemplos práticos
└── ANTI-PATTERNS.md              ← 10 armadilhas + antídotos
```

### Onde os dados moram

```
~/imperio/mentoradas/
├── maria-silva/
│   ├── 00-anamnese.json
│   ├── 01-perfil.json
│   ├── 02-diagnostico.json
│   ├── 03-voz-de-marca.json
│   ├── 04-CLAUDE.md
│   ├── 05-persona.json
│   ├── 06-mecanismo.json
│   ├── 07-historia-metodo.json
│   ├── 08-posicionamento.json
│   ├── 09-brand.json
│   ├── 10-programa.json
│   ├── 11-oferta.json
│   ├── 12-infra.json
│   ├── 13-funil.json
│   ├── 14-progresso.json
│   ├── 15-nivel.json
│   ├── 16-kpis-dashboard.json
│   ├── 17-cases.json
│   ├── 18-historico-decisoes.json
│   └── .backups/
│       └── snapshot-2026-05-08.zip
├── ana-paula/
│   └── (mesma estrutura)
└── ...
```

A pasta `~/imperio/mentoradas/` é **propriedade da Tata**, nunca compartilhada. Cada mentorada tem subpasta isolada por slug. Cross-contamination de dados entre mentoradas é bloqueio duro (ver [ANTI-PATTERNS](ANTI-PATTERNS.md)).

### Pré-requisitos

- Claude Code instalado em `~/.claude/`
- Pasta `~/imperio/` existente (criada pela primeira execução de `tatou-2.0`)
- Permissão de escrita em `~/imperio/mentoradas/`
- `jq` instalado (validação de schema): `brew install jq`

### Setup inicial (uma vez)

```bash
mkdir -p ~/imperio/mentoradas
cp -r /Users/tamiresgoncalves/Documents/travessia-imperatriz-site/skills-novas/dossie-mentorada ~/.claude/skills/
```

Depois disso, qualquer chamada `--criar [nome]` funciona.

---

## OS 7 MODOS DE OPERAÇÃO

### `--criar [nome-mentorada]`

Inicializa estrutura completa em `~/imperio/mentoradas/[slug]/` com os 19 JSONs em estado vazio (schema válido, valores nulos).

```
/dossie-mentorada --criar "Maria Silva"
```

Saída:
```
Dossiê criado em: ~/imperio/mentoradas/maria-silva/
19 arquivos JSON inicializados com schema_versao 1.0
14-progresso.json: porta_atual = "A0"
15-nivel.json: nivel = "aspirante"

Próximo passo: rodar /anamnese-mentorada --formulario maria-silva
```

### `--ler [slug] [arquivo|todos]`

Retorna conteúdo estruturado de um profile ou todos.

```
/dossie-mentorada --ler maria-silva 03-voz-de-marca
```

Skills usam isso como **hook automático antes de gerar** (toda skill de copy lê 03-voz-de-marca antes de escrever).

### `--gravar [slug] [arquivo] [conteudo-json]`

Grava output estruturado de uma skill no profile correspondente. Valida schema antes de escrever. Incrementa `versao`. Atualiza `atualizado_em`. Cria entrada em `18-historico-decisoes.json` se for decisão crítica.

```
/dossie-mentorada --gravar maria-silva 06-mecanismo "$(cat output-mecanismo.json)"
```

**Nenhuma skill escreve direto no JSON** — sempre passa por `--gravar`. Isso garante validação.

### `--status [slug]`

Dashboard rápido: porta atual + nível hierárquico + KPIs do mês + próximo passo recomendado.

```
/dossie-mentorada --status maria-silva
```

Saída:
```
MARIA SILVA · Princesa
Porta atual: J (Jornada — copy + página de vendas)
Tempo na Princesa: 4 meses
Próximo nível: Duquesa (precisa M concluída)

KPIs do mês:
   Página live (Bencivenga 8.5)
   Tráfego rodando (CPA R$87)
   Conversão LP: 0.8% (meta 1-3%)

Próximo passo recomendado:
   /diagnostico-gargalo-funil maria-silva
```

### `--sincronizar [slug]`

Cruza informações entre profiles. Detecta:
- Voz declarada em 03 inconsistente com posicionamento em 08
- Persona em 05 que não bate com público da oferta em 11
- Mecanismo em 06 ausente nos copies referenciados em 13
- Profiles `stale` (6+ meses sem update)

Reporta gaps. Não corrige automaticamente — sinaliza pra Tata decidir.

### `--listar`

Mostra todas as mentoradas do ecossistema com status resumido. Visão Tata da Corte inteira.

```
ANA-PAULA · Duquesa · Porta M · KPI verde · 8m na Casa
MARIA-SILVA · Princesa · Porta J · KPI amarelo · 4m
JULIANA-COSTA · Aspirante · Porta A · 0m · pendente anamnese
LARISSA-MENDES · Imperatriz · Porta E · KPI verde · 14m · case ativo
```

### `--exportar [slug]`

Markdown denso com TODAS as informações do dossiê — usado pra apresentação em call 1:1, revisão estratégica ou handoff entre Tata e celeste.

```
/dossie-mentorada --exportar maria-silva > ~/Desktop/dossie-maria.md
```

---

## REGRAS DURAS (a skill não negocia)

1. **Slug é canônico** — nome vira slug minúsculo-com-traço. Sem espaços, sem acentos. `Maria José da Silva` → `maria-jose-da-silva`.
2. **JSON é fonte de verdade** — markdown gerado é só visualização. Escrita SEMPRE no JSON.
3. **Nunca apagar dados** — atualização é versionamento (`versao` incrementa). Histórico fica.
4. **Schema versão obrigatória** — todo profile tem `schema_versao` pra migração futura.
5. **Timestamp obrigatório** — todo write registra `atualizado_em` em ISO 8601 (`2026-05-08T19:33:00-03:00`).
6. **Audit trail** — toda decisão crítica grava em `18-historico-decisoes.json`.
7. **Nenhuma skill grava direto no JSON** — sempre via `--gravar` da dossie-mentorada.
8. **Leitura é livre** — qualquer skill pode `--ler` qualquer profile da mentorada-em-contexto.
9. **Confidencialidade** — dados de uma mentorada NUNCA aparecem no contexto de outra. Slug determina escopo.
10. **Backup automático** — `~/imperio/mentoradas/[slug]/.backups/` com snapshot diário (cron `tatou-2.0`).

---

## INTEGRAÇÃO COM O ECOSSISTEMA

### Skills que GRAVAM no dossiê (28+)

Cada skill produtora despeja seu output no profile correspondente:

| Skill | Profile destino |
|-------|-----------------|
| `anamnese-mentorada` | 00-anamnese |
| `perfil-mentorada` | 01-perfil |
| `imperio-diagnostico` | 02-diagnostico |
| `voz-de-marca-builder` | 03-voz-de-marca |
| `skill-claude-md-builder` | 04-CLAUDE.md |
| `skill-persona-profunda` | 05-persona |
| `mecanismo-unico` | 06-mecanismo |
| `skill-historia-metodo` | 07-historia-metodo |
| `posicionamento-estrategico` | 08-posicionamento |
| `brand-guidelines` | 09-brand |
| `programa` | 10-programa |
| `skill-oferta-irresistivel` | 11-oferta |
| `skill-deploy-vps` | 12-infra |
| `funil-completo` | 13-funil |
| `tatou-2.0` | 14-progresso, 18-historico |
| `gates-imperatriz` | 14-progresso |
| `hierarquia-imperatriz` | 15-nivel |
| `dashboard-imperatriz` | 16-kpis-dashboard |
| `cases-imperatriz` | 17-cases |

Detalhes em [INTEGRACAO-ECOSSISTEMA](INTEGRACAO-ECOSSISTEMA.md).

### Skills que LEEM do dossiê (todas — ~225)

Toda skill que produz output relevante pra mentorada lê o dossiê primeiro. Padrão:

- Skills de copy → leem 03-voz, 05-persona, 06-mecanismo, 08-posicionamento
- Skills de oferta → leem 10-programa, 11-oferta, 17-cases
- Skills de tráfego → leem 11-oferta, 13-funil, 16-kpis
- Skills de design → leem 09-brand, 03-voz
- Skills de planejamento → leem 14-progresso, 15-nivel, 02-diagnostico

### Hooks automáticos

Configurados em `~/.claude/settings.json` via `update-config`:

```json
{
  "hooks": {
    "before_skill": "/dossie-mentorada --ler {mentorada} todos",
    "after_skill": "/dossie-mentorada --gravar {mentorada} {profile} {output}"
  }
}
```

Mentorada-em-contexto é detectada por:
1. Argumento explícito (`--mentorada maria-silva`)
2. Variável de ambiente (`IMPERIO_MENTORADA_ATUAL`)
3. Pasta de execução (se cwd está em `~/imperio/mentoradas/[slug]/`)

---

## INTEGRAÇÃO COM TRAVESSIA IMPERATRIZ

### Pilar 1 (Dados) — esta skill ATENDE

Implementação física do Pilar 1. Sem `dossie-mentorada` rodando, Pilar 1 não existe.

### Pilar 2 (Fluxo) — esta skill ALIMENTA

`gates-imperatriz` lê `14-progresso.json` pra validar gates entre portas (A → P → E → R → A → I → S → S → I → P → F → U → R → A → L → M → I → S → J → I → B → A → C).

### Pilar 4 (Medição) — esta skill ALIMENTA

`dashboard-imperatriz` lê `16-kpis-dashboard.json` pra agregar métricas mensais e gerar visão consolidada.

### Pilar 7 (Tribo) — esta skill ALIMENTA

`hierarquia-imperatriz` lê `15-nivel.json` pra mostrar nível atual (Aspirante → Princesa → Duquesa → Imperatriz).

### Porta A (Aterrissagem) — DEPENDÊNCIA CRÍTICA

Sem dossiê criado, Porta A não pode ser concluída. `tatou-2.0` bloqueia avanço.

---

## VERSIONAMENTO

- **v1.0** (atual) — 19 profiles, 7 modos, hooks automáticos, schema validado por jq
- **v1.5** (planejado) — sincronização incremental + cache em memória pra reduzir I/O
- **v2.0** (planejado) — interface web pra Tata visualizar Corte inteira em dashboard
- **v3.0** (planejado) — analytics agregados (insights cross-mentorada anonimizados)

---

## COMO COMPARTILHAR COM MENTORADAS

Esta skill é **interna do ecossistema Tata** — não é compartilhada diretamente com mentoradas. Mentoradas interagem com o dossiê via outras skills (`anamnese-mentorada`, `perfil-mentorada`, `mecanismo-unico`, etc.) que gravam automaticamente.

**Mentorada Master+** pode receber acesso de leitura ao próprio dossiê via:

```
/dossie-mentorada --exportar [seu-slug] --modo mentorada-friendly
```

O modo `mentorada-friendly` filtra campos internos da Tata (notas privadas, scoring de risco, observações de celeste) antes de exportar.

---

## ARQUIVOS DE REFERÊNCIA

- [SKILL.md](SKILL.md) — cérebro da skill (já entregue pela Tata)
- [SCHEMAS-JSON.md](SCHEMAS-JSON.md) — schemas detalhados dos 19 arquivos JSON
- [INTEGRACAO-ECOSSISTEMA.md](INTEGRACAO-ECOSSISTEMA.md) — como cada skill grava/lê
- [EXEMPLOS-USO.md](EXEMPLOS-USO.md) — 5+ exemplos práticos ponta a ponta
- [ANTI-PATTERNS.md](ANTI-PATTERNS.md) — 10 armadilhas + antídotos

---

## FILOSOFIA DA SKILL

> **Memória é diferencial. Sem dossiê, ecossistema é só uma coleção de skills sem cola.**

A `dossie-mentorada` não é glamourosa. Não escreve copy bombástica, não gera mecanismo, não fecha venda. Mas é a camada que faz TODO O RESTO funcionar.

É a diferença entre:
- Mentorada perguntar "qual minha voz de marca?" pela 4ª vez
- Mentorada chegar em qualquer skill e ela já saber tudo

Sistema de Memória da Travessia Imperatriz — propriedade intelectual Tata Gonçalves.
