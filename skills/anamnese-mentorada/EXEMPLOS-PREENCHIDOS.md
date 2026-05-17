# Exemplos Preenchidos — 3 Anamneses Completas

Tres exemplos reais (anonimizados/ficticios) de anamneses completas pra perfis distintos da Travessia. Cada exemplo mostra:

- JSON completo do `00-anamnese.json`
- Resumo executivo gerado pela skill
- Alertas detectados
- Proxima acao recomendada

Os 3 perfis cobrem o espectro tipico de mentoradas que entram na Travessia:

1. **Construtora Tecnica** — mulher engenheira/dev, faturando pouco, monta tudo sozinha
2. **Frustrada R$30k/mes** — fatura medio, parou de crescer, esgotada
3. **Premium Querendo Subir** — fatura alto, quer escalar pra R$300k+/mes

---

## EXEMPLO 1 — CONSTRUTORA TECNICA

**Perfil:** Engenheira de software, faturamento baixo, alto skill tecnico, baixa habilidade de marketing.

```json
{
  "schema_versao": "1.0",
  "skill_versao": "anamnese-mentorada-1.0",
  "slug": "juliana-rocha",
  "data_coleta": "2026-05-08",
  "data_atualizacao": "2026-05-08",
  "coletado_por": "call",
  "responsavel_coleta": "tata",
  "duracao_coleta_min": 82,
  "score_completude": {
    "geral": 88,
    "por_bloco": {
      "1_historico": 100,
      "2_negocio": 83,
      "3_tentativas": 75,
      "4_dores": 100,
      "5_objetivos": 100,
      "6_recursos": 100,
      "7_identidade": 80,
      "8_expectativas": 100
    }
  },

  "historico": {
    "nome_completo": "Juliana Rocha de Sousa",
    "idade": 32,
    "localizacao": {"cidade": "Florianopolis", "estado": "SC", "pais": "BR"},
    "estado_civil": "uniao_estavel",
    "filhos": {"tem": false, "quantidade": 0, "idades": []},
    "formacao": [
      {"curso": "Engenharia de Computacao", "instituicao": "UFSC", "ano_conclusao": 2017},
      {"curso": "Especializacao em Machine Learning", "instituicao": "USP online", "ano_conclusao": 2022}
    ],
    "trajetoria_profissional": "Engenheira de software CLT por 7 anos em fintech. Sai em janeiro 2025 pra empreender. Comecei oferecendo consultoria de IA pra agencias e em 6 meses tive minha primeira mentorada paga (R$2k/mes). Hoje tenho 3 mentoradas pagas e dois projetos de consultoria. Faturando R$8k/mes em media.",
    "trajetoria_timeline": [
      {"ano": 2017, "evento": "formada UFSC"},
      {"ano": 2018, "evento": "dev pleno em fintech"},
      {"ano": 2024, "evento": "tech lead - decidiu sair"},
      {"ano": 2025, "evento": "pediu demissao, comecou consultoria solo"}
    ],
    "canal_origem": "indicacao da Marina (mentorada Tata 2025)",
    "aquecimento_pre_compra": "morno",
    "auto_descricao_uma_frase": "Sou engenheira de IA que ajuda agencias e mentores a montarem agentes inteligentes pros negocios deles"
  },

  "negocio": {
    "tem_negocio": true,
    "meses_operacao": 16,
    "faturamento_medio_6m": {
      "faixa": "<10k",
      "valor_aproximado_brl": 8000,
      "valor_pior_mes_brl": 4500,
      "valor_melhor_mes_brl": 12000
    },
    "tipo": "digital",
    "produto_principal": {
      "nome": "Mentoria Mensal de IA pra Negocios",
      "preco_brl": 2000,
      "formato": "mensal recorrente, 4 calls + WhatsApp",
      "ticket_medio_brl": 2000
    },
    "outros_produtos": [
      {"nome": "Consultoria pontual de implementacao IA", "preco_brl": 5000, "formato": "projeto"}
    ],
    "audiencia": [
      {"canal": "linkedin", "handle": "Juliana Rocha", "conexoes": 6800, "frequencia_post": "2x semana"},
      {"canal": "instagram", "handle": "@juli.rocha.ia", "seguidores": 1100, "engajamento_medio_pct": 8.5}
    ],
    "time": []
  },

  "tentativas": {
    "mentorias_cursos": [
      {"nome": "Curso Erico Rocha Lancamento", "valor_brl": 3997, "ano": 2025, "concluiu": false, "avaliacao_pos": "metodologia legal mas nao implementei - travei na copy"}
    ],
    "investimento_total_ultimos_3_anos_brl": 5000,
    "ferramentas_ia": [
      {"nome": "ChatGPT Plus", "uso_atual": "diario - copy, codigo, briefing"},
      {"nome": "Claude", "plano": "Pro", "uso_atual": "diario - dev e analise"},
      {"nome": "Cursor", "uso_atual": "dev"},
      {"nome": "Midjourney", "uso_atual": "ocasional"}
    ],
    "o_que_funcionou": "Postar no LinkedIn 2x semana de forma tecnica e didatica gerou minhas 3 primeiras mentoradas. Indicacao boca a boca tambem funcionou - foi assim que cheguei na Marina.",
    "o_que_nao_funcionou": {
      "descricao": "Tentei rodar ads de Linkedin 1 mes, gastei R$1.500, zero leads.",
      "auto_diagnostico_dela": "Acho que copy do anuncio era muito tecnica, sem promessa clara. E pagina de destino era so meu Linktree."
    }
  },

  "dores": {
    "top_3": [
      {
        "ranking": 1,
        "descricao": "Saio da CLT ha 16 meses e ainda fatura abaixo do meu salario antigo. Preciso CHEGAR em R$15k/mes ate dezembro 2026 ou volto pra CLT.",
        "categoria": "financeiro",
        "intensidade_1_10": 10
      },
      {
        "ranking": 2,
        "descricao": "Sou tecnica demais. Travo na hora de escrever copy de venda, fazer reels, posar pra foto, gravar VSL. Me sinto fora do lugar.",
        "categoria": "identitario",
        "intensidade_1_10": 9
      },
      {
        "ranking": 3,
        "descricao": "Trabalho 50h/semana na consultoria + mentoria + criar conteudo + comercial + financeiro. Nao escala assim.",
        "categoria": "operacional",
        "intensidade_1_10": 8
      }
    ],
    "tentativas_solucao": [
      {"acao": "Comecei terapia 3 meses atras", "resultado": "ajudou na ansiedade"},
      {"acao": "Tentei contratar copywriter freelancer", "resultado": "saiu generico, nao usei"},
      {"acao": "Curso de copy do Erico", "resultado": "abandonei na semana 2"}
    ],
    "tempo_estagnacao": [
      {"dor_relacionada": "Faturamento abaixo do CLT", "meses": 16},
      {"dor_relacionada": "Trava de copy", "meses": 16}
    ],
    "custo_de_continuar_parada": "Volto pra CLT, perco a janela, perco a confianca de que consigo. Meu marido e que paga as contas hoje (ele aceita) mas eu morro um pouquinho por dentro. E vejo a janela da IA fechando."
  },

  "objetivos": {
    "curto_prazo_90d": {
      "descricao": "Chegar a 6 mentoradas pagas (R$12k/mes recorrente) e fechar 2 consultorias de R$8k cada",
      "kpi": "R$12k recorrente + R$16k pontual = R$28k em 90 dias",
      "prazo": "90 dias"
    },
    "medio_prazo_12m": {
      "descricao": "Faturar R$30k/mes sustentavel. Ter um produto de entrada digital de R$497 ja vendendo organicamente. Posicionada como referencia BR em IA pra mentores e agencias.",
      "kpi_faturamento_brl": 30000,
      "kpi_time_pessoas": 1,
      "kpi_posicionamento": "referencia BR em IA pra negocios de mentoria/agencia"
    },
    "longo_prazo_3_5a": {
      "descricao": "Empresa de produtos digitais de IA com 3-5 pessoas. Eu como rosto + tecnica. Treinamento corporativo pra agencias grandes. Possivel saida pra um fundo de venture.",
      "tags": ["produtos_digitais", "treinamento_b2b", "exit_estrategico"]
    },
    "vida_ideal": "Acordo as 7, treino, trabalho 5h profundas (3h de cliente + 2h de produto), almoco com meu companheiro (ele tambem trabalha de casa), tarde livre. Dois meses por ano viajando trabalhando do exterior. Filhos talvez em 2-3 anos."
  },

  "recursos": {
    "tempo_semanal_horas": {"valor": 40, "distribuicao": "8h/dia 5 dias"},
    "budget_mensal_alem_travessia_brl": {"faixa": "1-3k", "valor_confortavel": 1500, "valor_maximo_se_retorno_claro": 3000},
    "capacidade_contratar_90d": {"consegue": false, "tipo": "nao orcamento ainda"},
    "background_tecnico": {
      "nivel": "tecnica",
      "ferramentas_que_domina": ["Python", "Claude API", "OpenAI API", "n8n", "Supabase", "Vercel", "Notion avancado", "Make"],
      "ferramentas_que_nao_domina": ["copywriting", "edicao de video", "design"]
    }
  },

  "identidade": {
    "nicho_especifico": {
      "descricao": "Agencias de marketing digital (5-50 funcionarios) e mentores high-ticket que querem implementar IA pra escalar entrega sem aumentar time",
      "tags": {"setor": "agencia + mentoria", "tamanho": "5-50 pessoas", "momento": "querendo escalar com IA"}
    },
    "posicionamento_percebido": "No LinkedIn me veem como engenheira de IA boa tecnicamente. Fora do LinkedIn ninguem me conhece.",
    "diferencial_percebido": "Sou uma das poucas devs de IA mulher no Brasil que tambem entende negocio. Falo a lingua dos dois mundos. Construi sistemas em fintech CLT durante 7 anos - sei o que e producao de verdade.",
    "voz_tom_atual": {
      "descricao": "Tecnica didatica. Tipo professora paciente. Pouca emocao, muito 'como'.",
      "tags": ["tecnica", "didatica", "racional", "pouco_emocional"]
    },
    "expressoes_assinatura": ["bora ver na pratica", "vamos por partes", "mostra o codigo"]
  },

  "expectativas": {
    "resultado_concreto_6m": {
      "descricao": "Faturando R$25k+ recorrente. Aprendi a vender sem morrer de vergonha. Tenho um funil que nao depende SO de eu postar manual no LinkedIn. Vou pra cama dormindo.",
      "kpi_faturamento_brl": 25000,
      "kpi_qualitativo": "vender sem morrer de vergonha"
    },
    "o_que_anima": "Me anima ter outras mulheres tecnicas como referencia. Me anima ver mentor de marketing falar com mentora tecnica - quero aprender o caminho contrario do que voce ja fez.",
    "maior_receio": {
      "descricao": "Tenho medo de gastar a Travessia e voltar pra CLT. Tenho medo de descobrir que sou tecnica boa mas nao tenho dom pra empresarialismo. Tenho medo de comparacao com mentoradas que ja faturam mais.",
      "tags": ["financeiro", "identitario", "comparacao"]
    }
  },

  "alertas_detectados": [
    {
      "tipo": "financeiro_critico",
      "severidade": "alta",
      "evidencia": "Faturamento R$8k/mes ha 16 meses, abaixo do salario CLT antigo. Limite mental: 'volto pra CLT em dezembro 2026'.",
      "acao_sugerida": "Plano deve atacar faturamento RAPIDO (90d) com produto/oferta existente antes de qualquer construcao de imperio. Sem dinheiro entrando, ela quebra emocional."
    }
  ],

  "observacoes_tata": "Mentorada de OURO. Nivel tecnico altissimo (entrega ela sabe fazer). Gargalo e copy + venda + posicionamento. Plano: usar a tecnica DELA pra construir produto digital de entrada (curso) enquanto trabalho copy e funil. Casa muito bem com /imperio-agente e /headline-imperatriz. Nao gastar tempo em /imperio-infra - ela ja domina.",
  "proxima_acao_recomendada": "rodar /perfil-mentorada (provavel classificacao: Construtora Tecnica) + /imperio-diagnostico"
}
```

