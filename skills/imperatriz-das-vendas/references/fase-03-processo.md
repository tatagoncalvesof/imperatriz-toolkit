# Fase 3: Construcao da Maquina Comercial

## Proposito
Construir o processo comercial completo — do primeiro contato ao pos-venda — com funil desenhado, papeis definidos, scripts prontos, CRM operacional e rotinas de acompanhamento. O objetivo e transformar vendas de improviso em maquina previsivel. Sem processo, nao existe escala. Sem escala, o faturamento depende do dono.

**Principio:** Processo mata talento. Uma maquina comercial bem construida vende mesmo quando o dono nao esta.

---

## Etapa 1: Desenho do Funil Completo (12 Etapas)

### Execucao
Desenhar o funil comercial de ponta a ponta, cobrindo TODAS as etapas — incluindo as que 90% dos negocios ignoram.

**Mapear cada etapa do funil:**

| # | Etapa | Descricao | Responsavel | Ferramenta |
|---|-------|-----------|-------------|------------|
| 1 | **Entrada** | Lead chega (organico, pago, indicacao, parceria) | Marketing/IA | CRM + formulario |
| 2 | **Qualificacao** | Verificar se o lead tem perfil, dor, urgencia e orcamento | SDR | CRM + script |
| 3 | **Agendamento** | Marcar reuniao/call com lead qualificado | SDR | Agenda + CRM |
| 4 | **Reuniao** | Conduzir reuniao diagnostica, escuta ativa, personalizacao | Closer | Roteiro + CRM |
| 5 | **Proposta** | Apresentar proposta personalizada com stack de valor | Closer | Template + CRM |
| 6 | **Fechamento** | Negociacao final, quebra de objecoes, contrato | Closer | Script + CRM |
| 7 | **Onboarding** | Primeiros 7-14 dias — garantir que o cliente sinta valor rapido | Onboarding | Checklist + CRM |
| 8 | **Follow-up** | Acompanhamento pos-venda D+7, D+15, D+30 | Gestor/IA | CRM + cadencia |
| 9 | **Downsell** | Oferta alternativa pra quem nao fechou o ticket principal | Closer/IA | Script + CRM |
| 10 | **Reativacao** | Retomar contato com leads perdidos e clientes inativos | SDR/IA | Campanha + CRM |
| 11 | **Upsell** | Oferta superior pra clientes satisfeitos | Closer | Script + CRM |
| 12 | **Renovacao** | Garantir continuidade antes do vencimento | Gestor/IA | CRM + cadencia |

**Para cada etapa, definir:**
- Objetivo especifico
- Quem executa
- Qual ferramenta/canal usa
- Qual o gatilho de entrada
- Qual o criterio de saida (quando o lead avanca)
- Tempo maximo na etapa
- O que acontece se o lead nao avanca

**Usar skill auxiliar:** `consultorrussel` para estrutura de funil + `consultorialex` para logica de leads $100M.

### Entrega da Etapa
Funil visual completo em formato de fluxo:

```
ENTRADA → QUALIFICACAO → AGENDAMENTO → REUNIAO → PROPOSTA →
FECHAMENTO → ONBOARDING → FOLLOW-UP
    ↓ (nao fechou)           ↓ (satisfeito)
  DOWNSELL                 UPSELL
    ↓ (perdido)              ↓ (vencimento)
  REATIVACAO              RENOVACAO
```

Tabela completa com 12 etapas, responsaveis, ferramentas, gatilhos e criterios.

---

## Etapa 2: Definicao de Papeis por Etapa

### Execucao
Mapear quem faz o que em cada etapa — mesmo que hoje uma pessoa acumule tudo. O mapa serve pra quando o time crescer.

**Papeis fundamentais:**

| Papel | Responsabilidade principal | Etapas do funil |
|-------|---------------------------|-----------------|
| **Marketing/Trafego** | Gerar leads qualificados | Entrada |
| **SDR** | Qualificar + agendar | Qualificacao, Agendamento, Reativacao |
| **Closer** | Fechar + negociar | Reuniao, Proposta, Fechamento, Downsell, Upsell |
| **Onboarding** | Integrar o cliente | Onboarding, Follow-up D+7 |
| **Gestor Comercial** | Acompanhar metricas, qualidade, treinamento | Todas (supervisao) |
| **IA/Automacao** | Resposta inicial, triagem, follow-up, cadencia | Entrada, Follow-up, Reativacao, Renovacao |

