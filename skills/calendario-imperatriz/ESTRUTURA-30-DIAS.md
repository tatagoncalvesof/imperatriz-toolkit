# Estrutura 30 Dias — Template Visual + Schema JSON + Sazonalidade BR

Este arquivo é a **régua matemática** do calendário. Define quantas peças saem por semana, em quais dias, em quais canais, e como tudo se conecta.

---

## A matemática base

```
4 semanas × 1 ideia macro/semana   = 4 ideias macro
4 ideias macro × 5 peças por canal  = 20 peças adaptadas
+ 10 peças extras (engajamento)     = 10 extras
─────────────────────────────────────────
TOTAL MÊS                           = 30 peças mínimo
```

Se mentoranda usa WhatsApp Status com pulverização diária, total expande pra **45-60 peças/mês**.

---

## Visão calendário (vista de mês)

```
SEMANA 1 — Ideia Macro A
┌──────┬──────┬──────┬──────┬──────┬──────┬──────┐
│ SEG  │ TER  │ QUA  │ QUI  │ SEX  │ SÁB  │ DOM  │
├──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│CARROS│LINKED│REELS │STORIE│WHATS │BASTI │EMAIL │
│ 19h  │  8h  │ 12h  │  Q&A │ Stat │ DOR  │ 10h  │
│ ★A   │ ★A   │ ★A   │ ★A   │ ★A   │ extra│ ★A   │
└──────┴──────┴──────┴──────┴──────┴──────┴──────┘

SEMANA 2 — Ideia Macro B
[mesma estrutura, ideia macro diferente]

SEMANA 3 — Ideia Macro C
[mesma estrutura, ideia macro diferente]

SEMANA 4 — Ideia Macro D
[mesma estrutura, ideia macro diferente]

EXTRAS DO MÊS (10 peças pulverizadas):
- 4 stories de bastidor (qualquer dia)
- 2 lives/Reels reativos (qualquer dia)
- 2 drops surpresa (qualquer dia)
- 1 prova social (preferência meio do mês)
- 1 retrospectiva/futuro (último domingo)
```

---

## Tabela de horários ideais por canal (Brasil)

| Canal | Dia ideal | Horário ideal | Por quê |
|-------|-----------|---------------|---------|
| Instagram Carrossel | Seg, Qua, Sex | 19h-21h | Engajamento noturno, fim do expediente |
| Instagram Reels | Ter, Qui | 11h-13h ou 19h-21h | Almoço + noite, scroll de descanso |
| Instagram Stories | Diário | 9h-11h e 19h-22h | Acordar + dormir, 2 picos de visualização |
| Instagram Stories Q&A | Qui, Sex | 10h abre — 22h fecha | 12h pra acumular respostas |
| LinkedIn | Ter, Qui | 7h-9h ou 12h-14h | Antes/durante expediente B2B |
| Email | Domingo | 10h-11h | Maior taxa de abertura no Brasil |
| Email follow-up | Ter, Qui | 8h ou 16h | Reforço durante semana |
| WhatsApp Status | Diário pulverizado | 9h, 14h, 20h | 3 toques/dia sem saturar |

---

## Tabela de sazonalidade BR (calendário oficial)

A skill consulta essa tabela ao gerar ideias macro. Se data comemorativa cai no mês, vira tema obrigatório de pelo menos 1 das 4 semanas.

| Mês | Data comemorativa | Tema-âncora | Tipo |
|-----|------------------|-------------|------|
| Janeiro | Ano novo + planejamento | Recomeço, metas, virada | Reflexão |
| Fevereiro | Carnaval + volta às aulas | Pausa estratégica, retomada | Híbrido |
| Março | Dia da Mulher (08/03) + Páscoa* | Empoderamento + renovação | Identitário |
| Abril | Páscoa* + Dia do Trabalho prep | Renovação + propósito | Reflexão |
| Maio | Dia das Mães (2º domingo) | Maternidade, legado | Emocional |
| Junho | Dia dos Namorados (12/06) + Festas Juninas | Relacionamento, comunidade | Emocional |
| Julho | Férias escolares | Pausa, consumo lento | Suave |
| Agosto | Dia dos Pais (2º domingo) | Paternidade, autoridade | Emocional |
| Setembro | Independência (07/09) + primavera | Liberdade, recomeço | Identitário |
| Outubro | Dia das Crianças (12/10) + Day of Dead BR | Criança interior, legado | Emocional |
| Novembro | Black Friday (última sexta) + Consciência Negra (20/11) | Oferta + identidade | Comercial |
| Dezembro | Natal + Réveillon | Encerramento, gratidão, projeção | Reflexão |

