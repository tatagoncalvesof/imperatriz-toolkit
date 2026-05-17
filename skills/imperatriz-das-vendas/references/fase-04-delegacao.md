# Fase 4: Delegacao Estruturada (Delegar sem Perder Controle)

## Proposito
Criar a estrutura que permite ao empresario delegar o comercial sem perder controle, qualidade ou previsibilidade. Definir funcoes claras (SDR, closer, gestor, onboarding, IA), estabelecer criterios de qualidade, montar arquitetura de comissao e metas, e mapear onde a IA acelera vs onde o humano e insubstituivel. O objetivo e que o dono saia do operacional e entre na gestao estrategica.

**Principio:** Delegar sem estrutura e abandonar. Delegar COM estrutura e escalar.

---

## Etapa 1: Separacao de Funcoes (SDR / Closer / Gestor / Onboarding / IA)

### Execucao
Separar as funcoes comerciais de forma clara — mesmo que hoje uma pessoa faca tudo. A separacao e o primeiro passo pra escalar.

**As 5 funcoes do comercial estruturado:**

| Funcao | Missao | Perfil ideal | KPIs principais |
|--------|--------|-------------|-----------------|
| **SDR** | Qualificar leads e agendar reunioes | Comunicativo, organizado, resiliente, follow-up incansavel | Leads qualificados/dia, reunioes agendadas, taxa de qualificacao |
| **Closer** | Fechar vendas e negociar | Persuasivo, empático, bom ouvinte, domina objecoes | Taxa de fechamento, ticket medio, receita gerada |
| **Gestor Comercial** | Acompanhar metricas, treinar, garantir qualidade | Analitico, lider, orientado a dados | Receita total, taxa geral do funil, SLA cumprido |
| **Onboarding** | Integrar o cliente, garantir primeira experiencia | Acolhedor, detalhista, proativo | NPS D+7, taxa de ativacao, churn D+30 |
| **IA/Automacao** | Resposta inicial, triagem, follow-up, cadencia | Configurada, treinada, monitorada | Tempo de resposta, taxa de triagem, leads encaminhados |

**Mapeamento da situacao atual:**

| Funcao | Quem faz HOJE | Ideal | Gap |
|--------|---------------|-------|-----|
| SDR | [nome/dono/ninguem] | Pessoa dedicada ou IA | [descricao] |
| Closer | [nome/dono] | Pessoa dedicada | [descricao] |
| Gestor | [nome/dono/ninguem] | Dono ou gestor dedicado | [descricao] |
| Onboarding | [nome/ninguem] | Pessoa dedicada ou IA | [descricao] |
| IA | [nao existe] | Lara/bot configurado | [descricao] |

**Perguntas:**
- "Quem faz cada uma dessas funcoes hoje no seu negocio?"
- "Onde voce, como dono, esta mais preso no operacional?"
- "Se voce tirasse ferias por 30 dias, o que pararia?"
- "O que voce QUER continuar fazendo vs o que voce PRECISA delegar?"

### Entrega da Etapa
Organograma comercial com funcoes separadas + mapeamento atual vs ideal + plano de transicao.

---

## Etapa 2: Estruturacao da Funcao SDR

### Execucao
Detalhar tudo que o SDR faz, como faz, com que ferramentas, em que ordem e com que qualidade.

**Fluxo completo do SDR:**

```
Lista de leads → Primeiro contato (< 5 min) → Historico no CRM →
Qualificacao (BANT) → Encaminhamento pro closer (se qualificado) →
Nutricao (se morno) → Descarte com motivo (se frio)
```

**Rotina diaria do SDR:**

| Horario | Atividade | Ferramenta |
|---------|-----------|------------|
| 08:00-08:15 | Revisar pipeline + leads novos | CRM |
| 08:15-10:00 | Primeiro contato com leads novos | WhatsApp + CRM |
| 10:00-11:00 | Follow-up leads em andamento | WhatsApp + CRM |
| 11:00-12:00 | Qualificacao completa + agendamento | Script + Agenda |
| 14:00-15:00 | Retorno leads mornos + nurture | WhatsApp |
| 15:00-16:00 | Reativacao base fria (campanhas) | CRM + Script |
| 16:00-16:30 | Atualizar CRM + reportar numeros | CRM |

