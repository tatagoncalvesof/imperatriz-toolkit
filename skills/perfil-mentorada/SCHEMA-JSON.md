# SCHEMA JSON — `01-perfil.json`

> Esse documento define a estrutura do arquivo `01-perfil.json` gerado pela skill `/perfil-mentorada` ao final da classificação. O arquivo é **fonte de verdade** da mentorada nas demais etapas da Travessia Imperatriz — todas as skills downstream (dossie-mentorada, voz-de-marca-builder, /tatou customizado, etc.) consomem esse JSON.

---

## LOCALIZAÇÃO

```
~/Documents/Obsidian Vault/03 - Projetos/Travessia-Imperatriz/Mentoradas/[nome-da-mentorada]/01-perfil.json
```

Mesmo diretório onde mora `00-anamnese.json`. Se reclassificada, a skill arquiva versão anterior como `01-perfil-v1.json`, `01-perfil-v2.json` e mantém `01-perfil.json` sempre como o atual.

---

## SCHEMA COMPLETO

```json
{
  "$schema": "https://travessia-imperatriz.com/schemas/perfil-mentorada-v1.json",
  "versao_schema": "1.0",
  "versao_perfil": 1,

  "mentorada": {
    "nome": "Camila Vasconcelos",
    "instagram_handle": "@camila.financiarealfeminino",
    "anamnese_referencia": "00-anamnese.json",
    "data_anamnese": "2026-04-28"
  },

  "classificacao": {
    "data": "2026-05-08",
    "validado_por": "Tata Goncalves",
    "validado_pela_mentorada": true,
    "data_validacao_mentorada": "2026-05-08",

    "perfil_principal": {
      "id": "vendedora-avulsa",
      "nome": "Vendedora Avulsa",
      "score": 86
    },

    "perfil_secundario": {
      "id": null,
      "nome": null,
      "score": null
    },

    "delta_top1_top2": 26,
    "hibrido": false,
    "confianca": "alta",

    "boost_aplicado": null,
    "boost_motivo": null
  },

  "sinais": {
    "sinal_1_faturamento": {
      "valor": "medio",
      "fonte": "anamnese.faturamento_atual",
      "valor_bruto": "R$ 17.000/mes media 6 meses",
      "peso": 0.15
    },
    "sinal_2_produto": {
      "valor": "1_a_1",
      "fonte": "anamnese.produto_atual + deep_research",
      "valor_bruto": "consultoria financeira individual R$ 4.500",
      "peso": 0.15
    },
    "sinal_3_formato_venda": {
      "valor": "agenda_atendimento",
      "fonte": "anamnese.formato_atual_de_venda + site",
      "valor_bruto": "site com agenda online + DM",
      "peso": 0.12
    },
    "sinal_4_origem_cliente": {
      "valor": "indicacao",
      "fonte": "anamnese.origem_dos_clientes",
      "valor_bruto": "100% indicacao de clientes anteriores",
      "peso": 0.08
    },
    "sinal_5_tempo_mercado": {
      "valor": "mais_7_anos",
      "fonte": "anamnese.tempo_no_mercado",
      "valor_bruto": "11 anos de mercado",
      "peso": 0.06
    },
    "sinal_6_audiencia": {
      "valor": "pequena_engajada",
      "fonte": "deep_research.instagram",
      "valor_bruto": "8.400 seguidores, engajamento 4,2%",
      "peso": 0.08
    },
    "sinal_7_mecanismo": {
      "valor": "embrionario",
      "fonte": "anamnese.mecanismo_unico",
      "valor_bruto": "Metodo PRA Mulher na cabeca, sem nome publico",
      "peso": 0.06
    },
    "sinal_8_time": {
      "valor": "1_a_2",
      "fonte": "anamnese.estrutura_time",
      "valor_bruto": "ela + assistente de agenda",
      "peso": 0.06
    },
    "sinal_9_origem_conhecimento": {
      "valor": "profissao_pratica_longa",
      "fonte": "anamnese.formacao + tempo_no_mercado",
      "valor_bruto": "CFP + 11 anos atendendo mulheres",
      "peso": 0.06
    },
    "sinal_10_tom": {
      "valor": "intimo_amigo",
      "fonte": "deep_research.instagram + anamnese.voz",
      "valor_bruto": "tom proximo, didatico, sem jargao",
      "peso": 0.06
    },
    "sinal_11_copy_agressivo": {
      "valor": "aceita_com_filtro",
      "fonte": "anamnese.preferencias_copy",
      "valor_bruto": "aceita escassez se for verdadeira",
      "peso": 0.06
    },
    "sinal_12_trilha_desejada": {
      "valor": "produtizar_atendimento_1a1",
      "fonte": "anamnese.objetivo_proximos_12_meses",
      "valor_bruto": "criar produto digital sem perder 1:1",
      "peso": 0.06
    }
  },

  "scoring_completo": {
    "iniciante-zero": 18,
    "vendedora-avulsa": 86,
    "mentora-estabelecida": 52,
    "infoprodutora": 22,
    "empresa-fisica-mentora": 42,
    "especialista-tecnica": 35,
    "empresa-b2b": 25,
    "coach-terapeuta": 60
  },

  "sinais_decisivos": [
    {
      "sinal": "sinal_2_produto",
      "valor": "1_a_1",
      "contribuicao": 14.25,
      "explicacao": "Atendimento individual e a marca registrada da Vendedora Avulsa"
    },
    {
      "sinal": "sinal_1_faturamento",
      "valor": "medio",
      "contribuicao": 13.5,
      "explicacao": "Faixa R$ 5-30k/mes e onde Vendedora Avulsa opera"
    },
    {
      "sinal": "sinal_4_origem_cliente",
      "valor": "indicacao",
      "contribuicao": 7.6,
      "explicacao": "100% indicacao confirma que ainda nao construiu maquina digital"
    }
  ],

  "rota_az": {
    "sequencia": ["A", "F", "G", "J", "Q"],
    "porta_prioridade": "F",
    "estrategia": "Dois Trilhos — manter 1:1 enquanto constroi digital",
    "porta_descricao": {
      "A": "Diagnostico — entender o que sustenta o 1:1",
      "F": "Empacotar conhecimento em produto digital",
      "G": "Oferta irresistivel do produto digital",
      "J": "Primeiro lancamento simples",
      "Q": "Monetizacao da base atual (1:1 viram alunos)"
    }
  },

  "kit_skills": [
    "/skill-mentoria-tata",
    "/programa",
    "/pricing-strategy",
    "/imperatriz-das-vendas",
    "/blueprint-crm-operacional",
    "/skill-historia-metodo",
    "/mecanismo-unico",
    "/skill-oferta-irresistivel",
    "/skill-pagina-vendas",
    "/copy-conversacional-dm"
  ],

  "nao_usar": [
    "/skill-lancamento-digital lancamento gigante na primeira versao",
    "/skill-escala-ads sem produto digital validado",
    "/luxe-empire premium puro (perde base 1:1)",
    "/imperatriz-multiagentes (complexidade desnecessaria nessa fase)"
  ],

  "tempo_meses_estimado": 7,
  "nivel_inicial": "tatico",

  "modulacao_secundario": null,

  "alertas": [
    "Acompanhar mensalmente o split entre faturamento 1:1 vs digital",
    "Reclassificar quando digital atingir >= 50% do faturamento total"
  ],

  "proximas_acoes_recomendadas": [
    "Rodar /dossie-mentorada para gerar dossie executivo",
    "Rodar /voz-de-marca-builder para calibrar voz",
    "Iniciar Porta A da rota: /imperio-diagnostico"
  ],

  "metadata": {
    "skill_versao": "perfil-mentorada-v1.0",
    "gerado_em": "2026-05-08T14:32:00-03:00",
    "duracao_classificacao_minutos": 18,
    "iteracoes_validacao": 2
  }
}
```

