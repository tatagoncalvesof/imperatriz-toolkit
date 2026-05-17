# Formulario HTML — Anamnese Travessia Imperatriz

Quando a skill roda em `--formulario`, ela gera **um arquivo HTML standalone** (zero dependencia externa, funciona offline) com voz Tata, 8 blocos navegaveis, validacao basica e botao "exportar JSON" no final.

A mentorada baixa, preenche em 30-50 minutos, exporta o JSON e devolve por WhatsApp/email pra Tata. Tata roda `/anamnese-mentorada --validar` no JSON recebido.

**Caminho de salvamento:**
```
~/imperio/mentoradas/[slug]/formulario.html
```

---

## DIRETRIZES DE VOZ TATA NO FORMULARIO

A mentorada esta **lendo a Tata**. Nao e formulario asseptico. E provocativo, direto, intimo.

**Faz:**
- Tutea ("voce", nunca "a senhora")
- Provoca sem agredir ("sem polidez", "vai fundo", "sem firula")
- Reconhece o desconforto ("eu sei que essa pergunta e dificil")
- Promete sigilo ("ninguem mais le isso alem de mim")
- Usa expressoes de proximidade ("irma", "minha querida")
- Frases curtas. Pontuacao firme.

**Nao faz:**
- Linguagem juridica ("informe", "no campo abaixo")
- Burocratico ("preencha todos os campos obrigatorios")
- Generico ("seu feedback e importante pra nos")
- Emoji em excesso (1-2 por bloco maximo)

---

## TEMPLATE HTML COMPLETO

