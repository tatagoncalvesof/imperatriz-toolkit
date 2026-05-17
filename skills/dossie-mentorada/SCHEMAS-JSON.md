# SCHEMAS-JSON — Estrutura dos 19 Arquivos do Dossiê

Todos os 19 arquivos vivem em `~/imperio/mentoradas/[slug]/`. Cada arquivo tem **schema versionado**, **timestamps obrigatórios** e **valores nulos válidos** (skill aceita dossiê vazio).

---

## CAMPOS COMUNS (todos os JSONs)

Todo arquivo JSON tem este envelope obrigatório:

```json
{
  "schema_versao": "1.0",
  "slug": "maria-silva",
  "criado_em": "2026-05-01T10:00:00-03:00",
  "atualizado_em": "2026-05-08T19:33:00-03:00",
  "versao": 3,
  "fonte_skill": "anamnese-mentorada",
  "stale": false,
  "dados": { ... }
}
```

| Campo | Tipo | Validação |
|-------|------|-----------|
| `schema_versao` | string | semver (`"1.0"`, `"1.1"`) |
| `slug` | string | `^[a-z0-9-]+$`, obrigatório |
| `criado_em` | string | ISO 8601 com timezone |
| `atualizado_em` | string | ISO 8601 com timezone |
| `versao` | integer | incrementa a cada `--gravar` |
| `fonte_skill` | string | qual skill gerou o último update |
| `stale` | boolean | `true` se passou 6m sem update |
| `dados` | object | conteúdo específico do profile |

Os schemas abaixo descrevem APENAS o `dados`. O envelope é universal.

---

## 00-anamnese.json

**Output de:** `anamnese-mentorada`
**Lido por:** `perfil-mentorada`, `celeste`, `imperio-diagnostico`

Formulário inicial de entrada. Captura quem é a mentorada antes de qualquer diagnóstico.

```json
{
  "dados": {
    "identidade": {
      "nome_completo": "Maria Silva dos Santos",
      "nome_publico": "Maria Silva",
      "idade": 38,
      "cidade": "São Paulo - SP",
      "estado_civil": "casada",
      "tem_filhos": true,
      "instagram": "@mariasilva",
      "site": "https://mariasilva.com.br",
      "email_pessoal": "maria@email.com",
      "whatsapp": "+5511999999999"
    },
    "negocio": {
      "nicho_declarado": "saúde feminina hormonal",
      "tempo_atuacao_anos": 6,
      "tipo_negocio": "mentoria + curso digital",
      "esta_solo": false,
      "tamanho_time": 3,
      "faturamento_mensal_atual_brl": 45000,
      "faturamento_meta_12m_brl": 200000,
      "vende_o_que": "Mentoria 1:1 + curso evergreen + consultoria"
    },
    "historia": {
      "como_chegou_aqui": "Era nutricionista clínica, descobriu nicho hormonal há 4 anos",
      "momento_decisivo": "Caso pessoal de TPM resolvido aos 35",
      "cicatrizes_de_negocio": ["lançamento que fracassou em 2024", "sócia que saiu"],
      "vitorias_recentes": ["primeiros 50k em mês", "case Carla 12kg em 90d"]
    },
    "expectativas": {
      "por_que_travessia": "Quero estruturar pra escalar sem mim no meio",
      "medo_principal": "Não saber se aguenta sair do operacional",
      "compromisso_horas_semana": 12,
      "investimento_disponivel_brl": 25000
    }
  }
}
```

### Validações

- `idade`: 18-99
- `faturamento_mensal_atual_brl`: ≥ 0
- `tempo_atuacao_anos`: ≥ 0
- `instagram`: começa com `@`
- `whatsapp`: E.164 (`+55...`)

---

## 01-perfil.json

**Output de:** `perfil-mentorada`
**Lido por:** `tatou-2.0`, `celeste`, `raci-imperatriz`, `dashboard-imperatriz`

Síntese estratégica da anamnese. Perfil operacional usado pra calibrar todas as outras skills.

