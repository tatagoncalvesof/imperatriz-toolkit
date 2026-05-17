# Os 8 Playbooks de Crise — Detalhado

Cada playbook e um documento operacional. Quando a skill ativar `--ativar [tipo]`, ela carrega o playbook correspondente e segue passo a passo. Mentorada NAO precisa pensar — so executar.

Estrutura padrao de cada playbook:
1. **Diagnostico rapido** (sintomas que confirmam o tipo)
2. **Janela critica**
3. **Acoes nas primeiras horas** (cronologia precisa)
4. **Acoes 24h-7d**
5. **Acoes 7-30d (recuperacao)**
6. **Comunicacao** (referencia pra `PROTOCOLO-COMUNICACAO.md`)
7. **O que NAO fazer**
8. **Debrief obrigatorio**

---

## PLAYBOOK 1 — BAN META / GOOGLE

**Sintoma:** banner vermelho no Gerenciador. Conta de anuncios desativada. Email "violacao de politica" (ou nenhum email). Campanhas paradas.

### Janela critica: 24h

A primeira metade da janela (12h) e pra **recuperacao automatica** (caminho normal). A segunda metade (12h-24h) e pra **acionar canais alternativos** (Marketing Partner, agencia parceira, contato direto).

### Acoes 0-2h (primeiras 2 horas)

**1. Confirmar o tipo de ban (5 min)**
- Conta de anuncios desativada? (mais leve)
- Pixel desabilitado? (medio)
- BM inteira derrubada? (grave)
- Perfil pessoal do admin banido? (gravissimo — perde acesso a tudo)

Cada um tem caminho diferente. Confundir custa tempo.

**2. Tirar print de TUDO (10 min)**
- Print do banner de aviso
- Print do email recebido (se tiver)
- Print da BM e da conta de anuncios
- Print das campanhas que estavam rodando (CAC, ROAS, frequencia)
- Print do historico de pagamento da conta

Nao confiar que vai estar disponivel depois — Meta as vezes apaga acesso retroativo.

**3. Pedir revisao oficial (15 min)**
- Botao "Solicitar Revisao" no banner
- Se nao tiver, abrir chamado em https://www.facebook.com/business/help
- Texto curto, direto, sem emocao: "Conta [ID] desativada hoje [data]. Nao houve violacao consciente. Solicito revisao."

**4. Ativar conta backup (30 min)**
- Pausar todas as campanhas da BM principal (se ainda tiver acesso)
- Ativar BM secundaria (deve estar pre-criada — se nao tem, ver `CHECKLIST-PREVENCAO.md`)
- Subir 2-3 criativos backup (deve estar em pasta de reserva)
- Comecar com orcamento conservador (R$ 100-300/dia) pra nao queimar tambem

**5. Comunicar internamente (15 min)**
- Time precisa saber pra nao mandar mais trafego pra paginas que nao convertem
- Agencia (se tiver) precisa parar de otimizar campanha morta
- Atendimento precisa saber pra ajustar promessas de prazo

### Acoes 2-12h

**6. Tentar canais alternativos (paralelo)**
- **Agencia Marketing Partner:** se voce tem parceria com Tier 1/2/3 Meta, abre chamado prioritario
- **Rep Meta:** se voce ja teve rep de conta (faturamento >R$ 30k/mes em ads geralmente da direito), aciona
- **Comunidade:** grupos privados de gestores de trafego BR — alguem conhece alguem dentro do Meta
- **Twitter/X:** marcar @MetaForBusiness + screenshot do banner — funciona em casos de erro grosseiro

**7. Diversificar pra Google Ads (paralelo)**
- Se nunca rodou Google, pelo menos abrir conta + Pixel/Tag + 1 campanha Search da palavra-chave principal
- Senao, dobrar orcamento Google se ja tem

**8. Diversificar pra organico (paralelo)**
- Acionar lista de WhatsApp / email da base quente
- Reativar Stories diarios + Reels com proof
- Ver `/calendario-imperatriz` pra plano de 7 dias 100% organico

### Acoes 12-24h

**9. Avaliar persistencia**
- Meta respondeu? (geralmente em 12-72h)
- Conta voltou? Conta ficou banida? Conta voltou parcial?
- Decidir: insiste em recuperar ou move 100% pra backup?

