# Os 8 Blocos — Perguntas Literais + Criterio de Qualidade

Este documento e o **manual de campo** da anamnese. Aqui estao as **35+ perguntas literais** que a Tata faz na call (modo `--call`) ou que aparecem no formulario (modo `--formulario`).

Cada pergunta tem:
- **Texto literal** (PT-BR, voz Tata)
- **Por que importa** (justificativa estrategica)
- **Criterio de qualidade** (o que e resposta boa vs vaga)
- **Sondas (probing)** — perguntas de aprofundamento se a resposta for evasiva
- **Campo JSON** (onde grava no schema)

---

## BLOCO 1 — HISTORICO PESSOAL (8 campos, 8 minutos)

**Abertura na call:**
> "Antes de qualquer plano, eu preciso entender quem voce e — nao quem voce escreve no Insta. Me conta sua historia rapidinha."

### 1.1 Nome completo
- **Pergunta:** "Qual seu nome completo?"
- **Por que:** documentacao, formalizacao do dossie, evitar confusao de homonimos.
- **Resposta boa:** "Carolina Aparecida Mendes"
- **Resposta vaga:** "Carol so" → sondar: "E o sobrenome que aparece no contrato/CPF?"
- **Campo JSON:** `historico.nome_completo`

### 1.2 Idade
- **Pergunta:** "Quantos anos voce tem?"
- **Por que:** ancora geracional (millennial, gen X, gen Z), expectativas de vida, energia disponivel.
- **Resposta boa:** numero exato (37)
- **Resposta vaga:** "Trinta e poucos" → sondar: "Mais perto de 30 ou de 40?"
- **Campo JSON:** `historico.idade`

### 1.3 Cidade + Estado
- **Pergunta:** "Onde voce mora hoje?"
- **Por que:** fuso, custo de vida, mercado regional, encontros presenciais possiveis.
- **Resposta boa:** "Curitiba — PR"
- **Resposta vaga:** "Sul" → sondar: "Cidade especifica?"
- **Campo JSON:** `historico.localizacao` (objeto: cidade, estado, pais)

### 1.4 Estado civil + filhos
- **Pergunta:** "Casada, solteira, divorciada? Tem filhos?"
- **Por que:** carga emocional/operacional, tempo disponivel real, rede de apoio.
- **Resposta boa:** "Casada, dois filhos — 8 e 12 anos"
- **Resposta vaga:** "Tenho familia" → sondar: "Marido/companheira? Filhos pequenos ou grandes?"
- **Campo JSON:** `historico.estado_civil`, `historico.filhos` (numero + idades)

### 1.5 Formacao + curso
- **Pergunta:** "Qual sua formacao? Onde voce estudou?"
- **Por que:** background tecnico, capital cultural, network academico, sindrome do impostor.
- **Resposta boa:** "Direito pela PUC-PR, MBA em gestao pela FGV"
- **Resposta vaga:** "Faculdade qualquer" → sondar: "Em qual area voce se formou?"
- **Campo JSON:** `historico.formacao` (array de objetos: curso, instituicao, ano)

### 1.6 Trajetoria profissional ate hoje
- **Pergunta:** "Me conta em 2 minutos sua trajetoria — desde a primeira vez que ganhou dinheiro ate agora."
- **Por que:** entender padroes (sempre empreendeu? saiu de CLT? falencia anterior?), pontos de virada, identidade profissional.
- **Resposta boa:** narrativa em 3-4 fases com anos e papeis ("Trabalhei 8 anos como advogada, abri escritorio em 2019, comecei a ensinar em 2022, virei mentora em 2024")
- **Resposta vaga:** "Sempre mexi com isso" → sondar: "Quando comecou? Sempre foi essa area? Teve mudanca de carreira?"
- **Campo JSON:** `historico.trajetoria_profissional` (texto livre + timeline estruturada)

### 1.7 Como chegou ate a Tata
- **Pergunta:** "Como voce chegou ate mim? Indicacao? Anuncio? Insta? Webinar?"
- **Por que:** entender canal de origem (CRO de aquisicao), grau de aquecimento, expectativa pre-formada.
- **Resposta boa:** "Vi o webinar que voce fez com a Renata em marco, segui o Insta, depois fiz o Q&A da Larissa e fechei"
- **Resposta vaga:** "Te conheci no Insta" → sondar: "Qual conteudo te puxou? Quanto tempo ja segue? Ja interagiu antes?"
- **Campo JSON:** `historico.canal_origem`, `historico.aquecimento_pre_compra` (frio/morno/quente)

