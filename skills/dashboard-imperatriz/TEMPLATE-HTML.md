# Template HTML — Dashboard Imperatriz

Template HTML standalone com Mermaid embutido, paleta Tata (#D6A648), Inter (sans), Instrument Serif (display). Funciona offline, abre em qualquer browser, exporta pra PNG/CSV/JSON.

Dois templates: visão Tata (Corte) e visão mentorada (individual). Compartilham o mesmo `<style>` e estrutura base — diferem nos panels.

Os placeholders entre `{{...}}` são substituídos pela skill em runtime. Os blocos `<!-- LOOP:... -->` e `<!-- END LOOP -->` indicam onde a skill faz iteração sobre arrays do JSON.

---

## Paleta de cores (CSS Variables)

```css
:root {
  /* Tata Imperatriz palette */
  --bg: #0e0c0a;
  --bg-soft: #1a1612;
  --bg-card: #221d18;
  --ink: #f4ecdc;
  --ink-soft: #c8b89a;
  --ink-dim: #8a7d68;
  --gold: #D6A648;          /* cor mestra Tata */
  --gold-soft: #e8c994;
  --gold-deep: #a87f30;
  --green: #6f9b6e;
  --green-deep: #4a6e49;
  --yellow: #d4a838;
  --yellow-deep: #a67f1f;
  --red: #b85a4f;
  --red-deep: #7d3a32;
  --gray: #4a443c;
  --line: #3a3127;
  --serif: 'Instrument Serif', 'Cormorant Garamond', Georgia, serif;
  --sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --mono: 'JetBrains Mono', 'SF Mono', 'Courier New', monospace;
}
```

---

## TEMPLATE 1 — Visão Tata (Corte)

Arquivo gerado: `dashboard-tata.html`

```html
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Corte da Imperatriz · {{MES_ANO}}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<style>
:root {
  --bg: #0e0c0a; --bg-soft: #1a1612; --bg-card: #221d18;
  --ink: #f4ecdc; --ink-soft: #c8b89a; --ink-dim: #8a7d68;
  --gold: #D6A648; --gold-soft: #e8c994; --gold-deep: #a87f30;
  --green: #6f9b6e; --green-deep: #4a6e49;
  --yellow: #d4a838; --yellow-deep: #a67f1f;
  --red: #b85a4f; --red-deep: #7d3a32;
  --gray: #4a443c; --line: #3a3127;
  --serif: 'Instrument Serif', 'Cormorant Garamond', Georgia, serif;
  --sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --mono: 'JetBrains Mono', 'SF Mono', 'Courier New', monospace;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: var(--bg); color: var(--ink);
  font-family: var(--sans); line-height: 1.6;
  min-height: 100vh; -webkit-font-smoothing: antialiased;
}
header {
  border-bottom: 1px solid var(--line);
  padding: 56px 32px 40px;
  background: linear-gradient(180deg, var(--bg-soft) 0%, var(--bg) 100%);
}
.header-inner { max-width: 1280px; margin: 0 auto; }
.eyebrow {
  font-size: 11px; letter-spacing: 0.32em;
  text-transform: uppercase; color: var(--gold);
  margin-bottom: 14px;
}
h1 {
  font-family: var(--serif); font-size: 56px; font-weight: 400;
  letter-spacing: -0.01em; color: var(--ink); margin-bottom: 12px;
}
h1 em { color: var(--gold); font-style: italic; }
.subtitle { color: var(--ink-soft); font-size: 17px; max-width: 760px; }
.meta-row {
  display: grid; grid-template-columns: repeat(6, 1fr);
  gap: 20px; margin-top: 32px; padding-top: 28px;
  border-top: 1px solid var(--line);
}
.meta-item .label {
  font-size: 11px; text-transform: uppercase; letter-spacing: 0.18em;
  color: var(--ink-dim); margin-bottom: 6px;
}
.meta-item .value {
  font-family: var(--serif); font-size: 28px; color: var(--ink);
  font-variant-numeric: tabular-nums;
}
.meta-item .value.gold { color: var(--gold); }
.meta-item .value.red { color: var(--red); }
.meta-item .value.green { color: var(--green); }
nav.tabs {
  position: sticky; top: 0; z-index: 10;
  background: var(--bg); border-bottom: 1px solid var(--line);
  padding: 0 32px;
}
.tabs-inner { max-width: 1280px; margin: 0 auto; display: flex; gap: 4px; overflow-x: auto; }
.tab {
  padding: 18px 22px; background: transparent; color: var(--ink-soft);
  border: none; border-bottom: 2px solid transparent;
  font-family: var(--sans); font-size: 14px; font-weight: 500;
  cursor: pointer; white-space: nowrap; transition: all 0.2s;
}
.tab:hover { color: var(--ink); }
.tab.active { color: var(--gold); border-bottom-color: var(--gold); }
main { max-width: 1280px; margin: 0 auto; padding: 48px 32px 96px; }
.panel { display: none; }
.panel.active { display: block; animation: fade 0.3s; }
@keyframes fade { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
h2 {
  font-family: var(--serif); font-size: 36px; font-weight: 400;
  margin-bottom: 8px; color: var(--ink);
}
.panel-intro { color: var(--ink-soft); margin-bottom: 32px; max-width: 760px; }
h3 {
  font-family: var(--serif); font-size: 24px; font-weight: 400;
  margin: 36px 0 16px; color: var(--gold-soft);
}
h4 {
  font-size: 12px; text-transform: uppercase; letter-spacing: 0.14em;
  color: var(--ink-dim); margin: 24px 0 10px;
}
p { margin-bottom: 12px; color: var(--ink-soft); }
.card {
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 6px; padding: 24px; margin-bottom: 16px;
}
.card-gold { border-left: 3px solid var(--gold); }
.card-red { border-left: 3px solid var(--red); }
.card-green { border-left: 3px solid var(--green); }
.card-yellow { border-left: 3px solid var(--yellow); }

/* Filters */
.filters { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 20px; }
.chip {
  padding: 6px 14px; border-radius: 16px; font-size: 12px;
  background: var(--bg-soft); color: var(--ink-soft);
  border: 1px solid var(--line); cursor: pointer;
  font-weight: 500; transition: all 0.15s;
}
.chip:hover { border-color: var(--gold); color: var(--ink); }
.chip.active { background: var(--gold); color: var(--bg); border-color: var(--gold); }

/* Matrix */
.matrix-wrap { overflow-x: auto; margin: 24px 0; }
table.matrix {
  border-collapse: separate; border-spacing: 2px;
  font-size: 13px;
}
table.matrix th, table.matrix td {
  padding: 8px 6px; text-align: center; min-width: 28px;
  font-family: var(--mono); font-size: 11px;
}
table.matrix th.row-head, table.matrix td.row-head {
  text-align: left; padding: 8px 14px 8px 0; min-width: 180px;
  font-family: var(--sans); color: var(--ink); font-weight: 500;
}
table.matrix th.col-head {
  font-weight: 600; color: var(--gold); background: var(--bg-soft);
  border-radius: 3px;
}
table.matrix td.cell {
  border-radius: 3px; cursor: pointer; transition: transform 0.1s;
  font-size: 14px;
}
table.matrix td.cell:hover { transform: scale(1.15); }
.cell-green  { background: var(--green); color: var(--bg); }
.cell-yellow { background: var(--yellow); color: var(--bg); }
.cell-red    { background: var(--red); color: var(--ink); }
.cell-gray   { background: var(--gray); color: var(--ink-dim); }
.score-cell {
  background: var(--bg-soft); color: var(--gold);
  font-weight: 700; padding: 8px 14px;
}
.nivel-row {
  background: var(--bg-soft);
  font-family: var(--serif); font-style: italic;
  color: var(--gold); padding: 10px 14px;
  font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase;
}

/* Pills */
.pill {
  display: inline-block; padding: 3px 10px; border-radius: 12px;
  font-size: 11px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.1em;
}
.pill-green  { background: var(--green); color: var(--ink); }
.pill-yellow { background: var(--yellow); color: var(--bg); }
.pill-red    { background: var(--red); color: var(--ink); }
.pill-gold   { background: var(--gold); color: var(--bg); }

/* Alert cards */
.alert-card {
  background: var(--bg-card); border-left: 3px solid var(--red);
  padding: 18px 22px; margin-bottom: 12px; border-radius: 4px;
  display: flex; align-items: flex-start; gap: 16px;
}
.alert-card.high    { border-left-color: var(--red); }
.alert-card.medium  { border-left-color: var(--yellow); }
.alert-card.low     { border-left-color: var(--gold); }
.alert-icon { font-size: 24px; line-height: 1; }
.alert-body { flex: 1; }
.alert-mentorada {
  font-family: var(--serif); font-size: 18px; color: var(--ink);
  margin-bottom: 4px;
}
.alert-detail { color: var(--ink-soft); font-size: 14px; margin-bottom: 8px; }
.alert-action {
  font-family: var(--mono); font-size: 12px; color: var(--gold);
  background: var(--bg-soft); padding: 6px 10px; border-radius: 3px;
  display: inline-block;
}

/* Mermaid container */
.mermaid-wrap {
  background: var(--bg-soft); border: 1px solid var(--line);
  border-radius: 6px; padding: 32px; margin: 24px 0;
  text-align: center;
}

/* Legend */
.legend {
  display: flex; gap: 20px; flex-wrap: wrap;
  padding: 16px 0; margin: 16px 0; border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}
.legend-item { display: flex; align-items: center; gap: 8px; font-size: 12px; color: var(--ink-soft); }
.legend-dot { width: 14px; height: 14px; border-radius: 3px; }

/* Buttons */
.btn {
  background: var(--bg-card); color: var(--ink);
  border: 1px solid var(--line); padding: 8px 18px;
  border-radius: 3px; cursor: pointer; font-size: 13px;
  font-weight: 500; transition: all 0.15s;
}
.btn:hover { border-color: var(--gold); color: var(--gold); }
.btn-primary { background: var(--gold); color: var(--bg); border-color: var(--gold); font-weight: 600; }
.btn-primary:hover { opacity: 0.85; color: var(--bg); }
.btn-row { display: flex; gap: 8px; margin-top: 12px; }

/* Mentorada card (Investidura panel) */
.mentorada-card {
  background: var(--bg-card); border: 1px solid var(--line);
  border-radius: 6px; padding: 24px; margin-bottom: 14px;
}
.mentorada-card.pronta { border-left: 3px solid var(--gold); background: linear-gradient(90deg, rgba(214,166,72,0.08) 0%, var(--bg-card) 100%); }
.mentorada-card .nome {
  font-family: var(--serif); font-size: 22px; color: var(--ink); margin-bottom: 6px;
}
.mentorada-card .transicao { font-size: 13px; color: var(--gold); margin-bottom: 12px; }
.mentorada-card ul { padding-left: 20px; }
.mentorada-card li { color: var(--ink-soft); margin-bottom: 4px; font-size: 14px; }

/* Receita */
table.receita {
  width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;
}
table.receita th, table.receita td {
  padding: 12px 16px; text-align: right; border-bottom: 1px solid var(--line);
  font-variant-numeric: tabular-nums;
}
table.receita th:first-child, table.receita td:first-child { text-align: left; }
table.receita th { color: var(--gold); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.12em; }
table.receita td { color: var(--ink-soft); }
table.receita td strong { color: var(--ink); }
table.receita tr.total { background: var(--bg-soft); }
table.receita tr.total td { color: var(--gold); font-weight: 700; }

/* Footer */
footer {
  text-align: center; padding: 32px;
  color: var(--ink-dim); font-size: 12px;
  border-top: 1px solid var(--line);
}
footer a { color: var(--gold); text-decoration: none; }
footer a:hover { text-decoration: underline; }

@media (max-width: 768px) {
  h1 { font-size: 36px; }
  .meta-row { grid-template-columns: repeat(2, 1fr); }
  table.matrix th, table.matrix td { font-size: 10px; padding: 4px 2px; min-width: 22px; }
  table.matrix th.row-head, table.matrix td.row-head { min-width: 120px; font-size: 12px; }
}
</style>
</head>
<body>

<header>
  <div class="header-inner">
    <div class="eyebrow">Método Imperatriz · Dashboard Corte · {{MES_ANO}}</div>
    <h1>Corte da <em>Imperatriz</em></h1>
    <p class="subtitle">{{SUBTITLE}}</p>
    <div class="meta-row">
      <div class="meta-item"><div class="label">Mentoradas</div><div class="value">{{N_ATIVAS}}</div></div>
      <div class="meta-item"><div class="label">Receita Corte</div><div class="value gold">R$ {{RECEITA_BR}}</div></div>
      <div class="meta-item"><div class="label">Verde geral</div><div class="value green">{{PCT_VERDE}}%</div></div>
      <div class="meta-item"><div class="label">Vermelho geral</div><div class="value red">{{PCT_VERMELHO}}%</div></div>
      <div class="meta-item"><div class="label">Atenção urgente</div><div class="value">{{N_URGENTES}}</div></div>
      <div class="meta-item"><div class="label">Prontas Investidura</div><div class="value gold">{{N_PRONTAS}}</div></div>
    </div>
  </div>
</header>

<nav class="tabs">
  <div class="tabs-inner">
    <button class="tab active" data-tab="overview">1 · Visão Geral</button>
    <button class="tab" data-tab="heatmap">2 · Heatmap</button>
    <button class="tab" data-tab="investidura">3 · Investidura</button>
    <button class="tab" data-tab="cases">4 · Cases</button>
    <button class="tab" data-tab="receita">5 · Receita</button>
  </div>
</nav>

<main>

<!-- PANEL 1 — VISÃO GERAL -->
<section class="panel active" id="overview">
  <h2>Visão geral da Corte</h2>
  <p class="panel-intro">Matriz mentorada × porta. Cor por célula. Hover pra detalhe. Clique pra abrir o dashboard individual.</p>

  <div class="filters">
    <span class="chip active" data-filter="nivel" data-value="todos">Todos níveis</span>
    <span class="chip" data-filter="nivel" data-value="iniciada">Iniciada</span>
    <span class="chip" data-filter="nivel" data-value="cortesa">Cortesã</span>
    <span class="chip" data-filter="nivel" data-value="dama">Dama</span>
    <span class="chip" data-filter="nivel" data-value="imperatriz">Imperatriz</span>
  </div>

  <div class="legend">
    <div class="legend-item"><span class="legend-dot" style="background:var(--green)"></span>Verde — bateu benchmark</div>
    <div class="legend-item"><span class="legend-dot" style="background:var(--yellow)"></span>Amarelo — 70-99%</div>
    <div class="legend-item"><span class="legend-dot" style="background:var(--red)"></span>Vermelho — < 70% ou ausente</div>
    <div class="legend-item"><span class="legend-dot" style="background:var(--gray)"></span>Cinza — fora do escopo</div>
  </div>

  <div class="matrix-wrap">
    <table class="matrix">
      <thead>
        <tr>
          <th class="row-head"></th>
          <th class="col-head">A</th><th class="col-head">B</th><th class="col-head">C</th><th class="col-head">D</th>
          <th class="col-head">E</th><th class="col-head">F</th><th class="col-head">G</th><th class="col-head">H</th>
          <th class="col-head">I</th><th class="col-head">J</th><th class="col-head">K</th><th class="col-head">L</th>
          <th class="col-head">M</th><th class="col-head">N</th><th class="col-head">O</th><th class="col-head">P</th>
          <th class="col-head">Q</th><th class="col-head">R</th><th class="col-head">S</th><th class="col-head">T</th>
          <th class="col-head">U</th><th class="col-head">V</th><th class="col-head">W</th><th class="col-head">X</th>
          <th class="col-head">Y</th><th class="col-head">Z</th>
          <th class="col-head" style="min-width: 60px">Score</th>
        </tr>
      </thead>
      <tbody>
        <!-- LOOP: para cada nivel hierárquico (Imperatriz, Dama, Cortesã, Iniciada) -->
        <tr><td class="nivel-row" colspan="28">{{NIVEL}}</td></tr>
        <!-- LOOP: para cada mentorada do nível -->
        <tr data-nivel="{{NIVEL_LOWER}}">
          <td class="row-head">{{MENTORADA_NOME}}</td>
          <!-- LOOP: para cada porta A-Z -->
          <td class="cell cell-{{COR}}" 
              data-mentorada="{{MENTORADA_NOME}}" 
              data-porta="{{LETRA}}"
              title="{{LETRA}} — {{KPI_NOME}}: {{VALOR}} (benchmark {{BENCHMARK}})">
            {{ICON}}
          </td>
          <!-- END LOOP porta -->
          <td class="score-cell">{{SCORE_PCT}}%</td>
        </tr>
        <!-- END LOOP mentorada -->
        <!-- END LOOP nivel -->
        <tr style="border-top: 2px solid var(--gold);">
          <td class="row-head" style="color: var(--gold); font-weight: 700;">CORTE (% verde)</td>
          <!-- LOOP: para cada porta A-Z -->
          <td class="cell" style="background: var(--bg-soft); color: var(--gold); font-weight: 700;">{{PCT_PORTA}}</td>
          <!-- END LOOP -->
          <td class="score-cell">{{PCT_GERAL}}%</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3>Atenção urgente</h3>
  <!-- LOOP: para cada alerta priorizado -->
  <div class="alert-card {{SEVERIDADE_CLASS}}">
    <div class="alert-icon">{{ICONE_ALERTA}}</div>
    <div class="alert-body">
      <div class="alert-mentorada">{{MENTORADA}} — porta {{PORTA}}</div>
      <div class="alert-detail">{{DETALHE}}</div>
      <code class="alert-action">{{COMANDO_RECOMENDADO}}</code>
    </div>
  </div>
  <!-- END LOOP -->

  <h3>Receita do mês</h3>
  <div class="card card-gold">
    <h4>Agregado da Corte</h4>
    <p style="font-family: var(--serif); font-size: 36px; color: var(--gold); margin: 0;">R$ {{RECEITA_BR}}</p>
    <p style="margin-top: 8px;">vs mês anterior: <strong style="color: var(--green);">{{VAR_MES}}%</strong> · vs ano passado: <strong style="color: var(--green);">{{VAR_ANO}}%</strong></p>
  </div>
</section>

<!-- PANEL 2 — HEATMAP -->
<section class="panel" id="heatmap">
  <h2>Heatmap visual</h2>
  <p class="panel-intro">Mesma matriz expandida em diagrama Mermaid. Pra exportar PNG e mostrar em call.</p>
  <div class="mermaid-wrap">
    <pre class="mermaid">
{{MERMAID_HEATMAP}}
    </pre>
  </div>
  <div class="btn-row">
    <button class="btn btn-primary" onclick="exportPNG('heatmap')">Exportar PNG</button>
    <button class="btn" onclick="exportJSON()">Exportar JSON completo</button>
  </div>
</section>

<!-- PANEL 3 — INVESTIDURA -->
<section class="panel" id="investidura">
  <h2>Investidura</h2>
  <p class="panel-intro">Quem está pronta pra subir nível, quem está perto, quem está construindo.</p>

  <h3>Prontas agora</h3>
  <!-- LOOP: prontas -->
  <div class="mentorada-card pronta">
    <div class="nome">{{NOME}}</div>
    <div class="transicao">{{NIVEL_ATUAL}} → {{NIVEL_ALVO}}</div>
    <ul>
      <li>Todas portas exigidas verdes ({{PORTAS_EXIGIDAS}})</li>
      <li>Consistência {{N_MESES}} meses</li>
      <li>Sem alerta crítico ativo</li>
    </ul>
    <div class="btn-row">
      <button class="btn btn-primary" onclick="copyToClipboard('/calendario-imperatriz --evento investidura {{NOME}}')">Agendar cerimônia</button>
      <button class="btn">Ver dossiê</button>
    </div>
  </div>
  <!-- END LOOP -->

  <h3>Quase lá (1-2 portas)</h3>
  <!-- LOOP: quase_la -->
  <div class="mentorada-card">
    <div class="nome">{{NOME}}</div>
    <div class="transicao">{{NIVEL_ATUAL}} → {{NIVEL_ALVO}}</div>
    <ul>
      <li>Falta: {{PORTAS_FALTANDO}}</li>
      <li>Estimativa: {{ESTIMATIVA}}</li>
    </ul>
  </div>
  <!-- END LOOP -->

  <h3>Em construção</h3>
  <!-- LOOP: em_construcao -->
  <div class="mentorada-card">
    <div class="nome">{{NOME}}</div>
    <div class="transicao">{{NIVEL_ATUAL}} ({{N_VERDES}}/{{N_EXIGIDAS}})</div>
    <ul>
      <li>Foco prioritário: porta {{PORTA_FOCO}}</li>
    </ul>
  </div>
  <!-- END LOOP -->
</section>

<!-- PANEL 4 — CASES -->
<section class="panel" id="cases">
  <h2>Cases prontos pra documentar</h2>
  <p class="panel-intro">KPIs verdes consistentes 3+ meses. Material pra Tata documentar e mostrar.</p>
  <!-- LOOP: cases -->
  <div class="card card-gold">
    <h4>{{MENTORADA}} · Porta {{PORTA}}</h4>
    <p><strong>{{KPI_NOME}}:</strong> {{VALOR}} consistente {{N_MESES}} meses</p>
    <p>{{NARRATIVA}}</p>
    <div class="btn-row">
      <button class="btn btn-primary" onclick="copyToClipboard('/anamnese-mentorada --case {{MENTORADA}} {{PORTA}}')">Documentar caso</button>
      <button class="btn">Pedir depoimento</button>
    </div>
  </div>
  <!-- END LOOP -->
</section>

<!-- PANEL 5 — RECEITA -->
<section class="panel" id="receita">
  <h2>Receita agregada</h2>
  <p class="panel-intro">Mês a mês por mentorada (últimos 12 meses) + total Corte.</p>
  <table class="receita">
    <thead>
      <tr>
        <th>Mentorada</th>
        <!-- LOOP: meses (ultimos 12) -->
        <th>{{MES}}</th>
        <!-- END LOOP -->
        <th>Total 12m</th>
      </tr>
    </thead>
    <tbody>
      <!-- LOOP: mentoradas -->
      <tr>
        <td><strong>{{NOME}}</strong></td>
        <!-- LOOP: receita_mes -->
        <td>{{VALOR_BR}}</td>
        <!-- END LOOP -->
        <td><strong>{{TOTAL_BR}}</strong></td>
      </tr>
      <!-- END LOOP -->
      <tr class="total">
        <td>TOTAL CORTE</td>
        <!-- LOOP: total_mes -->
        <td>{{VALOR_BR}}</td>
        <!-- END LOOP -->
        <td>{{TOTAL_GERAL_BR}}</td>
      </tr>
    </tbody>
  </table>
</section>

</main>

<footer>
  Travessia Imperatriz · <strong>Pilar 4 (Medição)</strong> · Tata Gonçalves<br>
  Gerado em {{TIMESTAMP}} · Próximo update: {{PROXIMO_UPDATE}} · 
  <a href="dashboard-tata.json">Baixar JSON</a> · 
  <a href="#" onclick="exportCSV()">Exportar CSV</a>
</footer>

<script>
// Tabs
document.querySelectorAll('.tab').forEach(t => {
  t.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
    document.querySelectorAll('.panel').forEach(x => x.classList.remove('active'));
    t.classList.add('active');
    document.getElementById(t.dataset.tab).classList.add('active');
  });
});

// Filters
document.querySelectorAll('.chip').forEach(c => {
  c.addEventListener('click', () => {
    const filter = c.dataset.filter;
    const value = c.dataset.value;
    document.querySelectorAll(`.chip[data-filter="${filter}"]`).forEach(x => x.classList.remove('active'));
    c.classList.add('active');
    if (value === 'todos') {
      document.querySelectorAll('tr[data-nivel]').forEach(r => r.style.display = '');
    } else {
      document.querySelectorAll('tr[data-nivel]').forEach(r => {
        r.style.display = r.dataset.nivel === value ? '' : 'none';
      });
    }
    localStorage.setItem('dashboard_filter_' + filter, value);
  });
});

// Cell click → opens individual dashboard
document.querySelectorAll('.cell').forEach(c => {
  c.addEventListener('click', () => {
    const m = c.dataset.mentorada;
    if (m) window.open('../mentoradas/' + m.toLowerCase().replace(/ /g, '-') + '/dashboard.html', '_blank');
  });
});

// Copy to clipboard
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    alert('Comando copiado: ' + text);
  });
}

// Export PNG
function exportPNG(panelId) {
  const html2canvas = window.html2canvas;
  if (!html2canvas) {
    alert('Carregando html2canvas... tenta de novo em 2s');
    const s = document.createElement('script');
    s.src = 'https://html2canvas.hertzen.com/dist/html2canvas.min.js';
    document.head.appendChild(s);
    return;
  }
  html2canvas(document.getElementById(panelId)).then(canvas => {
    const link = document.createElement('a');
    link.download = 'corte-' + panelId + '.png';
    link.href = canvas.toDataURL();
    link.click();
  });
}

// Export JSON
function exportJSON() {
  window.location.href = 'dashboard-tata.json';
}

// Export CSV
function exportCSV() {
  let csv = 'Mentorada,Nivel,Score';
  for (let i = 65; i <= 90; i++) csv += ',' + String.fromCharCode(i);
  csv += '\n';
  document.querySelectorAll('tr[data-nivel]').forEach(r => {
    const nome = r.querySelector('.row-head').textContent;
    const nivel = r.dataset.nivel;
    const cells = Array.from(r.querySelectorAll('.cell')).map(c => {
      if (c.classList.contains('cell-green')) return 'V';
      if (c.classList.contains('cell-yellow')) return 'A';
      if (c.classList.contains('cell-red')) return 'R';
      return '-';
    });
    const score = r.querySelector('.score-cell').textContent;
    csv += [nome, nivel, score, ...cells].join(',') + '\n';
  });
  const blob = new Blob([csv], { type: 'text/csv' });
  const link = document.createElement('a');
  link.download = 'corte-{{MES_ANO_SLUG}}.csv';
  link.href = URL.createObjectURL(blob);
  link.click();
}

// Mermaid init
mermaid.initialize({ 
  startOnLoad: true, 
  theme: 'base',
  themeVariables: {
    primaryColor: '#221d18',
    primaryTextColor: '#f4ecdc',
    primaryBorderColor: '#D6A648',
    lineColor: '#D6A648',
    secondaryColor: '#1a1612',
    tertiaryColor: '#0e0c0a',
    background: '#0e0c0a',
    fontFamily: 'Inter, sans-serif'
  }
});

// Restore filter from localStorage
const savedFilter = localStorage.getItem('dashboard_filter_nivel');
if (savedFilter) {
  const chip = document.querySelector(`.chip[data-filter="nivel"][data-value="${savedFilter}"]`);
  if (chip) chip.click();
}
</script>

</body>
</html>
```

---

## TEMPLATE 2 — Visão Mentorada (Individual)

Arquivo gerado: `dashboard.html` (na pasta da mentorada)

Compartilha o `<style>` e header/tabs/footer base do template anterior, com adaptações:

### Header

```html
<header>
  <div class="header-inner">
    <div class="eyebrow">Método Imperatriz · Sua Travessia · {{MES_ANO}}</div>
    <h1>Sua <em>Travessia</em></h1>
    <p class="subtitle">{{MENTORADA_NOME}}, você está na porta {{PORTA_LETRA}} ({{PORTA_NOME}}). {{N_VERDES}} de {{N_ESCOPO}} KPIs verdes.</p>
    <div class="meta-row" style="grid-template-columns: repeat(4, 1fr);">
      <div class="meta-item"><div class="label">Nível atual</div><div class="value">{{NIVEL}}</div></div>
      <div class="meta-item"><div class="label">Porta atual</div><div class="value gold">{{PORTA_LETRA}} · {{PORTA_NOME}}</div></div>
      <div class="meta-item"><div class="label">Score</div><div class="value">{{SCORE}}%</div></div>
      <div class="meta-item"><div class="label">Próxima Investidura</div><div class="value">{{NIVEL_ALVO}} · faltam {{N_FALTAM}}</div></div>
    </div>
  </div>
</header>
```

### Tabs

```html
<nav class="tabs">
  <div class="tabs-inner">
    <button class="tab active" data-tab="atual">1 · Sua porta atual</button>
    <button class="tab" data-tab="proximo">2 · Próximo passo</button>
    <button class="tab" data-tab="portas">3 · Suas 26 portas</button>
    <button class="tab" data-tab="historico">4 · Histórico</button>
    <button class="tab" data-tab="proximo-nivel">5 · Próximo nível</button>
  </div>
</nav>
```

### Panel 1 — Sua porta atual

```html
<section class="panel active" id="atual">
  <h2>Sua porta atual</h2>
  <div class="card card-{{COR_PORTA}}">
    <h4>Porta {{PORTA_LETRA}} — {{PORTA_NOME}}</h4>
    <h3 style="margin-top: 16px;">KPI: {{KPI_NOME}}</h3>
    <div style="display: flex; align-items: baseline; gap: 24px; margin: 24px 0;">
      <div style="font-family: var(--serif); font-size: 96px; color: var(--{{COR_PORTA}}); line-height: 1;">{{VALOR_ATUAL}}</div>
      <div style="color: var(--ink-dim); font-size: 16px;">
        ─────<br>
        benchmark<br>
        <strong style="color: var(--ink); font-size: 22px;">{{BENCHMARK}}</strong>
      </div>
    </div>
    <p>Você está em <strong>{{PCT_BENCHMARK}}%</strong> do benchmark. {{MSG_DISTANCIA}}</p>
    <p style="margin-top: 16px;">STATUS: <span class="pill pill-{{COR_PORTA}}">{{COR_LABEL}}</span></p>
  </div>

  <h3>Diagnóstico</h3>
  <div class="card">
    <p>{{DIAGNOSTICO_TEXTO}}</p>
    {{#TEM_UPSTREAM_CONTAMINADA}}
    <p style="margin-top: 16px;"><strong style="color: var(--red);">Porta-fonte contaminada:</strong> {{PORTA_FONTE}} ({{PORTA_FONTE_NOME}})</p>
    <p>{{PORTA_FONTE_DETALHE}}</p>
    <p style="margin-top: 12px;"><strong style="color: var(--gold);">Rollback sugerido:</strong> refazer {{PORTA_FONTE}} antes de continuar {{PORTA_LETRA}}</p>
    {{/TEM_UPSTREAM_CONTAMINADA}}
  </div>

  <h3>Ação imediata</h3>
  <div class="card card-gold">
    <p>{{ACAO_DESCRICAO}}</p>
    <div class="btn-row">
      <code class="alert-action" style="margin-right: 8px;">{{COMANDO_1}}</code>
      <button class="btn" onclick="copyToClipboard('{{COMANDO_1}}')">Copiar</button>
    </div>
  </div>
</section>
```

### Panel 2 — Próximo passo (output do tatou-2.0)

```html
<section class="panel" id="proximo">
  <h2>Próximo passo (recomendado pelo tatou-2.0)</h2>
  <div class="card card-gold">
    <h4>Esta semana</h4>
    <ul>
      <!-- LOOP: passos esta semana -->
      <li><strong>{{ORDEM}}.</strong> {{ACAO}} <code class="alert-action">{{SKILL}}</code></li>
      <!-- END LOOP -->
    </ul>
    <h4>Próxima semana</h4>
    <ul>
      <!-- LOOP: passos próxima semana -->
      <li><strong>{{ORDEM}}.</strong> {{ACAO}} <code class="alert-action">{{SKILL}}</code></li>
      <!-- END LOOP -->
    </ul>
    <h4>Em 2 semanas</h4>
    <ul>
      <!-- LOOP: passos em 2 semanas -->
      <li><strong>{{ORDEM}}.</strong> {{ACAO}} <code class="alert-action">{{SKILL}}</code></li>
      <!-- END LOOP -->
    </ul>
    <div class="btn-row">
      <button class="btn btn-primary" onclick="copyPlanoCompleto()">Copiar plano completo</button>
    </div>
  </div>
</section>
```

### Panel 3 — Suas 26 portas

```html
<section class="panel" id="portas">
  <h2>Suas 26 portas</h2>
  <p class="panel-intro">Visão completa. Hover ou clique numa porta pra ver detalhe.</p>

  <div class="filters">
    <span class="chip active" data-filter="cor" data-value="todas">Todas</span>
    <span class="chip" data-filter="cor" data-value="verde">Verdes</span>
    <span class="chip" data-filter="cor" data-value="amarelo">Amarelas</span>
    <span class="chip" data-filter="cor" data-value="vermelho">Vermelhas</span>
    <span class="chip" data-filter="cor" data-value="escopo">Só do meu nível</span>
  </div>

  <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 12px;">
    <!-- LOOP: 26 portas -->
    <div class="card card-{{COR}}" data-cor="{{COR}}" data-escopo="{{NO_ESCOPO}}" style="text-align: center; padding: 16px;">
      <div style="font-family: var(--serif); font-size: 36px; color: var(--{{COR}});">{{LETRA}}</div>
      <div style="font-size: 11px; color: var(--ink-dim); text-transform: uppercase; letter-spacing: 0.1em;">{{PORTA_NOME_CURTO}}</div>
      <div style="margin-top: 12px; font-family: var(--mono); font-size: 13px; color: var(--ink);">{{VALOR}}</div>
      <div style="font-size: 11px; color: var(--ink-dim);">bench: {{BENCHMARK}}</div>
    </div>
    <!-- END LOOP -->
  </div>
</section>
```

### Panel 4 — Histórico

```html
<section class="panel" id="historico">
  <h2>Seu histórico (últimos 6 meses)</h2>
  <div class="matrix-wrap">
    <table class="matrix">
      <thead>
        <tr>
          <th class="row-head">Mês</th>
          <th class="col-head">A</th><!-- ...repete A-Z... --><th class="col-head">Z</th>
          <th class="col-head">Score</th>
        </tr>
      </thead>
      <tbody>
        <!-- LOOP: 6 meses -->
        <tr>
          <td class="row-head">{{MES_LABEL}}</td>
          <!-- LOOP: 26 portas -->
          <td class="cell cell-{{COR}}">{{ICON}}</td>
          <!-- END LOOP -->
          <td class="score-cell">{{SCORE_MES}}%</td>
        </tr>
        <!-- END LOOP -->
      </tbody>
    </table>
  </div>

  <div class="card card-gold">
    <h4>Tendência</h4>
    <ul>
      <!-- LOOP: insights tendencia -->
      <li>{{INSIGHT}}</li>
      <!-- END LOOP -->
    </ul>
  </div>
</section>
```

### Panel 5 — Próximo nível (Investidura)

```html
<section class="panel" id="proximo-nivel">
  <h2>Próximo nível: {{NIVEL_ALVO}}</h2>
  <p class="panel-intro">{{NIVEL_ATUAL}} → {{NIVEL_ALVO}}. Critério: portas {{PORTAS_EXIGIDAS_RANGE}} verdes.</p>

  <div class="card card-gold">
    <h4>Você tem</h4>
    <p style="font-family: var(--serif); font-size: 56px; color: var(--gold);">{{N_VERDES}}/{{N_EXIGIDAS}}</p>
  </div>

  <h3>Faltam</h3>
  <!-- LOOP: portas faltando -->
  <div class="card card-{{COR}}">
    <h4>Porta {{LETRA}} — {{PORTA_NOME}}</h4>
    <p>{{KPI_DESCRICAO}}</p>
    <p style="color: var(--ink-dim); font-size: 12px;">{{TAG_PRIORIDADE}}</p>
  </div>
  <!-- END LOOP -->

  <h3>Estimativa realista</h3>
  <p>{{ESTIMATIVA_TEXTO}}</p>

  <h3>Ordem sugerida</h3>
  <div class="mermaid-wrap">
    <pre class="mermaid">
flowchart LR
    Atual["{{NIVEL_ATUAL}} · {{N_VERDES}}/{{N_EXIGIDAS}}"]
    {{#PASSOS}}
    {{LETRA}}["Refazer {{LETRA}} · {{TEMPO}}"]
    {{/PASSOS}}
    Alvo["{{NIVEL_ALVO}} · {{N_EXIGIDAS}}/{{N_EXIGIDAS}}"]
    
    Atual --> {{PRIMEIRO_PASSO}}
    {{#TRANSICOES}}
    {{DE}} --> {{PARA}}
    {{/TRANSICOES}}
    {{ULTIMO_PASSO}} --> Alvo
    
    style Atual fill:#221d18,color:#f4ecdc
    style Alvo fill:#D6A648,color:#0e0c0a
    </pre>
  </div>
</section>
```

### Footer (mentorada)

```html
<footer>
  Sua Travessia · <strong>Tata Gonçalves</strong><br>
  Gerado em {{TIMESTAMP}} · Próximo update: {{PROXIMO_UPDATE}} · 
  <a href="dashboard.json">Baixar JSON</a>
</footer>
```

### Script adicional (mentorada)

```html
<script>
function copyPlanoCompleto() {
  const passos = [];
  document.querySelectorAll('#proximo li').forEach(li => passos.push(li.textContent.trim()));
  const texto = "Plano da próxima 2 semanas:\n\n" + passos.join('\n');
  navigator.clipboard.writeText(texto).then(() => alert('Plano copiado pra área de transferência'));
}

// Filter portas por cor
document.querySelectorAll('.chip[data-filter="cor"]').forEach(c => {
  c.addEventListener('click', () => {
    const value = c.dataset.value;
    document.querySelectorAll('.chip[data-filter="cor"]').forEach(x => x.classList.remove('active'));
    c.classList.add('active');
    document.querySelectorAll('#portas .card').forEach(card => {
      if (value === 'todas') card.style.display = '';
      else if (value === 'escopo') card.style.display = card.dataset.escopo === 'true' ? '' : 'none';
      else card.style.display = card.dataset.cor === value ? '' : 'none';
    });
  });
});
</script>
```

---

## Diretrizes de geração da skill

Quando a skill renderizar o template:

1. **Substituir placeholders** `{{...}}` com valores do JSON gerado
2. **Iterar loops** marcados `<!-- LOOP: ... -->` ... `<!-- END LOOP -->`
3. **Renderizar condicionais** `{{#FLAG}}...{{/FLAG}}` (mustache-style) — só inclui bloco se FLAG for true
4. **Mermaid heatmap** (Tata) — gerar string Mermaid dinâmica baseada nos dados, embutir no `<pre class="mermaid">`
5. **Formatos numéricos:**
   - Receita: `R$ 487.300` (ponto como milhar, sem casa decimal)
   - Percentuais: `67%` (sem casa decimal)
   - ROAS, multiplicadores: `2,4x` (vírgula decimal, 1 casa)
   - Datas: `Mai/2026` ou `2026-05-08`
6. **Cores das células** mapear de `verde/amarelo/vermelho/cinza` para classes CSS `cell-green/cell-yellow/cell-red/cell-gray`
7. **Ícones** dentro das células: pode usar emoji 🟢🟡🔴⬜ OU símbolos Unicode (●○) OU deixar vazio com cor sólida — preferência: deixar vazio (cor é o sinal)
8. **Responsividade:** o template já suporta mobile (matrix vira scroll horizontal abaixo de 768px)

---

## Validação pós-render

Antes de salvar, a skill valida:

- [ ] Todos placeholders `{{...}}` substituídos (regex de busca não retorna match)
- [ ] HTML válido (parser básico não dá erro)
- [ ] Mermaid string sintaticamente válida
- [ ] Tamanho do arquivo < 500kb (deve ser, com inline CSS + JSON em `<script type="application/json">`)
- [ ] Funciona offline (CDN do Mermaid e Google Fonts está como fallback opcional, esquema funciona com fontes do sistema)

---

## Compatibilidade

- Browsers: Chrome 90+, Safari 14+, Firefox 88+, Edge 90+
- Modo offline: 100% funcional (CDNs do Mermaid e fontes têm fallback graceful)
- Print: já está configurado pra A4 paisagem (matriz)
- Modo claro: não suportado (paleta da Tata é dark-only)

---

**Template HTML — propriedade Tata Gonçalves. Pilar 4 (Medição) da Travessia Imperatriz.**