Salvar como `formulario.html` na pasta da mentorada. Substituir `{NOME_MENTORADA}` antes de enviar.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Anamnese Travessia Imperatriz — Tata Goncalves</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background: #0a0a0a;
    color: #f4f4f4;
    line-height: 1.65;
    min-height: 100vh;
    padding: 0;
  }
  .container {
    max-width: 720px;
    margin: 0 auto;
    padding: 60px 32px 100px;
  }
  header {
    border-bottom: 1px solid #2a2a2a;
    padding-bottom: 32px;
    margin-bottom: 40px;
  }
  .brand {
    font-size: 11px;
    letter-spacing: 3px;
    color: #c9a961;
    text-transform: uppercase;
    margin-bottom: 12px;
  }
  h1 {
    font-size: 32px;
    font-weight: 600;
    line-height: 1.2;
    margin-bottom: 16px;
    color: #fff;
  }
  .intro {
    font-size: 17px;
    color: #c4c4c4;
    margin-bottom: 8px;
  }
  .progress {
    position: sticky;
    top: 0;
    background: #0a0a0a;
    padding: 16px 0;
    z-index: 10;
    margin-bottom: 32px;
    border-bottom: 1px solid #1f1f1f;
  }
  .progress-bar {
    height: 4px;
    background: #1f1f1f;
    border-radius: 2px;
    overflow: hidden;
  }
  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #c9a961, #e6c478);
    transition: width 0.3s;
    width: 0%;
  }
  .progress-text {
    font-size: 12px;
    color: #888;
    margin-top: 8px;
    letter-spacing: 1px;
  }
  .bloco {
    margin-bottom: 56px;
    padding: 32px;
    background: #131313;
    border-radius: 12px;
    border: 1px solid #1f1f1f;
  }
  .bloco-numero {
    font-size: 12px;
    color: #c9a961;
    letter-spacing: 2px;
    margin-bottom: 8px;
  }
  .bloco-titulo {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 16px;
    color: #fff;
  }
  .bloco-abertura {
    font-style: italic;
    color: #c4c4c4;
    margin-bottom: 32px;
    padding-left: 16px;
    border-left: 3px solid #c9a961;
  }
  .pergunta {
    margin-bottom: 28px;
  }
  .pergunta-label {
    display: block;
    font-size: 16px;
    font-weight: 500;
    margin-bottom: 8px;
    color: #f4f4f4;
  }
  .pergunta-hint {
    font-size: 13px;
    color: #888;
    margin-bottom: 12px;
    font-style: italic;
  }
  input[type="text"],
  input[type="number"],
  input[type="email"],
  select,
  textarea {
    width: 100%;
    padding: 14px 16px;
    font-size: 15px;
    background: #0a0a0a;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    color: #f4f4f4;
    font-family: inherit;
    transition: border 0.2s;
  }
  input:focus, select:focus, textarea:focus {
    outline: none;
    border-color: #c9a961;
  }
  textarea {
    min-height: 100px;
    resize: vertical;
  }
  .radio-group, .checkbox-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .radio-item, .checkbox-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 14px;
    background: #0a0a0a;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    cursor: pointer;
  }
  .radio-item:hover, .checkbox-item:hover {
    border-color: #c9a961;
  }
  .alerta-bloco {
    background: rgba(201, 169, 97, 0.08);
    border: 1px solid rgba(201, 169, 97, 0.3);
    padding: 16px;
    border-radius: 8px;
    font-size: 14px;
    color: #c9a961;
    margin-bottom: 16px;
  }
  .actions {
    margin-top: 48px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  button {
    padding: 18px 32px;
    font-size: 16px;
    font-weight: 600;
    background: #c9a961;
    color: #0a0a0a;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-family: inherit;
    transition: background 0.2s;
  }
  button:hover {
    background: #e6c478;
  }
  button.secondary {
    background: transparent;
    color: #c9a961;
    border: 1px solid #c9a961;
  }
  .footer {
    margin-top: 60px;
    padding-top: 32px;
    border-top: 1px solid #2a2a2a;
    font-size: 12px;
    color: #666;
    text-align: center;
    letter-spacing: 1px;
  }
  .preview {
    margin-top: 32px;
    padding: 20px;
    background: #0a0a0a;
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    font-family: ui-monospace, monospace;
    font-size: 12px;
    color: #888;
    max-height: 300px;
    overflow-y: auto;
    white-space: pre-wrap;
    word-break: break-word;
    display: none;
  }
  .preview.visible { display: block; }
  @media (max-width: 600px) {
    .container { padding: 40px 20px 80px; }
    h1 { font-size: 26px; }
    .bloco { padding: 24px 20px; }
  }
</style>
</head>
<body>

<div class="container">

<header>
  <div class="brand">TRAVESSIA IMPERATRIZ — TATA GONCALVES</div>
  <h1>Oi, mentorada nova. Senta aqui que eu vou te conhecer de verdade.</h1>
  <p class="intro">Antes de qualquer plano, eu preciso entender quem voce e — nao quem voce escreve no Insta.</p>
  <p class="intro">Sao 8 blocos. Tira 30 a 50 minutos. Responde com calma. Sem polidez. Eu nao monto plano em cima de mentira educada.</p>
  <p class="intro">Quando terminar, clica em <strong>Exportar minha anamnese</strong> la embaixo, baixa o arquivo e me manda no WhatsApp. Combinado?</p>
</header>

<div class="progress">
  <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
  <div class="progress-text" id="progressText">0 / 37 perguntas respondidas</div>
</div>

<form id="anamneseForm">

<!-- BLOCO 1 — HISTORICO PESSOAL -->
<section class="bloco" data-bloco="1">
  <div class="bloco-numero">BLOCO 1 DE 8</div>
  <h2 class="bloco-titulo">Quem voce e</h2>
  <p class="bloco-abertura">"Antes de qualquer plano, eu preciso entender quem voce e — nao quem voce escreve no Insta. Me conta sua historia rapidinha."</p>

  <div class="pergunta">
    <label class="pergunta-label">Qual seu nome completo?</label>
    <input type="text" name="nome_completo" required>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Quantos anos voce tem?</label>
    <input type="number" name="idade" min="18" max="99" required>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Onde voce mora hoje? (cidade e estado)</label>
    <input type="text" name="localizacao" placeholder="Ex: Curitiba — PR" required>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Estado civil</label>
    <select name="estado_civil" required>
      <option value="">Escolhe uma opcao</option>
      <option value="solteira">Solteira</option>
      <option value="casada">Casada</option>
      <option value="uniao_estavel">Uniao estavel</option>
      <option value="divorciada">Divorciada</option>
      <option value="viuva">Viuva</option>
      <option value="prefiro_nao_dizer">Prefiro nao dizer</option>
    </select>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Tem filhos? Se sim, quantos e que idades?</label>
    <p class="pergunta-hint">Ex: "Dois, 8 e 12 anos" ou "Nao tenho"</p>
    <input type="text" name="filhos">
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Qual sua formacao? Onde voce estudou?</label>
    <p class="pergunta-hint">Ex: "Direito pela PUC-PR, MBA em Gestao pela FGV"</p>
    <textarea name="formacao" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Me conta em 2 minutos sua trajetoria — desde a primeira vez que voce ganhou dinheiro ate agora.</label>
    <p class="pergunta-hint">Sem ediar. Pode ser tipo "Trabalhei 8 anos como X, abri Y em 2019, virei Z em 2024".</p>
    <textarea name="trajetoria_profissional" rows="5" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Como voce chegou ate mim?</label>
    <p class="pergunta-hint">Indicacao? Anuncio? Insta? Webinar? Quem te falou de mim?</p>
    <textarea name="canal_origem" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Se voce tivesse que se descrever em UMA frase pra alguem que nunca te viu, o que voce diria?</label>
    <p class="pergunta-hint">Ex: "Sou advogada que ensina outras advogadas a viver de mentoria"</p>
    <input type="text" name="auto_descricao_uma_frase" required>
  </div>
</section>

<!-- BLOCO 2 — NEGOCIO ATUAL -->
<section class="bloco" data-bloco="2">
  <div class="bloco-numero">BLOCO 2 DE 8</div>
  <h2 class="bloco-titulo">Onde voce esta hoje no negocio</h2>
  <p class="bloco-abertura">"Agora me conta do negocio. Sem polidez. Eu vou ouvir numero — e numero nao tem ego."</p>

  <div class="pergunta">
    <label class="pergunta-label">Voce ja tem um negocio que gera receita hoje?</label>
    <select name="tem_negocio" required>
      <option value="">Escolhe</option>
      <option value="sim">Sim</option>
      <option value="comecando">Comecando (ja faturou pouco)</option>
      <option value="nao">Nao tenho ainda</option>
    </select>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Ha quantos meses ele opera?</label>
    <input type="number" name="meses_operacao" min="0">
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Em media, quanto voce fatura por mes? (ultimos 6 meses)</label>
    <p class="pergunta-hint">Faixa serve. Pior mes e melhor mes ajudam.</p>
    <select name="faturamento_faixa" required>
      <option value="">Escolhe a faixa</option>
      <option value="<10k">Menos de R$10k/mes</option>
      <option value="10-30k">R$10k a R$30k/mes</option>
      <option value="30-100k">R$30k a R$100k/mes</option>
      <option value="100-300k">R$100k a R$300k/mes</option>
      <option value="300k+">R$300k+/mes</option>
    </select>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Pior mes e melhor mes do ultimo semestre? (em R$)</label>
    <input type="text" name="faturamento_pior_melhor" placeholder="Ex: pior R$18k, melhor R$52k">
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Seu negocio e:</label>
    <select name="tipo_negocio">
      <option value="">Escolhe</option>
      <option value="fisico">Fisico (loja, consultorio, escritorio)</option>
      <option value="digital">Digital (curso, mentoria, SaaS)</option>
      <option value="hibrido">Hibrido (presencial + online)</option>
    </select>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Qual o produto/servico que mais bota dinheiro pra dentro hoje?</label>
    <p class="pergunta-hint">Nome, preco, formato. Ex: "Mentoria 1-a-1 trimestral, R$8.500, encontros semanais Zoom"</p>
    <textarea name="produto_principal" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Onde voce tem audiencia hoje? Me da numeros.</label>
    <p class="pergunta-hint">Ex: "Insta @carolmendes 18k seguidores, lista email 2.300, LinkedIn 4k, YouTube nao"</p>
    <textarea name="audiencia" rows="3" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Voce trabalha sozinha ou tem time? Quem faz o que e quanto custa?</label>
    <p class="pergunta-hint">Ex: "VA part-time R$1.500/mes, social media freelancer R$2k/mes. Vendas e mentoria sou eu."</p>
    <textarea name="time" rows="3" required></textarea>
  </div>
</section>

<!-- BLOCO 3 — TENTATIVAS ANTERIORES -->
<section class="bloco" data-bloco="3">
  <div class="bloco-numero">BLOCO 3 DE 8</div>
  <h2 class="bloco-titulo">O que voce ja tentou antes</h2>
  <p class="bloco-abertura">"Esse bloco e ouro. Eu preciso saber o que voce ja tentou — pra eu nao te oferecer mais do mesmo. Sem vergonha. Tudo conta."</p>

  <div class="pergunta">
    <label class="pergunta-label">Quais mentorias e cursos voce ja fez nos ultimos 3 anos?</label>
    <p class="pergunta-hint">Lista o nome, mentor, valor e o que aconteceu. Ex: "Erico Rocha 2022 R$15k — montei oferta. Camila Porto R$2k — abandonei."</p>
    <textarea name="mentorias_cursos" rows="5" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Investimento total nos ultimos 3 anos em educacao? (aproximado)</label>
    <input type="text" name="investimento_total" placeholder="Ex: R$38.000">
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Quais ferramentas de IA voce usa ou ja tentou?</label>
    <p class="pergunta-hint">ChatGPT? Inner AI? Claude? Notion AI? Squad? Midjourney? Pra que usa cada uma e qual frustracao?</p>
    <textarea name="ferramentas_ia" rows="3"></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">De tudo que voce ja tentou, o que REALMENTE funcionou?</label>
    <p class="pergunta-hint">Pode ser pequeno. Cita ate 3 coisas.</p>
    <textarea name="o_que_funcionou" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">E o que NAO funcionou? Na sua cabeca, por que?</label>
    <p class="pergunta-hint">Ate 3 coisas. Conta pq voce ACHA que nao deu certo.</p>
    <textarea name="o_que_nao_funcionou" required></textarea>
  </div>
</section>

<!-- BLOCO 4 — DORES (CRITICO) -->
<section class="bloco" data-bloco="4">
  <div class="bloco-numero">BLOCO 4 DE 8 — O MAIS IMPORTANTE</div>
  <h2 class="bloco-titulo">O que tira o seu sono</h2>
  <p class="bloco-abertura">"Vamos pro pulo do gato: o que tira o seu sono. Sem polidez. Eu nao monto plano em cima de mentira educada."</p>

  <div class="alerta-bloco">
    Esse bloco e CRITICO. Sem voce articular suas dores, eu nao consigo te ajudar de verdade. Vai fundo. Ninguem mais le isso alem de mim.
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Dor #1 — a pior. Aquela que mais te corroi.</label>
    <p class="pergunta-hint">Especifica. Ex: "Cansaco mental cronico de tomar todas as decisoes sozinha"</p>
    <textarea name="dor_1" required></textarea>
    <label class="pergunta-label" style="margin-top:8px;">Categoria:</label>
    <select name="dor_1_categoria" required>
      <option value="">Escolhe</option>
      <option value="operacional">Operacional</option>
      <option value="financeiro">Financeiro</option>
      <option value="emocional">Emocional</option>
      <option value="identitario">Identitario (medo, sindrome impostor)</option>
      <option value="relacional">Relacional (familia, casamento)</option>
      <option value="saude">Saude</option>
      <option value="tempo">Tempo</option>
    </select>
    <label class="pergunta-label" style="margin-top:8px;">Intensidade (1-10):</label>
    <input type="number" name="dor_1_intensidade" min="1" max="10" required>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Dor #2</label>
    <textarea name="dor_2" required></textarea>
    <select name="dor_2_categoria" required style="margin-top:8px;">
      <option value="">Escolhe categoria</option>
      <option value="operacional">Operacional</option>
      <option value="financeiro">Financeiro</option>
      <option value="emocional">Emocional</option>
      <option value="identitario">Identitario</option>
      <option value="relacional">Relacional</option>
      <option value="saude">Saude</option>
      <option value="tempo">Tempo</option>
    </select>
    <input type="number" name="dor_2_intensidade" min="1" max="10" placeholder="Intensidade 1-10" style="margin-top:8px;" required>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Dor #3</label>
    <textarea name="dor_3" required></textarea>
    <select name="dor_3_categoria" required style="margin-top:8px;">
      <option value="">Escolhe categoria</option>
      <option value="operacional">Operacional</option>
      <option value="financeiro">Financeiro</option>
      <option value="emocional">Emocional</option>
      <option value="identitario">Identitario</option>
      <option value="relacional">Relacional</option>
      <option value="saude">Saude</option>
      <option value="tempo">Tempo</option>
    </select>
    <input type="number" name="dor_3_intensidade" min="1" max="10" placeholder="Intensidade 1-10" style="margin-top:8px;" required>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">O que voce TEM TENTADO fazer pra resolver essas dores?</label>
    <p class="pergunta-hint">Mesmo que nao tenha funcionado. Acoes concretas com tempo. Ex: "Faco terapia ha 1 ano, contratei e demiti 2 VAs..."</p>
    <textarea name="tentativas_solucao" rows="4" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Ha quanto tempo voce esta SENTINDO essas dores?</label>
    <p class="pergunta-hint">Meses ou anos. Pode ser por dor.</p>
    <input type="text" name="tempo_estagnacao" required>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Se nada mudar nos proximos 12 meses, qual o custo? O que voce perde?</label>
    <p class="pergunta-hint">Sanidade? Casamento? Janela de oportunidade? Filhos crescem sem voce?</p>
    <textarea name="custo_continuar_parada" rows="3" required></textarea>
  </div>
</section>

<!-- BLOCO 5 — OBJETIVOS -->
<section class="bloco" data-bloco="5">
  <div class="bloco-numero">BLOCO 5 DE 8</div>
  <h2 class="bloco-titulo">Pra onde voce quer ir</h2>
  <p class="bloco-abertura">"Agora a virada. Pra onde voce quer ir? Nao da pra montar plano sem destino."</p>

  <div class="pergunta">
    <label class="pergunta-label">Em 90 dias, qual o resultado MINIMO pra voce dizer "valeu a pena"?</label>
    <p class="pergunta-hint">Especifico + mensuravel. Ex: "Lancar minha primeira oferta high-ticket de R$15k e fechar 5 vendas"</p>
    <textarea name="objetivo_90d" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Em 12 meses, onde voce QUER estar?</label>
    <p class="pergunta-hint">Faturamento, time, posicionamento. Ex: "100k/mes recorrente, time de 3, referencia em mentoria juridica feminina"</p>
    <textarea name="objetivo_12m" rows="3" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Em 3 a 5 anos, qual a versao maxima do teu imperio?</label>
    <p class="pergunta-hint">Como se parece? Voce ainda atende cliente? Tem time grande? Mora onde? Tem livro? Palco?</p>
    <textarea name="objetivo_5a" rows="4" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Conta a vida que voce quer ter — fora do trabalho.</label>
    <p class="pergunta-hint">Como sao seus dias? Suas relacoes? Tua saude? Como acorda? Como dorme?</p>
    <textarea name="vida_ideal" rows="5" required></textarea>
  </div>
</section>

<!-- BLOCO 6 — RECURSOS -->
<section class="bloco" data-bloco="6">
  <div class="bloco-numero">BLOCO 6 DE 8</div>
  <h2 class="bloco-titulo">O que voce tem disponivel</h2>
  <p class="bloco-abertura">"Pra eu nao te entregar plano de academia pra quem ta na UTI — preciso saber o que voce tem disponivel."</p>

  <div class="pergunta">
    <label class="pergunta-label">Quantas horas por semana voce CONSEGUE dedicar pra construir essa virada? (honesto)</label>
    <input type="number" name="tempo_semanal_horas" min="1" max="80" required>
    <input type="text" name="tempo_distribuicao" placeholder="Ex: 2h/dia em 4 dias uteis" style="margin-top:8px;">
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Alem da Travessia, quanto voce pode investir POR MES em ferramentas, ads, gente?</label>
    <select name="budget_faixa" required>
      <option value="">Escolhe</option>
      <option value="<1k">Menos de R$1k/mes</option>
      <option value="1-3k">R$1k a R$3k/mes</option>
      <option value="3-10k">R$3k a R$10k/mes</option>
      <option value="10-30k">R$10k a R$30k/mes</option>
      <option value="30k+">R$30k+/mes</option>
    </select>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Em 90 dias, voce CONSEGUE contratar mais alguem se precisar?</label>
    <select name="capacidade_contratar" required>
      <option value="">Escolhe</option>
      <option value="sim_pj">Sim, PJ part-time</option>
      <option value="sim_freelancer">Sim, freelancer pontual</option>
      <option value="sim_clt">Sim, CLT full</option>
      <option value="talvez">Talvez, depende do retorno</option>
      <option value="nao">Nao, sem condicao agora</option>
    </select>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Voce e tecnica?</label>
    <p class="pergunta-hint">Programa? Mexe com Notion avancado, Make/Zapier? Ou prefere delegar tudo isso?</p>
    <select name="background_tecnico" required>
      <option value="">Escolhe</option>
      <option value="tecnica">Tecnica (programo, automacoes complexas)</option>
      <option value="intermediaria">Intermediaria (Notion, Make basico, ChatGPT)</option>
      <option value="delegadora">Delegadora (prefere terceirizar tudo tecnico)</option>
    </select>
    <textarea name="ferramentas_dominadas" placeholder="Quais ferramentas voce realmente domina?" style="margin-top:8px;" rows="2"></textarea>
  </div>
</section>

<!-- BLOCO 7 — IDENTIDADE -->
<section class="bloco" data-bloco="7">
  <div class="bloco-numero">BLOCO 7 DE 8</div>
  <h2 class="bloco-titulo">Quem voce e no mercado</h2>
  <p class="bloco-abertura">"Agora a parte que e SO sua. Identidade nao se constroi com mentor — mas a gente pode lapidar."</p>

  <div class="pergunta">
    <label class="pergunta-label">Qual seu nicho? Especifico. Nao "mulheres" — qual mulher?</label>
    <p class="pergunta-hint">Ex: "Advogadas de 30-45 anos com 5+ anos de carreira que querem virar mentora juridica"</p>
    <textarea name="nicho_especifico" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Como voce ACHA que o mercado te ve hoje? Em uma frase.</label>
    <input type="text" name="posicionamento_percebido" required>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">O que voce faz DIFERENTE de todo mundo no teu nicho?</label>
    <p class="pergunta-hint">Vai fundo. Pode ser metodologia, ordem, metafora, combinacao de skills.</p>
    <textarea name="diferencial_percebido" rows="3" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">Como voce fala no Insta hoje?</label>
    <p class="pergunta-hint">Engracada? Tecnica? Acolhedora? Provocadora? Mistura?</p>
    <textarea name="voz_tom_atual" rows="2" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">3 palavras ou expressoes que voce SEMPRE usa, que sao tua cara:</label>
    <input type="text" name="expressao_1" placeholder="Expressao 1" required>
    <input type="text" name="expressao_2" placeholder="Expressao 2" style="margin-top:8px;" required>
    <input type="text" name="expressao_3" placeholder="Expressao 3" style="margin-top:8px;" required>
  </div>
</section>

<!-- BLOCO 8 — EXPECTATIVAS (CRITICO) -->
<section class="bloco" data-bloco="8">
  <div class="bloco-numero">BLOCO 8 DE 8 — O ULTIMO E O MAIS HONESTO</div>
  <h2 class="bloco-titulo">O que voce espera de mim</h2>
  <p class="bloco-abertura">"Ultimo bloco. O que voce ESPERA de mim em 6 meses? Vai fundo. Ninguem mais le isso alem de mim."</p>

  <div class="alerta-bloco">
    Aqui nao tem resposta certa. Tem resposta verdadeira. Esse bloco define se a gente vai ter sucesso juntas.
  </div>

  <div class="pergunta">
    <label class="pergunta-label">No final dos 6 meses comigo, o que voce quer estar OLHANDO no espelho? Resultado concreto.</label>
    <p class="pergunta-hint">Mensuravel + emocional. Faturamento, time, rotina, sentimento.</p>
    <textarea name="resultado_concreto_6m" rows="5" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">O que mais te ANIMA nessa Travessia? O que voce ja nao aguenta de empolgada?</label>
    <textarea name="o_que_anima" rows="3" required></textarea>
  </div>

  <div class="pergunta">
    <label class="pergunta-label">E o maior MEDO? O que voce teme?</label>
    <p class="pergunta-hint">Pode ser sobre voce, sobre mim, sobre o processo. Mesmo pequeno.</p>
    <textarea name="maior_receio" rows="4" required></textarea>
  </div>
</section>

<div class="actions">
  <button type="button" id="exportarBtn">Exportar minha anamnese</button>
  <button type="button" class="secondary" id="previewBtn">Ver previa do que vou enviar</button>
</div>

<div class="preview" id="previewBox"></div>

</form>

<div class="footer">
  TRAVESSIA IMPERATRIZ &middot; ANAMNESE V1.0 &middot; TATA GONCALVES 2026<br>
  Tudo que voce escreveu fica APENAS no seu computador ate voce me enviar.
</div>

</div>

<script>
const form = document.getElementById('anamneseForm');
const exportarBtn = document.getElementById('exportarBtn');
const previewBtn = document.getElementById('previewBtn');
const previewBox = document.getElementById('previewBox');
const progressFill = document.getElementById('progressFill');
const progressText = document.getElementById('progressText');

const TOTAL_PERGUNTAS = 37;

function calcularProgresso() {
  const inputs = form.querySelectorAll('input, textarea, select');
  let preenchidas = 0;
  inputs.forEach(i => {
    if (i.value && i.value.trim() !== '') preenchidas++;
  });
  const pct = Math.min(100, Math.round((preenchidas / TOTAL_PERGUNTAS) * 100));
  progressFill.style.width = pct + '%';
  progressText.textContent = preenchidas + ' / ' + TOTAL_PERGUNTAS + ' campos respondidos (' + pct + '%)';
}

form.addEventListener('input', calcularProgresso);
form.addEventListener('change', calcularProgresso);

function montarJSON() {
  const data = new FormData(form);
  const obj = {};
  for (const [key, value] of data.entries()) {
    obj[key] = value;
  }

  return {
    schema_versao: "1.0",
    skill_versao: "anamnese-mentorada-1.0",
    slug: (obj.nome_completo || 'mentorada').toLowerCase()
      .normalize('NFD').replace(/[̀-ͯ]/g, '')
      .replace(/[^a-z0-9\s]/g, '').trim().replace(/\s+/g, '-'),
    data_coleta: new Date().toISOString().slice(0, 10),
    data_atualizacao: new Date().toISOString().slice(0, 10),
    coletado_por: "formulario",
    responsavel_coleta: "mentorada",
    historico: {
      nome_completo: obj.nome_completo,
      idade: parseInt(obj.idade) || null,
      localizacao: obj.localizacao,
      estado_civil: obj.estado_civil,
      filhos: obj.filhos,
      formacao: obj.formacao,
      trajetoria_profissional: obj.trajetoria_profissional,
      canal_origem: obj.canal_origem,
      auto_descricao_uma_frase: obj.auto_descricao_uma_frase
    },
    negocio: {
      tem_negocio: obj.tem_negocio,
      meses_operacao: parseInt(obj.meses_operacao) || null,
      faturamento_medio_6m: {
        faixa: obj.faturamento_faixa,
        pior_e_melhor_mes: obj.faturamento_pior_melhor
      },
      tipo: obj.tipo_negocio,
      produto_principal: obj.produto_principal,
      audiencia: obj.audiencia,
      time: obj.time
    },
    tentativas: {
      mentorias_cursos: obj.mentorias_cursos,
      investimento_total_ultimos_3_anos: obj.investimento_total,
      ferramentas_ia: obj.ferramentas_ia,
      o_que_funcionou: obj.o_que_funcionou,
      o_que_nao_funcionou: obj.o_que_nao_funcionou
    },
    dores: {
      top_3: [
        { ranking: 1, descricao: obj.dor_1, categoria: obj.dor_1_categoria, intensidade_1_10: parseInt(obj.dor_1_intensidade) },
        { ranking: 2, descricao: obj.dor_2, categoria: obj.dor_2_categoria, intensidade_1_10: parseInt(obj.dor_2_intensidade) },
        { ranking: 3, descricao: obj.dor_3, categoria: obj.dor_3_categoria, intensidade_1_10: parseInt(obj.dor_3_intensidade) }
      ],
      tentativas_solucao: obj.tentativas_solucao,
      tempo_estagnacao: obj.tempo_estagnacao,
      custo_de_continuar_parada: obj.custo_continuar_parada
    },
    objetivos: {
      curto_prazo_90d: obj.objetivo_90d,
      medio_prazo_12m: obj.objetivo_12m,
      longo_prazo_3_5a: obj.objetivo_5a,
      vida_ideal: obj.vida_ideal
    },
    recursos: {
      tempo_semanal_horas: parseInt(obj.tempo_semanal_horas) || null,
      tempo_distribuicao: obj.tempo_distribuicao,
      budget_mensal_alem_travessia: obj.budget_faixa,
      capacidade_contratar_90d: obj.capacidade_contratar,
      background_tecnico: obj.background_tecnico,
      ferramentas_dominadas: obj.ferramentas_dominadas
    },
    identidade: {
      nicho_especifico: obj.nicho_especifico,
      posicionamento_percebido: obj.posicionamento_percebido,
      diferencial_percebido: obj.diferencial_percebido,
      voz_tom_atual: obj.voz_tom_atual,
      expressoes_assinatura: [obj.expressao_1, obj.expressao_2, obj.expressao_3].filter(Boolean)
    },
    expectativas: {
      resultado_concreto_6m: obj.resultado_concreto_6m,
      o_que_anima: obj.o_que_anima,
      maior_receio: obj.maior_receio
    },
    score_completude: { calcular_no_servidor: true },
    alertas_detectados: [],
    proxima_acao_recomendada: "validar via /anamnese-mentorada --validar"
  };
}

previewBtn.addEventListener('click', () => {
  const json = montarJSON();
  previewBox.textContent = JSON.stringify(json, null, 2);
  previewBox.classList.toggle('visible');
});

exportarBtn.addEventListener('click', () => {
  const inputs = form.querySelectorAll('[required]');
  let faltam = 0;
  inputs.forEach(i => { if (!i.value || i.value.trim() === '') faltam++; });

  if (faltam > 5) {
    if (!confirm('Faltam ' + faltam + ' campos importantes. Quer exportar mesmo assim?')) return;
  }

  const json = montarJSON();
  const slug = json.slug || 'mentorada';
  const blob = new Blob([JSON.stringify(json, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = slug + '-anamnese.json';
  a.click();
  URL.revokeObjectURL(url);

  alert('Pronto. Agora a gente nao comeca do zero — comeca do mapa. Me manda esse arquivo no WhatsApp. Te espero. — Tata');
});

calcularProgresso();
</script>

</body>
</html>
```

---

## COMO ENTREGAR PRA MENTORADA

### Passo 1 — Gerar
Skill roda `--formulario` e salva em:
```
~/imperio/mentoradas/[slug]/formulario.html
```

### Passo 2 — Enviar
Tata (ou Severino delegado) envia por WhatsApp ou email:

> "Oi [nome]! Antes da gente comecar a Travessia, quero te conhecer de verdade.
>
> Anexei aqui o formulario de anamnese. Sao 8 blocos, leva uns 30-50 minutos. Responde com calma — sem polidez. Tudo que voce escrever fica SO no seu computador ate voce me mandar de volta.
>
> Quando terminar, clica no botao 'Exportar minha anamnese' la embaixo, baixa o arquivo `.json` e me manda nesse WhatsApp.
>
> Vamos juntas. — Tata"

### Passo 3 — Receber
Mentorada manda o JSON. Tata salva em:
```
~/imperio/mentoradas/[slug]/00-anamnese.json
```

### Passo 4 — Validar
```
/anamnese-mentorada --validar slug=[slug]
```

Skill roda auditoria, calcula score, detecta alertas, sugere proxima acao.

---

## CUSTOMIZACOES POSSIVEIS

O HTML acima e o template padrao. Variacoes possiveis:

- **Tema claro** — alguns nichos (medico, juridico) preferem fundo claro
- **Logo da Tata** — adicionar SVG no header
- **Campos extras por nicho** — bloco 9 customizado pra nicho especifico
- **Multi-page wizard** — em vez de scroll, paginas separadas

Por padrao, a skill entrega o template acima. Customizacoes precisam ser pedidas explicitamente.

---

**Formulario do Metodo Imperatriz de Anamnese — propriedade Tata Goncalves.**