### 1.8 Quem ela e em uma frase
- **Pergunta:** "Se voce tivesse que se descrever em UMA frase pra alguem que nunca te viu, o que voce diria?"
- **Por que:** auto-imagem, posicionamento interno, capacidade de sintese.
- **Resposta boa:** frase clara com substantivo + qualificador ("Sou advogada que ensina outras advogadas a viver de mentoria")
- **Resposta vaga:** "Sou eu" / "Difícil de explicar" → sondar: "Comeca com uma palavra. Se eu te apresentasse num evento, o que eu diria?"
- **Campo JSON:** `historico.auto_descricao_uma_frase`

**Criterio de qualidade do bloco 1:** 7 dos 8 campos preenchidos com resposta especifica. Se < 7, marcar bloco como `incompleto`.

---

## BLOCO 2 — NEGOCIO ATUAL (6 campos, 12 minutos)

**Abertura na call:**
> "Agora me conta do negocio. Sem polidez. Eu vou ouvir numero — e numero nao tem ego."

### 2.1 Tem negocio operando hoje?
- **Pergunta:** "Voce ja tem um negocio que gera receita hoje? Sim ou nao?"
- **Por que:** divide o universo em "construindo do zero" vs "otimizando existente".
- **Resposta boa:** sim/nao + meses de operacao
- **Resposta vaga:** "Tô comecando" → sondar: "Ja faturou alguma vez? Quanto?"
- **Campo JSON:** `negocio.tem_negocio` (boolean), `negocio.meses_operacao` (numero)

### 2.2 Faturamento medio dos ultimos 6 meses
- **Pergunta:** "Em media, quanto voce fatura por mes? Olhando os ultimos 6 meses."
- **Por que:** classificar estagio (sub-10k / 10-30k / 30-100k / 100k+) — base do `/perfil-mentorada`.
- **Resposta boa:** faixa especifica ("Entre R$25k e R$35k, com dois picos de R$50k")
- **Resposta vaga:** "Varia muito" / "Nao sei" → sondar: "Pior mes do ultimo semestre? Melhor mes? Roda na minha cabeca."
- **Faixas a usar:** `<10k`, `10-30k`, `30-100k`, `100-300k`, `300k+`
- **Campo JSON:** `negocio.faturamento_medio_6m` (faixa + valor exato se souber)

### 2.3 Tipo de negocio
- **Pergunta:** "Seu negocio e fisico, digital ou hibrido?"
- **Por que:** define stack, custo operacional, escalabilidade.
- **Opcoes:** fisico (loja, consultorio), digital (curso, mentoria, SaaS), hibrido (presencial + online)
- **Campo JSON:** `negocio.tipo` (fisico/digital/hibrido)

### 2.4 Produto/servico principal
- **Pergunta:** "Qual o produto ou servico que mais bota dinheiro pra dentro hoje? Nome, preco, formato."
- **Por que:** entender oferta-ancora, ticket medio, formato de entrega.
- **Resposta boa:** "Mentoria 1-a-1 trimestral, R$8.500, encontros semanais por Zoom + WhatsApp diario"
- **Resposta vaga:** "Tenho varias coisas" → sondar: "Pega a que mais vendeu mes passado. Essa."
- **Campo JSON:** `negocio.produto_principal` (objeto: nome, preco, formato, ticket_medio)

### 2.5 Audiencia (Insta, LinkedIn, lista, YouTube)
- **Pergunta:** "Onde voce tem audiencia hoje? Me da numeros."
- **Por que:** entender alavanca de aquisicao, dependencia de algoritmo, ativos digitais.
- **Resposta boa:** estrutura por canal: "Insta @carolmendes 18k seguidores, lista de email 2.300, LinkedIn 4k conexoes, YouTube nao"
- **Resposta vaga:** "Tenho insta" → sondar: "Quantos seguidores? Posta com que frequencia? Engajamento medio?"
- **Campo JSON:** `negocio.audiencia` (array de objetos: canal, handle, numero, engajamento)

