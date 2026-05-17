# 04 — Cadência por Canal

## Princípio

**Cadência é função da Porta da Travessia, não da ambição da mentorada.**

Mentorada na Porta C (Marca) postando 5x/dia em 6 canais é mentorada que vai pivotar em 30 dias. Mentorada na Porta N (Calendário) postando 1x/semana em 1 canal é mentorada que vai morrer no algoritmo.

A skill calibra cadência olhando:
1. Porta atual da Travessia
2. Canais que ela **já opera** (não inventa canal)
3. Tamanho do time de conteúdo (lê do `dossie-mentorada`)
4. Nível (Princesa / Marquesa / Imperatriz)
5. Estado do funil (lançamento ativo? venda quente? pré-aquecimento?)

## Tabela canônica de cadência (default por Porta)

Multiplicar por `1.0` se a mentorada tem time, `0.7` se sozinha, `0.5` se só ela e meio expediente.

### Portas A-D (Descoberta / Identidade / Marca / Posicionamento)

| Canal | Frequência semanal | Horário padrão | Voz do canal |
|---|---|---|---|
| Instagram Feed | 2-3 | 18h-21h | Reflexiva, manifesto-style |
| Instagram Stories | 5-7 sequências/sem | livre | Próxima, cotidiana |
| Instagram Reels | 1 | 18h-20h | Direta, hookada |
| LinkedIn | 1-2 | 8h-10h | Técnica, autoridade |
| Email | 0-1 | 8h-9h ter/qui | Carta longa |
| WhatsApp Status | 0-2 | 9h ou 19h | Bastidor íntimo |

### Portas E-H (Oferta / Promessa / Pitch / Preço)

| Canal | Frequência semanal |
|---|---|
| Instagram Feed | 3 |
| Instagram Stories | 7-10 sequências/sem |
| Instagram Reels | 2 |
| LinkedIn | 2 |
| Email | 1-2 |
| WhatsApp Status | 2-3 |

### Portas I-N (Funil / Tráfego / Lançamento / Calendário)

| Canal | Frequência semanal |
|---|---|
| Instagram Feed | 4-5 |
| Instagram Stories | 10-14 sequências/sem |
| Instagram Reels | 2-3 |
| LinkedIn | 2-3 |
| Email | 2 |
| WhatsApp Status | 3-5 |

### Portas O-R (Vendas / Operação / Atendimento)

| Canal | Frequência semanal |
|---|---|
| Instagram Feed | 4 |
| Instagram Stories | 14+ sequências/sem (atendimento + bastidor) |
| Instagram Reels | 2 |
| LinkedIn | 2 |
| Email | 2-3 (campanha) |
| WhatsApp Status | 5-7 |

### Portas U-Z (Escala / Sucessão)

| Canal | Frequência semanal |
|---|---|
| Instagram Feed | 3 |
| Instagram Stories | 7-10 sequências/sem |
| Instagram Reels | 1-2 |
| LinkedIn | 3-4 (canal de autoridade B2B) |
| Email | 1-2 (newsletter de pensamento) |
| WhatsApp Status | 2-3 |

## Voz por canal (mesma pessoa, formas diferentes)

A voz da mentorada NÃO muda — quem fala é a mesma. Mas a **forma** muda por canal:

| Canal | Forma | Exemplo de tom |
|---|---|---|
| **LinkedIn** | Técnica, didática, com framework nomeado | "3 sintomas de funil quebrado e como diagnosticar em 10 min" |
| **Instagram Feed (carrossel)** | Híbrida — gancho emocional, miolo técnico, fechamento provocativo | Capa: "Você não vende porque escreve áudio errado" / Slides: passo-a-passo |
| **Instagram Feed (post estático)** | Manifesto, frase de impacto | "Marca que não toma posição é marca que não fica na cabeça" |
| **Instagram Stories** | Conversacional, próxima, voz de áudio transcrito | "gente, abre o pote pra vocês: tô indo pra reunião e..." |
| **Instagram Reels** | Direto, hookado, executivo | "3 frases que destroem qualquer pitch" |
| **Email** | Carta longa, intimista, narrativa | "Tata, deixa eu te contar o que aconteceu na sexta..." |
| **WhatsApp Status** | Bastidor cru, foto + frase | Foto da agenda: "dia que decide o mês" |

## Regras de cadência

1. **Nunca propor cadência pra canal que a mentorada não opera.** Se ela não tem LinkedIn ativo, LinkedIn entra como "não publicar", não como "0/sem".
2. **Espaçar 2-3h entre peças no mesmo canal.** Postar 3 stories seguidos de assuntos diferentes mata todos.
3. **1 ideia central por semana × 5 adaptações por canal.** Regra herdada de `calendario-imperatriz` — a linha editorial **declara** a regra; o calendário **executa**.
4. **Bloco de Monetize concentrado.** Quando entra venda, entra forte (3-5 peças no mesmo dia em vez de pulverizar).
5. **Janela morta protegida.** Cadência é regra-base; mentorada pode ter janela de silêncio (ex: domingo desligado, manhã de criação) — a skill respeita se declarado.
6. **Aumentar cadência só se aumentou time.** Se quer dobrar volume, primeiro contrata. Não sobrecarrega quem já posta.

## Como apresentar cadência pra mentorada

A skill mostra cadência **sempre em termos operacionais**, nunca em termos abstratos:

❌ Errado: "Você deve ter alta presença no LinkedIn"
✅ Certo: "LinkedIn: 2 posts longos/semana — terça e quinta, 8h. Voz técnica, com framework nomeado. Tempo de produção estimado: 1h cada peça."

## Saída JSON

```json
"cadencia_por_canal": {
  "instagram_feed": {
    "frequencia_semanal": 4,
    "horario_padrao": "18h-21h",
    "voz_canal": "Híbrida — gancho emocional + miolo técnico",
    "formato_dominante": "carrossel",
    "tempo_producao_minutos": 90,
    "ativo": true
  },
  "instagram_stories": {
    "frequencia_semanal_sequencias": 12,
    "horario_padrao": "livre, distribuído",
    "voz_canal": "Conversacional, próxima",
    "formato_dominante": "sequência 5-8 stories",
    "tempo_producao_minutos": 30,
    "ativo": true
  },
  "instagram_reels": {
    "frequencia_semanal": 2,
    "horario_padrao": "18h-20h",
    "voz_canal": "Direto, hookado",
    "formato_dominante": "30-60s talking head",
    "tempo_producao_minutos": 60,
    "ativo": true
  },
  "linkedin": {
    "frequencia_semanal": 2,
    "horario_padrao": "8h-10h ter/qui",
    "voz_canal": "Técnica, autoridade",
    "formato_dominante": "post longo + carrossel mensal",
    "tempo_producao_minutos": 90,
    "ativo": true
  },
  "email": {
    "frequencia_semanal": 1,
    "horario_padrao": "8h ter/qui",
    "voz_canal": "Carta longa, intimista",
    "formato_dominante": "narrativa com PS",
    "tempo_producao_minutos": 60,
    "ativo": true
  },
  "whatsapp_status": {
    "frequencia_semanal": 3,
    "horario_padrao": "9h ou 19h",
    "voz_canal": "Bastidor íntimo",
    "formato_dominante": "foto + frase curta",
    "tempo_producao_minutos": 5,
    "ativo": true
  }
}
```