**Script de qualificacao (BANT adaptado):**
1. **Budget (Orcamento):** "Voce ja tem uma ideia de quanto esta disposta a investir pra resolver [dor]?"
2. **Authority (Autoridade):** "Voce decide sozinha ou precisa consultar alguem?"
3. **Need (Necessidade):** "Me conta: qual o maior problema que voce quer resolver AGORA?"
4. **Timeline (Urgencia):** "Se a gente resolver isso, pra quando voce precisa?"

**Criterios de lead qualificado (MQL → SQL):**
- Tem a dor que o produto resolve (Need = sim)
- Tem orcamento compativel (Budget = sim ou proximo)
- Tem autoridade de decisao (Authority = sim)
- Tem urgencia (Timeline = proximo 30 dias)
- Respondeu positivamente a pelo menos 3 dos 4 criterios

**Regras de encaminhamento:**
- 4/4 criterios = encaminha pro closer IMEDIATAMENTE
- 3/4 criterios = encaminha pro closer com observacao
- 2/4 criterios = nurture por 7 dias + requalificacao
- 1/4 ou 0/4 = descarte com motivo no CRM

### Entrega da Etapa
Job description SDR completa + rotina diaria + script de qualificacao + criterios de encaminhamento + metricas de desempenho.

---

## Etapa 3: Estruturacao da Funcao Closer

### Execucao
Detalhar o fluxo completo do closer — da reuniao ao fechamento.

**Fluxo completo do Closer:**

```
Lead qualificado chega (do SDR) → Revisar historico no CRM →
Reuniao diagnostica (escuta 70%) → Personalizacao da solucao →
Apresentacao do stack de valor → Quebra de objecoes →
Fechamento + contrato → Handoff pro onboarding
```

**As 6 etapas da reuniao de fechamento:**

### 1. Rapport + Contexto (5 min)
- Criar conexao humana
- Retomar o que o SDR ja levantou
- "O [SDR] me contou sobre [situacao]. Quero entender melhor direto de voce."

### 2. Escuta Diagnostica (15-20 min)
- 70% escutar, 30% falar
- Perguntas de aprofundamento: "Me conta mais sobre isso..."
- Identificar dor principal, dor secundaria, impacto financeiro
- Repetir o que ouviu: "Entao, se eu entendi, o que mais te incomoda e..."

### 3. Personalizacao da Solucao (5-10 min)
- Conectar dor com solucao
- "Com base no que voce me contou, o que vai resolver isso e..."
- Adaptar a apresentacao ao que o lead disse (nao pitch generico)

### 4. Stack de Valor (5-10 min)
- Apresentar oferta usando stack de valor
- Ancoragem: mostrar o valor real vs investimento
- Bonus estrategicos que quebram objecoes especificas
- Garantia que remove risco

### 5. Tratamento de Objecoes (5-10 min)
- Tecnica: CONCORDAR → RECONTEXTUALIZAR → PROVA SOCIAL → CTA
- "Entendo perfeitamente. Inclusive, a [nome] pensava exatamente assim e hoje..."
- Top 5 objecoes mapeadas com respostas prontas

### 6. Fechamento + Proximo Passo (5 min)
- Resumo da proposta
- "Faz sentido pra voce?"
- Instrucoes claras de pagamento/contrato
- Handoff pro onboarding: "Agora vou te passar pro [nome/equipe] que vai cuidar da sua integracao."

**Metricas do Closer:**

| Metrica | Meta | Como medir |
|---------|------|-----------|
| Taxa de fechamento | >25% | Fechados / reunioes realizadas |
| Ticket medio | R$ [X] | Media de valor dos contratos |
| Ciclo de venda | [N] dias | Tempo medio da reuniao ao fechamento |
| No-show | <20% | Reunioes marcadas vs realizadas |
| Receita gerada/mes | R$ [X] | Soma dos contratos fechados |