**Para cada papel:**
- Quantidade ideal de pessoas
- Metricas de desempenho (KPIs individuais)
- De quem recebe o lead
- Pra quem passa o lead
- O que NAO deve fazer (evitar acumulo)

### Entrega da Etapa
Matriz de responsabilidades (RACI simplificada):

| Etapa | Marketing | SDR | Closer | Onboarding | Gestor | IA |
|-------|-----------|-----|--------|------------|--------|----|
| Entrada | **E** | — | — | — | S | A |
| Qualificacao | — | **E** | — | — | S | A |
| Agendamento | — | **E** | — | — | S | A |
| Reuniao | — | — | **E** | — | S | — |
| Proposta | — | — | **E** | — | S | — |
| Fechamento | — | — | **E** | — | S | — |
| Onboarding | — | — | — | **E** | S | A |
| Follow-up | — | — | — | A | S | **E** |
| Downsell | — | — | **E** | — | S | A |
| Reativacao | — | **E** | — | — | S | **E** |
| Upsell | — | — | **E** | — | S | A |
| Renovacao | — | — | — | A | S | **E** |

*E = Executa, S = Supervisiona, A = Apoia/Automatiza*

---

## Etapa 3: Estruturacao do CRM Operacional

### Execucao
Transformar o CRM em ferramenta de gestao comercial real — nao apenas lista de contatos.

**Usar skill auxiliar:** `/blueprint-crm-operacional` para estrutura completa.

**Colunas obrigatorias do CRM:**

| Coluna | Tipo | Funcao |
|--------|------|--------|
| Nome | Texto | Identificacao |
| Telefone/WhatsApp | Texto | Canal principal |
| Email | Texto | Canal secundario |
| Origem | Lista | De onde veio (organico, pago, indicacao, parceria) |
| Etapa do funil | Lista | Onde esta AGORA no funil |
| Responsavel | Lista | Quem esta cuidando |
| Ultimo contato | Data | Quando foi o ultimo toque |
| Proximo passo | Texto | O que precisa ser feito |
| Data do proximo passo | Data | Quando fazer |
| Temperatura | Lista | Quente / Morno / Frio |
| Produto de interesse | Lista | Qual oferta |
| Ticket estimado | Numero | Valor potencial |
| Observacoes | Texto | Contexto relevante |
| Status | Lista | Ativo / Perdido / Fechado / Reativacao |
| Data de entrada | Data | Quando entrou no funil |
| Motivo de perda | Lista | Por que nao fechou (se aplicavel) |

**Logica de movimentacao:**
- Lead entra → automaticamente na coluna "Entrada"
- SDR qualifica → move para "Qualificado" ou "Descartado" (com motivo)
- Agendou → move para "Agendado" + data na agenda
- Reuniao feita → move para "Proposta Enviada"
- Fechou → move para "Cliente" + trigger de onboarding
- Nao fechou → move para "Follow-up" ou "Downsell" (conforme criterio)
- Perdido → move para "Reativacao" com data de retorno (30/60/90 dias)

**Visoes essenciais:**
1. Pipeline (visao Kanban por etapa)
2. Meus leads (filtro por responsavel)
3. Vencendo hoje (leads com proximo passo = hoje)
4. Leads frios (sem contato ha mais de 7 dias)
5. Reativacao (leads perdidos prontos pra retomar)

### Entrega da Etapa
Blueprint do CRM operacional com colunas, logica de movimentacao, visoes e regras de uso.

---

## Etapa 4: Criterios de Passagem entre Etapas

### Execucao
Definir criterios claros e objetivos pra um lead avancar de uma etapa pra outra. Sem criterio = lead avanca por intuicao = funil quebrado.

**Criterios por etapa:**

| Transicao | Criterios obrigatorios | Quem decide |
|-----------|----------------------|-------------|
| Entrada → Qualificacao | Lead respondeu + demonstrou interesse minimo | IA/SDR |
| Qualificacao → Agendamento | Tem perfil + tem dor + tem urgencia + tem orcamento (BANT adaptado) | SDR |
| Agendamento → Reuniao | Confirmou presenca + recebeu lembrete D-1 | SDR |
| Reuniao → Proposta | Participou da reuniao + confirmou interesse + pediu proposta | Closer |
| Proposta → Fechamento | Recebeu proposta + tirou duvidas + sinalizou decisao | Closer |
| Fechamento → Onboarding | Pagamento confirmado + contrato assinado | Closer |
| Onboarding → Follow-up | Completou checklist de boas-vindas + acessou o produto | Onboarding |
| Follow-up → Upsell | Cliente satisfeito + usando ativamente + resultado positivo | Gestor |
| Nao fechou → Downsell | Nao fechou por preco, mas tem interesse real | Closer |
| Perdido → Reativacao | 30+ dias sem contato + motivo de perda nao e desqualificacao | SDR/IA |
| Cliente → Renovacao | 30 dias antes do vencimento + cliente ativo | Gestor/IA |