### 2.6 Time atual
- **Pergunta:** "Voce trabalha sozinha ou tem time? Quem faz o que?"
- **Por que:** detectar gargalo pessoal (alerta), maturidade operacional, capacidade de delegacao.
- **Resposta boa:** "Tenho VA part-time pra agenda, social media freelancer pra reels, contadora terceirizada. Vendas e mentoria sou eu"
- **Resposta vaga:** "Tenho ajuda" → sondar: "Quantas pessoas? Sao CLT, PJ, freelancer? Quanto custa por mes?"
- **Campo JSON:** `negocio.time` (array: nome, papel, regime, custo_mensal)

**Criterio de qualidade do bloco 2:** todos os 6 campos preenchidos. Bloco 2 e CRITICO pra `/perfil-mentorada`.

---

## BLOCO 3 — TENTATIVAS ANTERIORES (4 campos, 8 minutos)

**Abertura na call:**
> "Esse bloco e ouro. Eu preciso saber o que voce ja tentou — pra eu nao te oferecer mais do mesmo. Sem vergonha. Tudo conta."

### 3.1 Mentorias e cursos ja feitos
- **Pergunta:** "Quais mentorias e cursos voce ja fez nos ultimos 3 anos? Quanto investiu, total?"
- **Por que:** medir nivel de informacao, deteccao de "vitima de curso", padroes de fuga.
- **Resposta boa:** lista com nome, mentor, valor, ano, resultado ("Mentoria do Erico Rocha 2022 — R$15k — montei minha primeira oferta. Curso da Camila Porto — R$2k — nao implementei")
- **Resposta vaga:** "Ja fiz alguns" → sondar: "Quais? Pega os 3 mais caros e mais marcantes. Bom ou ruim, conta."
- **Campo JSON:** `tentativas.mentorias_cursos` (array: nome, mentor, valor, ano, avaliacao_pos)
- **Campo JSON:** `tentativas.investimento_total_ultimos_3_anos`

### 3.2 Ferramentas de IA ja usadas
- **Pergunta:** "Quais ferramentas de IA voce usa ou ja tentou usar? ChatGPT, Inner AI, Squad, Notion AI, Claude, Midjourney?"
- **Por que:** medir maturidade tecnica, gap pra Travessia, calibrar `/imperatriz-bot` e `/imperio-agente`.
- **Resposta boa:** lista com ferramenta + uso atual + frustracao ("ChatGPT pago, uso pra copy de Insta, mas nao consigo fazer o tom soar meu. Inner AI testei, achei limitada")
- **Resposta vaga:** "Uso ChatGPT" → sondar: "Pra que? Com que frequencia? Pago ou gratis?"
- **Campo JSON:** `tentativas.ferramentas_ia` (array: nome, plano, uso_atual, frustracao)

### 3.3 O que funcionou
- **Pergunta:** "De tudo que voce ja tentou, o que REALMENTE funcionou? Pode ser pequeno."
- **Por que:** identificar fortalezas, padroes de execucao, ancorar plano em terreno familiar.
- **Resposta boa:** especifico ("Mentoria com Camila me fez postar todo dia por 60 dias — virei autoridade nicho")
- **Resposta vaga:** "Tudo um pouco" → sondar: "Cita 1 coisa. Mais marcante."
- **Campo JSON:** `tentativas.o_que_funcionou` (texto + tags)

### 3.4 O que NAO funcionou (e por que ela acha que nao)
- **Pergunta:** "E o que NAO funcionou? E na sua cabeca, por que?"
- **Por que:** entender narrativa interna de fracasso (auto-sabotagem? mentor errado? mercado?), evitar repetir.
- **Resposta boa:** "Lancamento de curso 2023 nao bombou — eu acho que era oferta fraca. Mas talvez tambem fosse meu medo de aparecer no IG"
- **Resposta vaga:** "Nada deu certo" → sondar: "Pega 1 coisa especifica. O que ela tinha que nao funcionou?"
- **Campo JSON:** `tentativas.o_que_nao_funcionou` (texto + auto_diagnostico_dela)

