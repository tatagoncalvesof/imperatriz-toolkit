# Produtos Imperatriz — Pilar 8 da Travessia Imperatriz

> *"Esteira é arquitetura, não improvisação. Cada produto tem hora de entrar na vida da mentorada."*

Skill de orquestração da **esteira de ascensão de produtos da Tata Gonçalves**. Mapeia os 10 produtos vendidos pela Tata (do skill público gratuito até a sucessão), aplica filtros automáticos de elegibilidade (nível hierárquico, pré-requisito, timing, saúde), gera scripts de cross-sell e responde a pergunta operacional mais cara da mentoria: **"qual produto eu ofereço pra ELA AGORA?"**

> ATENÇÃO: esta skill NÃO é dos produtos da mentorada — é dos produtos **DA TATA**. É o sistema de monetização da Corte.

---

## O QUE ELA FAZ

A `produtos-imperatriz` é o **gerente de receita** da Travessia. Em uma frase: **lê dossiê de cada mentorada, cruza com a esteira da Tata, e despacha qual produto oferecer, quando e como**.

Concretamente, ela:

- **Mapeia** os 10 produtos da Tata (R$0 → R$500k/ano) com critérios objetivos de elegibilidade
- **Bloqueia** ofertas inadequadas por nível hierárquico (sem exceção)
- **Calcula** janela ideal de cross-sell (60-90 dias, sazonalidade, lançamentos)
- **Gera** scripts literais por canal (WhatsApp, e-mail, call) com 5 objeções respondidas
- **Suspende** oferta automaticamente em mentorada com KPI vermelho ou crise
- **Roda** automaticamente após conclusão de qualquer pipeline em `tatou-2.0`
- **Registra** todas as ofertas (planejadas → apresentadas → respondidas) no `dossie-mentorada`
- **Audita** mensalmente toda a Corte: quem está pronta pra subir de produto

Ela NÃO escreve copy de lançamento (isso é `skill-pagina-vendas`). Ela NÃO precifica do zero (isso é `pricing-dinamico-imperatriz`). Ela é a **camada de decisão** sobre QUAL produto oferecer pra QUAL mentorada AGORA.

---

## QUANDO USAR

| Situação | Modo |
|----------|------|
| Tata pergunta "qual produto pra Maria?" | `--proximo` |
| Mentorada acabou de pagar produto X | `--proximo` (pra próximo) |
| Tata quer script literal de upgrade | `--cross-sell` |
| Auditoria mensal da Corte | `--mapa` + `--proximo` em loop |
| Lançamento da Tata, quer ver elegíveis | `--mapa` |
| Mentorada perguntou pela 1ª vez sobre Mastermind/1:1 | `--proximo` |
| Calcular quando vem a próxima oferta | `--timing` |
| Após qualquer pipeline em `tatou-2.0` | dispara automático |

**Regra crítica:** se `dossie-mentorada` não existe pra mentorada-alvo, a skill bloqueia e despacha criação primeiro. Sem dossiê, sem oferta.

---

## A ESTEIRA EM UMA TABELA

| # | Produto | Ticket | Nível mínimo |
|---|---------|--------|--------------|
| 1 | Skills compartilháveis (público) | R$0 | qualquer |
| 2 | Imperatriz Toolkit | R$297-997 | Aspirante |
| 3 | Bestseller (livro) | R$49-99 | Aspirante |
| 4 | Imersões presenciais | R$2-7k | Princesa |
| 5 | **Travessia Imperatriz** | R$30-50k | Princesa (com imersão) |
| 6 | Mastermind premium | R$30-100k/ano | Duquesa |
| 7 | 1:1 com Tata | R$200-500k/ano | Condessa |
| 8 | Consultoria B2B | R$100k+ | Empresa (qualquer nível, ICP B2B) |
| 9 | Programa de afiliados | comissão 50%+ | qualquer (se tiver audiência) |
| 10 | Sucessão (sócia/treinadora/white label) | varia | Imperatriz Plena |

Detalhamento completo em [`ESTEIRA-COMPLETA.md`](ESTEIRA-COMPLETA.md).

---

## INSTALAÇÃO

### Onde mora

```
~/.claude/skills/produtos-imperatriz/
├── SKILL.md                    ← cérebro (sempre carregado)
├── README.md                   ← este arquivo
├── ESTEIRA-COMPLETA.md         ← os 10 produtos detalhados
├── LOGICA-CROSS-SELL.md        ← matriz de quando oferecer o quê
├── SCRIPTS-CROSS-SELL.md       ← scripts literais por produto
└── EXEMPLOS-JORNADAS.md        ← 3 jornadas Aspirante → Imperatriz Plena
```

### Como ativar

```bash
# No terminal Claude Code
/produtos-imperatriz --mapa
/produtos-imperatriz --proximo maria-silva
/produtos-imperatriz --cross-sell maria-silva travessia
/produtos-imperatriz --timing maria-silva
```

### Pré-requisito de instalação

Esta skill EXIGE que estejam instaladas:
- `dossie-mentorada` — fonte de verdade dos dados da mentorada
- `hierarquia-imperatriz` — critérios objetivos por nível
- `tatou-2.0` — orquestrador (lê estado de pipeline ativo)

Sem essas três, a skill avisa o gap e bloqueia execução.

---

## OS 4 MODOS

