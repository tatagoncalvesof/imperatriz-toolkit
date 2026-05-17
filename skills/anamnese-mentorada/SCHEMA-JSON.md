# Schema JSON — `00-anamnese.json`

Este e o **contrato de dados** que toda anamnese da Travessia respeita. Qualquer skill que consome anamnese (`/perfil-mentorada`, `/dossie-mentorada`, `/imperio-diagnostico`, `/celeste`) le este schema.

**Caminho do arquivo:**
```
~/imperio/mentoradas/[slug]/00-anamnese.json
```

**Slug:** `nome-sobrenome` em lowercase, sem acento, hifen entre palavras. Ex: `tamires-goncalves`, `carolina-mendes`.

---

## ESTRUTURA RAIZ

```json
{
  "schema_versao": "1.0",
  "skill_versao": "anamnese-mentorada-1.0",
  "slug": "carolina-mendes",
  "data_coleta": "2026-05-08",
  "data_atualizacao": "2026-05-08",
  "coletado_por": "call",
  "responsavel_coleta": "tata",
  "duracao_coleta_min": 78,
  "score_completude": {
    "geral": 92,
    "por_bloco": {
      "1_historico": 100,
      "2_negocio": 100,
      "3_tentativas": 75,
      "4_dores": 100,
      "5_objetivos": 100,
      "6_recursos": 100,
      "7_identidade": 80,
      "8_expectativas": 100
    }
  },
  "alertas_detectados": [],
  "historico": { },
  "negocio": { },
  "tentativas": { },
  "dores": { },
  "objetivos": { },
  "recursos": { },
  "identidade": { },
  "expectativas": { },
  "observacoes_tata": "",
  "proxima_acao_recomendada": "rodar /perfil-mentorada"
}
```

---

## CAMPOS METADADOS

### `schema_versao` (string, obrigatorio)
Versao do schema. Ex: `"1.0"`. Quando schema mudar, anamneses antigas migram via script.

### `skill_versao` (string, obrigatorio)
Versao da skill que gerou. Ex: `"anamnese-mentorada-1.0"`.

### `slug` (string, obrigatorio)
Identificador unico da mentorada. Lowercase, sem acento, hifen.

### `data_coleta` (ISO 8601, obrigatorio)
Data da primeira coleta. Ex: `"2026-05-08"`.

### `data_atualizacao` (ISO 8601, obrigatorio)
Data da ultima atualizacao. Atualiza toda vez que `--validar` ou re-coleta acontece.

### `coletado_por` (enum, obrigatorio)
Modo de coleta:
- `"formulario"` — mentorada preencheu HTML standalone
- `"call"` — Tata conduziu entrevista
- `"auto"` — deep-research pre-populou
- `"hibrido"` — combinacao (ex: auto + call de validacao)

### `responsavel_coleta` (string, obrigatorio)
Quem coletou. Ex: `"tata"`, `"severino"`, `"automatica"`.

### `duracao_coleta_min` (numero, opcional)
Quantos minutos durou. Util pra modo `--call`.

### `score_completude` (objeto, obrigatorio)
- `geral` (0-100): media dos blocos
- `por_bloco`: percentual por bloco

### `alertas_detectados` (array, obrigatorio)
Riscos identificados durante coleta. Ver secao **Alertas** abaixo.

### `observacoes_tata` (texto, opcional)
Notas livres da Tata pos-call. Nunca vai pro formulario; so na call.

### `proxima_acao_recomendada` (string, obrigatorio)
String com proximo passo. Ex: `"rodar /perfil-mentorada"`, `"fechar gap bloco 3 com mini-call"`, `"refazer bloco 5"`.

---

## BLOCO 1 — `historico` (objeto)