**10. Comunicacao publica (so se necessario)**
- **NAO POSTAR** "estou banida" em panico. Cliente perde confianca, concorrente celebra, Meta nao revisa mais rapido.
- Se cliente perguntar (Stories de pergunta, DM), responder: "estamos com manutencao na conta de anuncios principal — operacao continua normal pelos outros canais." Calmo, curto.

### Acoes 24h-7d (recuperacao)

**11. Plano B viva**
- Se conta nao voltou, BM secundaria vira primaria
- Estabilizar criativos, ajustar CAC, voltar a escalar
- Documentar o que mudou pra evitar mesmo bug

**12. Diagnostico de causa raiz**
- Por que banaram? (criativo? landing page? pagamento? historico?)
- Auditar nos proximos 7 dias todos os criativos ativos contra politica Meta
- Auditar landing pages contra politica Meta (clausulas LGPD, claims de saude, claims financeiros, antes/depois)

**13. Aprendizado pro protocolo**
- Atualizar `CHECKLIST-PREVENCAO.md` com a brecha que pegou
- Decidir: precisa contratar agencia parceira Meta pra ter rep?

### O que NAO fazer

- **NAO criar BM nova com mesmo CPF/CNPJ no mesmo dia.** Meta cruza dados. Banimento se estende.
- **NAO mentir** na revisao oficial ("nao sei o que aconteceu" — eles veem teus criativos).
- **NAO postar revolta** publica contra Meta. Algoritmo le, conta secundaria sofre tambem.
- **NAO pagar** "consultor" que promete "resolver ban em 24h" no Telegram. Geralmente golpe.
- **NAO mover trafego** todo de uma vez pra Google sem ajustar copy/landing — performance Google e diferente.

### Debrief obrigatorio (7 dias depois)

- O que foi violado (real)?
- Tinha BM backup pronta? (TEM/NAO)
- Tempo total pra voltar a faturar como antes: X dias
- Custo da crise: receita perdida + custo de subir backup + custo emocional
- Acao corretiva permanente: [item adicionado ao protocolo]

---

## PLAYBOOK 2 — PROCESSO JUDICIAL

**Sintoma:** notificacao de citacao judicial (oficial de justica, AR, email forense). Cliente reclama que vai processar e manda print de advogado. Reclamacao trabalhista (ex-funcionaria). Processo de concorrente (concorrencia desleal, plagio, marca).

### Janela critica: 48h

Toda peticao tem prazo (geralmente 15 dias uteis pra contestar). Mas as primeiras 48h definem qualidade da defesa.

### Acoes 0-4h

**1. NAO RESPONDER NADA** (zero tolerancia)
- Nao responder cliente
- Nao responder advogado da outra parte
- Nao postar nada publico
- Nao pedir conselho em grupo de WhatsApp de empresarias
- Tudo o que voce escrever pode ser usado.

**2. Contratar advogada de retainer (se nao tiver)**
- **NAO usar advogado da familia.** Diferente especialidade, diferente padrao.
- **NAO usar advogado generalista.** Quer advogada do tipo de processo (consumerista, trabalhista, empresarial).
- Indicacoes: rede de empresarias, OAB local, escritorios especializados em info-produto/digital.
- Custo retainer mensal: R$ 1.500 - R$ 5.000 dependendo do tamanho do imperio. Caso pontual: R$ 3k - R$ 15k.

**3. Reunir TODAS as evidencias (fase de coleta)**
- Contrato com cliente (versao assinada)
- Prints de toda comunicacao (WhatsApp, DM, email) — exportar conversa completa, nao print
- Gravacoes de calls / aulas (se houver)
- Recibos de pagamento (Hotmart/Eduzz/conta corrente)
- Provas de entrega do produto/servico (acessos, certificados, mensagens de conclusao)
- Termos de uso e politica de privacidade vigentes na epoca
- Backups de versoes antigas do site/oferta (Wayback Machine se nao tiver local)

Tudo em pasta organizada por data. Compartilhar com advogada via Drive privado, NAO WhatsApp.

### Acoes 4-48h

**4. Reuniao com advogada**
- Briefing em 5 bullets (ver `PROTOCOLO-COMUNICACAO.md`)
- Definir estrategia: contestar, acordar, propor mediacao, contraprocessar
- Definir prazo (data limite real da peticao)
- Definir narrativa pro time (obrigatorio: ninguem inventa nada)