### `--mapa` — Visão da esteira completa

Mostra os 10 produtos com ticket, perfil, pré-requisito, calendário de lançamentos da Tata, e matriz de elegibilidade nível × produto.

Use quando: planejar Q1/Q2 de receita, briefing pra time comercial, onboarding de assistente da Tata.

### `--proximo [slug]` — Qual produto pra ELA agora

A pergunta operacional principal. Lê dossiê, aplica os 4 filtros (hierarquia, pré-requisito, timing, saúde), cruza com `tatou-2.0`, devolve recomendação.

Output: 1 produto principal + 1 alternativa + janela ideal + sinais de greenlight/red flag + script curto + 2 objeções respondidas.

Use quando: planejar próxima call, montar fila de cross-sell, auditoria mensal.

### `--cross-sell [slug] [produto]` — Script literal

Quando a Tata já decidiu o produto e quer o script pronto.

Output: 3 versões (WhatsApp curto, e-mail formal, mensagem na call) + 5 objeções respondidas + sinais de "agora não" + CTA específico.

Use quando: vai fazer a oferta hoje, quer texto pra colar.

### `--timing [slug]` — Quando próxima oferta?

Calcula janela ideal sem decidir o produto.

Output: data ideal + janela aceitável + janela proibida + condições mínimas + sinais de readiness.

Use quando: planejamento, não tem pressa, quer agendar.

---

## INTEGRAÇÃO COM ECOSSISTEMA

### Lê de
- `dossie-mentorada` (perfil, nível, histórico, KPIs, decisões)
- `hierarquia-imperatriz` (critérios objetivos por nível)
- `tatou-2.0` (estado atual de despacho)
- `dashboard-imperatriz` (KPIs e churn risk)
- `gates-imperatriz` (portas concluídas)
- `calendario-imperatriz` (sazonalidade e lançamentos)

### Grava em
- `19-historico-compras.json` (ofertas planejadas, apresentadas, respondidas)
- `18-historico-decisoes.json` (auditoria)

### Dispara
- `pricing-dinamico-imperatriz` (ticket exato por mentorada)
- `crise-imperatriz` (se detectar churn risk durante check)
- `reativacao-por-temperatura` (se mentorada tá fria)

### Hook automático
Roda **após cada conclusão de pipeline** em `tatou-2.0` (gancho automático). Tata não precisa pedir.

---

## REGRAS DE OURO (recap rápido)

1. Nível hierárquico = filtro automático. Aspirante NÃO recebe oferta de 1:1.
2. 60-90 dias entre cross-sells. Sem exceção.
3. KPI vermelho ou crise = SUSPENDE oferta. Cuida do humano primeiro.
4. Black Friday só pra Toolkit/Livro. Travessia/Mastermind/1:1 não tem desconto.
5. Comissão de afiliados 50%+. Sempre.
6. Sempre registra oferta no dossiê. Sempre.

Detalhes em `SKILL.md` (regras duras + anti-patterns).

---

## EXEMPLO RÁPIDO

```
$ /produtos-imperatriz --proximo maria-silva

# PRÓXIMA OFERTA — Maria Silva

## SITUAÇÃO ATUAL
- Nível: Princesa (validada há 4 meses)
- Última compra: Imersão Olimpo (R$3.997, há 67 dias)
- KPIs: verde (3/3)
- Pipeline ativo: nenhum

## RECOMENDAÇÃO
**Produto:** Travessia Imperatriz
**Ticket:** R$37k (à vista) ou 12x R$3.700
**Janela ideal:** próximas 3 semanas (turma fecha 15/Jun)

## POR QUÊ AGORA
Saiu da Imersão Olimpo há 67 dias (>60d, fora de saturação),
KPIs verdes em 3/3 áreas, e Porta E concluída no gate de
ontem — estado emocional alto pra absorver Travessia.

## SCRIPT CURTO (WhatsApp)
"Maria, vi seu gate da Porta E ontem. Boa, garota!
Quero te chamar pra uma conversa de 30min — acho que
chegou a hora de você entrar na Travessia. Tem 3 vagas
na turma de Junho. Posso te ligar amanhã 14h?"
```

---

## FAQ

**P: Por que Aspirante não recebe oferta de Travessia direto?**
R: Travessia é R$30-50k de comprometimento. Aspirante ainda não validou que vai executar — tem que passar por Toolkit + Imersão pra Tata ter prova de que ela termina o que começa. Sem prova, refund alto e churn na Travessia.

**P: Posso forçar oferta se a mentorada PEDIR?**
R: Tata pode. Mas a skill sinaliza risco e pede confirmação dupla. E o dossiê registra "oferta forçada por pedido da mentorada" pra auditoria. Se der ruim, fica claro.

**P: E se a mentorada compra produto premium e quer DESISTIR?**
R: Suspende imediatamente próximo cross-sell (mínimo 90 dias), ativa `crise-imperatriz`, agenda conversa de cuidado. Não tenta salvar a venda — salva a relação.

**P: Comissão de afiliados de 50% não come muito margem?**
R: Não. CAC de afiliada qualificada é 10x menor que tráfego pago. 50% de comissão em mentorada que já validou é o melhor CAC do mercado high-ticket.

---

**Pilar 8 da Travessia Imperatriz — propriedade intelectual Tata Gonçalves.**