```json
{
  "historico": {
    "nome_completo": "Carolina Aparecida Mendes",
    "idade": 37,
    "localizacao": {
      "cidade": "Curitiba",
      "estado": "PR",
      "pais": "BR"
    },
    "estado_civil": "casada",
    "filhos": {
      "tem": true,
      "quantidade": 2,
      "idades": [8, 12]
    },
    "formacao": [
      {
        "curso": "Direito",
        "instituicao": "PUC-PR",
        "ano_conclusao": 2010
      },
      {
        "curso": "MBA em Gestao",
        "instituicao": "FGV",
        "ano_conclusao": 2017
      }
    ],
    "trajetoria_profissional": "Trabalhei 8 anos como advogada em escritorio grande. Em 2019 abri meu proprio. Em 2022 comecei a postar conteudo de carreira juridica no Insta. Em 2024 fiz minha primeira mentoria 1-a-1 e descobri que era o que queria.",
    "trajetoria_timeline": [
      {"ano": 2010, "evento": "formada Direito PUC-PR"},
      {"ano": 2011, "evento": "advogada em escritorio Souza & Souza"},
      {"ano": 2019, "evento": "abriu escritorio proprio"},
      {"ano": 2022, "evento": "comecou conteudo no Insta"},
      {"ano": 2024, "evento": "primeira mentoria"}
    ],
    "canal_origem": "webinar com Renata Ferraz",
    "aquecimento_pre_compra": "quente",
    "auto_descricao_uma_frase": "Sou advogada que ensina outras advogadas a viver de mentoria"
  }
}
```

**Estado civil — enum:** `"solteira"`, `"casada"`, `"uniao_estavel"`, `"divorciada"`, `"viuva"`, `"prefiro_nao_dizer"`.

**Aquecimento — enum:** `"frio"` (nao conhecia), `"morno"` (segue ha < 6 meses), `"quente"` (segue ha 6+ meses, consome conteudo), `"hot"` (ja comprou antes).

---

## BLOCO 2 — `negocio` (objeto)

```json
{
  "negocio": {
    "tem_negocio": true,
    "meses_operacao": 36,
    "faturamento_medio_6m": {
      "faixa": "30-100k",
      "valor_aproximado_brl": 32000,
      "valor_pior_mes_brl": 18000,
      "valor_melhor_mes_brl": 52000
    },
    "tipo": "hibrido",
    "produto_principal": {
      "nome": "Mentoria Juridica Trimestral 1-a-1",
      "preco_brl": 8500,
      "formato": "1-a-1 trimestral",
      "ticket_medio_brl": 8500,
      "frequencia_entrega": "encontros semanais Zoom + WhatsApp diario"
    },
    "outros_produtos": [
      {
        "nome": "Curso Online Carreira Juridica",
        "preco_brl": 297,
        "formato": "online auto-instrucional"
      }
    ],
    "audiencia": [
      {
        "canal": "instagram",
        "handle": "@carolmendescoach",
        "seguidores": 18400,
        "engajamento_medio_pct": 4.2,
        "frequencia_post": "diaria"
      },
      {
        "canal": "lista_email",
        "tamanho": 2300,
        "abertura_media_pct": 28
      },
      {
        "canal": "linkedin",
        "handle": "Carolina Mendes",
        "conexoes": 4100,
        "frequencia_post": "semanal"
      }
    ],
    "time": [
      {
        "papel": "VA",
        "regime": "PJ_part_time",
        "custo_mensal_brl": 1500,
        "ha_quanto_tempo_meses": 8
      },
      {
        "papel": "social_media",
        "regime": "freelancer",
        "custo_mensal_brl": 2000,
        "ha_quanto_tempo_meses": 4
      }
    ]
  }
}
```

**Faturamento faixa — enum:** `"<10k"`, `"10-30k"`, `"30-100k"`, `"100-300k"`, `"300k+"`.

**Tipo — enum:** `"fisico"`, `"digital"`, `"hibrido"`.

**Canal audiencia — enum:** `"instagram"`, `"linkedin"`, `"youtube"`, `"tiktok"`, `"facebook"`, `"lista_email"`, `"telegram"`, `"comunidade_paga"`, `"outro"`.

**Regime time — enum:** `"clt"`, `"pj_full_time"`, `"pj_part_time"`, `"freelancer"`, `"socia"`, `"estagiaria"`.

---

## BLOCO 3 — `tentativas` (objeto)

