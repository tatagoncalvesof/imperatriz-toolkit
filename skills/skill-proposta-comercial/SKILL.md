---
name: skill-proposta-comercial
description: Gera propostas comerciais profissionais para clientes de consultoria tech/IA. Use quando o usuario pedir proposta, proposta comercial, orcamento, contrato, escopo, investimento, proposal, ou client proposal.
---

# Skill: Proposta Comercial

Gere propostas comerciais completas e profissionais para projetos de tecnologia e IA.

## Identidade do Prestador

- **Nome:** Tata Gonçalves
- **Empresa:** Instituto Tata Gonçalves
- **Atuação:** Consultoria em Tecnologia e Inteligência Artificial
- **Especialidades:** Bots WhatsApp, plataformas IA, landing pages, dashboards, apps SaaS, automações
- **Stack:** Node.js, React, TypeScript, IA (Gemini/OpenAI/Claude), deploy VPS
- **Contato:** tatagoncalvesoficial@gmail.com
- **Site:** iacomtata.com.br

## Workflow

### Etapa 1 — Coleta de Informações

Pergunte ao usuário (se não fornecido):

1. **Nome do cliente** e empresa/projeto
2. **Tipo de proposta:** projeto completo | MVP | manutenção | consultoria
3. **Descrição do que o cliente precisa** (problema a resolver)
4. **Funcionalidades principais** (lista)
5. **Prazo desejado** (se houver)
6. **Orçamento estimado do cliente** (se souber)

### Etapa 2 — Geração da Proposta

Com base nas informações coletadas:

1. Selecione o template adequado em `references/`:
   - Projeto completo → `template-proposta-completa.md`
   - MVP → `template-proposta-mvp.md`
   - Manutenção/retainer → `template-manutencao.md`
2. Preencha todas as seções do template
3. Calcule o investimento usando a Tabela de Precificação abaixo
4. Inclua os termos de `references/termos-condicoes.md`
5. Prepare o email de envio de `references/emails-followup.md`

### Etapa 3 — Revisão e Ajustes

1. Apresente a proposta completa ao usuário
2. Pergunte se deseja ajustar escopo, prazo ou valores
3. Aplique alterações solicitadas
4. Gere versão final

### Etapa 4 — Entrega

1. Salve a proposta como arquivo `.md` no diretório do projeto do cliente
2. Gere o email de envio personalizado
3. Sugira próximos passos (follow-up em 3 dias, reunião, etc.)

## Tabela de Precificação

### Valores por Hora (referência interna — NÃO incluir na proposta)

| Complexidade | Valor/Hora |
|---|---|
| Simples (landing page, bot básico) | R$ 150–200 |
| Média (dashboard, API, integrações) | R$ 200–300 |
| Alta (SaaS, IA avançada, multi-canal) | R$ 300–450 |

### Faixas por Tipo de Projeto

| Tipo de Projeto | Faixa de Investimento | Prazo Típico |
|---|---|---|
| Landing page simples | R$ 1.500–3.000 | 3–5 dias |
| Landing page + integração | R$ 3.000–6.000 | 5–10 dias |
| Bot WhatsApp básico | R$ 3.000–5.000 | 5–7 dias |
| Bot WhatsApp + IA | R$ 5.000–10.000 | 7–14 dias |
| Dashboard/painel admin | R$ 5.000–12.000 | 10–20 dias |
| Plataforma SaaS (MVP) | R$ 10.000–25.000 | 15–30 dias |
| Plataforma SaaS completa | R$ 25.000–60.000 | 30–60 dias |
| App com IA generativa | R$ 8.000–20.000 | 10–25 dias |
| Automação/integração | R$ 2.000–8.000 | 3–10 dias |
| Consultoria (por hora) | R$ 300–450/hora | — |

### Manutenção Mensal

| Plano | Inclui | Valor/Mês |
|---|---|---|
| Básico | Monitoramento, correções, 4h suporte | R$ 800–1.500 |
| Profissional | Básico + melhorias, 8h suporte | R$ 1.500–3.000 |
| Premium | Profissional + novas features, 16h suporte | R$ 3.000–6.000 |

### Opções de Pagamento

| Condição | Desconto/Acréscimo |
|---|---|
| À vista (PIX) | 10% de desconto |
| 2x (50/50 — início + entrega) | Valor cheio |
| 3x (40/30/30 — início + meio + entrega) | Valor cheio |
| Por milestone (marcos de entrega) | Valor cheio |
| Parcelamento 4x+ | Acréscimo de 5% |

## Regras de Formatação

1. Usar linguagem profissional mas acessível — sem jargão excessivo
2. Sempre incluir tabela de investimento com valores claros
3. Prazo em dias úteis, com data estimada de início e entrega
4. Listar entregas (deliverables) como checklist
5. Incluir seção "O que NÃO está incluso" para evitar scope creep
6. Proposta válida por 15 dias (padrão)
7. Número da proposta no formato: `PROP-AAAAMM-NNN` (ex: PROP-202602-001)
8. Data no formato brasileiro: DD/MM/AAAA

## Estrutura Obrigatória da Proposta

Toda proposta DEVE conter estas seções, nesta ordem:

1. **Cabeçalho** — número, data, cliente, projeto
2. **Resumo Executivo** — 2-3 parágrafos sobre o problema e a solução
3. **Escopo do Projeto** — descrição detalhada do que será feito
4. **Entregas** — lista de deliverables com checklist
5. **Cronograma** — tabela com fases, atividades e prazos
6. **Investimento** — tabela com itens, valores e total
7. **Condições de Pagamento** — opções disponíveis
8. **O Que NÃO Está Incluso** — lista de exclusões
9. **Sobre a Consultora** — mini bio da Tata
10. **Termos e Condições** — resumo dos termos principais
11. **Aceite** — espaço para assinatura/confirmação

## Seção "Sobre a Consultora" (usar em todas as propostas)

> **Tata Gonçalves** é consultora de tecnologia e inteligência artificial com experiência
> na criação de soluções digitais sob medida. Especializada em automações com IA,
> desenvolvimento de plataformas web e bots inteligentes, Tata já entregou projetos
> envolvendo WhatsApp bots com IA generativa, plataformas SaaS, dashboards de gestão
> e sistemas de automação para diversos segmentos. Fundadora do Instituto Tata Gonçalves,
> oferece soluções que combinam tecnologia de ponta com praticidade para negócios reais.

## Exemplo de Uso

**Usuário:** "Preciso fazer uma proposta pro Maurício, ele quer uma plataforma de ensino com IA que gera conteúdo personalizado. Orçamento dele é uns R$ 15 mil."

**Ação:** Usar template de projeto completo, escopo de plataforma com IA, prazo ~25 dias úteis, investimento R$ 15.000, pagamento por milestone.