### Entrega da Etapa
Job description Closer completa + roteiro de reuniao (6 etapas) + tratamento de objecoes + metricas de desempenho.

---

## Etapa 4: Papel do Gestor Comercial

### Execucao
Definir o que o gestor faz para manter a maquina funcionando — metricas, gargalos, qualidade e treinamento.

**As 4 responsabilidades do gestor:**

### 1. Acompanhar Metricas
- Dashboard diario: leads novos, respondidos, qualificados, agendados, fechados
- Dashboard semanal: taxas de conversao por etapa, SLA cumprido, receita
- Dashboard mensal: resultado vs meta, tendencia, projecao

### 2. Identificar Gargalos
- Onde os leads estao travando no funil?
- Qual etapa tem a menor taxa de conversao?
- Qual pessoa do time esta abaixo da meta?
- Qual campanha esta trazendo lead ruim?

### 3. Garantir Qualidade
- Ouvir 3-5 conversas por semana (SDR + closer)
- Avaliar: tom, script, qualificacao, objecoes, fechamento
- Dar feedback especifico e construtivo
- Scorecard por conversa (nota de 0-10 em 5 criterios)

**Scorecard de qualidade:**

| Criterio | 0-2 | 3-5 | 6-8 | 9-10 |
|----------|-----|-----|-----|------|
| Rapport/Conexao | Frio, robotico | Educado mas generico | Pessoal, caloroso | Excelente conexao |
| Escuta ativa | Nao escuta, interrompe | Escuta superficial | Escuta bem, faz perguntas | Escuta profunda, repete |
| Qualificacao | Nao qualifica | Qualifica parcialmente | BANT completo | BANT + dor + urgencia |
| Objecoes | Ignora ou perde | Responde fraco | Responde bem | Transforma em venda |
| Fechamento | Nao tenta | Tenta fraco | Tenta com tecnica | Fecha naturalmente |

### 4. Treinar o Time
- Roleplay semanal (simular situacoes reais)
- Revisao de scripts (o que funcionou, o que nao)
- Treinamento em produto (time precisa conhecer profundamente)
- Benchmark: compartilhar melhores praticas do time

**Rotina do gestor:**

| Frequencia | Atividade | Duracao |
|-----------|-----------|---------|
| Diaria | Revisar dashboard + SLAs | 15 min |
| Diaria | Check-in rapido com time | 10 min |
| Semanal | Reuniao comercial | 30 min |
| Semanal | Ouvir conversas + feedback | 45 min |
| Semanal | Roleplay/treinamento | 30 min |
| Mensal | Revisao estrategica | 60 min |
| Mensal | 1:1 com cada membro | 30 min cada |

### Entrega da Etapa
Job description Gestor completa + scorecard de qualidade + rotina de gestao + dashboard de metricas.

---

## Etapa 5: Mapeamento IA vs Humano

### Execucao
Mapear com precisao onde a IA acelera o processo e onde o humano e insubstituivel. Evitar dois erros fatais: (1) automatizar tudo e perder humanizacao, (2) fazer tudo manual e nao escalar.

**Usar skill auxiliar:** `lara-builder` para especificar a vendedora IA.

**Matriz completa IA vs Humano:**