**Criterio de qualidade do bloco 3:** 3 dos 4 campos. Critico pra evitar repetir cemiterio.

---

## BLOCO 4 — DORES ESPECIFICAS (4 campos, 12 minutos) — **CRITICO**

**Abertura na call:**
> "Vamos pro pulo do gato: o que tira o seu sono. Sem polidez. Eu nao monto plano em cima de mentira educada."

### 4.1 Top 3 dores
- **Pergunta:** "Me da as 3 dores que mais te corroem hoje. Em ordem. A pior primeiro."
- **Por que:** alavancas emocionais do plano, prioridade de ataque, conexao Tata-mentorada na call.
- **Resposta boa:** 3 dores especificas e nomeadas ("1. Cansaco mental cronico de tomar todas as decisoes sozinha. 2. Faturamento estacionado em 30k ha 8 meses. 3. Sensacao que vou ser descoberta como fraude")
- **Resposta vaga:** "Tudo da errado" / "Estou perdida" → sondar com cada categoria:
  - **Operacional:** "Onde no dia-a-dia voce trava?"
  - **Financeiro:** "Quando olha o extrato, qual o pensamento?"
  - **Emocional:** "Quando voce chora ou tem ansiedade — sobre o que?"
  - **Relacional:** "Tem briga em casa por causa do trabalho?"
- **Campo JSON:** `dores.top_3` (array de 3 objetos: descricao, categoria, intensidade_1_10)

### 4.2 O que ela tem tentado fazer pra resolver
- **Pergunta:** "O que voce tem TENTADO pra resolver isso? Mesmo que nao tenha funcionado."
- **Por que:** medir nivel de acao vs paralisia, identificar repetidores de erro.
- **Resposta boa:** acoes concretas com tempo ("Faco terapia ha 1 ano, contratei 2 VAs e demiti as 2, comprei mentoria que abandonei no terceiro mes")
- **Resposta vaga:** "Tenho tentado" → sondar: "Tentado o que? Cita 1 acao."
- **Campo JSON:** `dores.tentativas_solucao` (array de objetos: acao, periodo, resultado)

### 4.3 Quanto tempo ela esta parada (estagnacao)
- **Pergunta:** "Ha quanto tempo voce esta SENTINDO essa mesma dor? Meses? Anos?"
- **Por que:** detectar `risco: estagnacao` (12+ meses = alerta alto), urgencia real.
- **Resposta boa:** numero claro ("18 meses no mesmo faturamento, 3 anos com sindrome do impostor")
- **Resposta vaga:** "Faz tempo" → sondar: "Mais de 6 meses? Mais de 1 ano?"
- **Campo JSON:** `dores.tempo_estagnacao` (objeto: dor, meses)

### 4.4 Custo emocional/financeiro de continuar parada
- **Pergunta:** "Se nada mudar nos proximos 12 meses, qual o custo? O que voce perde?"
- **Por que:** ancorar urgencia, gerar consciencia de oportunidade perdida, alavanca de execucao.
- **Resposta boa:** especifico ("Perco minha sanidade. Meu casamento entra em crise. E perco a janela de IA que vai fechar em 2 anos")
- **Resposta vaga:** "Continua igual" → sondar: "Igual NAO e neutro. O que se desgasta? Saude? Dinheiro? Casamento?"
- **Campo JSON:** `dores.custo_de_continuar_parada` (texto)

**Criterio de qualidade do bloco 4:** 4 de 4 campos OBRIGATORIOS. Sem dores top 3, anamnese nao fecha.

---

## BLOCO 5 — OBJETIVOS (4 campos, 10 minutos)

**Abertura na call:**
> "Agora a virada. Pra onde voce quer ir? Nao da pra montar plano sem destino."

### 5.1 Objetivo de curto prazo (90 dias)
- **Pergunta:** "Em 90 dias, qual o resultado MINIMO que voce quer ter alcancado pra dizer 'valeu a pena'?"
- **Por que:** ancora de execucao rapida, primeiro KPI da Travessia.
- **Resposta boa:** especifico + mensuravel ("Lancar minha primeira oferta high-ticket de R$15k e fechar 5 vendas")
- **Resposta vaga:** "Crescer" → sondar: "Crescer quanto? Em que? Me da numero."
- **Campo JSON:** `objetivos.curto_prazo_90d` (objeto: descricao, kpi, prazo)