```json
{
  "tentativas": {
    "mentorias_cursos": [
      {
        "nome": "Mentoria do Erico Rocha",
        "mentor": "Erico Rocha",
        "valor_brl": 15000,
        "ano": 2022,
        "duracao_meses": 6,
        "avaliacao_pos": "boa - montei minha primeira oferta",
        "concluiu": true
      },
      {
        "nome": "Curso Camila Porto Insta",
        "mentor": "Camila Porto",
        "valor_brl": 1997,
        "ano": 2023,
        "duracao_meses": 2,
        "avaliacao_pos": "ruim - nao implementei",
        "concluiu": false
      }
    ],
    "investimento_total_ultimos_3_anos_brl": 38000,
    "ferramentas_ia": [
      {
        "nome": "ChatGPT",
        "plano": "Plus",
        "uso_atual": "copy de Insta",
        "frustracao": "tom nao soa meu",
        "frequencia": "diaria"
      },
      {
        "nome": "Inner AI",
        "plano": "free",
        "uso_atual": "abandonou",
        "frustracao": "limitada"
      }
    ],
    "o_que_funcionou": "Mentoria com Camila Brito me fez postar todo dia por 60 dias. Virei autoridade no nicho de carreira juridica feminina. Faturamento dobrou nos 6 meses seguintes.",
    "o_que_nao_funcionou": {
      "descricao": "Lancamento de curso digital em 2023 vendeu so 8 unidades de 50 previstas",
      "auto_diagnostico_dela": "Acho que era oferta fraca. Mas talvez tambem fosse meu medo de aparecer"
    }
  }
}
```

---

## BLOCO 4 — `dores` (objeto)

```json
{
  "dores": {
    "top_3": [
      {
        "ranking": 1,
        "descricao": "Cansaco mental cronico de tomar todas as decisoes sozinha",
        "categoria": "emocional",
        "intensidade_1_10": 9
      },
      {
        "ranking": 2,
        "descricao": "Faturamento estacionado em 30k ha 8 meses",
        "categoria": "financeiro",
        "intensidade_1_10": 8
      },
      {
        "ranking": 3,
        "descricao": "Sensacao recorrente de que vou ser descoberta como fraude",
        "categoria": "identitario",
        "intensidade_1_10": 7
      }
    ],
    "tentativas_solucao": [
      {
        "acao": "Terapia individual semanal",
        "periodo_meses": 12,
        "resultado": "ajudou na ansiedade mas nao no operacional"
      },
      {
        "acao": "Contratei e demiti 2 VAs",
        "periodo_meses": 6,
        "resultado": "frustrante - nao soube delegar"
      }
    ],
    "tempo_estagnacao": [
      {
        "dor_relacionada": "Faturamento estacionado",
        "meses": 8
      },
      {
        "dor_relacionada": "Sindrome do impostor",
        "meses": 36
      }
    ],
    "custo_de_continuar_parada": "Perco minha sanidade. Casamento ja entrou em crise no ano passado por causa disso. E perco a janela de IA que vai fechar em 2 anos."
  }
}
```

**Categoria dor — enum:** `"operacional"`, `"financeiro"`, `"emocional"`, `"identitario"`, `"relacional"`, `"saude"`, `"tempo"`.

---

## BLOCO 5 — `objetivos` (objeto)

```json
{
  "objetivos": {
    "curto_prazo_90d": {
      "descricao": "Lancar primeira oferta high-ticket de R$15k e fechar 5 vendas",
      "kpi": "5 vendas a R$15k = R$75k",
      "prazo": "90 dias"
    },
    "medio_prazo_12m": {
      "descricao": "Faturando 100k/mes recorrente, time de 3 pessoas, posicionada como referencia em mentoria juridica feminina",
      "kpi_faturamento_brl": 100000,
      "kpi_time_pessoas": 3,
      "kpi_posicionamento": "referencia em mentoria juridica feminina BR"
    },
    "longo_prazo_3_5a": {
      "descricao": "Escola online com 500+ alunas. Sair da operacao 1-a-1. Escrever um livro. Falar em palco grande tipo Hering Live ou TEDx.",
      "tags": ["escola_online", "saida_operacao", "livro", "palco"]
    },
    "vida_ideal": "Acordo as 6, treino, levo as criancas pra escola. Trabalho 4h profundas ate 14h. Almoco com o marido. Dirijo pro consultorio 2x semana so pra ver casos antigos. Final de semana sagrado pra familia."
  }
}
```

