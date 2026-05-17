# Validador — Balanceamento

## Por que importa

Mapa visualmente balanceado é mapa **lido em 10 segundos**. Mapa desbalanceado força olho a focar no ramo gordo, ignora os outros. Perde função.

## Regras

### Regra 1 — Ratio entre ramos principais

Nenhum ramo pode ter MAIS DE 3X sub-ramos que outro.

```
Ramo maior: max 3x sub-ramos do menor
```

Exemplo:
- Menor: 2 sub-ramos
- Maior permitido: 6 sub-ramos
- ❌ Maior atual: 10 sub-ramos → FALHA

### Regra 2 — Profundidade equilibrada

Diferença máxima de 1 nível entre profundidade do ramo mais raso e do mais profundo.

```
Ramo A: profundidade 2
Ramo B: profundidade 4
Diferença: 2 → ❌ FALHA
```

Acceptable:
```
Ramo A: profundidade 3
Ramo B: profundidade 4
Diferença: 1 → ✓
```

### Regra 3 — Sem ramo solitário (1 sub-ramo só)

Ramo com APENAS 1 sub-ramo é sintoma de hierarquia errada. Ou esse sub-ramo deveria ser irmão do pai, ou faltam outros sub-ramos.

```
Ramo X
└── Único sub  ← FALHA
```

Corrigir:
```
Ramo X (renomeado pro nome do "único sub")
```

OU adicionar mais sub-ramos.

### Regra 4 — Sem ramo vazio

Ramo principal sem nenhum sub-ramo é sintoma de subdesenvolvimento. Ou desenvolve, ou remove.

## Como corrigir desbalanceamento

### Caso 1: ramo gigante (12 sub-ramos)

**Estratégia:** agrupar em sub-categorias.

Antes:
```
Tráfego
├── Meta Ads
├── Google Ads
├── TikTok Ads
├── Bing Ads
├── LinkedIn Ads
├── Indicação
├── SEO
├── Conteúdo orgânico
├── Email
├── Influenciador
├── Afiliado
└── Direct mail
```

Depois:
```
Tráfego
├── Pago
│   ├── Meta Ads
│   ├── Google Ads
│   ├── TikTok Ads
│   └── Outros (LinkedIn, Bing)
├── Orgânico
│   ├── SEO
│   └── Conteúdo
└── Outros canais
    ├── Email
    ├── Indicação
    └── Afiliado
```

### Caso 2: ramo anêmico (2 sub-ramos)

**Estratégia:** absorver em ramo irmão OU desenvolver.

Antes:
```
Métricas
├── ROI
└── CPL
```

Depois (absorvido):
```
Negócio
├── Oferta
├── Funil
└── Métricas
    ├── ROI
    └── CPL
```

OU desenvolver:
```
Métricas
├── ROI
├── CPL
├── Conversão
├── LTV
└── CAC
```

### Caso 3: profundidade desigual

Se um ramo desce 4 níveis e outros 2, ou:
- (a) os outros precisam descer mais
- (b) o profundo está sobre-detalhado

Decisão: manter coerência. Se mapa é **estratégico**, profundidade rasa. Se é **operacional**, profundidade média.

## Output do validador

```
Balanceamento:
  Ramos principais: 6
  Sub-ramos por ramo:
    - Persona: 4
    - Dor: 5
    - Desejo: 3
    - Objeção: 4
    - Prova: 12  ⚠️
    - Mecanismo: 2  ⚠️
  Ratio: 6x (Prova:Mecanismo) — ❌ FALHA (max 3x)
  Profundidade: 2-3 (✓)

Sugestão automática:
  → Quebrar "Prova" em sub-categorias (Cases, Depoimentos, Autoridade, Dados)
  → Absorver "Mecanismo" ou desenvolver mais

Status: ⚠️ DESBALANCEADO — aplicar correção
```