### 5.2 Objetivo de medio prazo (12 meses)
- **Pergunta:** "Em 12 meses, onde voce QUER estar? Faturamento, time, posicionamento."
- **Por que:** norte da Travessia, ancora pra perfilamento (faturamento alvo).
- **Resposta boa:** "Faturando 100k/mes recorrente, com 3 pessoas no time, posicionada como referencia em mentoria juridica feminina"
- **Resposta vaga:** "Bem" → sondar: "Defina bem. 50k? 100k? 300k? Time de 1 ou de 5?"
- **Campo JSON:** `objetivos.medio_prazo_12m` (objeto: descricao, kpi_faturamento, kpi_time, kpi_posicionamento)

### 5.3 Objetivo de longo prazo (3-5 anos)
- **Pergunta:** "Em 3 a 5 anos, qual a versao maxima do teu imperio?"
- **Por que:** visao de imperio, ancorar decisoes maiores (parar de operar?, vender?, virar publica?).
- **Resposta boa:** narrativa concreta ("Quero ter escola online com 500+ alunas, sair da operacao 1-a-1, escrever um livro, falar em palco grande")
- **Resposta vaga:** "Sucesso" → sondar: "Como ele se PARECE? Voce ainda atende cliente? Tem time? Mora onde?"
- **Campo JSON:** `objetivos.longo_prazo_3_5a` (texto + tags)

### 5.4 Vida ideal (qualidade de vida + relacoes)
- **Pergunta:** "Conta a vida que voce quer ter — fora do trabalho. Como sao seus dias? Suas relacoes? Tua saude?"
- **Por que:** anamnese sem essa pergunta vira esteira de gado. Aqui a Tata humaniza o plano.
- **Resposta boa:** narrativa de dia ideal ("Acordo as 6, treino, levo as criancas pra escola, trabalho 4h profundas ate as 14h, almoco com o marido, dirijo pro consultorio 2x semana")
- **Resposta vaga:** "Mais tempo" → sondar: "Tempo pra que? Pra quem? Como sao tuas semanas?"
- **Campo JSON:** `objetivos.vida_ideal` (texto livre)

**Criterio de qualidade do bloco 5:** todos os 4 campos. Critico pra `/celeste`.

---

## BLOCO 6 — RECURSOS (4 campos, 8 minutos)

**Abertura na call:**
> "Pra eu nao te entregar plano de academia pra quem ta na UTI — preciso saber o que voce tem disponivel."

### 6.1 Tempo disponivel por semana
- **Pergunta:** "Quantas horas por semana voce CONSEGUE dedicar pra construir essa virada? Honesto."
- **Por que:** dimensionar plano, evitar overcommit, calibrar expectativa de velocidade.
- **Resposta boa:** numero realista ("8 horas por semana — 2h por dia em 4 dias")
- **Resposta vaga:** "Posso me dedicar" → sondar: "Em horas. 5? 10? 20?"
- **Campo JSON:** `recursos.tempo_semanal_horas` (numero + distribuicao)

### 6.2 Budget mensal pra investir alem da Travessia
- **Pergunta:** "Alem da Travessia, quanto voce pode investir POR MES em ferramentas, ads, gente?"
- **Por que:** dimensionar agressividade (ads sim/nao, ferramentas premium, contratacoes).
- **Resposta boa:** faixa ("R$3-5k/mes confortavel, ate R$10k se for retorno claro")
- **Resposta vaga:** "Depende" → sondar: "Hoje, sem aperto, R$1k? R$5k? R$10k?"
- **Faixas a usar:** `<1k`, `1-3k`, `3-10k`, `10-30k`, `30k+`
- **Campo JSON:** `recursos.budget_mensal_alem_travessia` (faixa + valor)

### 6.3 Equipe atual + capacidade de contratar
- **Pergunta:** "Quem voce tem hoje no time? E em 90 dias, voce CONSEGUE contratar mais alguem se precisar?"
- **Por que:** capacidade de delegar, alavanca de tempo, pre-condicao pra escalar.
- **Resposta boa:** "Tenho VA part-time. Em 90d posso contratar mais 1 PJ se for crucial"
- **Campo JSON:** `recursos.time_atual` (referencia bloco 2.6) + `recursos.capacidade_contratar_90d` (boolean + tipo)

