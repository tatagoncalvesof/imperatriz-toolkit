# Processo de Decisao — Sucessao Formal

Sucessao Imperatriz nao e cargo, nao e promocao, nao e concessao. E **acordo bilateral cerimonial** entre Tata + Conselho da Soberana e a Imperatriz Plena. O processo formal abaixo e obrigatorio — pular passos invalida a sucessao.

---

## Visao geral — 7 passos

```
1. ELEGIBILIDADE       → 12+ meses Imperatriz Plena ativa (skill --avaliar)
2. CONVITE             → Conselho da Soberana convoca conversa
3. AVALIACAO 3 CAMINHOS → mentorada + Conselho discutem fit (skill --cenarios)
4. NEGOCIACAO          → juridico + financeiro
5. ACORDO FORMAL       → contrato assinado (skill --escolher)
6. COMUNICACAO PUBLICA → manifesto + sub-brand + posts
7. ASSUNCAO            → mentorada assume responsabilidades + auditoria periodica
```

Tempo medio total: **45-90 dias** entre convite (passo 2) e assuncao (passo 7).

---

## PASSO 1 — ELEGIBILIDADE

**Quem dispara:** Conselho da Soberana (revisao trimestral) OU mentorada via auto-candidatura.

**O que acontece:**
- Roda `sucessao-imperatriz --avaliar [nome]`
- Skill le `dossie-mentorada` + `gates-imperatriz` + `compliance-imperatriz`
- Checa 6 pre-requisitos duros:
  1. 12+ meses CONSECUTIVOS Imperatriz Plena ativa
  2. Pilar 1 (Fluxo) saturado nos ultimos 90 dias
  3. Faturamento estavel/crescente nos ultimos 6 meses
  4. Compliance zerada (juridico, fiscal, etica)
  5. NPS interno >= 8
  6. Tata + Conselho com agenda

**Saidas possiveis:**
- **ELEGIVEL (6/6)** → vai pro passo 2
- **QUASE-ELEGIVEL (4-5/6)** → checklist remediacao + reavaliacao em 90 dias
- **NAO ELEGIVEL (<= 3/6)** → permanece na Travessia, reavaliacao em 180 dias

**Documento gerado:** Laudo de Elegibilidade (1 pagina, fica no dossie da mentorada).

**Prazo:** 1-3 dias.

---

## PASSO 2 — CONVITE

**Quem dispara:** Tata + Conselho da Soberana.

**O que acontece:**
- Conselho envia **Carta Convite Sucessao** (formato fechado, Selo Travessia em alto-relevo digital)
- Carta contem:
  - Reconhecimento dos 12+ meses ativos
  - Convite formal pra "Conversa de Sucessao" (data marcada)
  - Materiais pra estudar antes (este arquivo + `OS-3-CAMINHOS.md`)
  - Pergunta de pre-call: "Voce ja pensou em qual dos 3 caminhos faz sentido pra voce?"
  - Confidencialidade — Imperatriz nao comunica publicamente ate passo 6

**Resposta esperada:** mentorada confirma em ate 7 dias. Se recusar, fica na Travessia normalmente (sem prejuizo).

**Documento gerado:** Carta Convite + Acordo de Confidencialidade Pre-Sucessao (NDA leve).

**Prazo:** 7-14 dias entre envio e Conversa de Sucessao.

---

## PASSO 3 — AVALIACAO DOS 3 CAMINHOS

**Quem dispara:** Mentorada + Conselho juntos, em call de 90 minutos (Conversa de Sucessao).

**O que acontece:**
- Roda `sucessao-imperatriz --cenarios [nome]` antes da call
- Skill gera ranking dos 3 caminhos com fit % + projecao financeira + riscos
- Na call:
  - Conselho apresenta diagnostico
  - Mentorada compartilha intuicao dela
  - Discutem cada caminho (15-20 min cada)
  - **Nao se decide nessa call** — propositalmente
- Pos-call, mentorada tem 14-21 dias pra decidir
- Pode pedir 1 call extra com a Tata (somente Tata) pra duvidas finais
- Decisao: enviada por escrito ao Conselho

**Saida:** Mentorada escolhe 1 caminho (Socia / Treinadora-Mor / White Label) OU pede mais 90 dias na Travessia pra amadurecer decisao.

**Documento gerado:**
- Ata da Conversa de Sucessao
- Carta de Decisao (mentorada → Conselho)