---

## BLOCO 6 — `recursos` (objeto)

```json
{
  "recursos": {
    "tempo_semanal_horas": {
      "valor": 8,
      "distribuicao": "2h por dia em 4 dias uteis"
    },
    "budget_mensal_alem_travessia_brl": {
      "faixa": "3-10k",
      "valor_confortavel": 5000,
      "valor_maximo_se_retorno_claro": 10000
    },
    "time_atual_referencia_bloco_2": true,
    "capacidade_contratar_90d": {
      "consegue": true,
      "tipo": "PJ_part_time",
      "budget_mensal_brl_para_contratacao": 3000
    },
    "background_tecnico": {
      "nivel": "intermediaria",
      "ferramentas_que_domina": ["Notion", "Make basico", "Canva", "ChatGPT"],
      "ferramentas_que_nao_domina": ["programacao", "API", "Zapier avancado"]
    }
  }
}
```

**Background tecnico — enum:** `"tecnica"`, `"intermediaria"`, `"delegadora"`.

---

## BLOCO 7 — `identidade` (objeto)

```json
{
  "identidade": {
    "nicho_especifico": {
      "descricao": "Advogadas mulheres de 30-45 anos, com 5+ anos de carreira em escritorio, que querem virar mentora juridica",
      "tags": {
        "profissao": "advogada",
        "genero": "feminino",
        "idade_min": 30,
        "idade_max": 45,
        "momento_carreira": "5+ anos escritorio querendo virar mentora"
      }
    },
    "posicionamento_percebido": "Me veem como advogada que ensina rede social. O que e meio injusto, eu ensino mentoria juridica.",
    "diferencial_percebido": "Sou a unica advogada que junta 8 anos de processo + 4 anos de mentoria. Combino tecnica juridica com pedagogia de adulto.",
    "voz_tom_atual": {
      "descricao": "Acolhedora com pitada provocadora. Falo de voce, uso 'irma', tiro sarro de mim mesma.",
      "tags": ["acolhedora", "provocadora_leve", "intima", "auto_ironica"]
    },
    "expressoes_assinatura": ["vamos juntas", "corre comigo", "sem firula"]
  }
}
```

---

## BLOCO 8 — `expectativas` (objeto)

```json
{
  "expectativas": {
    "resultado_concreto_6m": {
      "descricao": "Faturamento triplicado pra 90k/mes recorrente. Time de 3 pessoas. Eu trabalhando 25h/semana. Dormindo bem.",
      "kpi_faturamento_brl": 90000,
      "kpi_time": 3,
      "kpi_horas_semana": 25,
      "kpi_qualitativo": "dormir bem"
    },
    "o_que_anima": "Me anima ter voce como referencia perto. E me anima criar minha primeira oferta high-ticket de verdade.",
    "maior_receio": {
      "descricao": "Tenho medo de gastar essa grana e nao implementar nada. E medo de descobrir que sou pior do que penso.",
      "tags": ["financeiro", "identitario"]
    }
  }
}
```

---

## ALERTAS — `alertas_detectados` (array)

Cada alerta detectado durante a fase 3 vira um objeto:

```json
{
  "alertas_detectados": [
    {
      "tipo": "estagnacao",
      "severidade": "alta",
      "evidencia": "Faturamento estacionado ha 8 meses + sindrome do impostor ha 36 meses",
      "acao_sugerida": "Plano de Celeste deve atacar primeiro o emocional/identitario antes do operacional"
    },
    {
      "tipo": "vitima_de_curso",
      "severidade": "media",
      "evidencia": "R$38k investidos em 3 anos com 1 mentoria abandonada e 1 curso nao implementado",
      "acao_sugerida": "Contrato emocional reforcado: trilha curta com checkpoints semanais"
    }
  ]
}
```

