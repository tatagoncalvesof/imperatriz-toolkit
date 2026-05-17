# Exemplos de Casos — 3 Simulacoes Resolvidas

Casos reais (anonimizados) para mentorada estudar como o playbook se aplica em situacao concreta. Mostrar tempo real, decisoes reais, custo real.

---

## CASO 1 — BAN META R$ 50K/MES

**Mentorada:** Marina (nome ficticio), mentora high-ticket, ticket medio R$ 8.000, faturamento R$ 200k/mes, 80% via Meta Ads. Imperio com 3 anos de operacao.

**Crise:** quarta-feira, 14h32. Abre BM e ve banner vermelho. Conta de anuncios principal desativada. Email recebido as 14:15: "Sua conta de anuncios foi desativada por violacao das nossas politicas de publicidade." Sem detalhamento.

### Linha do tempo (baseada em playbook)

**14:32 — T+0**
Marina entra em panico. Abre WhatsApp da Tata: "FUI BANIDA ME AJUDA"

**14:34 — T+2min**
Tata aciona `/crise-imperatriz --ativar ban-meta`. Skill cronometra janela de 24h. Comeca FASE 0 (triagem).

**14:35 — T+3min**
Skill confirma:
- Tipo: conta de anuncios desativada (nao BM, nao perfil pessoal — alivio relativo)
- Quando: 14:15 (decorrido 17 min)
- Quem sabe: so Marina

**14:38 — T+6min**
Skill abre playbook. Marina recebe lista de 5 acoes 0-2h.

**14:40-14:50 — T+8min a T+18min**
Marina executa:
1. Print do banner, email, BM, conta, campanhas, historico de pagamento (10 min)
2. Solicitacao de revisao oficial via botao do banner (1 min)
3. Pausa em todas as campanhas (sem mexer mais)

**14:55 — T+23min**
Marina liga pra agencia parceira (Marketing Partner Tier 2 que ja tinha acesso BM por contrato). Agencia escala chamado prioritario internamente.

**15:10 — T+38min**
Marina abre BM secundaria (criada havia 6 meses por orientacao do `--prevenir`). Pixel duplicado ja rodava. Sobe 3 criativos backup com R$ 200/dia (orcamento conservador).

**15:30 — T+58min**
Marina comunica time: "manutencao na conta principal, BM secundaria ativa, operacao continua, nao comentar com clientes nem postar". Time alinhado.

**16:00 — T+1h28min**
Skill da check-in: "Como esta? Conta voltou? Backup rodando? Volume estabilizando?". Marina responde: backup rodando, sem reposta do Meta ainda.

**18:00 — T+3h28min**
Skill puxa proximo bloco: tentar canais alternativos.
- Twitter: Marina nao posta (regra dura — nao postar publico).
- Comunidade: pergunta em grupo privado de gestoras se alguem conhece rep Meta. Conseguiu contato.
- Marketing Partner: ja escalou.

**Quinta-feira 09:00 — T+18h**
Sem retorno do Meta. BM backup com R$ 800 gastos, 4 vendas registradas (R$ 32.000 receita = ROAS 40). Operacao continua.

**Quinta 16:00 — T+25h**
Meta responde: "Conta reativada. Anuncio violava politica X.Y (claim financeiro implicito em depoimento de mentorada)." Conta volta.

### Acoes 24h-7d (recuperacao)

**Sexta**
- Auditoria de TODOS os criativos contra politica financeira Meta
- Refazer 4 criativos com claims ajustados
- Manter BM backup ativa em paralelo (nunca desligar)

**Semana 2**
- Reuniao com agencia: pra cada novo criativo, validacao previa de compliance
- Treinamento da equipe de criativo sobre politica financeira Meta
- Cliente de "depoimento" foi avisada: nao usar mais palavras como "mudou minha vida financeira" no video

**Semana 3 — Debrief**
- Causa raiz: depoimento de cliente com claim financeiro implicito ("triplicou meu faturamento em 2 meses") — Meta classificou como "promessa irrealista"
- Custo da crise:
  - Receita perdida nas 25h: ~R$ 7.000 (ROAS estava em 40, R$ 700/h normal)
  - Receita backup gerada: R$ 32.000 (ROAS 40 manteve)
  - **Perda liquida: R$ 0** (backup compensou)
  - Custo emocional: ALTO (panico, ansiedade)
