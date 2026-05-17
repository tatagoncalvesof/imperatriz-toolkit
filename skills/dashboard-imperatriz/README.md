# Dashboard Imperatriz

> Pilar 4 (Medição) da Travessia Imperatriz — Tata Gonçalves

Mede. Agrega. Alerta. Decide quem sobe nível.

26 KPIs primários (1 por porta A-Z), benchmark BR mentora high-ticket, regra de cor (verde/amarelo/vermelho), 2 visões (Tata vê a Corte / mentorada vê só ela), 4 modos, output HTML + JSON.

---

## Por que existe

A Travessia Imperatriz tem 4 pilares: 1) Mapa (26 portas A-Z), 2) Fluxo (gates objetivos via `gates-imperatriz`), 3) Execução (RACI via `raci-imperatriz`), 4) Medição — esta skill.

Sem o Pilar 4, mentorada confunde movimento com progresso. Faz copy, posta carrossel, manda DM e acha que "andou". Achou. KPI mede. Sem KPI por fase, mentorada acha que andou.

Esta skill resolve isso: 1 KPI primário por porta, benchmark fixo, cor automática, alerta antes do colapso.

---

## O que entrega

### Dois dashboards HTML interativos

1. **Visão Tata** — Corte inteira, matriz mentorada × porta, agregados, alertas, prontas pra Investidura, cases prontos, receita agregada
2. **Visão mentorada** — só a porta dela, KPIs próprios, próximo gate, próximo passo, histórico 6 meses, distância pra próximo nível hierárquico

### JSON estruturado

Pra alimentar `tatou-2.0`, integrações futuras (Marketing Command app, Notion, Airtable), automações.

### Quatro modos

| Modo | Usa quando |
|---|---|
| `--tata` | Tata abre call mensal de Corte e quer ver tudo de cima |
| `--mentorada [nome]` | Mentorada pede o painel dela ou Tata revisa caso individual |
| `--alertas` | Tata quer só vermelhos urgentes (priorizados) pra resolver primeiro |
| `--prontas-investidura` | Trimestre fechando, decidir quem sobe nível hierárquico |

---

## Hierarquia da Corte

A Travessia tem 4 níveis hierárquicos. Esta skill decide quem sobe.

| Nível | KPIs verdes exigidos | Tempo médio |
|---|---|---|
| **Iniciada** | A-F (6 portas) | 0-3 meses |
| **Cortesã** | A-L (12 portas) | 3-9 meses |
| **Dama** | A-V (22 portas) | 9-18 meses |
| **Imperatriz** | A-Z (26 portas, ciclos W-Z em dia) | 18+ meses |

Subir nível = Investidura. Cerimônia interna da Corte. Critério é binário: KPIs verdes ou não.

---

## Os 26 KPIs (resumo)

Detalhe completo em `KPIS-POR-PORTA.md`. Resumo da régua:

| Porta | KPI primário | Benchmark verde |
|---|---|---|
| A | Dossiê completo | 100% |
| B | ICP convertendo | > 2x conversão geral |
| C | CTR pattern interrupt | 2x baseline nicho |
| D | Motivos pra escolher ela | 3 articulados |
| E | Ativos consistentes | 3 visualmente alinhados |
| F | Piloto sem ajuda | 1 entregue |
| G | Aceitação pós-pitch | > 25% |
| H | Site + área + tracking | 100% funcionando |
| I | Leads orgânicos | 50+/mês |
| J | Conversão página | 1-3% frio / 8-15% quente |
| K | ROAS | > 3x |
| L | Lift teste | > 15% sig. estatística |
| M | Conversão funil | 0,5-2% (frio→cliente) |
| N | Publicações/semana | 4+ |
| O | 1ª resposta DM / close DM | < 5min / > 30% |
| P | Show-up / conversão evento | > 30% / > 5% |
| Q | Variação fechamento mês a mês | < 20% |
| R | Reembolso / NPS | < 5% / > 60 |
| S | Tarefas delegadas | 80%+ |
| T | Reativação base / indicação | 15%+ / 20%+ |
| U | Retenção 12 meses | > 60% |
| V | Mídia / LinkedIn | 1+/trim, 10k+ |
| W | Termos no Google | 100+ |
| X | Audit trimestral | > 80/100 |
| Y | Margem líquida | > 30% |
| Z | Melhoria/mês | 1+ |

---

## Como roda

### Manual
```bash
/dashboard-imperatriz --tata
/dashboard-imperatriz --mentorada Larissa
/dashboard-imperatriz --alertas
/dashboard-imperatriz --prontas-investidura
```

### Automatizado (mensal)
- Cron dia 1 do mês roda `--tata` com dado fechado do mês anterior
- Cron dia 1 do mês roda `--mentorada` pra cada uma da Corte
- Cron dia 1 do mês envia `--alertas` pro WhatsApp da Tata se houver crítico
- Cron dia 1 de mês de fim de trimestre roda `--prontas-investidura`

---

## Output esperado

### Pasta no Obsidian Vault

```
~/Documents/Obsidian Vault/03 - Projetos/Dashboard-Corte/
└── 2026-05/
    ├── dashboard-tata.html
    ├── dashboard-tata.json
    ├── alertas-criticos.md
    └── prontas-investidura.md

~/Documents/Obsidian Vault/04 - Mentoradas/[Nome]/Dashboard/
└── 2026-05/
    ├── dashboard.html
    ├── dashboard.json
    └── proximo-passo.md
```

### Visual

- Cores: dourado #D6A648 (acento), preto #0e0c0a (fundo), creme #f4ecdc (texto)
- Fontes: Inter (sans), Instrument Serif (display)
- Diagramas: Mermaid embutido (heatmap das portas, flowchart da Investidura)
- Interativo: tabs, filtros por nível hierárquico, expand/collapse por mentorada

---

## Integração

**Lê de:**
- `/dossie-mentorada` profile `16-kpis-dashboard`
- `/gates-imperatriz`
- `/perfil-mentorada`

**Alimenta:**
- `/tatou-2.0`
- `/raci-imperatriz`
- Marketing Command app (via JSON)

**Despacha pra:**
- `/diagnostico-gargalo-funil` (quando vermelho em K-M)
- `/calendario-imperatriz` (quando vermelho em N)
- `/reativacao-por-temperatura` (quando vermelho em T)
- `/gates-imperatriz --rollback` (quando upstream contaminada)

---

## Filosofia

> "Sem KPI por fase, mentorada acha que andou."

A skill não conforta. Mede. O conforto vem de saber exatamente onde está e o que falta pra próxima Investidura.

Verde = passou. Amarelo = chegou perto. Vermelho = não passou. Sem subjetivismo. Sem "tá quase". Sem "deu pra ver evolução". Bate benchmark BR mentora high-ticket ou não bate.

---

## Arquivos da skill

- `SKILL.md` — definição da skill, modos, regras duras
- `README.md` — este arquivo
- `KPIS-POR-PORTA.md` — 26 KPIs com benchmark + regras de cor
- `VISAO-TATA.md` — layout do dashboard agregado
- `VISAO-MENTORADA.md` — layout do dashboard individual
- `ALERTAS-LOGICA.md` — regras de alerta + priorização
- `TEMPLATE-HTML.md` — template HTML interativo

---

**Travessia Imperatriz — propriedade intelectual Tata Gonçalves. Pilar 4 (Medição) operado por esta skill.**