**5. Congelar comunicacao publica sobre o caso**
- NAO postar Stories sobre o tema do processo
- NAO falar mal de cliente publicamente (mesmo de forma indireta)
- NAO mexer em landing page / copy do produto envolvido (pode ser visto como ocultacao)
- Manter operacao normal, sem cara de fugitiva

**6. Briefing pro time interno**
- "Existe uma demanda juridica em andamento envolvendo [tema generico]. Nao discutimos detalhes interna ou externamente. Se cliente perguntar, encaminha pra mim. Continuamos operando normal."
- Sem dramatizar, sem dar detalhe, sem culpar ninguem.

### Acoes 48h-15d

**7. Suporte da advogada na peticao**
- Voce nao escreve resposta. Advogada escreve.
- Voce so responde pergunta dela com fato.
- Voce assina e revisa.

**8. Avaliar acordo (caso a caso)**
- Acordo pode ser melhor que sentenca em muitos casos (custo + tempo + risco)
- Advogada aconselha
- Se acordo, narrativa publica nunca menciona "acordo"

### Acoes pos-sentenca / acordo

**9. Comunicacao publica (so se inevitavel)**
- Ver `PROTOCOLO-COMUNICACAO.md` se foi caso publico
- Nunca celebrar vitoria publicamente (cliente de vitima vira heroi)

**10. Aprendizado pro protocolo**
- Que clausula faltou no contrato?
- Que processo interno previne reincidencia?
- Atualizar contrato base + onboarding cliente

### O que NAO fazer

- **NAO responder cliente** que ja contratou advogado. Tudo via advogada agora.
- **NAO apagar mensagens** ou prints do WhatsApp (omissao de prova = pior).
- **NAO falar mal** do cliente em grupo, mesmo privado. Print circula.
- **NAO postar** "estou sendo processada injustamente" em rede social. Pessima narrativa.
- **NAO usar advogado da familia.**
- **NAO ignorar prazo.** Revelia = quase derrota automatica.
- **NAO assumir culpa** em comunicacao escrita ("foi minha falha, vou devolver" — cliente usa de prova).

### Debrief obrigatorio

- Causa raiz: contrato fraco, expectativa errada do cliente, falha na entrega, cobranca?
- Custo total: honorarios + valor sentenca/acordo + tempo + impacto emocional
- Atualizacao de protocolo: clausula nova, onboarding novo, comunicacao nova

---

## PLAYBOOK 3 — VAZAMENTO DE DADOS (LGPD)

**Sintoma:** banco de dados acessado por terceiro. Lista de mentoradas vazada (publicada, vendida, encaminhada). Plataforma comprometida (Hotmart, CRM, ferramenta de email). Funcionaria ex-time sai com base. Phishing acessou conta.

### Janela critica: 72h legais

LGPD (Lei 13.709/2018) obriga comunicar ANPD (Autoridade Nacional de Protecao de Dados) e titulares afetados em prazo "razoavel" — pratica de mercado: 72h. Atrasar e infrair (multa ate 2% do faturamento, limite R$ 50 mi).

### Acoes 0-4h

**1. Mitigar tecnico (urgente)**
- Trocar TODAS as senhas do imperio (admin painel, hosting, banco, plataformas, gateway pagamento)
- Revogar acessos de qualquer pessoa que nao deveria ter
- Fechar a brecha tecnica (IP suspeito? endpoint vulneravel? conta pessoal hackeada?)
- Ativar 2FA em tudo
- Rodar `/shield` e `/security-audit` pra varredura completa

**2. Acionar DPO ou advogada LGPD**
- Toda empresa que trata dados pessoais precisa ter DPO (encarregado de protecao de dados)
- Se nao tem, contratar emergencial uma advogada especializada em LGPD (custo: R$ 3k-10k caso)

**3. Documentar o incidente**
- Quando aconteceu (timestamp)
- Como descobriu (logs)
- Quais dados afetados (nome, email, telefone, CPF, dado sensivel)
- Quantas pessoas afetadas
- Qual a causa provavel
- O que ja foi feito pra mitigar

### Acoes 4-72h

**4. Comunicar ANPD**
- Formulario oficial em https://www.gov.br/anpd
- Advogada/DPO preenche
- Prazo razoavel (72h e o consenso de mercado)
- Tom: factual, sem omitir, sem dramatizar