- Acao corretiva permanente:
  - Compliance check pre-publicacao (rodada `/ads-meta`)
  - 2 BMs ativas permanentemente (60% principal / 40% secundaria, redundancia real)
  - 3 criativos novos por semana em pasta backup constante

### Score do imperio antes vs depois

**Antes da crise (auditoria):**
- BM secundaria criada: SIM (preventivo da Tata foi chave)
- Pixel duplicado: SIM
- Criativos backup: SIM
- Agencia parceira: SIM
- Score Crise 1: 10/12 = 83% (ROBUSTO)

**Por que Marina sobreviveu:** ela ja tinha 83% das protecoes da Crise 1 ativadas. A crise foi gerenciada em 25h sem perda liquida.

**Marinas com 30% de protecao tipicamente perdem R$ 30k-80k em ban Meta de 3-7 dias.**

### Lições da Marina

1. **BM backup nao e "pra um dia".** E pra hoje. Crise pode bater amanha.
2. **Compliance pre-publicacao economiza ban.** 1h de revisao previa vale R$ 50k de receita preservada.
3. **Nao postar publico em panico.** Marina nao postou. Cliente nem percebeu manutencao. Confianca preservada.
4. **Agencia parceira e seguro.** Custou R$ 5k/mes de retainer. Salvou em 25h.

---

## CASO 2 — POST NEGATIVO VIRAL

**Mentorada:** Renata (nome ficticio), agencia de social media, ticket R$ 3.500-12.000, time de 8 pessoas, base de 2.500 clientes lifetime.

**Crise:** terca-feira, 11:00. Cliente posta no Twitter/X print de conversa onde atendente do time da Renata respondeu rispidamente quando ela cobrou um relatorio atrasado. Print: "ja te respondi 3x essa semana, vc nao le? leia antes de me cobrar de novo." Post viraliza em 90 minutos: 12k retweets, 28k curtidas. Influencer de marketing digital comparte. Vai pra capa do trending Brasil.

### Linha do tempo

**11:00 — T+0**
Cliente posta. Renata nao sabe ainda.

**11:45 — T+45min**
Funcionaria do time avisa Renata via WhatsApp: "olha isso ta viralizando".

**11:48 — T+48min**
Renata abre `/crise-imperatriz --ativar post-viral`. Skill cronometra janela de 4h.

**11:50 — T+50min**
Skill confirma:
- Tipo: post viral em rede aberta (X)
- Volume: 12k retweets em 90 min (alto)
- Bolha: marketing/empreendedorismo (publico-alvo direto)
- Cliente tem razao? Skill pede: "le toda a thread e me responde — fato + narrativa"

**11:55 — T+55min**
Renata le. Diagnostico:
- Fato: atendente respondeu mal, com tom errado.
- Cliente reclamava de relatorio atrasado havia 5 dias (procedente).
- Ela publicou fora do contexto (omitiu que tinha mandado 3 audios irritados antes), MAS o tom da resposta da atendente foi inadequado mesmo descontextualizado.
- Conclusao: cliente tem razao parcial. Atendente errou. Cliente exagerou na expressao publica mas tem fundamento.

**12:00 — T+1h**
Skill abre playbook. Acoes 1-4h:
1. NAO apagar nada
2. NAO responder em panico
3. Preparar resposta enquadrada
4. DM privada com oferta concreta
5. Comunicacao comunidade leal (nao mencionar caso)

**12:15 — T+1h15min**
Renata responde no proprio post (template do `PROTOCOLO-COMUNICACAO.md`):

> "[Nome cliente], recebi sua mensagem aqui — lamento profundamente que tenha chegado a esse ponto. Quero entender exatamente o que aconteceu e encontrar uma solucao real pra ti. Te chamei na DM agora. Posso te responder ali nos proximos minutos."

**12:18 — T+1h18min**
DM privada pra cliente:

> "Oi [nome], conversamos por aqui. Antes de mais nada: lamento. O tom da resposta que voce recebeu nao representa como atendemos aqui — e muito menos como queremos que voce se sinta como cliente. Aqui a minha proposta concreta: 1) reembolso integral do mes corrente (R$ 4.200), processado hoje. 2) Mes adicional gratuito caso queira continuar (sem obrigacao). 3) Conversa direta entre voce e eu pra revisar como podemos refazer essa relacao. Independente de aceitar a proposta, vou usar teu caso pra revisar o protocolo de atendimento aqui — pra que ninguem mais passe pelo mesmo. Aguardo teu retorno."