```json
{
  "dados": {
    "arquetipo_negocio": "expert-criadora-conteudo",
    "estagio_carreira": "estabelecida-pre-escala",
    "modelo_receita_principal": "high-ticket-mentoria",
    "modelo_receita_secundaria": "curso-evergreen",
    "publico_alvo_resumo": "Mulher 35-50, profissional, com TPM/perimenopausa, faturamento próprio",
    "ticket_medio_brl": 12000,
    "ltv_estimado_brl": 18000,
    "cac_atual_brl": 1800,
    "margem_operacional_pct": 62,
    "canais_aquisicao": ["organico-instagram", "indicacao", "trafego-pago"],
    "stack_tech": ["Hotmart", "ManyChat", "Notion", "WhatsApp Business"],
    "perfis_psicograficos": {
      "openness": "alta",
      "conscientiousness": "media-alta",
      "estilo_decisao": "analitica-emocional",
      "tolerancia_risco": "media"
    },
    "raci": {
      "responsavel": "ela",
      "executor_operacional": "assistente",
      "consultada": "marido + sócia",
      "informada": "time"
    },
    "bandeira_alerta": null
  }
}
```

### Validações

- `arquetipo_negocio`: enum (`expert-criadora-conteudo`, `consultora-b2b`, `agencia`, `infoprodutor`, `mentora-high-ticket`, etc.)
- `estagio_carreira`: enum (`iniciante`, `crescimento`, `estabelecida-pre-escala`, `escala`, `imperio`)
- `ticket_medio_brl`: ≥ 0
- `bandeira_alerta`: null ou string explicando flag (ex: `"em-burnout"`, `"problema-fiscal"`)

---

## 02-diagnostico.json

**Output de:** `imperio-diagnostico`
**Lido por:** `tatou-2.0`, `dashboard-imperatriz`, `celeste`

Diagnóstico aplicando frameworks DOMINIO + FRIO + PENTA da apostila.

```json
{
  "dados": {
    "dominio": {
      "setor": "saude-bem-estar",
      "subsetor": "hormonal-feminino",
      "score_setorial_0_100": 72
    },
    "frio": {
      "f_fundamentos": 8,
      "r_receita": 6,
      "i_imperio": 4,
      "o_oferta": 7,
      "score_total": 25,
      "prioridade_1": "i_imperio",
      "prioridade_2": "r_receita"
    },
    "penta": {
      "nivel_autonomia_atual": 2,
      "nivel_alvo_12m": 4,
      "gargalo_principal": "ela-no-meio-de-toda-venda"
    },
    "diagnostico_textual": "Mentorada em estágio crescimento-estabilidade...",
    "5_acoes_prioritarias": [
      {"acao": "Estruturar funil low-ticket", "impacto": "alto", "esforco": "medio"},
      {"acao": "Documentar mecanismo único", "impacto": "alto", "esforco": "baixo"}
    ],
    "data_diagnostico": "2026-05-01"
  }
}
```

### Validações

- `f_fundamentos`, `r_receita`, `i_imperio`, `o_oferta`: 0-10
- `score_total`: soma dos 4 (0-40)
- `nivel_autonomia_atual`, `nivel_alvo_12m`: 0-5

---

## 03-voz-de-marca.json

**Output de:** `voz-de-marca-builder`
**Lido por:** TODAS as skills de copy (~50)

Voz autoral. Documento mais lido do dossiê. Abastece humanização, headline, copy de página.

```json
{
  "dados": {
    "tom_dominante": "amiga-autoridade",
    "atributos_voz": ["direta", "carinhosa", "tecnica-acessivel", "irreverente-pontual"],
    "atributos_proibidos": ["formal", "corporativo", "guru-mistico", "auto-ajuda-pura"],
    "registro": "informal-respeitoso",
    "nivel_intimidade": "alta",
    "uso_giria": "moderado",
    "uso_palavrao": "raro",
    "vocabulario_assinatura": [
      "imperatriz", "casa-própria", "cortisol travesso", "mente em looping",
      "bagunça hormonal", "TPM que rouba a vida"
    ],
    "vocabulario_banido": [
      "jornada", "transformacional", "empoderamento", "mindset", "delivery",
      "performance", "high-performance", "alavancagem"
    ],
    "frases_assinatura": [
      "Hormônio não é destino — é receita.",
      "Você não tá louca, tá com cortisol travesso."
    ],
    "estilo_pontuacao": {
      "uso_travessao": "nunca",
      "uso_reticencias": "moderado",
      "frase_curta_dominante": true,
      "paragrafo_longo": "raro"
    },
    "exemplos_canonicos": {
      "instagram_post": "[trecho real de post que define a voz]",
      "email": "[trecho real de e-mail]",
      "whatsapp": "[trecho real de WhatsApp]"
    },
    "anti_exemplos": [
      "Vamos juntas embarcar nessa transformação maravilhosa..."
    ]
  }
}
```