**Prazo:** 14-21 dias entre Conversa e Decisao.

---

## PASSO 4 — NEGOCIACAO

**Quem dispara:** Conselho (apos receber Carta de Decisao).

**O que acontece:**
- Conselho contrata juridico (escritorio fixo Travessia OU advogado externo conforme caso)
- Skill gera **brief juridico** via `sucessao-imperatriz --escolher [nome] [caminho]`
- Brief tem:
  - Tipo de contrato (LTDA com vesting / Licenca Selo / Licenca Selo White Label)
  - Clausulas-chave pre-acordadas
  - % / royalty / pro-labore / vesting
  - Conditions precedentes (ex: declaracao de saida da operacao propria, NDAs, registro de marca)
- Mentorada tambem pode trazer advogado proprio (recomendado)
- 3-5 rodadas de negociacao tipicas
- **Linhas vermelhas Tata** (nao negociaveis):
  - Compliance e padrao de qualidade auditavel
  - Confidencialidade perpetua sobre metodologia interna
  - Direito de auditoria do Conselho
  - Clausula de termino por violacao etica
- **Linhas verdes** (negociaveis):
  - %/royalty exato dentro da faixa
  - Vigencia (dentro dos limites: 24/36/48 meses)
  - Distribuicao de carga horaria
  - Bonus de performance
  - Clausulas de bonus pra primeira janela

**Documento gerado:**
- Minuta do contrato (versao 1)
- Anexos: rubrica de qualidade, plano de negocio inicial, cronograma de marcos

**Prazo:** 21-45 dias.

---

## PASSO 5 — ACORDO FORMAL

**Quem dispara:** Conselho + Mentorada apos minuta final aceita.

**O que acontece:**
- **Cerimonia de Assinatura** (presencial OU video chamada solene)
- Presentes: Tata + 2 membros do Conselho + Mentorada + advogados
- Leitura do **Manifesto Interno de Sucessao** (1 pagina, escrito pela mentorada com apoio da skill)
- Assinatura digital + fisica em cartorio
- Selo Travessia entregue (digital + fisico — placa, broche, livro de prata)

**Documento gerado:**
- Contrato assinado (juridico)
- Manifesto Interno (interno, vai pro arquivo da Tribo)
- Foto cerimonial (uso interno e, em passo 6, posts publicos com aprovacao)

**Prazo:** 1 dia (a cerimonia em si).

---

## PASSO 6 — COMUNICACAO PUBLICA

**Quem dispara:** Mentorada com supervisao Tata.

**O que acontece:**
- Roda `sucessao-imperatriz --planejar [nome] [caminho]` pra plano completo
- Roda `marca-sistemica-imperatriz` pra sub-brand (caminhos 2 e 3)
- Roda `bestseller-book` pra autobiografia (opcional, recomendado pra Imperatrizes com cabedal)
- Roda `calendario-imperatriz` pra sequencia de comunicacao
- Producao:
  - **Manifesto publico** (post longo + carrossel) — texto + visual gerados em parceria
  - **Sequencia de 5-7 posts** pos-anuncio (D+0, D+1, D+3, D+7, D+14, D+30, D+60)
  - **Entrevista publica com a Tata** (live, podcast ou video) — D+7
  - **Sub-handles sociais** (caminhos 2 e 3) — Instagram + LinkedIn + site
  - **Pagina dedicada no site da Travessia** linkando o caminho dela
- **Aprovacao final pela Tata** antes de publicar (linha vermelha)

**Documento gerado:**
- Pacote de comunicacao (15-25 entregaveis)
- Plano editorial 90 dias pos-anuncio
- Sub-brand kit completo (logo, paleta, tipografia, identidade visual)
- Manuscrito do livro (se opcao escolhida) ou roadmap editorial

**Prazo:** 30-60 dias entre cerimonia (passo 5) e anuncio publico.

---

## PASSO 7 — ASSUNCAO + AUDITORIA

**Quem dispara:** Mentorada (a partir do dia D do anuncio publico).

**O que acontece:**
- Mentorada assume responsabilidades formais do caminho
- **Onboarding 30 dias** com time da Tata (varia por caminho):
  - Socia: integracao com C-level + acesso a sistemas
  - Treinadora-Mor: handoff de mentoradas + materiais da Camara + protocolos
  - White Label: kit de marca Selo + acesso a stack + framework de reporting