**5. Comunicar titulares afetados**
- Email ou mensagem direta a cada pessoa
- Template em `PROTOCOLO-COMUNICACAO.md`
- O que dizer: o que vazou, o que foi feito, o que a pessoa pode fazer
- Tom: responsavel, claro, sem desculpas vazias

**6. Comunicacao publica (caso aplicavel)**
- Se vazamento e grande (>1000 pessoas) ou virou noticia, publicar nota oficial
- Site + email + redes
- Template em `PROTOCOLO-COMUNICACAO.md`
- NUNCA esconder. NUNCA minimizar.

### Acoes 72h-30d

**7. Auditoria de seguranca completa**
- Rodar `/security-audit`
- Auditar todos os fornecedores que tem acesso a dado (CRM, plataforma, agencia, freelancer)
- Revisar termo de confidencialidade
- Implementar logs de acesso

**8. Politica de privacidade atualizada**
- Revisar com DPO/advogada
- Publicar versao nova
- Notificar mudanca a base

**9. Treinamento do time**
- Toda funcionaria recebe treinamento basico LGPD
- Documentar processo de offboarding (revogar acessos no dia da saida)

### O que NAO fazer

- **NAO esconder** o vazamento. Detectado depois = multa pior + reputacao destruida.
- **NAO atrasar** comunicacao "pra entender melhor antes". Comunica com info parcial.
- **NAO blame** publico em funcionario / fornecedor especifico ("foi a Joana"). Responsabilidade da empresa.
- **NAO oferecer** dinheiro pra silencio (chantagem reversa = crime).
- **NAO ignorar** ANPD. Eles cruzam dado, descobrem.
- **NAO usar** advogado generalista. LGPD e especializacao recente.

### Debrief obrigatorio

- Causa raiz: senha fraca? funcionario? fornecedor? phishing?
- Quantidade de afetados, severidade dos dados
- Custo total: tempo + advogada/DPO + multa eventual + comunicacao + reputacao
- Acao corretiva permanente: 2FA obrigatorio, log de acesso, contrato com fornecedor, treinamento anual

---

## PLAYBOOK 4 — SOCIA / SOCIO SAI

**Sintoma:** socia comunica saida. Conflito societario explicito (ela quer sair, voce quer ela fora, divergencia estrategica). Crise pessoal entre socias (briga, traicao, confianca quebrada). Socio aceita oferta de outro lugar e quer divisao.

### Janela: 30-90 dias (nao e crise de horas, e crise de meses)

Mas as primeiras 72h definem se vai sair limpo ou virar guerra publica.

### Acoes 0-72h

**1. Conversa privada e sem testemunha** entre as socias
- Confirmar a decisao (e pra valer ou e desabafo?)
- Definir intencao: saida amigavel ou litigiosa?
- Combinar **silencio publico** ate plano estar pronto. NINGUEM posta nada nas redes ate alinhamento.

**2. Acionar advogada empresarial**
- NAO advogada da relacao pessoal (familia, amiga)
- Advogada especializada em societario
- Contrato social, distrato, divisao patrimonial

**3. Acionar contadora**
- Levantar patrimonio (caixa, equipamento, marca, base de clientes)
- Fluxo de caixa atual
- Valor real da empresa (geralmente diferente do que socias acham)

**4. NAO comunicar publico ainda**
- Time nao pode saber ainda (alem do nivel C, se tiver)
- Cliente nao pode saber
- Concorrente nao pode saber

### Acoes 3-30d

**5. Definir estrutura da saida**
- Quem fica com qual parte do negocio (marca? canal Instagram? base de email? produto X? produto Y?)
- Quanto se paga (laudo de avaliacao = R$ 3k-10k com contadora)
- Forma de pagamento (vista, parcelado, performance)
- Periodo de transicao (geralmente 30-60 dias)
- Clausula de nao-concorrencia (em qual prazo, em qual nicho, em qual area)
- Clausula de nao-aliciamento de funcionarias e clientes
- NDA reciproco

**6. Distrato formalizado**
- Advogada redige
- Ambas assinam
- Registra na Junta Comercial

**7. Continuidade operacional**
- Quem assume o que socia fazia (operacional + estrategico)
- Backup de tudo que estava na cabeca dela
- Acessos transferidos / revogados (data de corte clara)

### Acoes 30-90d