### Validações

- `tom_dominante`: enum em catálogo de 12 tons
- `vocabulario_assinatura`: array de 5+ termos
- `frases_assinatura`: array de 3+ frases reais (não inventadas)
- `exemplos_canonicos`: pelo menos 2 dos 3 canais preenchidos

---

## 04-CLAUDE.md

**Output de:** `skill-claude-md-builder`
**Lido por:** toda IA do negócio da mentorada

Caso especial: é **markdown**, não JSON. Mas vive na pasta. Contém manual operacional pra Claude rodar dentro do negócio dela.

Estrutura:

```markdown
# CLAUDE.md — Maria Silva Hormonal

## CONTEXTO DE NEGÓCIO
- Nicho: saúde hormonal feminina
- Público: mulheres 35-50 com TPM/perimenopausa
...

## VOZ DE MARCA
[importado de 03-voz-de-marca.json em modo legível]

## MECANISMO ÚNICO
[importado de 06-mecanismo.json]

## OFERTA ATUAL
[importado de 11-oferta.json]

## REGRAS DURAS
- Não usa "jornada"
- Não usa travessão
- Sempre cita "cortisol travesso" quando falar de TPM
...
```

Frontmatter YAML com metadados:

```yaml
---
slug: maria-silva
schema_versao: 1.0
atualizado_em: 2026-05-08T19:33:00-03:00
versao: 5
fonte_skill: skill-claude-md-builder
sincronizado_de: [03, 05, 06, 08, 09, 11]
---
```

---

## 05-persona.json

**Output de:** `skill-persona-profunda`
**Lido por:** skills de copy, criativos, ads, página de vendas

Persona profunda com 30 dimensões + Buyer Persona + ICP + Mapa de Empatia + Anti-Persona.

```json
{
  "dados": {
    "persona_principal": {
      "nome_fictício": "Carla, 42",
      "demografico": {
        "idade": 42,
        "genero": "feminino",
        "renda_mensal_brl": 18000,
        "escolaridade": "superior-completo",
        "estado_civil": "casada-2-filhos"
      },
      "psicografico": {
        "valores_centrais": ["autonomia", "saude", "familia"],
        "medos_centrais": ["envelhecer-mal", "perder-energia", "ser-substituida"],
        "aspiracoes": ["voltar-a-ter-libido", "perder-peso-sem-dieta"],
        "crencas_limitantes": ["TPM-é-genética", "menopausa-é-fim"]
      },
      "30_dimensoes": {
        "estilo_decisao": "racional-com-overlay-emocional",
        "fonte_de_informacao": ["Instagram-de-medica", "podcast-bem-estar"],
        "horario_consumo_conteudo": "manha-cedo-7h",
        "device_dominante": "mobile-iOS",
        "objecoes_recorrentes": ["preço-alto", "ja-tentei-tudo", "tempo-pra-aplicar"]
      }
    },
    "icp": {
      "criterios_inclusao": [
        "mulher-35-55",
        "renda-10k+",
        "diagnostico-tpm-ou-perimenopausa",
        "abertura-pra-protocolo-natural"
      ],
      "criterios_exclusao": [
        "buscando-pilula-sintetica",
        "renda-menos-6k"
      ]
    },
    "mapa_empatia": {
      "pensa_e_sente": "...",
      "ouve": "...",
      "ve": "...",
      "fala_e_faz": "...",
      "dores": "...",
      "ganhos": "..."
    },
    "anti_persona": {
      "perfil": "Mulher 25-30 buscando emagrecer rápido sem causa hormonal real",
      "por_que_nao_atende": "Não tem o problema-raiz que o método resolve"
    }
  }
}
```

### Validações

- `30_dimensoes`: pelo menos 20 das 30 preenchidas
- `icp.criterios_inclusao`: array de 4+ critérios
- `anti_persona`: obrigatório (skill recusa persona sem anti-persona)

---

## 06-mecanismo.json