### Resumo executivo (Exemplo 1)
> **Juliana Rocha, 32, Floripa.** Engenheira de IA ex-CLT em fintech, saiu ha 16 meses pra empreender. Fatura R$8k/mes (3 mentoradas + projetos). **Top 3 dores:** (1) ainda fatura abaixo do CLT antigo, (2) trava de copy/marketing, (3) trabalha 50h/sem sem escalar. **Top 3 objetivos:** R$28k em 90d, R$30k/mes em 12m, empresa de produtos IA em 3-5a. **Alerta alto:** financeiro critico — janela mental ate dezembro 2026 ou volta pra CLT. **Stack tecnico forte** (Python, Claude API, n8n). **Proxima acao:** rodar `/perfil-mentorada`.

---

## EXEMPLO 2 — FRUSTRADA R$30K/MES

**Perfil:** Mulher 38, mentora de carreira, fatura R$30k/mes ha 18 meses sem crescer, esgotada.

```json
{
  "schema_versao": "1.0",
  "skill_versao": "anamnese-mentorada-1.0",
  "slug": "fernanda-coelho",
  "data_coleta": "2026-05-08",
  "data_atualizacao": "2026-05-08",
  "coletado_por": "formulario",
  "responsavel_coleta": "mentorada",
  "duracao_coleta_min": 47,
  "score_completude": {
    "geral": 95,
    "por_bloco": {
      "1_historico": 100,
      "2_negocio": 100,
      "3_tentativas": 100,
      "4_dores": 100,
      "5_objetivos": 100,
      "6_recursos": 100,
      "7_identidade": 80,
      "8_expectativas": 100
    }
  },

  "historico": {
    "nome_completo": "Fernanda Coelho Vieira",
    "idade": 38,
    "localizacao": {"cidade": "Sao Paulo", "estado": "SP", "pais": "BR"},
    "estado_civil": "casada",
    "filhos": {"tem": true, "quantidade": 2, "idades": [4, 7]},
    "formacao": [
      {"curso": "Psicologia", "instituicao": "USP", "ano_conclusao": 2010},
      {"curso": "MBA Recursos Humanos", "instituicao": "FGV", "ano_conclusao": 2014}
    ],
    "trajetoria_profissional": "10 anos em RH corporativo - de analista a head em multinacional. Em 2021 fiz coaching de carreira como hobby pro pessoal proximo. Em 2022 pedi demissao, virei mentora full-time. Cresci rapido em 2023 (saltei de 0 a R$30k/mes em 8 meses). Mas DESDE entao - 18 meses - estou estacionada em R$30k.",
    "trajetoria_timeline": [
      {"ano": 2010, "evento": "psicologa formada USP"},
      {"ano": 2011, "evento": "RH em multinacional - analista"},
      {"ano": 2019, "evento": "head de RH"},
      {"ano": 2022, "evento": "pediu demissao - virou mentora full"},
      {"ano": 2023, "evento": "explosao - chegou a R$30k/mes"},
      {"ano": 2024, "evento": "estagnou em R$30k"}
    ],
    "canal_origem": "anuncio do webinar 'Imperio de Agentes' em fevereiro 2026",
    "aquecimento_pre_compra": "quente",
    "auto_descricao_uma_frase": "Sou ex-head de RH que ajuda mulheres CLT a fazerem transicao de carreira pra um trabalho que ame"
  },

  "negocio": {
    "tem_negocio": true,
    "meses_operacao": 36,
    "faturamento_medio_6m": {
      "faixa": "30-100k",
      "valor_aproximado_brl": 32000,
      "valor_pior_mes_brl": 24000,
      "valor_melhor_mes_brl": 41000
    },
    "tipo": "digital",
    "produto_principal": {
      "nome": "Mentoria Trimestral de Transicao de Carreira",
      "preco_brl": 4500,
      "formato": "trimestral - encontros quinzenais Zoom + grupo Whatsapp",
      "ticket_medio_brl": 4500,
      "frequencia_entrega": "12 encontros em 90 dias + suporte daily"
    },
    "outros_produtos": [
      {"nome": "Curso Online 'Sair da CLT'", "preco_brl": 697, "formato": "auto-instrucional 8 modulos"}
    ],
    "audiencia": [
      {"canal": "instagram", "handle": "@fecoelho.carreira", "seguidores": 38000, "engajamento_medio_pct": 5.2, "frequencia_post": "diaria"},
      {"canal": "lista_email", "tamanho": 8500, "abertura_media_pct": 32}
    ],
    "time": [
      {"papel": "VA", "regime": "PJ_part_time", "custo_mensal_brl": 1800, "ha_quanto_tempo_meses": 14},
      {"papel": "social_media", "regime": "freelancer", "custo_mensal_brl": 2500, "ha_quanto_tempo_meses": 8}
    ]
  },

  "tentativas": {
    "mentorias_cursos": [
      {"nome": "Mentoria Camila Brito", "valor_brl": 12000, "ano": 2023, "concluiu": true, "avaliacao_pos": "boa - me deu o pulo de R$0 a R$30k"},
      {"nome": "Imersao Erico Rocha", "valor_brl": 7000, "ano": 2024, "concluiu": true, "avaliacao_pos": "media - aprendi mas nao implementei lancamento"},
      {"nome": "Mentoria de Trafego com Pedro Sobral", "valor_brl": 18000, "ano": 2025, "concluiu": false, "avaliacao_pos": "ruim - travei na criatividade do anuncio, gastei R$8k em ads sem ROI"},
      {"nome": "Curso de Copy do Diego Maia", "valor_brl": 4500, "ano": 2025, "concluiu": false, "avaliacao_pos": "abandonei semana 3"}
    ],
    "investimento_total_ultimos_3_anos_brl": 41500,
    "ferramentas_ia": [
      {"nome": "ChatGPT Plus", "uso_atual": "diario pra copy de Insta", "frustracao": "tom muito generico, parece que e IA"},
      {"nome": "Inner AI", "uso_atual": "abandonou", "frustracao": "muito travada"}
    ],
    "o_que_funcionou": "1) Postar 5x/semana no Insta com depoimento de aluna virou minha maquina de organico. 2) Lancamento via webinar +emails (mentoria Camila) gerou meu primeiro pico de R$60k em 1 mes.",
    "o_que_nao_funcionou": {
      "descricao": "Trafego pago - gastei R$8k em ads em 2025 sem retorno. Lancamento de novo curso digital em 2024 vendeu so 12 unidades.",
      "auto_diagnostico_dela": "Acho que sou ruim em tracao paga. E lancamento eu sai do cronograma e furou. Mas no fundo sei que e medo - se eu lancar serio, dou conta da entrega? Se eu trafego serio, fica gigante demais?"
    }
  },

  "dores": {
    "top_3": [
      {
        "ranking": 1,
        "descricao": "Estacionada em R$30k/mes ha 18 meses. Vendo concorrentes mais novas passarem, e eu travada.",
        "categoria": "financeiro",
        "intensidade_1_10": 10
      },
      {
        "ranking": 2,
        "descricao": "Esgotamento operacional - sou eu fazendo TUDO: vendas, mentoria 1-a-1 com 8 mentoradas simultaneas, conteudo, decisao, financeiro. Acordo as 5h pra criar conteudo antes dos filhos acordarem.",
        "categoria": "operacional",
        "intensidade_1_10": 10
      },
      {
        "ranking": 3,
        "descricao": "Casamento em crise - meu marido reclamou na pascoa que eu trabalho 24/7 e nao to mais presente.",
        "categoria": "relacional",
        "intensidade_1_10": 9
      }
    ],
    "tentativas_solucao": [
      {"acao": "Contratei VA part-time ha 14 meses", "resultado": "ajudou em agenda mas nao em escala"},
      {"acao": "Tentei aumentar preco da mentoria 4500->6000", "resultado": "perdi 2 vendas seguidas, voltei pro 4500"},
      {"acao": "Tentei trafego pago", "resultado": "queimei R$8k sem retorno"},
      {"acao": "Reduzi entrega de 16 pra 12 encontros", "resultado": "alunas continuaram pedindo mais"}
    ],
    "tempo_estagnacao": [
      {"dor_relacionada": "Faturamento estagnado", "meses": 18},
      {"dor_relacionada": "Esgotamento", "meses": 24},
      {"dor_relacionada": "Crise casamento", "meses": 4}
    ],
    "custo_de_continuar_parada": "Meu casamento acaba. Minha saude (ja com refluxo, insonia, ganho de peso). Meus filhos crescem com mae ausente. E eu volto pra CLT humilhada em 2 anos. Mas o pior: a janela de IA fecha pra mim."
  },

  "objetivos": {
    "curto_prazo_90d": {
      "descricao": "Subir pra R$50k/mes consistente. Reduzir minha mentoria 1-a-1 de 8 pra 5 alunas. Lancar versao em grupo (turma) por R$2.997 com 10 alunas.",
      "kpi": "R$50k = (5 x R$4500) + (10 x R$300/mes turma) + (R$697 curso x 10 vendas) = R$53k",
      "prazo": "90 dias"
    },
    "medio_prazo_12m": {
      "descricao": "Faturar R$100k/mes recorrente. Time de 4 pessoas (eu + VA + commercial + assistente de mentoria). Eu fora do 1-a-1, so dando turmas + ofertas digitais.",
      "kpi_faturamento_brl": 100000,
      "kpi_time_pessoas": 4,
      "kpi_posicionamento": "referencia BR em transicao de carreira pra mulheres CLT"
    },
    "longo_prazo_3_5a": {
      "descricao": "Empresa de R$500k/mes. Eu liderando um grupo de mentoras (escola). Programa de afiliados estruturado. Livro publicado. Talvez palco em evento grande tipo CES/RD Summit.",
      "tags": ["escola", "afiliados", "livro", "palco"]
    },
    "vida_ideal": "Acordo 7h sem despertador. Cafe com meu marido. Levo as criancas pra escola. Trabalho 4h profundas das 9 as 13. Almoco em casa. Tarde livre - treino ou amigas ou ler. 18h busco as criancas. Noite com a familia. Final de semana sagrado. 4 viagens internacionais por ano em familia."
  },

  "recursos": {
    "tempo_semanal_horas": {"valor": 35, "distribuicao": "7h/dia 5 dias - quero baixar pra 25h"},
    "budget_mensal_alem_travessia_brl": {"faixa": "3-10k", "valor_confortavel": 5000, "valor_maximo_se_retorno_claro": 15000},
    "capacidade_contratar_90d": {"consegue": true, "tipo": "PJ_part_time", "budget_mensal_brl_para_contratacao": 5000},
    "background_tecnico": {
      "nivel": "intermediaria",
      "ferramentas_que_domina": ["Notion basico", "Canva", "ChatGPT Plus", "Hotmart", "ManyChat basico"],
      "ferramentas_que_nao_domina": ["Make", "Zapier avancado", "Claude", "automacoes complexas", "ads"]
    }
  },

  "identidade": {
    "nicho_especifico": {
      "descricao": "Mulheres CLT de 30-45 anos, classe B, em cargos de media gerencia, que sentem 'isso aqui nao e mais pra mim' e querem fazer transicao pra empreender mas com seguranca",
      "tags": {"genero": "feminino", "idade_min": 30, "idade_max": 45, "momento_carreira": "CLT media gerencia querendo sair"}
    },
    "posicionamento_percebido": "Me veem como mentora de carreira amorosa - tipo amiga sabia. Algumas me veem como 'aquela ex-RH que virou mentora boa'.",
    "diferencial_percebido": "Sou uma das poucas mentoras de carreira que TRABALHOU 10 anos em RH corporativo do outro lado da mesa. Sei como recrutador pensa. Sei contrato, sei salario, sei demissao. Outras mentoras sao coaches sem essa vivencia.",
    "voz_tom_atual": {
      "descricao": "Acolhedora maternal. Falo de voce, abracos virtuais, choro junto. As vezes me sinto mole demais.",
      "tags": ["acolhedora", "maternal", "emocional"]
    },
    "expressoes_assinatura": ["minha querida", "voce nao ta sozinha", "e mais coragem que talento"]
  },

  "expectativas": {
    "resultado_concreto_6m": {
      "descricao": "Faturando R$70k+/mes. Dormindo 8h. Marido voltando a sorrir comigo. Lancamento de turma em grupo aprontado e funcional. Eu trabalhando 25h/sem max.",
      "kpi_faturamento_brl": 70000,
      "kpi_horas_semana": 25,
      "kpi_qualitativo": "casamento de volta + sono"
    },
    "o_que_anima": "Me anima ver outras mentoras que ja saltaram desse plato com voce. Me anima poder aprender em vez de ficar tentando sozinha. Me anima ter espaco pra desabafar sem pagar terapia tambem.",
    "maior_receio": {
      "descricao": "Medo de gastar a Travessia e nao implementar (de novo). Medo de descobrir que o problema sou eu, nao minha estrategia. Medo de fim de casamento. E um medo bobo: nao quero ser comparada com mentoras que ja faturam R$200k+ na sala.",
      "tags": ["financeiro", "identitario", "relacional", "comparacao"]
    }
  },

  "alertas_detectados": [
    {
      "tipo": "estagnacao",
      "severidade": "alta",
      "evidencia": "18 meses no mesmo faturamento R$30k. Tentou aumento de preco e voltou. Tentou trafego e queimou. Tentou novo lancamento e furou.",
      "acao_sugerida": "Plano deve atacar GARGALO ESPECIFICO - nao mais lancamento e nao mais trafego. Provavel: reorganizacao de modelo de produto (sair de 1-a-1 escala-zero pra turma)."
    },
    {
      "tipo": "gargalo_pessoal",
      "severidade": "critica",
      "evidencia": "Faturamento R$30k operando 35h/sem sozinha + 2 freelancers part-time. 8 mentoradas 1-a-1 simultaneas. Acorda 5h.",
      "acao_sugerida": "Reduzir 1-a-1 de 8 pra 5 IMEDIATAMENTE. Subir preco do remanescente. Construir turma em grupo nos proximos 60d."
    },
    {
      "tipo": "vitima_de_curso",
      "severidade": "media",
      "evidencia": "R$41.500 investidos em 3 anos. 2 cursos abandonados. 1 mentoria com ROI ruim.",
      "acao_sugerida": "Trilha curta com checkpoints semanais. Severino monitora implementacao - sem auto-implementacao livre."
    },
    {
      "tipo": "relacional",
      "severidade": "alta",
      "evidencia": "Casamento em crise ha 4 meses. Marido fez fala explicita na pascoa.",
      "acao_sugerida": "Plano deve incluir reducao de horas trabalhadas como KPI tao importante quanto faturamento. Sem reducao de horas, plano fracassa."
    }
  ],

  "observacoes_tata": "Caso classico de PLATEAU de R$30k - 90% das mentoras travam aqui. Diagnostico: produto-principal mal modelado (1-a-1 nao escala). Time mal estruturado. Trafego mal calibrado. Casamento entrando em crise. Plano: 1) reduzir 1-a-1 IMEDIATAMENTE, 2) construir turma em grupo R$2997 nos 60d, 3) reposicionar de 'mentora amorosa' pra 'ex-RH que virou referencia', 4) terapia de casal em paralelo (nao negociavel). NAO mexer em ads agora - prioridade 0.",
  "proxima_acao_recomendada": "rodar /perfil-mentorada (provavel: Frustrada Plateau) + /imperio-diagnostico"
}
```