**8. Comunicacao interna pro time**
- Reuniao alinhada (ambas socias presentes idealmente)
- Narrativa unica: "X esta tomando novo caminho profissional. Operacao segue normal. Equipe agradece contribuicao."
- Sem detalhes, sem julgamento, sem versao "quem tem razao"

**9. Comunicacao publica (so se necessario)**
- Se socia era publica (perfil pessoal divulgava marca), comunicacao e necessaria
- Template unificado em `PROTOCOLO-COMUNICACAO.md`
- Ambas postam o mesmo texto, mesmo dia
- Tom: gratidao, novo capitulo, sem dor exposta
- NUNCA versao "quem tem razao". NUNCA atacar. NUNCA chorar publico.

**10. Estabilizar marca**
- Se socia era rosto, redesenhar comunicacao com voce como rosto
- Se socia tinha publico proprio, ela leva pra novo projeto (ate honesto)
- Reposicionamento de marca eventual (rodar `/posicionamento-estrategico`)

### O que NAO fazer

- **NAO postar** sobre o conflito ate distrato assinado.
- **NAO falar mal** da socia (mesmo privado, com terceiros). Print circula.
- **NAO arrastar** o time pra tomar lado.
- **NAO esquecer** clausula de nao-concorrencia.
- **NAO aceitar** divisao verbal ("a gente acerta depois") — sempre por escrito.
- **NAO usar** advogado da familia (vies emocional).

### Debrief obrigatorio

- Causa raiz: divergencia estrategica, conflito pessoal, oportunidade externa, desigualdade financeira?
- Custo total: valor pago + tempo + perda de receita transitoria + reputacional
- Aprendizado pra futuras parcerias: contrato social robusto, clausula de saida desde dia 1, comunicacao mensal

---

## PLAYBOOK 5 — POST NEGATIVO VIRAL

**Sintoma:** print de cliente reclamando viraliza (Twitter/X, TikTok, Instagram, LinkedIn). Reclame Aqui em alta. Influenciador grande critica voce/teu metodo. Mensagem propria viralizou descontextualizada.

### Janela critica: 4h primeiras

Algoritmo recompensa engajamento rapido. Se voce nao responde em 4h, narrativa solidifica.

### Acoes 0-1h

**1. NAO responder em panico**
- Respira. Le tudo.
- O que e fato? O que e narrativa?
- Cliente tem razao parcial? razao total? nenhuma razao?

**2. Triagem de viralidade**
- Esta viralizando MESMO ou e bolha pequena?
- Quantos compartilhamentos / curtidas?
- Esta fora do publico habitual (rede maior) ou so na bolha do nicho?

**3. Nao apagar nada**
- Nao apagar comentario hostil
- Nao apagar print original (se foi voce que postou algo descontextualizado)
- Apagar = confessar = piorar

### Acoes 1-4h

**4. Resposta enquadrada**
- Templates em `PROTOCOLO-COMUNICACAO.md`
- Estrutura: reconhecer + esclarecer + oferecer resolucao + privado
- NUNCA brigar publico
- NUNCA defensiva ("voce nao entendeu")
- NUNCA atacar ("ela e mentirosa")
- Tom: serio, profissional, gentil sem subserviencia

**5. DM privada pra resolver**
- Se cliente tem razao parcial: oferecer reembolso, troca, sessao extra
- Se cliente tem razao total: assumir, devolver, pedir desculpa especifica
- Se cliente nao tem razao: explicar privado com calma, sem ofensa
- Documentar a conversa

**6. Comunicar comunidade leal**
- Stories proprios (Instagram, LinkedIn): nao mencionar o post viral diretamente
- Postar conteudo de proof, depoimento de outros clientes felizes (gerar contranarrativa)
- Mostrar a operacao normal, sem ar defensivo

### Acoes 4-24h

**7. Monitorar**
- Mencoes em redes (Brand24, Mention, ou busca manual)
- Reclame Aqui (responder em 24h e obrigatorio pra reputacao)
- Influenciadores que repercutiram (DM privada, calma, esclarecer)

**8. Avaliar resolucao publica**
- Se cliente publicar "resolveu, satisfeita" — nao repostar (parece encenacao). Curtir e comentar gentil basta.
- Se cliente nao publicar nada apos resolucao privada, deixar quieto. Nao force "ela admitiu que estava errada".

### Acoes 1-7d