**12:35 — T+1h35min**
Cliente responde DM, mais aberta. Aceita reembolso e diz que decide depois sobre continuar.

**13:00 — T+2h**
Renata posta nos Stories proprios:
- Story 1: bastidor real do dia (gravando aula com mentorada — proof de operacao normal)
- Story 2: print de mensagem de cliente feliz (com permissao — banco de proof)
- Story 3: foto cotidiana

NAO mencionou o caso publico. Algoritmo entende: tudo normal aqui.

**13:30 — T+2h30min**
Renata reune time:
- Apresenta o caso ao time COMPLETO (nao culpa atendente publicamente)
- Conversa privada com a atendente envolvida (sem demitir, mas com formacao/recolocacao em area sem atendimento)
- Comunica diretrizes: nao responder publico, nao comentar, atendimento aos demais clientes super acolhedor essa semana

**14:00 — T+3h**
Cliente edita o post original adicionando: "Atualizando: a propria Renata me chamou em DM, me ofereceu reembolso e proposta justa. Reconheco que minha postagem foi mais agressiva que precisava. Caso resolvido."

**14:30 — T+3h30min**
Algoritmo do X percebe: post original perdeu tracao. Engajamento despenca. Em 24h, vai pra fundo do feed.

### Acoes 1-7d (recuperacao)

**Quarta-quinta**
- Renata grava video de 4 min nos Stories falando sobre "como cuidamos do atendimento aqui" — sem mencionar caso especifico, mas reforcando padrao
- Time recebe treinamento de protocolo de atendimento de cliente irritado

**Semana 2 — Debrief**
- Causa raiz:
  - Atendente sobrecarregada (gerenciava 35 clientes sozinha — limite era 25)
  - Sem protocolo claro pra cliente que cobra varias vezes
  - Resposta sem revisao previa (mensagem direta sem segundo olhar)
- Custo:
  - Reembolso: R$ 4.200
  - Mes gratis adicional: -R$ 4.200
  - 2 churns de clientes que viram o post e desconfiaram: R$ 18.000 lifetime
  - Tempo do time gerenciando crise: ~16h-pessoa
  - **Total: ~R$ 28.000**
- Acao corretiva permanente:
  - Carga maxima de cliente por atendente revista (de 35 pra 22)
  - Protocolo de cliente irritado escrito (escalonamento, oferta padrao)
  - Mensagem critica sempre revisada por outra pessoa antes de mandar
  - NPS mensal pra detectar problema antes de virar publico

### Score do imperio antes vs depois

**Antes da crise:**
- SLA de resposta <24h: SIM
- Atendente treinada em protocolo: PARCIAL (treinada em onboarding, nao em conflito)
- Politica de reembolso publicada: SIM
- NPS / pesquisa de satisfacao mensal: NAO
- Templates de resposta a reclamacao publica salvos: NAO
- Score Crise 5: 6/10 = 60% (ESTAVEL — limite inferior)

**Por que Renata sobreviveu:**
- Resposta em <2h (dentro da janela de 4h)
- Resposta enquadrada, nao defensiva
- Oferta concreta privada
- Nao apagou, nao brigou, nao mobilizou tropa
- Cliente acabou retratando publicamente

**Renatas que respondem em panico (defensivo, brigando, apagando) tipicamente perdem R$ 100k-300k em churn de 90 dias e demoram 6+ meses pra reconstruir confianca.**

### Lições da Renata

1. **As primeiras 4h definem o resto.** Janela curta exige protocolo pronto.
2. **Reconhecer + oferta privada > defensiva publica.** Sempre.
3. **Cliente irritada quase sempre tem razao parcial.** Reconhecer parte e mais forte que negar tudo.
4. **Carga do time vira fundamento de crise.** Sobrecarregar atendente vira post viral 6 meses depois.

---

## CASO 3 — SOCIA SAI

**Mentorada:** Camila + Beatriz (nomes ficticios), socias 50/50 ha 4 anos. Empresa de cursos de copywriting. Faturamento R$ 480k/mes. Time de 12 pessoas. Marca pessoal e mista (ambas aparecem em material).

**Crise:** segunda-feira, 17:00. Beatriz pede reuniao privada. Comunica que decidiu sair pra empreender solo. Quer formalizar saida em 90 dias. Sem conflito explicito — apenas "quer outro caminho".