*Páscoa varia entre março/abril.

### Datas comerciais quentes (foco vendas)

| Data | Mês | Tipo de campanha sugerida |
|------|-----|--------------------------|
| Black Friday | última sexta novembro | 7 dias de pré + 1 dia ofertão |
| Cyber Monday | segunda após BF | continuação BF |
| Volta às aulas | fevereiro | mentoria/curso/método |
| Dia das Mães | maio | high-ticket emocional |
| Dia dos Pais | agosto | high-ticket emocional |
| Aniversário Mentoria | personalizado | celebração + oferta especial |

---

## Schema JSON do calendário (output --gerar)

Salvo em `~/imperio/mentoradas/[nome]/calendario-[YYYY-MM].json`

```json
{
  "meta": {
    "mentoranda": "Maria Silva",
    "mes": "2026-06",
    "porta_atual": "L",
    "lancamento_ativo": {
      "ativo": true,
      "produto": "Mentoria Imperio 2.0",
      "fase": "aquecimento",
      "data_abertura": "2026-06-15",
      "data_fechamento": "2026-06-22"
    },
    "sazonalidade": ["Dia dos Namorados", "Festa Junina"],
    "objetivo_comercial": "30 vagas vendidas",
    "canais_ativos": ["carrossel", "stories", "reels", "linkedin", "email", "whatsapp"],
    "voz_marca_aplicada": "~/imperio/mentoradas/maria/03-voz-de-marca.json",
    "validacao_voz_humana_br": "aprovado"
  },
  "semanas": [
    {
      "numero": 1,
      "periodo": "2026-06-01 a 2026-06-07",
      "ideia_macro": {
        "tema_central": "Por que mentora high-ticket vende barato sem perceber",
        "angulo_narrativo": "contraintuitivo",
        "cruzamento_porta": "Porta L — aquecimento, prepara dor pra abertura",
        "cruzamento_lancamento": "fase aquecimento — desperta dor",
        "cruzamento_sazonalidade": "nenhuma essa semana",
        "promessa_semana": "Você vai entender por que cobra barato e como reverter"
      },
      "cronograma": [
        {
          "dia": "2026-06-02",
          "dia_semana": "segunda",
          "canal": "carrossel",
          "horario": "19h",
          "titulo": "3 erros que travam mentora high-ticket",
          "despacha_pra": "/skill-carrossel-instagram",
          "briefing_completo": "..."
        },
        {
          "dia": "2026-06-03",
          "dia_semana": "terca",
          "canal": "linkedin",
          "horario": "8h",
          "titulo": "Por que high-ticket é decisão de posicionamento",
          "despacha_pra": "/linkedin-empire",
          "briefing_completo": "..."
        }
      ],
      "validacao": {
        "espacamento_minimo_aprovado": true,
        "tom_calibrado_aprovado": true,
        "voz_marca_aprovada": true,
        "voz_humana_br_aprovada": true
      }
    }
  ],
  "extras": {
    "bastidor": [...],
    "reativos": [...],
    "drops": [...],
    "prova_social": [...],
    "retrospectiva": [...]
  },
  "auditoria_anti_canibalizacao": {
    "score": 96,
    "canibalizacoes_detectadas": 0,
    "gaps_de_canal": [],
    "descolamento_porta": "nenhum"
  }
}
```

---

## Schema JSON do briefing por peça

Cada peça dentro do `cronograma` tem o briefing completo:

```json
{
  "id": "2026-06-02-carrossel",
  "canal": "carrossel",
  "subcanal": "feed_instagram",
  "tema": "3 erros que travam mentora high-ticket",
  "hook": "Você tá vendendo barato e nem percebe.",
  "ideia_macro_id": "semana-1",
  "estrutura": {
    "formato": "lista_3_itens",
    "slides": 7,
    "slide_1": {
      "tipo": "hook",
      "titulo": "3 erros que travam mentora high-ticket",
      "subtitulo": "Você comete pelo menos 1 hoje"
    },
    "slide_2": {
      "tipo": "erro_1",
      "titulo": "Erro 1: Vender por hora",
      "corpo": "Hora vira commodity. Resultado vira ativo."
    },
    "slide_7": {
      "tipo": "cta",
      "titulo": "Salva esse pra revisar antes do próximo orçamento",
      "badge": "SALVE"
    }
  },
  "caption": "[texto completo da legenda...]",
  "hashtags": ["#mentoriahighticket", "#imperioia", "#vendaspremium"],
  "design": {
    "paleta": "coach_mentora",
    "cor_primaria": "#1E1B4B",
    "cor_secundaria": "#8B5CF6",
    "fonte": "Montserrat Bold"
  },
  "horario_publicacao": "2026-06-02T19:00:00-03:00",
  "despacha_pra": "/skill-carrossel-instagram",
  "filhos_relacionados": [
    "2026-06-03-linkedin",
    "2026-06-04-reels",
    "2026-06-05-stories-qa",
    "2026-06-08-email"
  ],
  "validacao": {
    "voz_marca": "aprovado",
    "voz_humana_br": "aprovado",
    "anti_canibalizacao": "aprovado"
  }
}
```