**Output de:** `mecanismo-unico`
**Lido por:** `headline-imperatriz`, `briefing-copy-360`, `analise-anuncio-1000`, `bestseller-book`, página de vendas

Estrutura espelha output da skill `mecanismo-unico` (23 critérios validados).

```json
{
  "dados": {
    "nome_proprietario": "Protocolo Hormônio-Casa",
    "nomes_alternativos_descartados": ["Método Imperatriz Hormonal", "Sistema Casa-Própria"],
    "causa_raiz": "Cortisol noturno elevado bloqueia conversão de progesterona pela enzima 21-hidroxilase",
    "vilao_externo": {
      "tipo": "industria-farmaceutica-pilula-sintetica",
      "nomeavel_legalmente_seguro": true
    },
    "razao_fracasso_alheio": "Métodos anteriores tratam sintoma (humor, peso) sem corrigir cascata cortisol→progesterona",
    "metafora_explicativa": {
      "tipo": "casa-cozinha",
      "frase": "Hormônio é receita de bolo. Cortisol noturno é fogão alto demais. Receita queima toda."
    },
    "sequencia_funcionamento": [
      {"passo": 1, "verbo": "Reduzir", "o_que_faz": "cortisol noturno via 3 alavancas"},
      {"passo": 2, "verbo": "Ativar", "o_que_faz": "21-hidroxilase com nutrientes-chave"},
      {"passo": 3, "verbo": "Regular", "o_que_faz": "ciclo via janelas circadianas"}
    ],
    "proof_stack": [
      {"tipo": "cientifico", "fonte": "Cleveland Clinic 2024 n=1.847", "url": "..."},
      {"tipo": "casuistico", "case": "Carla 12kg/90d", "vinculado_a_17_cases": "case-001"},
      {"tipo": "numerico_agregado", "dado": "347 alunas média 6,3kg em 60 dias"}
    ],
    "oponibilidade": "Não é dieta. Não é pílula. Não é jejum. É correção da cascata hormonal cortisol-progesterona.",
    "elevator_pitch_100w": "...",
    "diagrama_visual_descricao": "...",
    "scoring_23_criterios": {
      "estruturais_13": 13,
      "estrategicos_10": 7,
      "classificacao": "nota-1000"
    }
  }
}
```

### Validações

- `nome_proprietario`: 2-4 palavras (anti-pattern de nome longo)
- `proof_stack`: array de 3+ tipos diferentes
- `scoring_23_criterios.estruturais_13`: 13 obrigatório (skill bloqueia se < 13)
- `vilao_externo.nomeavel_legalmente_seguro`: true obrigatório

---

## 07-historia-metodo.json

**Output de:** `skill-historia-metodo`
**Lido por:** `bestseller-book`, `palco-digital`, página de vendas (bloco "minha história"), VSL

Storyline em 5 atos da descoberta pessoal do método.

```json
{
  "dados": {
    "ato_1_estado_inicial": "Era nutricionista clínica padrão...",
    "ato_2_problema_pessoal": "Aos 35 desenvolvi TPM incapacitante...",
    "ato_3_descoberta": "Estudando protocolo X numa conferência...",
    "ato_4_validacao": "Apliquei em 12 pacientes-piloto, 11 resolveram...",
    "ato_5_metodo": "Sistematizei como Protocolo Hormônio-Casa...",
    "duracao_falada_minutos": 3,
    "ganchos_emocionais": ["filha-vendo-mae-irritada", "viagem-cancelada-por-TPM"],
    "personagens_secundarios": ["Dr. Carla (mentora)", "Carla (primeira aluna)"]
  }
}
```

---

## 08-posicionamento.json

**Output de:** `posicionamento-estrategico`
**Lido por:** `brand-guidelines`, `luxe-empire`, headline, página de vendas