- **Pontos de auditoria do Conselho:**
  - **D+30** — check-in operacional (esta executando?)
  - **D+90** — review primeiros resultados (3 meses)
  - **D+180** — review semestral (vai bem?)
  - **D+365** — review anual (renovacao automatica ou ajuste de contrato?)
- Cada review gera **Ata de Auditoria** + plano de ajuste se necessario

**Linhas vermelhas pos-assuncao:**
- Royalty atrasado > 60 dias = perda de Selo (caminhos 2 e 3)
- NPS < 7 sustentado 6 meses = revisao obrigatoria
- Violacao de codigo de etica = termino imediato
- Conflito nao declarado = termino com bad leaver

**Documento gerado:**
- Atas D+30 / D+90 / D+180 / D+365
- Relatorios de performance
- Renovacao ou ajuste contratual (passo 4 reversivel se necessario)

**Prazo:** 365 dias do primeiro ciclo, depois renovacao em ciclos de 24-48 meses (varia por caminho).

---

## Reversibilidade — e se nao der certo?

A sucessao TEM mecanismos de saida. Nenhum caminho e prisao.

### Saida da Imperatriz (good leaver)
- Notificacao formal 90 dias antes
- Mantem % vested ate a data de saida (caminho 1)
- Recebe royalty residual de 12-18 meses (caminhos 2 e 3)
- Pode voltar pra Travessia como Imperatriz Plena (sem regressao de status)
- Mantem confidencialidade perpetua

### Saida pelo Conselho (bad leaver)
- Termino imediato em caso de:
  - Violacao etica
  - Compliance perdida (juridico/fiscal)
  - NPS < 7 sustentado > 6 meses sem plano de acao
  - Royalty atrasado > 90 dias
- Perde % nao vested
- Sem royalty residual
- Nao-concorrencia ativada
- Pode ou nao voltar pra Travessia (decisao caso a caso)

### Saida pelo Tata (mudanca estrategica)
- Tata pode descontinuar braco (caminho 1) ou Selo (caminhos 2 e 3) com 180 dias notificacao
- Imperatriz recebe % vested integral + indenizacao proporcional
- Royalty residual de 24 meses
- Goodwill: Tata facilita transicao (apresenta concorrentes, ajuda a reposicionar)

---

## Casos especiais

### "Quero combinar 2 caminhos"
Excecao rara. Pleito direto a Tata + Conselho. So aprovado se:
- Imperatriz tem energia + recursos pra ambos
- Caminhos nao geram conflito (ex: Treinadora-Mor da Camara X + White Label de nicho NAO sobreposto a Camara X)
- Royalty/dedicacao sao recalculados manualmente

### "Quero pular o pre-requisito de 12 meses"
Nao e oferecido. Justificativa: 12 meses e o tempo minimo de saturacao + maturacao. Pular = ineficiencia comprovada (cases historicos).

### "Quero virar Sucessora mas nao quero anuncio publico"
So permitido no Caminho 1 (Socia) com clausula de cargo nao-publico. Caminhos 2 e 3 exigem anuncio porque dependem de marca publica pra funcionar.

### "Posso ser Sucessora e continuar minha mentoria atual?"
- Caminho 1: nao (precisa sair ou reduzir muito)
- Caminho 2: sim, mas mentoria propria nao pode competir com Camara
- Caminho 3: sua mentoria atual VIRA o White Label (com renomeacao)

---

## Indicadores de saude do programa de sucessao

A Tata + Conselho monitoram trimestralmente:

| Indicador | Meta | Acao se desvia |
|---|---|---|
| Taxa de elegibilidade (Imperatrizes Plenas que se tornam elegiveis) | 30-50%/ano | Se < 20%, revisar criterios |
| Taxa de aceitacao do convite | 70%+ | Se < 50%, repensar atratividade |
| Taxa de conclusao do processo (passo 1 → 7) | 80%+ | Se < 60%, revisar atrito |
| Renovacao em D+365 | 85%+ | Se < 70%, revisar fit do caminho |
| NPS Sucessoras | >= 9 | Se < 8, intervencao Tata direta |
| % das Sucessoras que viram referencia publica | 60%+ em 24 meses | Se < 40%, reforcar passo 6 |

---

**Metodo Imperatriz de Sucessao — propriedade intelectual Tata Goncalves.**