---

## Distribuição de carga semanal recomendada

```
SEGUNDA   ████████████░░░░░░░░  60% peso (carrossel = ativo principal)
TERÇA     ██████░░░░░░░░░░░░░░  30% peso (LinkedIn — público B2B)
QUARTA    ██████████░░░░░░░░░░  50% peso (Reels — viralidade)
QUINTA    ████████░░░░░░░░░░░░  40% peso (Stories Q&A — engajamento)
SEXTA     ████░░░░░░░░░░░░░░░░  20% peso (WhatsApp + descanso conteúdo pesado)
SÁBADO    ██░░░░░░░░░░░░░░░░░░  10% peso (bastidor leve)
DOMINGO   ██████░░░░░░░░░░░░░░  30% peso (email = encerramento da semana)
```

Princípio: **picos terça e quarta** (decisão de compra) + **abertura segunda** (semana começa) + **fechamento domingo** (preparar a próxima).

---

## Volume mínimo vs ideal por canal/mês

| Canal | Mínimo viável | Ideal | Saturação (parar) |
|-------|--------------|-------|--------------------|
| Carrossel | 4/mês | 8-12/mês | 16+/mês |
| Reels | 4/mês | 8/mês | 12+/mês |
| Stories | 30/mês (1/dia) | 90/mês (3/dia) | 180+/mês (6+/dia) |
| Stories Q&A (caixinha) | 1/mês | 4/mês | 6+/mês |
| LinkedIn | 4/mês | 8/mês | 12+/mês |
| Email | 4/mês | 6-8/mês | 12+/mês |
| WhatsApp Status | 30/mês | 60/mês | 100+/mês |

Se passar saturação, mentoranda corre risco de mute/unfollow. A skill alerta.

---

## Estados especiais do calendário

### Lançamento ativo (modo intensificado)

Quando `lancamento_ativo.ativo = true`, calendário muda:

- **Aquecimento (D-14 a D-7):** intensifica sintomas/dor
- **Abertura (D-7 a D0):** apresenta solução/método/oferta
- **Urgência (D0 a D+5):** prova social + scarcity + bônus
- **Fechamento (D+5 a D+7):** última chance + medo de perder
- **Pós-venda (D+7 a D+30):** consolidação + próximo lançamento

Cada fase tem proporção de canais diferente. Detalhe em `EXEMPLOS-CALENDARIOS.md` (calendário Porta L).

### Sem lançamento (modo recorrente)

Mix balanceado: 40% educativo + 30% engajamento + 20% prova social + 10% pessoal.

### Modo descanso (férias, mudança, recuperação)

3 dias mín. de pausa anunciada > silêncio sem aviso. Skill sugere conteúdo evergreen agendado.

---

## Checklist de validação do calendário gerado

Antes de salvar, a skill valida:

- [ ] 4 ideias macro distintas (sem repetição de tema)
- [ ] Cada ideia macro cruza os 3 vetores (Porta + Lançamento + Sazonalidade)
- [ ] 20 peças adaptadas (5 canais × 4 semanas)
- [ ] 10 peças extras (4 bastidor + 2 reativos + 2 drops + 1 prova + 1 retro)
- [ ] Espaçamento mínimo 2 dias entre peças do mesmo tema
- [ ] Tom calibrado por canal (cada peça nativa)
- [ ] Voz-de-marca aplicada em todas
- [ ] Voz-humana-br aprovou todos os textos
- [ ] Horários respeitam tabela de horários ideais
- [ ] Distribuição de carga semanal balanceada
- [ ] Volume por canal dentro do ideal (nem mínimo, nem saturação)

Se 1 item falhar, regerar antes de salvar.