---

## CAMPOS OBRIGATÓRIOS vs OPCIONAIS

### Obrigatórios

- `versao_schema`
- `versao_perfil`
- `mentorada.nome`
- `mentorada.instagram_handle`
- `classificacao.data`
- `classificacao.validado_por`
- `classificacao.perfil_principal.id`
- `classificacao.perfil_principal.nome`
- `classificacao.perfil_principal.score`
- `classificacao.delta_top1_top2`
- `classificacao.hibrido`
- `classificacao.confianca`
- `sinais.sinal_X_*` (todos os 12)
- `scoring_completo` (8 perfis)
- `sinais_decisivos` (mínimo 3)
- `rota_az.sequencia`
- `rota_az.porta_prioridade`
- `kit_skills`
- `nao_usar`
- `tempo_meses_estimado`
- `nivel_inicial`
- `metadata`

### Opcionais (preencher quando aplicável)

- `classificacao.perfil_secundario` (só se híbrido = true)
- `classificacao.boost_aplicado` (só se boost foi disparado)
- `modulacao_secundario` (só se híbrido)
- `alertas` (recomendado, mas opcional)
- `proximas_acoes_recomendadas` (recomendado)

---

## VOCABULÁRIO CONTROLADO

### `perfil_principal.id` (8 valores fixos)

```
iniciante-zero
vendedora-avulsa
mentora-estabelecida
infoprodutora
empresa-fisica-mentora
especialista-tecnica
empresa-b2b
coach-terapeuta
```

### `confianca` (3 valores fixos)

```
alta
media
baixa
```

### `nivel_inicial` (5 valores fixos)

```
fase-zero
iniciante
tatico
inteligente
imperio
```

### `rota_az.sequencia` — letras das 26 portas (A-Z)

A rota usa letras A-Z. Pode ter sufixos:
- `A-revisita` — revisita de porta já passada
- `C-profunda` — versão aprofundada da porta
- `F-prioridade` — marca explícita de prioridade
- `K-reduzido` — versão reduzida da porta

### `sinal_X.valor` — vocabulários por sinal