| Etapa do Funil | IA pode fazer? | Humano essencial? | Recomendacao | Justificativa |
|----------------|---------------|-------------------|-------------|---------------|
| Primeiro contato (< 5 min) | **SIM** | Nao | **IA** | Velocidade e critica — IA responde em segundos |
| Triagem inicial | **SIM** | Nao | **IA** | Perguntas padronizadas, classificacao automatica |
| Qualificacao BANT | **PARCIAL** | Sim | **IA inicia + Humano valida** | IA coleta dados, humano interpreta nuances |
| Agendamento | **SIM** | Nao | **IA** | Logica de agenda, confirmacao, lembrete |
| Reuniao diagnostica | Nao | **SIM** | **HUMANO** | Escuta ativa, empatia, leitura corporal |
| Apresentacao de proposta | Nao | **SIM** | **HUMANO** | Personalizacao profunda, conexao emocional |
| Tratamento de objecoes | **PARCIAL** | Sim | **HUMANO (IA apoia)** | Humano negocia, IA sugere respostas |
| Fechamento | Nao | **SIM** | **HUMANO** | Momento de confianca, decisao emocional |
| Onboarding D+0-D+3 | **SIM** | Parcial | **IA + Humano supervisiona** | IA envia boas-vindas, checklist, acesso |
| Follow-up D+7 a D+90 | **SIM** | Parcial | **IA executa + Humano estrategico** | IA cadencia, humano intervem quando necessario |
| Downsell | **PARCIAL** | Sim | **IA inicia + Humano fecha** | IA retoma contato, humano adapta oferta |
| Reativacao | **SIM** | Parcial | **IA** | Volume alto, mensagem padronizada, humano so se responder |
| Upsell | Nao | **SIM** | **HUMANO** | Requer conhecimento profundo do cliente |
| Renovacao (lembrete) | **SIM** | Nao | **IA** | Cadencia automatica, humano so se problema |
| Pedido de depoimento | **SIM** | Nao | **IA** | Mensagem padronizada, momento automatizado |
| Pedido de indicacao | **PARCIAL** | Sim | **IA inicia + Humano acompanha** | IA dispara, humano converte a indicacao |

**Resumo da divisao:**

| Categoria | IA | Humano | Hibrido |
|-----------|-----|--------|---------|
| Velocidade (resposta < 5 min) | X | — | — |
| Volume (reativacao, follow-up) | X | — | — |
| Empatia (reuniao, objecoes) | — | X | — |
| Decisao (fechamento, upsell) | — | X | — |
| Cadencia (nurture, renovacao) | X | — | — |
| Qualificacao | — | — | X |
| Onboarding | — | — | X |

**Regra de ouro:** IA faz o que exige VELOCIDADE e VOLUME. Humano faz o que exige EMPATIA e DECISAO. Hibrido quando IA inicia e humano finaliza.

**Usar skill auxiliar:** `imperatriz-multiagentes` para arquitetar a estrutura multi-agente se o negocio comportar.

### Entrega da Etapa
Matriz completa IA vs Humano (16 etapas) + regras de handoff IA→Humano + spec da vendedora IA + recomendacao de implementacao.

---

## Etapa 6: Regras de Qualidade SDR-Closer

### Execucao
Definir criterios claros de qualidade na passagem SDR→Closer para evitar o maior problema de times comerciais: closer recebe lead ruim e perde tempo, SDR agenda reuniao so pra bater meta.

**Criterios obrigatorios para passagem SDR→Closer:**

| Criterio | Obrigatorio | Como verificar |
|----------|------------|----------------|
| Lead respondeu e demonstrou interesse | Sim | Historico de conversa no CRM |
| BANT preenchido (minimo 3/4) | Sim | Campos no CRM |
| Dor principal identificada | Sim | Anotacao no CRM |
| Urgencia confirmada (proximo 30 dias) | Sim | Resposta do lead |
| Horario de reuniao confirmado | Sim | Agenda + confirmacao |
| Briefing escrito pro closer | Sim | Campo de observacoes no CRM |

**Consequencias de passagem ruim:**
- Closer rejeita lead → volta pro SDR com motivo
- 3 rejeicoes consecutivas → treinamento obrigatorio
- Taxa de rejeicao > 20% → alerta pro gestor
- **Comissao vinculada a qualidade:** SDR so ganha comissao se lead qualificado que passou FECHOU (ou pelo menos compareceu a reuniao)

**Metricas de qualidade cruzada:**

| Metrica | Meta | O que significa |
|---------|------|----------------|
| Taxa de rejeicao (closer rejeita lead do SDR) | <15% | SDR ta qualificando bem |
| Taxa de comparecimento (reuniao marcada vs realizada) | >70% | SDR ta confirmando direito |
| Taxa de fechamento (dos leads que o SDR passou) | >20% | Qualidade do lead esta boa |
| Tempo de passagem (SDR qualifica → closer recebe) | <2h | Velocidade da operacao |