### Linha do tempo

**Segunda 17:00 — T+0**
Beatriz comunica saida. Camila ouve, agradece coragem da decisao, pede 24h pra processar antes de proxima conversa.

**Segunda 22:00 — T+5h**
Camila aciona `/crise-imperatriz --ativar socia-sai`. Skill cronometra janela diferente das outras (30-90 dias, nao horas).

**Segunda 22:30 — T+5h30**
Skill abre playbook. Confirma:
- Saida amigavel (sem conflito explicito)
- Prazo proposto: 90 dias
- Marca: mista (ambas aparecem)
- Estrutura societaria: 50/50

**Terca 08:00 — T+15h**
Camila + Beatriz se reunem. Acordos preliminares:
- Saida em 90 dias
- Beatriz mantem direito a metade do caixa atual (~R$ 600k)
- Beatriz nao leva produto, marca ou base
- Beatriz pode continuar no nicho de copywriting com restricoes (nao-aliciamento)
- Comunicacao publica conjunta apos distrato

**Terca 14:00 — T+21h**
Camila aciona advogada empresarial (em retainer ha 2 anos). Briefing em 5 bullets enviado.

**Quarta — T+45h**
Reuniao com advogada empresarial + contadora.
- Avaliacao da empresa: definir multiplo de receita (12x EBITDA = R$ 4.8mi base)
- Beatriz tem direito a 50% = R$ 2.4mi (em pagamento parcelado conforme contrato social)
- Mas caixa real liquido = R$ 1.2mi (resto e ativo intangivel, base de cliente, marca)
- Negociacao: Beatriz aceita R$ 600k vista + R$ 1.8mi parcelado em 36 meses sem juros + clausula de earnout

**Semana 2 — T+10d**
Distrato sendo redigido pela advogada. Discussoes:
- Clausula de nao-concorrencia: 24 meses, restrita a "produtos digitais de copywriting com publico mentora high-ticket" (deixa Beatriz livre pra atuar em copy B2B, agencia, outras areas)
- Nao-aliciamento de funcionarias e clientes: 24 meses
- NDA reciproco: 5 anos
- Direito de imagem: Beatriz pode continuar com nome dela; conteudo em que ela aparece pode permanecer no acervo da empresa por 12 meses, depois retirado
- Marca: registrada na empresa, segue com Camila

**Semana 3 — T+17d**
- Acessos sendo mapeados (lista mestre criada)
- Cronograma de transferencia: que sistema vira de quem em qual data
- Beatriz comeca a documentar: papeis estrategicos que ela fazia (relacionamento com top affiliates, criacao de produto novo, edicao do podcast)

**Semana 4 — T+30d**
- Distrato assinado por ambas + registro Junta Comercial
- Comunicacao interna pro time agendada pra quarta-feira

**Semana 4, quarta-feira — T+33d**
Reuniao com time inteiro (presencial + video pras remotas):
- Camila + Beatriz juntas
- Comunicado factual (template `PROTOCOLO-COMUNICACAO.md`)
- Cronograma de transicao apresentado
- Espaco pra perguntas (1h)
- Time recebe a noticia bem (sem demissoes em massa, todos ficam)

**Mes 2 — T+30 a T+60d**
- Beatriz documenta operacionalmente (5h gravadas + manuais escritos)
- Camila assume relacionamento direto com top affiliates
- Contratada novo gestor de podcast (mes 2)
- Comunicacao publica comeca a se preparar

**Mes 3 — T+60 a T+90d**
- Comunicacao publica final agendada (ambas postam mesmo texto, mesmo dia)
- Substituta de operacao integrada
- Beatriz reduz aparicoes em conteudo (saida da producao gradual)
- Ultimas semanas de transicao

**Dia 90 — T+90d**
- Comunicacao publica:
  - Story conjunta: "encerro um ciclo importante" (template)
  - Post Instagram (ambas postam)
  - Email pra base
  - Manhã de uma sexta-feira
- Reacao do publico: respeitosa. Sem drama. Ambas marcas seguem.
- Beatriz lança nova empresa 30 dias depois (nicho B2B, conforme acordado)
- Camila mantem empresa original com novo posicionamento (rosto unico)

### Custo da crise