### Resumo executivo (Exemplo 2)
> **Fernanda Coelho, 38, SP. Casada, 2 filhos pequenos.** Ex-head de RH virou mentora de carreira em 2022. Saltou de R$0 a R$30k/mes em 8 meses, **estacionada em R$30k ha 18 meses.** Audiencia forte (38k Insta, 8.5k lista). **Top 3 dores:** (1) plateau financeiro, (2) esgotamento operacional 35h/sem, (3) casamento em crise. **Top 3 objetivos:** R$50k em 90d, R$100k/mes em 12m, R$500k/mes + escola em 5a. **4 alertas detectados:** estagnacao alta, gargalo pessoal critica, vitima de curso media, relacional alta. R$41k investidos em educacao com 2 cursos abandonados. **Proxima acao:** `/perfil-mentorada` + `/imperio-diagnostico` urgente.

---

## EXEMPLO 3 — PREMIUM QUERENDO SUBIR

**Perfil:** Mulher 44, mentora ja consolidada R$180k/mes, quer subir pra R$500k+ e construir escola.

```json
{
  "schema_versao": "1.0",
  "skill_versao": "anamnese-mentorada-1.0",
  "slug": "patricia-meneses",
  "data_coleta": "2026-05-08",
  "data_atualizacao": "2026-05-08",
  "coletado_por": "hibrido",
  "responsavel_coleta": "tata",
  "duracao_coleta_min": 95,
  "score_completude": {
    "geral": 100,
    "por_bloco": {
      "1_historico": 100,
      "2_negocio": 100,
      "3_tentativas": 100,
      "4_dores": 100,
      "5_objetivos": 100,
      "6_recursos": 100,
      "7_identidade": 100,
      "8_expectativas": 100
    }
  },

  "historico": {
    "nome_completo": "Patricia Meneses Albuquerque",
    "idade": 44,
    "localizacao": {"cidade": "Belo Horizonte", "estado": "MG", "pais": "BR"},
    "estado_civil": "casada",
    "filhos": {"tem": true, "quantidade": 1, "idade": 16},
    "formacao": [
      {"curso": "Medicina", "instituicao": "UFMG", "ano_conclusao": 2005},
      {"curso": "Residencia em Dermatologia", "instituicao": "Santa Casa BH", "ano_conclusao": 2009},
      {"curso": "Pos em Marketing Medico", "instituicao": "INSPER", "ano_conclusao": 2019}
    ],
    "trajetoria_profissional": "Dermatologista clinica desde 2009. Em 2017 abri segunda clinica focada em dermato estetica. Em 2019 comecei a ensinar outras dermatos como crescer no Insta - primeiro de graca, depois mentoria. Em 2022 vendi participacao das clinicas pro socio e fui full-mentora. Em 2024 cheguei a R$180k/mes consistente. Hoje opero programa premium R$45k de 12 meses com 30 alunas + curso digital R$3997.",
    "trajetoria_timeline": [
      {"ano": 2005, "evento": "formada Medicina UFMG"},
      {"ano": 2009, "evento": "dermatologista titulada"},
      {"ano": 2017, "evento": "abriu segunda clinica"},
      {"ano": 2019, "evento": "comecou a ensinar outras dermatos"},
      {"ano": 2022, "evento": "vendeu participacao - virou mentora full"},
      {"ano": 2024, "evento": "chegou a R$180k/mes"}
    ],
    "canal_origem": "indicacao da Renata Ferraz (mentorada Tata 2024) + ja segue Tata ha 1 ano",
    "aquecimento_pre_compra": "hot",
    "auto_descricao_uma_frase": "Sou medica dermatologista que virou referencia em mentoria pra outras medicas crescerem alem do consultorio"
  },

  "negocio": {
    "tem_negocio": true,
    "meses_operacao": 84,
    "faturamento_medio_6m": {
      "faixa": "100-300k",
      "valor_aproximado_brl": 178000,
      "valor_pior_mes_brl": 145000,
      "valor_melhor_mes_brl": 215000
    },
    "tipo": "digital",
    "produto_principal": {
      "nome": "Mentoria Premium 'Medica Lider' 12 meses",
      "preco_brl": 45000,
      "formato": "12 meses - encontros mensais grupo + 4 encontros 1-a-1 + comunidade ativa",
      "ticket_medio_brl": 45000,
      "cohort_atual": 30
    },
    "outros_produtos": [
      {"nome": "Curso Digital 'Posicionamento pra Medica'", "preco_brl": 3997, "formato": "evergreen"},
      {"nome": "Imersao presencial anual 'Encontro Medica Lider'", "preco_brl": 8500, "formato": "3 dias presencial Sao Paulo"}
    ],
    "audiencia": [
      {"canal": "instagram", "handle": "@dra.patmeneses", "seguidores": 165000, "engajamento_medio_pct": 4.8, "frequencia_post": "diaria"},
      {"canal": "youtube", "handle": "Dra Patricia Meneses", "inscritos": 22000, "frequencia_post": "semanal"},
      {"canal": "lista_email", "tamanho": 28000, "abertura_media_pct": 38},
      {"canal": "comunidade_paga", "tamanho": 30, "tipo": "alunas mentoria"}
    ],
    "time": [
      {"papel": "gestora_operacional", "regime": "PJ_full_time", "custo_mensal_brl": 9000, "ha_quanto_tempo_meses": 24},
      {"papel": "social_media_lead", "regime": "PJ_full_time", "custo_mensal_brl": 7000, "ha_quanto_tempo_meses": 18},
      {"papel": "editor_video", "regime": "freelancer", "custo_mensal_brl": 5500, "ha_quanto_tempo_meses": 12},
      {"papel": "trafego_pago", "regime": "agencia", "custo_mensal_brl": 8000, "ha_quanto_tempo_meses": 8},
      {"papel": "VA_pessoal", "regime": "PJ_part_time", "custo_mensal_brl": 2500, "ha_quanto_tempo_meses": 36}
    ]
  },

  "tentativas": {
    "mentorias_cursos": [
      {"nome": "Mentoria Empire Building (gringa)", "valor_brl": 65000, "ano": 2023, "concluiu": true, "avaliacao_pos": "boa - aprendi modelo de turma high-ticket"},
      {"nome": "Mastermind High Ticket Brasil", "valor_brl": 35000, "ano": 2024, "concluiu": true, "avaliacao_pos": "media - network bom mas conteudo fraco"},
      {"nome": "Imersao Russell Brunson (online)", "valor_brl": 12000, "ano": 2024, "concluiu": true, "avaliacao_pos": "boa - usei sales funnel"}
    ],
    "investimento_total_ultimos_3_anos_brl": 145000,
    "ferramentas_ia": [
      {"nome": "ChatGPT Team", "uso_atual": "time todo usa", "frustracao": "tom generico"},
      {"nome": "Claude Pro", "uso_atual": "ela usa pessoal pra escrever email", "frustracao": "ainda nao explorou tudo"},
      {"nome": "Make + Zapier", "uso_atual": "automacoes basicas", "frustracao": "nao sabe escalar"},
      {"nome": "Notion AI", "uso_atual": "documentacao interna"}
    ],
    "o_que_funcionou": "1) Programa de 12 meses high-ticket gerou previsibilidade. 2) Imersao anual presencial vira renovacao automatica. 3) Conteudo daily no IG + parcerias com medicas top construiu autoridade absoluta no nicho. 4) Lista de email de 28k e ouro - cada lancamento converte 4-7%.",
    "o_que_nao_funcionou": {
      "descricao": "Tentei 2x lancar produto secundario pra publico mais frio (curso R$497 'introducao'). Nao escalou - meu publico paga R$45k, nao quer R$497.",
      "auto_diagnostico_dela": "Errei publico-alvo. Meu posicionamento ja e premium - tentar pegar mass market diluiu marca."
    }
  },

  "dores": {
    "top_3": [
      {
        "ranking": 1,
        "descricao": "Bati teto da minha capacidade pessoal - 30 alunas premium e ja nao consigo acompanhar individualmente. Queremos cohort 50+ mas nao tem como SEM sair do 1-a-1.",
        "categoria": "operacional",
        "intensidade_1_10": 9
      },
      {
        "ranking": 2,
        "descricao": "Time bom mas todos olham pra mim em decisoes finais. Eu sou o gargalo de aprovacao. Precisaria de uma 'numero 2' real, nao gestora operacional.",
        "categoria": "operacional",
        "intensidade_1_10": 8
      },
      {
        "ranking": 3,
        "descricao": "Quero lancar escola (10+ professoras formadas) mas nao sei modelar. Tenho receio de canibalizar minha marca pessoal.",
        "categoria": "identitario",
        "intensidade_1_10": 7
      }
    ],
    "tentativas_solucao": [
      {"acao": "Tentei contratar 'numero 2' 2x", "resultado": "ambas saíram em 6 meses - acho que tom autoritario meu"},
      {"acao": "Fiz mentoria gringa pra modelar turma", "resultado": "modelo bom mas sem traducao BR"},
      {"acao": "Comecei a delegar mentorias do programa", "resultado": "alunas pediram eu de volta - nao querem assistente"}
    ],
    "tempo_estagnacao": [
      {"dor_relacionada": "Plateau pessoal-operacional R$180k", "meses": 12}
    ],
    "custo_de_continuar_parada": "Perco 5 anos. Marca pessoal vira ceiling - quando eu parar, acaba. Filha entra em fase de saida de casa e eu perdi tempo trabalhando demais. Novas concorrentes (3-4 dermatos lancando programa proximo ao meu) podem comer meu mercado em 18 meses se eu nao escalar."
  },

  "objetivos": {
    "curto_prazo_90d": {
      "descricao": "Estruturar lancamento da Cohort 2026 (turma 50 alunas) com pricing R$60k. Contratar 'numero 2' real (estrategista, nao gestora). Documentar metodologia pra ser ensinavel.",
      "kpi": "Cohort vendida 50/50 a R$60k = R$3MM em 90d. Numero 2 contratada e em onboarding.",
      "prazo": "90 dias"
    },
    "medio_prazo_12m": {
      "descricao": "Faturar R$500k/mes recorrente. Time de 10 pessoas. Escola 'Medica Lider' lancada em formato modular com 3 mentoras-professoras (escolhidas entre alunas). Eu reduzindo a 20h/sem - operando estrategia, marca, palco.",
      "kpi_faturamento_brl": 500000,
      "kpi_time_pessoas": 10,
      "kpi_horas_semana": 20,
      "kpi_posicionamento": "referencia BR em mentoria de medicas + escola formadora"
    },
    "longo_prazo_3_5a": {
      "descricao": "Empresa de R$2MM/mes recorrente. Escola com 200+ alunas anuais. 3-5 mentoras-professoras formadas. Saida possivel: vender pra grupo educacional ou abrir capital. Livro publicado. Palco em RD Summit, Empretec, talvez TEDx.",
      "tags": ["escola_madura", "saida_estrategica", "livro", "palco_grande", "marca_alem_de_mim"]
    },
    "vida_ideal": "Acordo 7h. Yoga 1h. Cafe com marido. Trabalho 4h profundas. Almoco com filha (que ainda mora em casa) ou com amiga. Tarde livre 2x semana - leitura, palestras, escrita. Treino. Jantar familia. Final de semana sagrado. 4-5 viagens internacionais por ano - 2 sozinha com marido, 2 com filha. Lecionar 1x/ano em palco grande sem stress."
  },

  "recursos": {
    "tempo_semanal_horas": {"valor": 50, "distribuicao": "10h/dia 5 dias - quero baixar pra 25-30h"},
    "budget_mensal_alem_travessia_brl": {"faixa": "30k+", "valor_confortavel": 35000, "valor_maximo_se_retorno_claro": 80000},
    "capacidade_contratar_90d": {"consegue": true, "tipo": "PJ_full_time_senior_e_CLT", "budget_mensal_brl_para_contratacao": 30000},
    "background_tecnico": {
      "nivel": "intermediaria",
      "ferramentas_que_domina": ["ChatGPT", "Claude", "Notion avancado", "Hotmart", "Active Campaign", "Make basico"],
      "ferramentas_que_nao_domina": ["programacao", "agentes IA avancados", "automacao complexa de funil"]
    }
  },

  "identidade": {
    "nicho_especifico": {
      "descricao": "Medicas mulheres de 35-50 anos, dermato/clinico geral/ginecologistas de classe AB, com 8+ anos de carreira em consultorio, que querem sair do consultorio e construir marca pessoal/digital sem perder seriedade medica",
      "tags": {"profissao": "medica", "especialidade": "dermato/clinico/gineco", "genero": "feminino", "idade_min": 35, "idade_max": 50, "classe": "AB", "momento_carreira": "8+ anos consultorio querendo digital"}
    },
    "posicionamento_percebido": "Sou A referencia BR em mentoria pra medicas. Top 3 mentoras de nicho saude no IG.",
    "diferencial_percebido": "Sou a unica que combina (1) credencial medica solida com 13 anos clinica, (2) marca digital 165k seguidores, (3) modelo de programa 12 meses high-ticket validado com 100+ medicas formadas, (4) traducao do mundo gringo pra realidade BR de medico. Outras mentoras sao OU clinicas SEM marca OU com marca SEM credencial.",
    "voz_tom_atual": {
      "descricao": "Autoritaria amorosa. Falo como medica chefe - direta, tecnica, sem firula. Mas com cuidado. Tom feminino classico premium - sofisticada, nunca grita.",
      "tags": ["autoritaria", "amorosa", "tecnica", "sofisticada", "premium"]
    },
    "expressoes_assinatura": ["medica lider", "isso aqui nao e suficiente", "voce vale mais que isso"]
  },

  "expectativas": {
    "resultado_concreto_6m": {
      "descricao": "Faturamento R$300k/mes recorrente. Time de 8 pessoas com numero 2 estabelecida. Escola modelada e em pre-lancamento (turma 1 vendendo pra abertura janeiro 2027). Eu trabalhando 30h/sem.",
      "kpi_faturamento_brl": 300000,
      "kpi_time": 8,
      "kpi_horas_semana": 30,
      "kpi_qualitativo": "estrutura de empresa, nao de mentora autonoma"
    },
    "o_que_anima": "Me anima trabalhar com mentora que ja saiu do plateau de R$200k. Me anima ter par - sempre fui referencia, raramente sou aluna. Me anima documentar metodologia pra escola - vai ser meu legado.",
    "maior_receio": {
      "descricao": "Receio que escola dilua minha marca pessoal. Receio que delegar entrega caia qualidade. Receio que mentoradas que pagam R$45k sintam que estao recebendo menos. E receio de perder tempo com framework que nao se aplica a medicina (nicho regulado pelo CFM).",
      "tags": ["marca", "qualidade", "regulacao_medica"]
    }
  },

  "alertas_detectados": [
    {
      "tipo": "gargalo_pessoal",
      "severidade": "alta",
      "evidencia": "R$180k/mes operando 50h/sem com cohort de 30 alunas premium - Patricia e gargalo de aprovacao em todas decisoes. Time bom mas todos olham pra ela.",
      "acao_sugerida": "Contratacao de 'numero 2' (estrategista, nao gestora) e prioridade ZERO. Sem isso, nao escala alem de R$250k."
    },
    {
      "tipo": "regulacao",
      "severidade": "media",
      "evidencia": "Nicho medico regulado pelo CFM. Programa 'Medica Lider' precisa cuidar com promessa de resultado e exposicao em rede social.",
      "acao_sugerida": "Validar copy de venda com juridico medico. Plano de escola precisa modelo CFM-safe."
    }
  ],

  "observacoes_tata": "OURO. Mentorada Premium classica - R$180k/mes, 7 anos de operacao, time de 5, audiencia gigante. Quer escala pra R$500k. Diagnostico: gargalo principal e ela mesma (numero 2 nao existe), e modelo de produto preso em 1-a-1 ate hoje (cohort de 30 esta no limite operacional). Plano: 1) contratar numero 2 estrategica em 60d, 2) modelar escola formadora em 90d (3 professoras-mentoras saidas das alunas), 3) Cohort 2026 R$60k x 50 alunas, 4) lancamento escola janeiro 2027. CFM e questao critica - validar tudo com juridico. Ela ja tem maturidade, nao precisa de basico - precisa de framework de escala e documentacao de metodologia.",
  "proxima_acao_recomendada": "rodar /perfil-mentorada (provavel: Premium querendo escola) + /imperio-diagnostico + acionar /skill-mentoria-tata pra modelar escola"
}
```