**Criterio de desqualificacao (quando NAO avancar):**
- Sem orcamento E sem perspectiva de ter
- Nao tem a dor que o produto resolve
- Nao tem autoridade de decisao
- Nao responde apos 3 tentativas em 14 dias (move pra reativacao futura)

### Entrega da Etapa
Tabela completa de criterios de passagem + criterios de desqualificacao + regras de retorno.

---

## Etapa 5: Scripts-Base por Etapa (10 Scripts)

### Execucao
Criar 10 scripts operacionais — roteiros que qualquer pessoa do time pode usar. Nao sao textos rigidos, sao guias com estrutura + tom + pontos obrigatorios.

**Usar skill auxiliar:** `skill-oferta-irresistivel` para scripts de proposta e fechamento.

**Os 10 scripts:**

### Script 1: Primeiro Contato (SDR)
- Abertura pessoal + contexto de onde veio
- Pergunta de qualificacao inicial
- Transicao pra conversa (nao vender no primeiro contato)
- CTA: agendar proximo passo

### Script 2: Qualificacao Completa (SDR)
- Perguntas BANT adaptadas (Budget, Authority, Need, Timeline)
- Tecnica de escuta ativa
- Classificacao: quente / morno / frio
- Decisao: agendar reuniao ou nutrir

### Script 3: Agendamento de Reuniao (SDR)
- Proposta de horarios (maximo 3 opcoes)
- Confirmacao com lembrete automatico
- Pre-briefing: o que esperar da reuniao
- Reconfirmacao D-1

### Script 4: Condução de Reuniao Diagnostica (Closer)
- Abertura: rapport + expectativa
- Escuta: 70% escutar, 30% falar
- Diagnostico: identificar dor, urgencia, impacto financeiro
- Transicao: "com base no que voce me contou..."
- Apresentacao personalizada da solucao

### Script 5: Apresentacao de Proposta (Closer)
- Stack de valor (usar `skill-oferta-irresistivel`)
- Ancoragem de preco
- Bonus que quebram objecoes
- Garantia
- CTA com urgencia real

### Script 6: Tratamento de Objecoes (Closer)
- Top 10 objecoes mais comuns do negocio
- Resposta padrao pra cada uma
- Tecnica: concordar → recontextualizar → prova social → CTA
- Objecoes de preco, tempo, consultar alguem, "vou pensar"

### Script 7: Fechamento (Closer)
- Resumo da proposta
- Confirmacao verbal
- Instrucoes de pagamento/contrato
- Celebracao + proximo passo
- Transicao pro onboarding

### Script 8: Onboarding (D+1 a D+14)
- Mensagem de boas-vindas (D+0)
- Checklist de acesso (D+1)
- Check-in de progresso (D+3)
- Verificacao de satisfacao (D+7)
- Abertura pra duvidas (D+14)

### Script 9: Follow-up Pos-Venda (D+15 a D+90)
- Check-in de resultado (D+15)
- Pedido de depoimento (D+30)
- Oferta de indicacao (D+45)
- Preparacao pra upsell (D+60)
- Preparacao pra renovacao (D+75-90)

### Script 10: Downsell (Lead que nao fechou)
- Retomada da conversa (sem pressao)
- Reconhecimento da objecao
- Apresentacao da oferta alternativa (menor ticket, menor escopo)
- CTA com prazo
- Encerramento elegante se nao aceitar

### Entrega da Etapa
10 scripts completos, prontos pra uso, com tom adequado ao negocio, personalizaveis por nicho.

**Pausa de validacao:** "Vou te mostrar o funil completo e os 10 scripts. Quero que voce valide: o tom ta certo? As objecoes sao essas mesmas? O fluxo faz sentido pro seu mercado?"

---

## Etapa 6: SLAs e Tempos de Resposta

### Execucao
Definir tempos maximos de resposta e atuacao por etapa. SLA (Service Level Agreement) e o que separa amadorismo de maquina comercial.

**SLAs por etapa:**