**Financeiro:**
- Pagamento a Beatriz: R$ 600k vista + R$ 50k/mes por 36 meses
- Honorarios advogada empresarial: R$ 35k (caso pontual + retainer 6 meses)
- Honorarios contadora avaliacao: R$ 12k
- Recrutamento gestor podcast: R$ 8k
- Recrutamento + onboarding outros 2 papeis: R$ 25k
- **Total fora retainer: R$ 80k + parcelado**

**Operacional:**
- Receita primeiros 30 dias pos-saida: -8% (estabilizacao)
- Receita 60 dias depois: -3%
- Receita 90 dias depois: voltou ao patamar
- 2 funcionarias adicionais saem nos meses 2-4 (efeito secundario — algumas se identificavam mais com Beatriz)

**Reputacional:**
- Publico recebeu bem (comunicacao alinhada)
- Sem rumor publico de conflito
- Algumas mentoradas perguntaram em DM, todas tiveram resposta padrao

### Score do imperio antes vs depois

**Antes da crise:**
- Contrato social com clausula de saida explicita: SIM (revisado ano anterior)
- Clausula de nao-concorrencia: SIM
- Nao-aliciamento: SIM
- Mecanismo de avaliacao pre-acordado: SIM
- Acessos em duas pessoas: PARCIAL
- Marca registrada na empresa: SIM
- Documentacao operacional escrita: PARCIAL
- Reuniao societaria mensal: SIM
- Score Crise 4: 7/8 = 87% (ROBUSTO/ANTIFRAGIL)

**Por que sobreviveram bem:** Camila e Beatriz fizeram contrato social robusto no dia 1 (com advogada empresarial competente). A saida foi dolorosa mas previsivel — e por isso gerenciavel.

**Camilas com contrato social fraco (50% das socias info-produto BR) tipicamente passam 12-24 meses em conflito juridico com perda 30%-60% do faturamento + ruptura publica.**

### Lições da Camila

1. **Contrato social bem feito no dia 1 = Crise 4 gerenciavel no ano 4.** Dor previsivel e dor barata.
2. **Comunicacao ALINHADA entre as socias e tudo.** Mesmo texto, mesmo dia, mesmo tom. Publico aceita.
3. **Saida amigavel ainda custa muito** (R$ 80k+ em honorarios + perda transitoria de receita). Saida hostil custa 5x.
4. **Time aceita melhor que voce pensa** se a comunicacao vier no momento certo. Surpresa total e o pior — pista de pouso longa e melhor.
5. **Beatriz lancou empresa propria 30d depois.** Camila nao tomou isso como traicao — era o que estava acordado. Maturidade societaria virou sobrevivencia.

---

## SINTESE DOS 3 CASOS

| Caso | Janela | Score pre-crise | Custo bruto | Custo liquido | Resultado |
|------|--------|-----------------|-------------|---------------|-----------|
| Marina (ban Meta) | 24h | 83% | R$ 7k receita perdida | R$ 0 (backup compensou) | OK em 25h |
| Renata (post viral) | 4h | 60% | R$ 28k churn+reembolso | R$ 28k | OK em 24h, lessons learned |
| Camila (socia sai) | 90d | 87% | R$ 80k honorarios + 8% receita 30d | R$ 80k | OK em 90d |

**Padrao transversal:**
- Score pre-crise > 60% = imperio sobreviveu
- Score pre-crise < 40% = imperio teria amargado 3-10x mais
- Comunicacao publica controlada = reputacao preservada em 100% dos casos
- Cronometragem da janela = decisao melhor

---

## COMO USAR ESSES CASOS

**Em modo `--simular`:** mentorada le um caso e responde "o que eu faria diferente?" Skill compara com playbook ideal.

**Em modo `--prevenir`:** identificar quais protecoes Marina, Renata, Camila tinham que VOCE nao tem.

**Em modo `--ativar`:** lembrar que outras passaram por isso. Voce nao e a primeira. Tem caminho.

**Apos uma crise pessoal:** virar caso 4. Adicionar aqui (anonimizado) pra mentoradas futuras.

---

**Voltar a `SKILL.md` pra fluxo geral. Ver `OS-8-PLAYBOOKS.md` pra protocolo executivo. Ver `PROTOCOLO-COMUNICACAO.md` pra templates.**

---

**Crise Imperatriz — Pilar 5 da Travessia. Propriedade intelectual Tata Goncalves.**
