---
name: dossie-mentorada
description: Sistema de memória persistente da mentorada na Travessia Imperatriz. Lê/grava em 19 arquivos JSON estruturados (anamnese, perfil, voz, mecanismo, brand, oferta, funil, KPIs, cases) e abastece automaticamente todas as ~225 skills do ecossistema com dados da mentorada. Pilar 1 (Dados) — fundação que destrava todas as outras.
---

# DOSSIE-MENTORADA — Sistema de Memória da Travessia

> *"Quem não tem dossiê não tem mentorada — tem desconhecida pagando."*

## FILOSOFIA CENTRAL

A `dossie-mentorada` é a **espinha dorsal** do ecossistema Tata Gonçalves. Ela é o Pilar 1 (Dados) da Travessia Imperatriz e existe pra resolver UM problema crítico:

**Sem memória persistente, cada skill pergunta tudo de novo.** Mentorada cansa, fica inconsistente, e o ecossistema "esquece" quem ela é.

**Solução:** estrutura única em `~/imperio/mentoradas/[nome]/` com 19 arquivos JSON. Cada skill grava seu output ali. Cada skill lê dali antes de gerar.

## QUANDO USAR

- **Primeira ativação:** quando mentorada nova entra (Porta A) — `--criar`
- **Toda skill que produz output:** grava no dossiê — `--gravar`
- **Toda skill que precisa contexto:** lê do dossiê — `--ler`
- **Auditoria periódica:** verificar consistência — `--sincronizar`
- **Visão Tata:** ver status atual da mentorada — `--status`

## REGRA CRÍTICA

**Antes de qualquer skill operar pela 1ª vez na mentorada, o dossiê DEVE estar criado.** Se não existe, o orquestrador `tatou-2.0` força criação automática antes de prosseguir.

---

## OS 7 MODOS DE OPERAÇÃO

### `--criar [nome-mentorada]`
Inicializa estrutura completa em `~/imperio/mentoradas/[nome]/` com os 19 arquivos JSON em estado vazio (schema válido, conteúdo nulo).

### `--ler [nome] [arquivo]`
Retorna conteúdo de um profile específico. Ex: `--ler tata 03-voz-de-marca` retorna voz de marca da Tata.

### `--gravar [nome] [arquivo] [conteudo]`
Grava output estruturado de uma skill no profile correspondente. Hook automático: toda skill com output → grava ao concluir.

### `--status [nome]`
Mostra dashboard rápido: porta atual + nível hierárquico + KPIs do mês + próximo passo recomendado.

### `--sincronizar [nome]`
Valida consistência entre profiles. Detecta inconsistências (ex: voz mencionada em posicionamento diferente da voice profile). Reporta gaps.

### `--listar`
Lista todas as mentoradas do ecossistema com status resumido. Pra Tata enxergar a Corte inteira.

### `--exportar [nome]`
Exporta dossiê completo em formato visual (markdown denso) pra revisão da Tata ou apresentação em call 1:1.

---

## PROCESSO DE INICIALIZAÇÃO (`--criar`)

```
1. Recebe nome da mentorada
2. Sanitiza nome (slug-friendly: "Maria Silva" → "maria-silva")
3. Cria pasta ~/imperio/mentoradas/[slug]/
4. Cria os 19 arquivos JSON com schema válido + valores null
5. Cria CLAUDE.md inicial com placeholders
6. Cria 14-progresso.json com porta-atual: "A0"
7. Cria 15-nivel.json com nivel: "aspirante"
8. Retorna confirmação + caminho da pasta
```

## ESTRUTURA DOS 19 ARQUIVOS

Ver [[SCHEMAS-JSON]] pra detalhes completos. Resumo:

| # | Arquivo | Output de | Lido por |
|---|---------|-----------|----------|
| 00 | anamnese.json | anamnese-mentorada | perfil-mentorada, celeste |
| 01 | perfil.json | perfil-mentorada | tatou-2.0, celeste, raci-imperatriz |
| 02 | diagnostico.json | imperio-diagnostico | tatou-2.0, dashboard-imperatriz |
| 03 | voz-de-marca.json | voz-de-marca-builder | TODAS skills de copy |
| 04 | CLAUDE.md | skill-claude-md-builder | toda IA do negócio |
| 05 | persona.json | skill-persona-profunda | skills de copy, criativos, ads |
| 06 | mecanismo.json | mecanismo-unico | headline-imperatriz, briefing-copy-360 |
| 07 | historia-metodo.json | skill-historia-metodo | bestseller-book, palco-digital |
| 08 | posicionamento.json | posicionamento-estrategico | brand-guidelines |
| 09 | brand.json | brand-guidelines | design-page-builder, criativos-* |
| 10 | programa.json | programa | skill-oferta-irresistivel |
| 11 | oferta.json | skill-oferta-irresistivel | skill-pagina-vendas, stack-closer |
| 12 | infra.json | skill-deploy-vps | tatou-2.0 |
| 13 | funil.json | funil-completo | maestro-trafego, dashboard-imperatriz |
| 14 | progresso.json | tatou-2.0 + gates-imperatriz | TODAS |
| 15 | nivel.json | hierarquia-imperatriz | tatou-2.0, dashboard-imperatriz |
| 16 | kpis-dashboard.json | dashboard-imperatriz | tatou-2.0 |
| 17 | cases.json | cases-imperatriz | bestseller-book, copy de prova |
| 18 | historico-decisoes.json | tatou-2.0 (auto) | celeste, dashboard-imperatriz |

---

## REGRAS DURAS (não negociáveis)

1. **Slug é canônico** — nome da mentorada vira slug minúsculo-com-traço. Sem espaços, sem acentos.
2. **JSON é fonte de verdade** — markdown gerado é só visualização. Escrita SEMPRE no JSON.
3. **Nunca apagar dados** — atualização é versionamento (campo `versao` incrementa). Histórico fica.
4. **Schema versão obrigatória** — todo profile tem `schema_versao` pra migração futura.
5. **Timestamp obrigatório** — todo write registra `atualizado_em` (ISO 8601).
6. **Audit trail** — toda decisão crítica grava em `18-historico-decisoes.json`.
7. **Nenhuma skill grava direto no JSON** — sempre via `--gravar` da dossie-mentorada (garante validação de schema).
8. **Leitura é livre** — qualquer skill pode `--ler` qualquer profile.
9. **Confidencialidade** — dados de uma mentorada NUNCA aparecem no contexto de outra.
10. **Backup automático** — pasta `~/imperio/mentoradas/[nome]/.backups/` com snapshot diário.

---

## INTEGRAÇÃO COM ECOSSISTEMA

### Skills que GRAVAM no dossiê (28+)

- `anamnese-mentorada` → 00
- `perfil-mentorada` → 01
- `imperio-diagnostico` → 02
- `voz-de-marca-builder` → 03
- `skill-claude-md-builder` → 04
- `skill-persona-profunda` → 05
- `mecanismo-unico` → 06
- `skill-historia-metodo` → 07
- `posicionamento-estrategico` → 08
- `brand-guidelines` → 09
- `programa` → 10
- `skill-oferta-irresistivel` → 11
- `skill-deploy-vps` → 12
- `funil-completo` → 13
- `tatou-2.0` → 14, 18
- `gates-imperatriz` → 14
- `hierarquia-imperatriz` → 15
- `dashboard-imperatriz` → 16
- `cases-imperatriz` → 17

### Skills que LEEM do dossiê (todas — ~225)

Toda skill de copy lê 03-voz-de-marca antes de gerar. Toda skill de oferta lê 11-oferta. Etc.

### Hooks automáticos

```python
# Pseudo-código do hook
@before_skill_execute
def carregar_contexto():
    if mentorada in args:
        contexto = dossie.ler(mentorada, "todos")
        skill.injetar_contexto(contexto)

@after_skill_execute
def salvar_output():
    if skill.tem_output_estruturado:
        dossie.gravar(mentorada, skill.profile_destino, skill.output)
```

---

## FORMATO DE OUTPUT