**9. Diagnostico de causa raiz**
- O que falhou no atendimento / produto / promessa?
- Foi caso isolado ou padrao?
- Outros clientes com mesma queixa silenciosa?

**10. Acao corretiva visivel**
- Se padrao: comunicar publico que houve mudanca de processo (sem detalhar caso especifico)
- Onboarding atualizado, garantia revisada, comunicacao revisada

### O que NAO fazer

- **NAO responder em panico** na primeira hora.
- **NAO brigar publicamente** com cliente. Nunca. Mesmo se cliente esta mentindo.
- **NAO apagar** comentarios negativos do proprio post (a nao ser ofensa pessoal grosseira).
- **NAO mobilizar tropa** ("gente, defendam ela!"). Parece encenacao e gera ojeriza.
- **NAO oferecer dinheiro** publicamente pra apagar post.
- **NAO ameacar** processo publicamente ("vou processar quem postou"). Faz se for, sem aviso.
- **NAO sumir.** Fugir agrava.

### Debrief obrigatorio

- O post tinha razao? (parcial / total / nenhuma)
- Causa raiz: produto, atendimento, comunicacao, expectativa?
- Custo: tempo, reembolso, reputacional, conversao perdida
- Acao corretiva permanente: protocolo de atendimento, onboarding, comunicacao de promessa

---

## PLAYBOOK 6 — CONTA ZERADA / SUMIDA (Hotmart, Eduzz, banco)

**Sintoma:** saldo Hotmart/Eduzz zerado sem aviso. Conta de banco bloqueada (PJ ou PF). Saque negado. Mensagem da plataforma "investigacao em andamento". Pagamento de cliente nao caiu.

### Janela: 7-14 dias (depende da plataforma)

Plataformas tem prazo regulamentar mas geralmente demoram 7-21 dias. Banco bloqueia ate 30 dias em casos extremos.

### Acoes 0-2h

**1. Confirmar a situacao**
- Login na plataforma e ver mensagem oficial
- Email da plataforma (caixa principal + spam)
- Print de tudo

**2. Contato direto via canal premium**
- Se voce e cliente Premium (Hotmart >R$ 30k/mes, Eduzz Diamond, etc), tem rep dedicado
- Se nao, abrir chamado URGENTE com print + contexto + pedido
- Hotmart: helpdesk ou consultor designado
- Eduzz: chat direto da conta
- Banco: agencia presencial (mais rapido) + ouvidoria (formal)

**3. Comunicar time**
- Se a conta zerada e o gateway principal, time precisa redirecionar comissionados, afiliados, fornecedores
- Pausar pagamentos automaticos que sairiam dessa conta

### Acoes 2-48h

**4. Plataforma backup ja tem? Ativa**
- Se ja tem oferta espelho em outra plataforma (Hotmart espelho na Eduzz, por exemplo), redirecionar links de venda
- Se nao tem, criar oferta minima viavel em outra plataforma em 24h
- Atualizar pixel, integracoes, automacoes

**5. Comunicacao cliente sobre delay**
- Cliente que pagou e nao recebeu acesso: comunicar individualmente
- Template em `PROTOCOLO-COMUNICACAO.md`
- Tom: factual, com expectativa real ("ate X dias"), com plano B se nao resolver

**6. Documentar tudo**
- Print de comunicacao com plataforma
- Print de saldo congelado
- Todos os tickets abertos
- Datas e horarios

### Acoes 48h-14d

**7. Insistir + escalonar**
- Reabrir chamado a cada 48h se nao tiver resposta
- Subir nivel: gerente, ouvidoria, redes sociais (Twitter @ marca)
- Se passou 7 dias e zero resposta: notificacao extrajudicial via advogada
- Se passou 14 dias e zero resposta: ProconRJ/SP, ANS, Banco Central (banco), denuncia formal

**8. Plano B paralelo full**
- Migrar 100% das vendas pra plataforma backup
- Manter conta principal pendente em paralelo
- Nunca colocar todas as vendas futuras na mesma plataforma de novo

### Acoes pos-resolucao

**9. Receber + sacar imediatamente**
- Quando saldo voltar, sacar 80% no mesmo dia
- Manter so o minimo operacional
- Diversificar conta bancaria (pelo menos 2 bancos PJ)

**10. Aprendizado pro protocolo**
- Sempre 2 plataformas ativas (espelho)
- Sempre saque rapido (nao acumular saldo)
- Sempre conta backup em outro banco