```json
{
  "dados": {
    "posicionamento_central": "A nutricionista que decifra o cortisol travesso",
    "categoria_competitiva": "saúde-hormonal-feminina-baseada-em-protocolo",
    "diferenciador_principal": "Único método que ataca cascata cortisol-progesterona",
    "ticket_posicionado": "high-ticket",
    "tom_premium_ou_acessivel": "premium-acessivel",
    "concorrentes_diretos": [
      {"nome": "Dra. X", "diferenca_da_mentorada": "Ela trata sintoma, eu trato causa"},
      {"nome": "Y Hormonal", "diferenca_da_mentorada": "Ele é genérico, eu sou cortisol-first"}
    ],
    "frase_de_posicionamento": "Pra mulher 35-50 com TPM ou perimenopausa que já tentou de tudo, Maria Silva é a nutricionista que ensina o Protocolo Hormônio-Casa, único método baseado em cascata cortisol-progesterona — diferente de pílulas, dietas e jejum.",
    "promessas_centrais": [
      "TPM resolvida em 60 dias",
      "Energia constante sem café",
      "Sono profundo sem remédio"
    ]
  }
}
```

---

## 09-brand.json

**Output de:** `brand-guidelines`
**Lido por:** `design-page-builder`, todas as skills de criativos, `theme-factory`

```json
{
  "dados": {
    "logo_url": "https://cdn.tata.io/maria-silva/logo.svg",
    "logo_variantes": ["primaria", "monocromatica", "negativa", "icone"],
    "paleta_cores": {
      "primaria": "#7B2D26",
      "secundaria": "#F2C57C",
      "neutro_escuro": "#1B1B1E",
      "neutro_claro": "#F5F1EB",
      "alerta": "#C84630"
    },
    "tipografia": {
      "titulos": {"familia": "Playfair Display", "pesos": [600, 700]},
      "corpo": {"familia": "Inter", "pesos": [400, 500]}
    },
    "fotografia": {
      "estilo": "natural-luz-dourada",
      "cenarios_aprovados": ["consultorio-amadeirado", "casa-cozinha", "outdoor-natureza"],
      "vestuario_paleta": ["bege", "vinho", "branco-off"],
      "joias": "ouro-discreto",
      "expressoes_proibidas": ["pose-corporativa-rigida", "sorriso-forcado"]
    },
    "elementos_graficos": {
      "icones_estilo": "linha-fina-organica",
      "ilustracoes": "minimalistas-organicas",
      "padronagens": ["folhas-secas", "ondulacoes-suaves"]
    },
    "voice_visual": "elegancia-feminina-acessivel"
  }
}
```

### Validações

- `paleta_cores.*`: hex válido `#[0-9A-F]{6}`
- `tipografia.titulos.familia`: existe no Google Fonts ou Adobe Fonts
- `logo_variantes`: pelo menos 2 das 4

---

## 10-programa.json

**Output de:** `programa`
**Lido por:** `skill-oferta-irresistivel`, `onboarding-comercial-7dias`

Estrutura curricular do programa principal.

```json
{
  "dados": {
    "nome_programa": "Mentoria Hormônio-Casa",
    "duracao_semanas": 12,
    "formato": "hibrido-ao-vivo-mais-evergreen",
    "modulos": [
      {
        "numero": 1,
        "titulo": "Diagnóstico Hormonal Pessoal",
        "duracao_semanas": 2,
        "aulas": ["Cortisol travesso explicado", "Mapa hormonal seu", "Protocolo de exames"],
        "entregaveis": ["Mapa Hormonal preenchido"]
      }
    ],
    "encontros_ao_vivo": {
      "frequencia": "semanal",
      "duracao_min": 90,
      "formato": "Q&A + hot-seat"
    },
    "comunidade": {
      "plataforma": "Telegram-VIP",
      "moderacao": "assistente"
    },
    "certificacao": false,
    "limite_alunas_turma": 30
  }
}
```

---

## 11-oferta.json

**Output de:** `skill-oferta-irresistivel`
**Lido por:** `skill-pagina-vendas`, `stack-closer`, `webinario`, `email-sequence`

```json
{
  "dados": {
    "oferta_principal": {
      "nome": "Mentoria Hormônio-Casa — Turma 14",
      "preco_brl": 8997,
      "preco_parcelado": "12x R$897",
      "stack_valor": [
        {"item": "12 semanas mentoria ao vivo", "valor_brl": 8000},
        {"item": "Acesso vitalício curso evergreen", "valor_brl": 4997},
        {"item": "Comunidade Telegram VIP", "valor_brl": 1997},
        {"item": "Bônus 1: Protocolo de Exames", "valor_brl": 997}
      ],
      "valor_total_stack_brl": 15991,
      "ancora_premium_brl": 25000,
      "garantia": "7-dias-incondicional",
      "urgencia": "turma-fecha-em-30-dias",
      "escassez": "limite-30-vagas"
    },
    "ofertas_complementares": [
      {"nome": "Curso Hormônio-Casa Solo", "preco_brl": 1497, "tipo": "low-ticket"}
    ],
    "objecoes_top_5_e_resposta": [
      {"objecao": "Já tentei de tudo", "resposta": "Você não tentou Protocolo Hormônio-Casa porque ele só existe há 2 anos..."},
      {"objecao": "Preço alto", "resposta": "Stack de R$15.991 entregue por R$8.997..."}
    ]
  }
}
```