Ver [`LOGICA-CLASSIFICACAO.md`](LOGICA-CLASSIFICACAO.md) — cada sinal tem lista fechada de valores aceitos.

---

## REGRAS DE GRAVAÇÃO

1. **Validação JSON Schema** antes de gravar — campos obrigatórios + tipos + vocabulários controlados
2. **Backup automático** — se já existir `01-perfil.json`, renomear pra `01-perfil-v[N].json` antes de sobrescrever
3. **UTF-8 sem BOM** — arquivo em UTF-8 puro
4. **Indentação:** 2 espaços
5. **Datas:** ISO 8601 com timezone (`2026-05-08T14:32:00-03:00`)
6. **Strings em português:** acentuação correta
7. **Booleans:** `true` / `false` (lowercase, sem aspas)

---

## EXEMPLO DE HÍBRIDO (perfil_secundario preenchido)

```json
{
  "classificacao": {
    "perfil_principal": {
      "id": "vendedora-avulsa",
      "nome": "Vendedora Avulsa",
      "score": 78
    },
    "perfil_secundario": {
      "id": "coach-terapeuta",
      "nome": "Coach/Terapeuta",
      "score": 72
    },
    "delta_top1_top2": 6,
    "hibrido": true,
    "confianca": "media",
    "boost_aplicado": "+20 no coach",
    "boost_motivo": "sinal_11 = rejeita_totalmente — regra fundadora Coach"
  },
  "modulacao_secundario": {
    "ajustes_de_tom": [
      "tom delicado em todas as copy",
      "rejeitar copy de urgencia agressiva"
    ],
    "skills_adicionadas": [
      "/voz-humana-br [modo delicado]",
      "/brand-guidelines [suave]"
    ],
    "skills_removidas": [
      "/criativos-urgencia",
      "/stack-closer agressivo"
    ],
    "ajuste_cronograma_meses": 2,
    "alerta_critico": "Sensibilidade ao tom Coach prevalece — auditar TODA copy"
  }
}
```

---

## CONSUMO DOWNSTREAM

As skills que leem `01-perfil.json` ao iniciar:

| Skill | Campos consumidos | Uso |
|-------|-------------------|-----|
| `/dossie-mentorada` | `perfil_principal`, `rota_az`, `sinais_decisivos` | Montar dossiê executivo |
| `/voz-de-marca-builder` | `sinal_10_tom`, `sinal_11_copy_agressivo`, `perfil_principal` | Calibrar voz inicial |
| `/tatou` (customizado Travessia) | `rota_az`, `kit_skills`, `nao_usar` | Rotear próximo passo |
| `/imperio-diagnostico` (na Travessia) | `nivel_inicial` | Calibrar perguntas iniciais |
| `/mecanismo-unico` (na Travessia) | `sinal_7_mecanismo`, `perfil_principal` | Decidir modo (express vs completo) |
| `/celeste` | tudo | Analisar mentorada pra reunião 1:1 |

---

## VERSIONAMENTO DO SCHEMA

- **v1.0** *(atual)* — 12 sinais, 8 perfis, scoring 0-100, híbrido binário
- **v1.5** *(planejado)* — adicionar `historico_perfil` (lista de reclassificações)
- **v2.0** *(planejado)* — adicionar `metricas_realizadas` (faturamento real após X meses na Travessia) pra feedback loop
- **v3.0** *(planejado)* — `recomendacoes_dinamicas` baseadas em mentoradas similares já classificadas

---

## EXEMPLO MÍNIMO VÁLIDO

Pra casos onde algumas informações não puderam ser extraídas:

```json
{
  "versao_schema": "1.0",
  "versao_perfil": 1,
  "mentorada": {
    "nome": "Maria Exemplo",
    "instagram_handle": "@maria.exemplo"
  },
  "classificacao": {
    "data": "2026-05-08",
    "validado_por": "Tata Goncalves",
    "perfil_principal": {
      "id": "iniciante-zero",
      "nome": "Iniciante Zero",
      "score": 88
    },
    "delta_top1_top2": 46,
    "hibrido": false,
    "confianca": "alta"
  },
  "sinais": { /* 12 sinais com valor + peso */ },
  "scoring_completo": { /* 8 perfis com scores */ },
  "sinais_decisivos": [ /* mínimo 3 */ ],
  "rota_az": {
    "sequencia": ["A", "B", "C", "F", "G", "I", "J"],
    "porta_prioridade": "F"
  },
  "kit_skills": [ /* lista */ ],
  "nao_usar": [ /* lista */ ],
  "tempo_meses_estimado": 4,
  "nivel_inicial": "fase-zero",
  "metadata": {
    "skill_versao": "perfil-mentorada-v1.0",
    "gerado_em": "2026-05-08T14:32:00-03:00"
  }
}
```

---

**Schema versionado, validado, auditável. Toda mentorada com `01-perfil.json` válido pode entrar nas skills downstream sem retrabalho.**

**Método Travessia Imperatriz — propriedade Tata Gonçalves.**