| Etapa | SLA (tempo maximo) | Consequencia se estourar |
|-------|-------------------|--------------------------|
| Lead novo → primeiro contato | **5 minutos** (IA) / **30 minutos** (humano) | Lead esfria, taxa de conversao cai 80% |
| Qualificacao completa | **24 horas** apos primeiro contato | Lead perde interesse, vai pro concorrente |
| Agendamento → reuniao | **48 horas** (maximo 72h) | Lead esquece, no-show aumenta |
| Envio de proposta | **2 horas** apos reuniao | Perde o calor da conversa |
| Follow-up apos proposta | **24 horas** (D+1) | Lead "esfria" e objecoes crescem |
| Resposta a duvida do cliente | **1 hora** (horario comercial) | Insatisfacao, churn |
| Reativacao de lead perdido | **30 dias** apos perda | Lead vira irrelevante apos 90 dias |
| Onboarding completo | **7 dias** apos pagamento | Cliente nao percebe valor, pede reembolso |
| Check-in pos-venda | **D+7, D+15, D+30** | Perde chance de upsell e indicacao |

**Metricas de SLA:**
- % de leads respondidos dentro do SLA
- Tempo medio de resposta por etapa
- % de SLA estourado por responsavel
- Impacto financeiro do SLA estourado (leads perdidos x ticket)

### Entrega da Etapa
Tabela de SLAs por etapa + metricas de acompanhamento + alertas automaticos sugeridos.

---

## Etapa 7: Rotina de Acompanhamento

### Execucao
Definir a rotina diaria, semanal e mensal que mantem a maquina comercial funcionando.

**Rotina diaria (15 minutos):**
- Revisar pipeline: quais leads vencem hoje?
- Verificar SLAs: algum lead estourou o tempo?
- Priorizar: quais leads estao mais quentes?
- Executar: primeiras 3 acoes do dia no comercial

**Rotina semanal (30 minutos — reuniao comercial):**
- Revisar numeros da semana (leads, qualificados, agendados, fechados)
- Analisar taxas de conversao por etapa
- Identificar gargalos (onde os leads estao travando?)
- Ouvir 2-3 conversas do time (qualidade)
- Definir prioridades da proxima semana
- Celebrar fechamentos

**Rotina mensal (60 minutos — revisao estrategica):**
- Comparar resultado vs meta
- Analisar funil completo (volume + taxas)
- Identificar os 3 maiores gargalos do mes
- Revisar scripts (estao funcionando?)
- Ajustar SLAs se necessario
- Planejar campanhas do proximo mes
- Atualizar projecao de faturamento

**Dashboard de acompanhamento (metricas visiveis):**

| Metrica | Frequencia | Meta | Onde acompanhar |
|---------|-----------|------|-----------------|
| Leads novos | Diaria | [N]/dia | CRM |
| Taxa de resposta | Diaria | >90% em 30min | CRM |
| Reunioes agendadas | Semanal | [N]/semana | Agenda + CRM |
| Taxa de comparecimento | Semanal | >70% | CRM |
| Propostas enviadas | Semanal | [N]/semana | CRM |
| Taxa de fechamento | Semanal | >20% | CRM |
| Ticket medio | Mensal | R$ [X] | CRM |
| Faturamento | Mensal | R$ [X] | Financeiro |
| SLA cumprido | Semanal | >85% | CRM |
| Leads no pipeline | Diaria | [N] | CRM |

### Entrega da Etapa
Rotina completa (diaria + semanal + mensal) + dashboard de metricas + template de reuniao comercial.

---

## Conclusao da Fase 3

> Resumir: "Agora voce tem uma maquina comercial completa: funil desenhado de ponta a ponta, papeis definidos, CRM operacional, 10 scripts prontos, SLAs claros e rotina de acompanhamento. Voce saiu do improviso e entrou no processo. O proximo passo e delegar isso de forma estruturada — pra que a maquina funcione sem depender de voce."

**Salvar output em:** `outputs/03-maquina-comercial.md`

Conteudo do output:
- Funil completo (12 etapas) com fluxo visual
- Matriz de responsabilidades (papeis x etapas)
- Blueprint do CRM operacional (colunas, movimentacoes, visoes)
- Criterios de passagem entre etapas
- 10 scripts-base completos
- Tabela de SLAs por etapa
- Rotina de acompanhamento (diaria + semanal + mensal)
- Playbook comercial v1

Transicao automatica para a proxima fase.