### O que NAO fazer

- **NAO postar publico** "Hotmart me roubou". Plataforma le, dificulta resolucao + risco juridico.
- **NAO mentir** pro cliente ("ja foi liberado"). Cliente descobre, vira post viral (Playbook 5).
- **NAO criar conta nova com mesmo CPF** na mesma plataforma. Sistema cruza, bloqueia tambem.
- **NAO ignorar** comunicacao com cliente afetado. Silencio = fuga = post negativo iminente.
- **NAO desabilitar** integracoes apressadamente (pixel, email automatico) — perde dados de quem pagou e nao recebeu.

### Debrief obrigatorio

- Causa raiz: chargeback alto? denuncia de cliente? politica violada (claim de saude/financeiro)?
- Custo: receita travada x dias + custo migracao + churn de cliente impaciente
- Acao corretiva: backup ativo, saque diario, diversificacao bancaria, auditoria de claims

---

## PLAYBOOK 7 — FORNECEDOR CRITICO SOME

**Sintoma:** dev nao responde ha 5 dias e site quebrou. Designer abandonou no meio do projeto de lancamento. Plataforma de email automatico subiu preco 3x ou foi vendida. Editor de video desapareceu na vespera de subir VSL. Agencia rompe contrato sem aviso.

### Janela: 7-30 dias (depende do papel critico)

### Acoes 0-24h

**1. Avaliar criticidade**
- O que para se essa pessoa nao retornar?
- Tem lancamento marcado? Afeta? Adia ou substitui?
- Cliente afetado direto?

**2. Acessar tudo**
- TODOS os arquivos do projeto (Drive, Github, Figma, Frame.io, Trello)
- Senhas, integracoes, accesses
- Se acesso era so pessoa: abrir novo acesso emergencial (Github, hosting, dominio)

**3. Tentativa final de contato**
- WhatsApp + ligacao + email (uma vez de cada)
- Se nao responder em 24h: assume que sumiu
- Documentar tentativas (prints, registros)

### Acoes 24h-7d

**4. Acionar substituto da lista pre-aprovada**
- Cada papel critico tem 2-3 substitutos pre-aprovados (ver `CHECKLIST-PREVENCAO.md`)
- Briefing rapido em 1 pagina (contexto + entregavel + prazo + acesso)
- Pagamento adiantado de 50% pra acelerar

**5. Comunicar cliente afetado (se houver)**
- Lancamento adiado? Cliente espera promessa? Comunicar antes que ele pergunte
- Template em `PROTOCOLO-COMUNICACAO.md`

**6. Backup de arquivos**
- Tudo do projeto antigo migrado pra Drive/repo proprio (caso fornecedor sumido nao volte mais)
- Versionar e datar

### Acoes 7-30d

**7. Resolver pendencia financeira**
- Se pessoa sumiu devendo entrega, ela tambem tem direitos (devido x entregue parcial)
- Se contrato bem feito: clausula de rescisao por descumprimento, recisao do contrato, sem pagamento das parcelas seguintes
- Se nao tem contrato: bloquear pagamentos seguintes + tentar acordo

**8. Implementar redundancia**
- Cada papel critico nunca mais com 1 pessoa so
- 2 opcoes ativas (mesmo que primaria seja principal)

**9. Contrato base com clausula de transicao**
- Toda nova contratacao tem clausula: "fornecedor compromete a passar bastao com 30 dias minimo"
- Acessos sempre na empresa, nunca so na pessoa

### O que NAO fazer

- **NAO esperar** mais de 48h por resposta. Tempo perdido nao volta.
- **NAO pagar** valor cheio adiantado pra novo fornecedor em panico (vira segundo desaparecimento).
- **NAO confiar** acesso unico em 1 pessoa nunca mais (admin Github, hosting, dominio).
- **NAO postar publicamente** "fulano sumiu". Mercado pequeno, vira fofoca, segunda crise.

### Debrief obrigatorio

- Causa raiz: sobrecarga? burnout? oferta melhor? conflito? pessoa instavel?
- Custo: prazo perdido + custo substituto urgente + retrabalho + desgaste com cliente
- Acao corretiva: redundancia, contrato com clausula, acesso na empresa, lista de reservas

---

## PLAYBOOK 8 — TIME INTERNO QUEBRA