### Modo `--criar`
```
✅ Dossiê criado em: ~/imperio/mentoradas/maria-silva/

19 arquivos JSON inicializados:
  📄 00-anamnese.json (vazio — preencher via /anamnese-mentorada)
  📄 01-perfil.json (vazio)
  ... (lista todos)

Próximo passo: rodar /anamnese-mentorada --formulario maria-silva
```

### Modo `--status`
```
👑 MARIA SILVA · Princesa
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 Porta atual: J (Jornada — copy + página de vendas)
📊 KPIs do mês:
   ✅ Página live (Bencivenga 8.5)
   ✅ Tráfego rodando (CPA R$87)
   ⚠️ Conversão LP: 0.8% (meta: 1-3%)
   
🎯 Próximo passo recomendado:
   → /diagnostico-gargalo-funil maria-silva
   (KPI vermelho detectado em LP)

⏱️  Tempo na Princesa: 4 meses
🎯 Próximo nível: Duquesa (precisa M concluída)
```

### Modo `--exportar`
Markdown denso com TODAS as informações — usado pra apresentação 1:1.

---

## ANTI-PATTERNS

1. **Nunca grave em JSON sem validar schema** — corromper estrutura quebra todas as outras skills
2. **Nunca leia dados de outra mentorada** — confidencialidade absoluta
3. **Nunca apague entrada do histórico** — audit trail é sagrado
4. **Nunca salve credenciais no dossiê** — só metadados; senhas vão pro 1Password
5. **Nunca use nome bruto** — sempre slug
6. **Nunca pule sincronização** — depois de 5 writes seguidos, rodar `--sincronizar`
7. **Nunca trate dossiê vazio como erro** — mentorada nova tem dossiê vazio é normal
8. **Nunca confie em data antiga** — se profile tem 6+ meses sem update, marcar como "stale"
9. **Nunca duplique informação entre profiles** — cada dado vive em UM lugar canônico
10. **Nunca exponha dossiê pra mentorada SEM filtrar** — alguns campos são internos da Tata

---

## INTEGRAÇÃO COM TRAVESSIA IMPERATRIZ

### Pilar 1 (Dados) — esta skill ATENDE
Esta skill é a implementação física do Pilar 1.

### Pilar 2 (Fluxo) — esta skill ALIMENTA
`gates-imperatriz` lê `14-progresso.json` pra validar gates.

### Pilar 4 (Medição) — esta skill ALIMENTA
`dashboard-imperatriz` lê `16-kpis-dashboard.json` pra agregar.

### Pilar 7 (Tribo) — esta skill ALIMENTA
`hierarquia-imperatriz` lê `15-nivel.json` pra mostrar nível.

### Porta A (Aterrissagem) — DEPENDÊNCIA CRÍTICA
Sem dossiê criado, Porta A não pode ser concluída.

---

## VERSIONAMENTO

- **v1.0** (atual) — 19 profiles, 7 modos, hooks automáticos
- **v1.5** (planejado) — sincronização incremental + cache em memória
- **v2.0** (planejado) — interface web pra Tata visualizar Corte inteira
- **v3.0** (planejado) — analytics agregados (insights cross-mentorada)

---

## COMO COMPARTILHAR COM MENTORADAS

Esta skill é **interna do ecossistema Tata** — não compartilhada diretamente. Mentoradas interagem com o dossiê via outras skills (anamnese-mentorada, perfil-mentorada, etc.) que gravam automaticamente.

Mentorada Master+ pode receber acesso de leitura ao próprio dossiê via `--exportar [seu-nome]`.

---

## ARQUIVOS DE REFERÊNCIA

- [[SCHEMAS-JSON]] — schemas detalhados dos 19 arquivos
- [[INTEGRACAO-ECOSSISTEMA]] — como cada skill interage
- [[EXEMPLOS-USO]] — 5+ exemplos práticos
- [[ANTI-PATTERNS]] — armadilhas + antídotos
- [[README]] — instalação e visão geral

---

**Sistema de Memória da Travessia Imperatriz — propriedade intelectual Tata Gonçalves.**