---

## 12-infra.json

**Output de:** `skill-deploy-vps`, `imperio-infra`
**Lido por:** `tatou-2.0`, troubleshooting

**Importante:** NUNCA armazenar credenciais aqui. Só metadados (qual ferramenta, em qual porta). Senhas vão pro 1Password.

```json
{
  "dados": {
    "vps": {
      "provedor": "Hostinger",
      "ip_publico": "147.79.83.123",
      "datacenter": "São Paulo",
      "specs": "8GB RAM / 4 vCPU / 100GB SSD"
    },
    "dominios": [
      {"dominio": "mariasilva.com.br", "registrar": "Registro.br", "expira_em": "2027-03-15"},
      {"dominio": "hormoniocasa.com.br", "registrar": "Hostinger", "expira_em": "2027-08-10"}
    ],
    "stack_aplicacao": [
      {"servico": "Nginx", "porta": 80, "ssl": true},
      {"servico": "Node-funil", "porta": 3001, "pm2": true},
      {"servico": "WhatsApp-bot", "porta": 3002, "pm2": true}
    ],
    "ferramentas_saas": [
      {"nome": "Hotmart", "uso": "checkout", "credencial_em": "1password://maria/hotmart"},
      {"nome": "ManyChat", "uso": "instagram-DM"},
      {"nome": "ActiveCampaign", "uso": "email-marketing"}
    ],
    "backups": {
      "frequencia": "diaria",
      "retencao_dias": 30,
      "destino": "S3-Wasabi"
    },
    "monitoramento": {
      "uptime": "Uptimerobot",
      "logs": "PM2 + Papertrail",
      "alertas": "Telegram-bot-tata"
    }
  }
}
```

### Validações

- `ip_publico`: regex IPv4 ou IPv6 válido
- `credencial_em`: deve começar com `1password://` (forçar uso do gerenciador)
- Bloquear qualquer campo com nome `password`, `senha`, `api_key`, `secret`, `token` (skill recusa)

---

## 13-funil.json

**Output de:** `funil-completo`, `maestro-trafego`
**Lido por:** `dashboard-imperatriz`, `analise-anuncio-1000`, `ads`

```json
{
  "dados": {
    "funil_principal": {
      "nome": "Funil Webinário Mentoria H-Casa",
      "topo": {
        "canal": "Meta Ads",
        "criativos_ativos": 4,
        "cpa_medio_brl": 87,
        "cpm_brl": 35
      },
      "meio": {
        "lead_magnet": "Quiz Hormonal Casa",
        "taxa_conversao_pct": 32,
        "pagina_url": "https://hormoniocasa.com.br/quiz"
      },
      "webinar": {
        "plataforma": "WebinarJam",
        "show_up_pct": 38,
        "stay_pct": 28,
        "compra_pct": 4.2
      },
      "fundo": {
        "checkout_url": "https://hormoniocasa.com.br/checkout",
        "abandono_pct": 64,
        "remarketing_recovery_pct": 12
      }
    },
    "funis_secundarios": [
      {"nome": "Funil Curso Solo", "ticket_brl": 1497, "status": "ativo"}
    ],
    "kpis_funil": {
      "ROAS": 2.8,
      "CPA_compra_brl": 1820,
      "ticket_medio_brl": 8997,
      "LTV_brl": 11500
    },
    "ultima_atualizacao_metricas": "2026-05-07"
  }
}
```

---

## 14-progresso.json

**Output de:** `tatou-2.0`, `gates-imperatriz`
**Lido por:** TODAS

Estado da mentorada na Travessia. Onde ela está nas 23 portas (A-P-E-R-A-I-S-S-I-P-F-U-R-A-L-M-I-S-J-I-B-A-C).