**Sintoma:** funcionaria-chave (ops, atendimento, gestor de trafego, designer interno) pede demissao sem aviso. Pessoa que sabia "como tudo funciona" sai. Multiple saidas em sequencia. Burnout coletivo + solicitacao de saida de 2-3 pessoas.

### Janela: 30 dias (transferencia de conhecimento)

### Acoes 0-24h

**1. Conversa final**
- Aceitar a saida (sem tentar segurar com aumento desesperado)
- Definir periodo de transicao (idealmente 30 dias trabalhados)
- Negociar transferencia de conhecimento (incluido na saida)

**2. Triagem de funcoes**
- O que ela fazia? (lista exaustiva)
- Urgente vs adiavel
- Substituivel por automacao? Por outro do time? Por terceirizado?

**3. Acessos**
- Mapear TODOS os acessos (plataformas, contas, arquivos)
- Plano de revogacao (data exata da saida = revogacao automatica)
- 2FA migrado pra nova pessoa antes de revogar

### Acoes 1-14d

**4. Redistribuicao imediata**
- Quem do time absorve cada tarefa (temporario)
- Quem terceirizar (lista de reservas)
- Que automacao implementar pra reduzir carga futura

**5. Contratacao da substituta**
- Job description atualizado (ver papel real, nao papel original)
- Triagem em 5 dias maximo
- Onboarding em 7 dias

**6. Transferencia de conhecimento**
- Se saida amigavel: 5-10h gravadas com ela explicando processos
- Manuais escritos (idealmente ja existiam — ver `CHECKLIST-PREVENCAO.md`)
- Acompanhamento 1-2 semanas com substituta

### Acoes 14-30d

**7. Estabilizar nova estrutura**
- Reuniao 1:1 quinzenal com cada substituta nos primeiros 3 meses
- Auditar entregas (ela esta acompanhando?)
- Ajustar processos com base no que aprendeu

**8. Comunicacao publica (se aplicavel)**
- Funcionaria era publica (rosto da marca)? Comunicar
- Funcionaria nao era publica? Nao precisa anunciar
- Sem dramas, sem versao "ela errou"

### O que NAO fazer

- **NAO surtar** e oferecer aumento desesperado. Sinaliza que voce e dependente. Pessoa que ja decidiu, sai mesmo.
- **NAO falar mal** da pessoa que sai (mesmo se ela falhou). Time observa.
- **NAO pular** transferencia de conhecimento. 30 dias gastos AGORA economizam 6 meses depois.
- **NAO sobrecarregar** o resto do time. Quem fica olha pra carga e tambem sai.
- **NAO contratar em panico**. Substituta errada custa mais que vaga aberta por 60 dias.

### Debrief obrigatorio

- Causa raiz: salario? gestao? sobrecarga? falta de proposito? conflito interpessoal?
- Custo: vaga aberta x dias + recrutamento + onboarding + curva de aprendizado da nova
- Acao corretiva: documentacao de processos, reuniao 1:1 mensal, plano de carreira, banco de talentos passivos

---

## TABELA RESUMO DAS 8 CRISES

| # | Crise | Janela | Ator chave | Custo medio R$ |
|---|-------|--------|-----------|----------------|
| 1 | Ban Meta/Google | 24h | Mentorada + agencia | 5k-50k receita perdida |
| 2 | Processo judicial | 48h | Advogada especializada | 5k-50k honorarios+acordo |
| 3 | Vazamento LGPD | 72h | DPO/advogada LGPD | 10k-500k (multa eventual) |
| 4 | Socia sai | 30-90d | Advogada empresarial | 10k-500k+ (divisao) |
| 5 | Post viral | 4h | Mentorada + atendimento | 0-30k (reembolsos+conversao) |
| 6 | Conta zerada | 7-14d | Mentorada + plataforma | 5k-50k receita travada |
| 7 | Fornecedor some | 7-30d | Substituto da lista | 2k-20k retrabalho |
| 8 | Time quebra | 30d | RH + lideranca | 5k-30k recrutamento+curva |

**Custo total medio de uma crise nao gerenciada: 3x a 10x o custo de uma crise gerenciada com protocolo.**

---

**Voltar a `SKILL.md` pra fluxo geral. Ver `PROTOCOLO-COMUNICACAO.md` pra templates de mensagem. Ver `CHECKLIST-PREVENCAO.md` pra protecoes preventivas.**