### 6.4 Background tecnico
- **Pergunta:** "Voce e tecnica? Programa, mexe com Notion avancado, automacoes, Make, Zapier? Ou voce delega tudo isso?"
- **Por que:** calibrar trilha (mais hands-on vs mais delegacao), saber se vai usar `/imperio-agente` direto ou precisa de Severino.
- **Resposta boa:** "Sou intermediaria. Notion eu uso bem, automacao basica em Make, programar nao."
- **Niveis a usar:** `tecnica` / `intermediaria` / `delegadora`
- **Campo JSON:** `recursos.background_tecnico` (nivel + ferramentas_que_domina)

**Criterio de qualidade do bloco 6:** todos os 4 campos.

---

## BLOCO 7 — IDENTIDADE (5 campos, 8 minutos)

**Abertura na call:**
> "Agora a parte que e SO sua. Identidade nao se constroi com mentor — mas a gente pode lapidar."

### 7.1 Nicho especifico
- **Pergunta:** "Qual seu nicho? Especifico. Nao 'mulheres' — qual mulher?"
- **Por que:** base de toda copy, ads, posicionamento. Nicho amplo demais = morte.
- **Resposta boa:** "Advogadas mulheres de 30-45 anos com 5+ anos de carreira que querem virar mentora juridica"
- **Resposta vaga:** "Mulheres que querem empreender" → sondar 3x: "Que tipo de mulher? Profissao? Faixa etaria? Ja empreende ou nao?"
- **Campo JSON:** `identidade.nicho_especifico` (texto + tags: profissao, idade, momento_carreira)

### 7.2 Posicionamento percebido (como o mercado a ve)
- **Pergunta:** "Como voce ACHA que o mercado te ve hoje? Em uma frase."
- **Por que:** detectar gap entre auto-imagem e percepcao real, ancorar reposicionamento se preciso.
- **Resposta boa:** especifico ("Me veem como advogada que ensina rede social — o que e meio injusto, eu ensino mentoria")
- **Resposta vaga:** "Nao sei" → sondar: "Quando alguem te indica, o que fala?"
- **Campo JSON:** `identidade.posicionamento_percebido`

### 7.3 Diferencial percebido (o que ela acha que a torna unica)
- **Pergunta:** "O que voce acha que voce faz DIFERENTE de todo mundo no teu nicho?"
- **Por que:** materia-prima pra `/mecanismo-unico`, ancorar diferencial real.
- **Resposta boa:** "Sou a unica advogada que junta 8 anos de processo + 4 anos de mentoria. Combino tecnica juridica com pedagogia de adulto"
- **Resposta vaga:** "Sou eu mesma" → sondar: "O que voce explica diferente? Que metafora voce usa? Que ordem?"
- **Campo JSON:** `identidade.diferencial_percebido`

### 7.4 Voz e tom atual
- **Pergunta:** "Como voce fala no Insta hoje? Engracada? Tecnica? Acolhedora? Provocadora?"
- **Por que:** input pra `/voz-humana-br` e calibragem de copy.
- **Resposta boa:** "Acolhedora com pitada provocadora. Falo de voce, uso 'irma', tiro sarro de mim mesma."
- **Campo JSON:** `identidade.voz_tom_atual` (tags + descricao)

### 7.5 Tres palavras/expressoes que sao a cara dela
- **Pergunta:** "Tres palavras ou expressoes que voce SEMPRE usa, que sao tua cara?"
- **Por que:** input pra `/voz-humana-br` e formacao de bordoes.
- **Resposta boa:** "Vamos juntas, corre comigo, sem firula"
- **Campo JSON:** `identidade.expressoes_assinatura` (array)

**Criterio de qualidade do bloco 7:** 4 dos 5 campos.

---

## BLOCO 8 — EXPECTATIVAS (3 campos, 8 minutos) — **CRITICO**

**Abertura na call:**
> "Ultimo bloco. O que voce ESPERA de mim em 6 meses? Vai fundo. Ninguem mais le isso alem de mim."