```json
{
  "dados": {
    "porta_atual": "J",
    "porta_letra_significado": "Jornada (copy + página de vendas)",
    "portas_concluidas": ["A", "P", "E", "R", "A", "I", "S", "S", "I", "P", "F", "U", "R", "A", "L", "M", "I", "S"],
    "portas_pendentes": ["I", "B", "A", "C"],
    "data_inicio_travessia": "2026-01-15",
    "data_porta_atual_iniciada": "2026-04-22",
    "dias_na_porta_atual": 16,
    "media_dias_por_porta_ate_aqui": 9,
    "gates_status": {
      "gate_porta_atual_aprovado": false,
      "criterios_pendentes": [
        "Bencivenga 8.0+ na headline da LP",
        "Aprovação visual da página"
      ]
    },
    "bloqueios_ativos": [],
    "proxima_acao_recomendada": "rodar /headline-imperatriz pra resolver gate"
  }
}
```

---

## 15-nivel.json

**Output de:** `hierarquia-imperatriz`
**Lido por:** `tatou-2.0`, `dashboard-imperatriz`, comunicação interna

```json
{
  "dados": {
    "nivel_atual": "princesa",
    "niveis_possiveis": ["aspirante", "princesa", "duquesa", "imperatriz"],
    "criterios_aspirante_atendidos": true,
    "criterios_princesa_atendidos": true,
    "criterios_duquesa_atendidos": false,
    "criterios_duquesa_pendentes": ["concluir-porta-M-modelagem", "primeiro-mes-50k-recorrente"],
    "data_promocao_atual": "2026-03-10",
    "tempo_no_nivel_meses": 2,
    "previsao_proxima_promocao": "2026-08-15"
  }
}
```

### Validações

- `nivel_atual`: enum dos 4 níveis
- Hierarquia respeitada: não pode ser duquesa sem ter sido princesa

---

## 16-kpis-dashboard.json

**Output de:** `dashboard-imperatriz`
**Lido por:** `tatou-2.0`, Tata em call

Snapshot mensal de métricas de negócio.

```json
{
  "dados": {
    "mes_referencia": "2026-04",
    "faturamento_brl": 67000,
    "faturamento_meta_brl": 80000,
    "novos_alunos": 7,
    "ticket_medio_brl": 9571,
    "cac_brl": 1820,
    "ltv_brl": 11500,
    "razao_ltv_cac": 6.3,
    "margem_liquida_pct": 58,
    "tempo_ela_no_operacional_h_semana": 22,
    "satisfacao_alunas_NPS": 71,
    "indicadores_porta_atual": {
      "porta": "J",
      "kpi_principal": "conversao-LP-pct",
      "valor_atual": 0.8,
      "meta": 1.5,
      "status": "amarelo"
    },
    "historico_12m": [
      {"mes": "2025-05", "faturamento_brl": 32000},
      {"mes": "2025-06", "faturamento_brl": 38000}
    ]
  }
}
```

### Validações

- `mes_referencia`: formato `YYYY-MM`
- `razao_ltv_cac`: calculado, não inserido manualmente
- `historico_12m`: array de até 12 meses

---

## 17-cases.json

**Output de:** `cases-imperatriz`
**Lido por:** `bestseller-book`, copy de prova, página de vendas, depoimentos

```json
{
  "dados": {
    "cases": [
      {
        "id": "case-001",
        "aluno_nome": "Carla M.",
        "aluno_idade": 41,
        "aluno_perfil": "advogada-2-filhos",
        "antes": "TPM 10 dias por mês, 8kg de retenção, sem libido",
        "depois": "TPM 2 dias, -12kg em 90d, libido restaurada",
        "tempo_para_resultado_dias": 90,
        "deposit_em_video_url": "https://cdn.tata.io/maria/cases/carla.mp4",
        "depoimento_texto": "...",
        "autorizacao_uso_publico": true,
        "data_autorizacao": "2026-02-15",
        "destacavel_em_pagina_vendas": true,
        "vinculado_ao_mecanismo": "Protocolo Hormônio-Casa"
      }
    ],
    "estatisticas_agregadas": {
      "total_alunos_concluintes": 347,
      "media_perda_peso_kg": 6.3,
      "pct_resolveram_TPM": 87,
      "tempo_medio_resultado_dias": 65
    }
  }
}
```