**Comissao vinculada a qualidade (modelo sugerido):**
- SDR ganha comissao base por lead qualificado que compareceu a reuniao
- SDR ganha bonus adicional se o lead fechou
- Closer ganha comissao por fechamento
- Closer ganha bonus por ticket acima da media
- **Ambos perdem bonus se SLA estourar**

### Entrega da Etapa
Regras de qualidade SDR→Closer + metricas cruzadas + modelo de comissao vinculada + consequencias.

**Pausa de validacao:** "Vou te mostrar o plano de comissao, metas e carreira do time. Antes de seguir, valida comigo: essas regras de qualidade fazem sentido pro seu time? A comissao vinculada funciona pro seu modelo?"

---

## Etapa 7: Arquitetura de Comissao + Metas + Carreira

### Execucao
Construir o sistema completo de remuneracao variavel, metas progressivas e plano de carreira que atrai, retém e desenvolve o time comercial.

**Delegar para agente especialista:** `flavio` (pilares 2, 3 e 4 — Comissao, Metas e Carreira).

**O que o agente Flavio entrega:**

### Pilar 2 — Motor de Comissao (via `flavio`)
- Estrutura de comissao por funcao (SDR, closer, gestor)
- Gatilhos de pagamento (quando a comissao e liberada)
- Aceleradores (comissao aumenta conforme performance)
- Desaceleradores (comissao reduz se qualidade cai)
- Calculo automatico de comissao
- Split de comissao (quando SDR + closer dividem)
- Exemplos numericos com cenarios (pessimista, realista, otimista)

### Pilar 3 — Sistema de Metas (via `flavio`)
- Metas individuais por funcao
- Metas do time (coletivas)
- Progressao: meta base → meta agressiva → meta stretch
- Frequencia: diaria, semanal, mensal
- Dashboard de acompanhamento
- Consequencias de nao bater meta (coaching, nao punicao)
- Celebracao de metas batidas

### Pilar 4 — Plano de Carreira (via `flavio`)
- Niveis dentro de cada funcao (Junior → Pleno → Senior → Lider)
- Criterios claros de promocao (baseados em metricas, nao tempo)
- Aumento de remuneracao por nivel
- Caminho de carreira: SDR → Closer → Gestor → Diretor Comercial
- Tempo medio em cada nivel
- O que precisa entregar pra subir

**Regras do jogo (documento formal):**
1. Como a comissao e calculada
2. Quando e paga (data, frequencia)
3. O que gera comissao e o que nao gera
4. Criterios de qualidade que afetam comissao
5. Como as metas sao definidas e revisadas
6. Como funciona a progressao de carreira
7. O que acontece se nao bater meta 3 meses seguidos
8. Como sair do time (processo justo e transparente)

### Entrega da Etapa
Plano completo de comissao (por funcao) + sistema de metas (individual + coletivo) + plano de carreira (niveis + criterios) + documento "Regras do Jogo".

---

## Conclusao da Fase 4

> Resumir: "Agora voce tem a delegacao estruturada: funcoes separadas, job descriptions claras, matriz IA vs humano definida, regras de qualidade entre SDR e closer, plano de comissao que incentiva performance E qualidade, sistema de metas progressivo e plano de carreira. Voce saiu do 'eu faço tudo' pro 'eu gerencio a maquina'. O proximo passo e treinar e capacitar esse time pra operar com excelencia."

**Salvar output em:** `outputs/04-delegacao-estruturada.md`

Conteudo do output:
- Organograma comercial com 5 funcoes
- Job description SDR (rotina + script + criterios)
- Job description Closer (roteiro reuniao + objecoes + metricas)
- Job description Gestor (scorecard + rotina + dashboard)
- Matriz completa IA vs Humano (16 etapas)
- Spec da vendedora IA (pra construir com lara-builder)
- Regras de qualidade SDR→Closer
- Plano de comissao por funcao
- Sistema de metas (individual + coletivo)
- Plano de carreira (niveis + criterios)
- Documento "Regras do Jogo"

Transicao automatica para a proxima fase.