### 8.1 O que espera da Travessia (resultado concreto)
- **Pergunta:** "No final dos 6 meses comigo, o que voce quer estar OLHANDO no espelho? Resultado concreto."
- **Por que:** alinhamento de expectativa, base do contrato emocional, deteccao de `risco: expectativa_irrealista`.
- **Resposta boa:** mensuravel + emocional ("Faturamento triplicado pra 90k/mes, time de 3 pessoas, eu trabalhando 25h/semana, dormindo bem")
- **Resposta vaga:** "Mudar de vida" → sondar: "Mudar como? Em numero. Em rotina."
- **Sinais de alerta:**
  - "Quero faturar 1M nos primeiros 90 dias" → `risco: expectativa_irrealista`
  - "Quero que voce faca por mim" → `risco: alinhamento` (Tata nao executa)
- **Campo JSON:** `expectativas.resultado_concreto_6m`, `expectativas.alertas_detectados`

### 8.2 O que mais a anima
- **Pergunta:** "O que mais te ANIMA nessa Travessia? O que voce ja nao aguenta de empolgada?"
- **Por que:** ancora emocional positiva, motor de execucao em momento dificil.
- **Resposta boa:** "Me anima ter tu como referencia perto, e me anima criar minha primeira oferta high-ticket de verdade"
- **Resposta vaga:** "Tudo" → sondar: "Pega 1. O mais forte."
- **Campo JSON:** `expectativas.o_que_anima` (texto)

### 8.3 Maior receio
- **Pergunta:** "E o maior MEDO? O que voce teme? Pode ser sobre voce, sobre mim, sobre o processo."
- **Por que:** materia-prima pra trabalhar resistencias, antecipa pontos de drop-out.
- **Resposta boa:** "Tenho medo de gastar essa grana e nao implementar nada. E medo de descobrir que sou pior do que penso"
- **Resposta vaga:** "Nenhum" → sondar: "Vou insistir. Mesmo pequenino. Algo te coca."
- **Campo JSON:** `expectativas.maior_receio` (texto + tags: financeiro, identitario, relacional)

**Criterio de qualidade do bloco 8:** 3 de 3 campos OBRIGATORIOS. Sem expectativas claras, anamnese nao fecha.

---

## RESUMO DE QUALIDADE GERAL

| Bloco                    | Min Campos | Critico? | Tempo |
|--------------------------|------------|----------|-------|
| 1. Historico pessoal     | 7/8        | Sim      | 8min  |
| 2. Negocio atual         | 6/6        | Sim      | 12min |
| 3. Tentativas anteriores | 3/4        | Medio    | 8min  |
| 4. Dores especificas     | **4/4**    | CRITICO  | 12min |
| 5. Objetivos             | 4/4        | Sim      | 10min |
| 6. Recursos              | 4/4        | Medio    | 8min  |
| 7. Identidade            | 4/5        | Sim      | 8min  |
| 8. Expectativas          | **3/3**    | CRITICO  | 8min  |

**Score de completude:**
- 90-100% campos = `pronto` (rodar `/perfil-mentorada`)
- 70-89% = `quase` (rodar `--validar`, fechar gaps)
- < 70% = `incompleto` (refazer bloco)

---

## REGRA DE OURO: SONDAGEM

A diferenca entre anamnese mediocre e anamnese nota 1000 esta na **sondagem**. Quando a mentorada responde vago, a Tata (ou a skill) sonda. Sempre.

Padroes de sondagem:
- **Especificacao:** "Especifica. Numero, prazo, nome."
- **Exemplo:** "Da um exemplo concreto da ultima vez que isso aconteceu."
- **Contraste:** "Comparado ao que? Comparado a 6 meses atras, ta melhor ou pior?"
- **Categorizacao:** "Isso e operacional, financeiro, emocional ou relacional?"
- **Cronometragem:** "Ha quanto tempo? Semanas, meses, anos?"
- **Reflexao:** "Por que voce acha que isso acontece?"

Sem sondagem, anamnese vira formulario de banco. Com sondagem, vira diagnostico medico.

---

**Metodo Imperatriz de Anamnese — propriedade Tata Goncalves.**