### Validações

- `autorizacao_uso_publico`: true obrigatório pra usar publicamente (LGPD)
- `data_autorizacao`: obrigatória se `autorizacao_uso_publico` true
- Bloqueio: skill recusa expor case sem autorização

---

## 18-historico-decisoes.json

**Output de:** `tatou-2.0` (automático), Tata (manual via `--gravar`)
**Lido por:** `celeste`, `dashboard-imperatriz`, auditoria

Audit trail de decisões críticas. Append-only.

```json
{
  "dados": {
    "decisoes": [
      {
        "id": "dec-001",
        "data": "2026-03-10T14:00:00-03:00",
        "tipo": "promocao-nivel",
        "descricao": "Mentorada promovida de Aspirante pra Princesa",
        "criterios_atendidos": ["porta-A-concluida", "anamnese-validada", "primeiro-50k"],
        "decidido_por": "tatou-2.0-automatico",
        "validado_por": "tata"
      },
      {
        "id": "dec-002",
        "data": "2026-04-22T10:15:00-03:00",
        "tipo": "pivote-mecanismo",
        "descricao": "Mecanismo evoluiu de v1 (Sistema Hormonal) pra v2 (Protocolo Hormônio-Casa)",
        "razao": "Nome v1 falhou no teste do WhatsApp; v2 aprovado em 5/5 testes",
        "decidido_por": "tata",
        "skill_usada": "mecanismo-unico"
      }
    ]
  }
}
```

### Validações

- Append-only: nunca permitir delete ou update de entradas existentes
- `id`: gerado sequencialmente (`dec-NNN`)
- `tipo`: enum (`promocao-nivel`, `pivote-mecanismo`, `pivote-oferta`, `bandeira-vermelha`, `intervencao-tata`, `lancamento`, `crise`, `vitoria-marco`)

---

## VALIDAÇÃO GLOBAL — `--sincronizar`

A skill cruza profiles pra detectar inconsistências:

| Inconsistência | Profiles envolvidos | Ação |
|----------------|---------------------|------|
| Voz declarada em 03 não casa com posicionamento em 08 | 03, 08 | Alertar Tata |
| Persona em 05 vende ticket diferente da oferta em 11 | 05, 11 | Alertar |
| Mecanismo em 06 não aparece em 13-funil | 06, 13 | Alertar |
| Case em 17 sem autorização sendo usado em copy | 17 | Bloquear publicação |
| Brand em 09 com cor que conflita com voz_visual | 09 | Alertar |
| KPI em 16 não bate com funil em 13 | 13, 16 | Recalcular |
| Profile com `atualizado_em` > 6 meses | qualquer | Marcar `stale: true` |
| Slug em algum profile diferente da pasta | todos | Erro grave — bloquear |

---

## EXEMPLO DE FLUXO `--gravar`

Quando `mecanismo-unico` termina, ela chama:

```
/dossie-mentorada --gravar maria-silva 06-mecanismo "$(output-mecanismo-unico)"
```

A skill:

1. Lê o JSON entregue
2. Valida contra schema de 06-mecanismo
3. Se válido:
   - Lê versão atual
   - Incrementa `versao` (de 2 → 3)
   - Atualiza `atualizado_em`
   - Salva como `06-mecanismo.json`
   - Cria entrada em `18-historico-decisoes.json` se for primeira vez ou pivote
   - Atualiza `04-CLAUDE.md` (re-importa seção de mecanismo)
4. Se inválido:
   - Retorna erro com lista de campos faltantes/inválidos
   - NÃO grava
   - Skill produtora deve corrigir output

---

## SCHEMA VERSIONING

Quando schema mudar (v1.0 → v1.1), seguir migração:

1. Criar `migrations/1.0-to-1.1.js` que transforma JSONs antigos
2. Rodar `/dossie-mentorada --migrar [slug]` (ou `--migrar todas`)
3. Backup automático em `.backups/pre-migration-1.1.zip` antes de migrar
4. Atualizar `schema_versao` em todos os profiles afetados

Nunca quebrar compatibilidade sem migração.

---

**Schemas — propriedade intelectual Tata Gonçalves. Versão 1.0.**