**Tipo — enum:**
- `"estagnacao"` — parada ha 12+ meses
- `"gargalo_pessoal"` — fatura alto sem time
- `"vitima_de_curso"` — investiu R$30k+ sem implementar
- `"expectativa_irrealista"` — quer transformacao em 30d
- `"confusao_estrategica"` — sem produto definido apos 2+ anos
- `"alinhamento"` — nao sabe o que a Tata faz
- `"saude_emocional"` — sinais de burnout/depressao
- `"financeiro_critico"` — endividada ou pagando Travessia com sacrificio
- `"relacional"` — casamento/familia em crise por causa do trabalho

**Severidade — enum:** `"baixa"`, `"media"`, `"alta"`, `"critica"`.

---

## CAMPOS PENDENTES (modo `--auto`)

Quando a skill roda em `--auto`, campos nao confirmaveis viram:

```json
{
  "negocio": {
    "faturamento_medio_6m": {
      "pendente": true,
      "motivo": "exige confirmacao na call - dado nao publico",
      "estimativa_inferencia_publica": "30-100k baseado em audiencia 18k + ticket high-ticket aparente"
    }
  }
}
```

**Regra:** todo campo `pendente: true` precisa ter `motivo` (string explicativa). Pode opcionalmente ter `estimativa_inferencia_publica` mas SEM substituir o campo real.

---

## VALIDACAO DO JSON

Toda anamnese deve passar por validador antes de salvar:

1. **Schema valido** — todos os campos obrigatorios preenchidos OU marcados como `pendente`/`incompleto`
2. **Tipos corretos** — numeros sao numeros, strings sao strings, enums dentro do dominio
3. **Score calculado** — `score_completude` recalculado a cada salvamento
4. **Alertas atualizados** — re-rodar deteccao da fase 3
5. **Backup gerado** — se for atualizacao, salvar `00-anamnese.json.bak` antes

---

## EXEMPLO MINIMO VALIDO

Para teste rapido (preenchimento minimo viavel):

```json
{
  "schema_versao": "1.0",
  "skill_versao": "anamnese-mentorada-1.0",
  "slug": "teste-mentorada",
  "data_coleta": "2026-05-08",
  "data_atualizacao": "2026-05-08",
  "coletado_por": "formulario",
  "responsavel_coleta": "automatica",
  "score_completude": {"geral": 0, "por_bloco": {}},
  "alertas_detectados": [],
  "historico": {"nome_completo": "Teste Mentorada", "pendente": true, "motivo": "minimo viavel"},
  "negocio": {"pendente": true, "motivo": "minimo viavel"},
  "tentativas": {"pendente": true, "motivo": "minimo viavel"},
  "dores": {"pendente": true, "motivo": "minimo viavel"},
  "objetivos": {"pendente": true, "motivo": "minimo viavel"},
  "recursos": {"pendente": true, "motivo": "minimo viavel"},
  "identidade": {"pendente": true, "motivo": "minimo viavel"},
  "expectativas": {"pendente": true, "motivo": "minimo viavel"},
  "proxima_acao_recomendada": "preencher anamnese completa via /anamnese-mentorada --formulario"
}
```

---

## QUEM CONSOME O QUE

| Skill                        | Blocos consumidos                  |
|------------------------------|------------------------------------|
| `/perfil-mentorada`          | 1, 2, 4, 5 (classificacao)        |
| `/dossie-mentorada`          | TODOS (copia integral)            |
| `/imperio-diagnostico`       | 2, 4, 5, 6                        |
| `/celeste`                   | TODOS                             |
| `/headline-imperatriz`       | 7 (voz, identidade)               |
| `/copy-conversacional-dm`    | 2, 4, 7                           |
| `/imperatriz-bot`            | 2, 7, 8                           |
| `/skill-mentoria-tata`       | 5, 6, 8                           |
| `/mecanismo-unico`           | 2, 7                              |

---

**Schema do Metodo Imperatriz de Anamnese — propriedade Tata Goncalves.**