### Resumo executivo (Exemplo 3)
> **Patricia Meneses, 44, BH. Casada, 1 filha 16.** Dermatologista que virou mentora full em 2022. **R$180k/mes ha 12 meses** com programa Premium R$45k de 12 meses (30 alunas) + curso evergreen. Audiencia 165k IG + 28k email + 22k YouTube. Time de 5 (R$32k/mes). **Top 3 dores:** (1) bateu teto operacional pessoal, (2) sem numero 2 real, (3) quer escola mas nao sabe modelar. **Top 3 objetivos:** R$300k em 6m, R$500k em 12m, R$2MM/mes + escola madura em 5a. **2 alertas:** gargalo pessoal alto + nicho regulado CFM medio. Investiu R$145k em educacao com bom ROI. **Proxima acao:** `/perfil-mentorada` + `/imperio-diagnostico` + `/skill-mentoria-tata` pra escola.

---

## CONTRASTE ENTRE OS 3 PERFIS

| Dimensao              | Juliana (Tecnica)   | Fernanda (Frustrada)  | Patricia (Premium)     |
|-----------------------|---------------------|------------------------|-------------------------|
| Faturamento           | R$8k/mes            | R$30k/mes             | R$180k/mes              |
| Anos de operacao      | 1.3                 | 3                     | 7                       |
| Time                  | 0                   | 2 part-time           | 5 (full + agencia)      |
| Audiencia principal   | LinkedIn 6.8k       | Insta 38k             | Insta 165k              |
| Background tecnico    | Tecnica forte       | Intermediaria         | Intermediaria           |
| Investimento educ 3a  | R$5k                | R$41.5k               | R$145k                  |
| Alerta principal      | Financeiro critico  | Estagnacao + gargalo  | Gargalo + regulacao     |
| Proxima skill         | /perfil + /diagnostico | /perfil + /diagnostico urgente | /perfil + /diagnostico + /escola |
| KPI 12m               | R$30k/mes           | R$100k/mes            | R$500k/mes              |
| Tempo semanal hoje    | 40h                 | 35h                   | 50h                     |
| Quer reduzir pra      | Mantém 35-40h       | 25h/sem               | 20-25h/sem              |

---

## COMO USAR ESSES EXEMPLOS

### 1. Treinamento da skill
A skill carrega esses 3 exemplos quando precisa ancorar julgamento ("essa anamnese parece com qual perfil?").

### 2. Calibragem de Tata
Quando Tata abre uma anamnese nova, pode rodar:
```
/anamnese-mentorada --validar slug=[mentorada-nova]
```
A skill compara a nova com os 3 exemplos pra inferir perfil aproximado.

### 3. Templates pra teste
Em desenvolvimento de novas integracoes (`/perfil-mentorada`, `/celeste`), usar os 3 JSONs como casos de teste.

---

**Exemplos do Metodo Imperatriz de Anamnese — propriedade Tata Goncalves.**
