# Lara Builder — Vendedora IA Personalizada

Skill que cria uma vendedora IA completa (clone personalizado da "Lara") para qualquer produto digital. Gera projeto full-stack com widget de chat, backend com IA, dashboard de conversas, UTM tracking e deploy.

## Trigger

Ativar quando o usuario pedir para:
- Criar uma vendedora IA / chatbot de vendas / assistente de vendas
- Criar uma "Lara" para o produto dele
- `/lara-builder`
- "quero uma vendedora no meu site"
- "cria um chat de vendas com IA"
- "quero um chatbot que vende"

## Importante

- Cada execucao cria UMA vendedora para UM produto especifico
- O mesmo mentorado pode rodar a skill varias vezes para produtos diferentes
- Cada vendedora tem seu proprio projeto, banco, prompt e widget
- A skill SEMPRE comeca pelo onboarding — nunca pula etapas

## Fluxo Completo (7 Fases)

### FASE 1 — ONBOARDING (Coleta de Informacoes)

Fazer as perguntas UMA POR VEZ, esperando a resposta antes de prosseguir. Usar tom amigavel e direto.

**Pergunta 1 — Nome da Vendedora:**
"Primeiro, vamos dar um nome pra sua vendedora IA! A da Tata se chama Lara. Qual nome voce quer dar pra sua? (Ex: Sofia, Clara, Bia, Ana...)"

**Pergunta 2 — Seu Produto:**
"Qual e o seu produto? Me conta:
- Nome do produto
- O que ele entrega (resultado principal)
- Preco (ou faixa de preco)
- Link de checkout (Eduzz, Hotmart, Kiwify, etc)"

**Pergunta 3 — Pagina de Vendas:**
"Me manda o link da sua pagina de vendas. Vou analisar ela completamente pra treinar sua vendedora com TUDO que ta la — headlines, beneficios, garantia, depoimentos, FAQ, tudo."

**Pergunta 4 — Depoimentos:**
"Agora me indica onde estao seus depoimentos. Pode ser:
- Uma pasta no seu computador com prints/screenshots
- Links de videos no YouTube
- Textos copiados de WhatsApp/Instagram
- Tudo junto misturado — eu processo qualquer formato!

Se nao tem depoimentos ainda, tudo bem — a gente cria a vendedora sem e adiciona depois."

**Pergunta 5 — Tom de Voz:**
"Como sua vendedora deve falar? Escolha o estilo:
1. Amigavel e informal (como uma amiga no WhatsApp)
2. Profissional e consultivo (como uma especialista)
3. Energetico e motivacional (como uma coach)
4. Outro (descreva como quer)

Dica: a vendedora da Tata fala como consultora — nao empurra venda, faz perguntas e guia a pessoa."

**Pergunta 6 — Perguntas Frequentes:**
"Quais sao as perguntas que seus clientes mais fazem? Liste pelo menos 5. Ex:
- Funciona pra quem ta comecando?
- Quanto tempo pra ter resultado?
- Tem garantia?
- Preciso de experiencia?
- Como funciona o acesso?"

**Pergunta 7 — Redirecionamento Comercial:**
"Quando a vendedora nao conseguir resolver ou o lead quiser falar com alguem, pra onde direciona?
- Link do WhatsApp do time comercial
- Ou email de contato"

**Pergunta 8 — Visual:**
"Qual a cor principal da sua marca? (Ex: roxo, azul, verde, laranja...)
Se tiver o codigo hex, melhor ainda! (Ex: #7C3AED)"

Ao final do onboarding, apresentar um RESUMO de tudo que foi coletado e pedir confirmacao antes de prosseguir.

---

### FASE 2 — ANALISE DA PAGINA DE VENDAS

Usar WebFetch para acessar a pagina de vendas do mentorado e extrair:

1. **Headlines e Sub-headlines** — todas as promises
2. **Beneficios** — lista completa do que o produto entrega
3. **Publico-alvo** — pra quem e (e pra quem NAO e)
4. **Garantia** — tipo e prazo
5. **Preco e Condicoes** — valores, parcelamento, cupons
6. **FAQ** — perguntas e respostas existentes
7. **Depoimentos na pagina** — nomes e resultados mencionados
8. **Objecoes implicitas** — o que a pagina tenta resolver
9. **CTA principal** — chamada para acao
10. **Diferenciais** — o que torna unico

Salvar toda a analise em um arquivo `analise-pagina.md` dentro do projeto.

---

### FASE 3 — PROCESSAMENTO DE DEPOIMENTOS

Para cada tipo de depoimento fornecido:

**Screenshots/Prints (imagens):**
- Ler cada imagem com o tool Read (multimodal)
- Extrair: nome da pessoa, resultado obtido, contexto, emocao
- Classificar por tipo de objecao que quebra

**Videos (YouTube links):**
- Usar WebFetch para acessar e extrair conteudo
- Ou pedir ao mentorado para transcrever os principais trechos

**Textos:**
- Organizar por categoria
- Identificar os mais persuasivos

Gerar arquivo `depoimentos-processados.md` com formato:
```
## Depoimento 1 — [Nome]
- Resultado: "..."
- Contexto: ...
- Quebra objecao: [qual objecao este depoimento responde]
- Frase-chave: "..."
```

---

### FASE 4 — GERACAO DO SYSTEM PROMPT

Usar o template em `templates/prompt-template.md` para gerar o system prompt personalizado.

O prompt deve conter:
1. **Identidade** — nome, personalidade, tom de voz
2. **Conhecimento do produto** — tudo extraido da pagina de vendas
3. **Depoimentos** — cada um com nome real e resultado real
4. **FAQ completo** — perguntas e respostas pre-prontas
5. **Regras de comportamento:**
   - NUNCA inventar depoimentos ou resultados que nao existem
   - NUNCA ser agressiva ou insistente
   - Fazer perguntas antes de oferecer solucao
   - Usar depoimentos APENAS quando relevante pra objecao
   - Enviar link de compra APENAS quando detectar interesse real
   - Redirecionar pro time comercial quando nao souber responder
6. **Estagios da conversa** — Discovery > Posicionamento > Objecao > Checkout > Follow-up
7. **Intent detection** — purchase, objection, question, whatsapp, churn_risk
8. **Link de checkout com UTM** — template com parametros dinamicos

Salvar em `src/prompt.ts` como constante exportada.

---

### FASE 5 — GERACAO DO PROJETO

Criar o projeto completo na pasta `~/[nome-da-vendedora]/` com a estrutura:

```
~/[nome-vendedora]/
├── CLAUDE.md                    # Contexto do projeto
├── package.json                 # Dependencies
├── tsconfig.json                # TypeScript config
├── .env.example                 # Template de variaveis
├── .gitignore
├── src/
│   ├── server.ts                # Express server principal
│   ├── database.ts              # Schema SQLite + migrations
│   ├── prompt.ts                # System prompt personalizado
│   ├── routes/
│   │   ├── chat.ts              # POST /api/chat (conversa com IA)
│   │   ├── leads.ts             # CRUD leads
│   │   ├── conversations.ts     # Historico de conversas
│   │   ├── metrics.ts           # Metricas e KPIs
│   │   ├── settings.ts          # Configuracoes
│   │   └── webhooks.ts          # Webhooks de plataforma (Eduzz/Hotmart/etc)
│   ├── services/
│   │   ├── ai.ts                # Integracao Google Gemini
│   │   ├── intent.ts            # Deteccao de intencao
│   │   └── utm.ts               # Geracao de UTM tracking
│   └── utils/
│       └── helpers.ts           # Utilidades
├── public/
│   └── chat-widget.js           # Widget embed (vanilla JS)
├── dashboard/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   ├── tailwind.config.ts
│   └── src/
│       ├── App.tsx              # Router principal
│       ├── main.tsx             # Entry point
│       ├── pages/
│       │   ├── Dashboard.tsx    # KPIs e graficos
│       │   ├── Conversations.tsx # Lista de conversas
│       │   ├── Leads.tsx        # Gestao de leads
│       │   └── Settings.tsx     # Configuracoes
│       └── components/
│           ├── MetricCard.tsx
│           ├── ConversationView.tsx
│           └── LeadTable.tsx
├── docs/
│   ├── analise-pagina.md        # Analise da pagina de vendas
│   └── depoimentos-processados.md # Depoimentos organizados
└── deploy/
    ├── ecosystem.config.js      # PM2 config
    └── nginx.conf               # Nginx template
```

#### Regras do Backend:

**server.ts:**
- Express 5 com CORS, JSON parser
- Serve static files (widget + dashboard)
- Rota `/api/chat` como endpoint principal
- Health check em `/api/health`
- Porta configuravel via .env (default: 3XXX)

**database.ts:**
- 4 tabelas: leads, conversations, metrics, settings
- Schema IDENTICO ao original (ver templates/schema.sql)
- WAL mode habilitado
- Indices otimizados

**chat.ts (rota principal):**
```
POST /api/chat
Body: { message: string, sessionId: string }
Response: { reply: string, intent: string }

Fluxo:
1. Receber mensagem
2. Buscar/criar lead pelo sessionId
3. Salvar mensagem do usuario (role: 'user')
4. Montar contexto: system prompt + historico da conversa
5. Enviar pro Gemini
6. Detectar intent da resposta
7. Se intent = 'purchase', incluir link com UTM
8. Salvar resposta (role: 'bot')
9. Registrar metrica
10. Retornar reply + intent
```

**utm.ts:**
```
Gerar URL: {checkout_url}?
  utm_source=vendedora-ia
  &utm_medium=chat-widget
  &utm_campaign={nome_vendedora}
  &utm_content={intent}
  &utm_term={session_id}
```

**intent.ts:**
```
Detectar intencoes:
- 'purchase' — quer comprar, pedir link, preco
- 'objection' — duvida, medo, resistencia
- 'question' — pergunta informativa
- 'whatsapp' — quer falar com humano
- 'positive' — elogio, agradecimento
- 'churn_risk' — desinteresse, despedida
```

#### Regras do Widget (v6 — Mobile-First):

Usar o template em `templates/chat-widget.js` e personalizar o objeto CONFIG:
- `name` — Nome da vendedora
- `subtitle` — Ex: "Assistente do [Negocio]"
- `apiUrl` — URL do backend
- `primaryColor` / `secondaryColor` — Cores do gradiente
- `textOnPrimary` — Cor do texto nos botoes (white ou #0d0d0d)
- `bgDark` — Cor de fundo do chat (ex: #0D0B15 ou #111)
- `welcomeMessage` — Mensagem de boas-vindas
- `quickReplies` — Array de quick replies iniciais
- `avatarLetter` — Letra do avatar
- `whatsappUrl` — Link WhatsApp comercial
- `tooltipText` — Texto do tooltip pre-abertura
- `tooltipDelay` / `tooltipDuration` — Timing do tooltip (ms)
- `btnPosition` — { bottom, right } desktop
- `btnPositionMobile` — { bottom, right } mobile

REGRAS CRITICAS:
1. O widget NUNCA abre sozinho — so no clique do botao flutuante
2. Badge "1" aparece pra atrair atencao + tooltip aparece apos tooltipDelay
3. NO MOBILE: abre tela cheia (fullscreen), NAO parcial
4. NO MOBILE: NAO faz auto-focus no input — usuario le primeiro, toca quando quiser
5. NO MOBILE: body fica locked (overflow hidden + position fixed) pra nao rolar pagina atras
6. KEYBOARD HANDLING: usa polling agressivo (50ms) no focus + visualViewport API pra redimensionar o chat quando teclado abre — funciona em TODOS os browsers incluindo Instagram, Facebook, TikTok in-app WebViews
7. Swipe down no header fecha o chat (mobile)
8. Botao ✕ grande (36x36px) sempre visivel
9. font-size: 16px no input pra evitar zoom automatico no iOS
10. Quick replies scrollam horizontalmente no mobile (overflow-x: auto)

#### Regras do Dashboard:

- Login simples (email/senha do admin)
- 4 paginas: Dashboard (KPIs), Conversas, Leads, Config
- KPIs: total leads, conversas hoje, checkouts enviados, conversoes, taxa conversao
- Graficos com Recharts
- Tabela de leads com TanStack Table
- Visualizador de conversa individual
- Filtros por data e status

---

### FASE 6 — CONFIGURACAO E TESTE

1. Criar arquivo `.env` com valores do mentorado
2. Rodar `npm install` no backend e dashboard
3. Rodar `npm run build` no dashboard
4. Iniciar servidor com `npm run dev`
5. Testar endpoint `/api/chat` com curl
6. Abrir dashboard e verificar
7. Mostrar como embed o widget na pagina de vendas:
   ```html
   <script src="https://SEU-DOMINIO:PORTA/chat-widget.js"></script>
   ```

---

### FASE 7 — INSTRUCOES DE DEPLOY

Gerar guia personalizado em `deploy/DEPLOY.md`:
1. Como fazer deploy na VPS (PM2 + Nginx)
2. Como configurar SSL (Certbot)
3. Como apontar DNS
4. Como monitorar (pm2 logs)
5. Como atualizar depoimentos depois
6. Como adicionar novas FAQs
7. Como ver as conversas no dashboard

---

## Stack Tecnica Obrigatoria

- **Backend:** Express 5 + TypeScript + better-sqlite3
- **IA:** @google/generative-ai (Gemini 2.5 Flash)
- **Frontend Dashboard:** React 19 + Vite 6 + Tailwind 4 + Recharts
- **Widget:** Vanilla JavaScript (zero dependencias)
- **Banco:** SQLite (WAL mode)
- **Auth:** JWT simples
- **Deploy:** PM2 + Nginx reverse proxy

## Arquivos de Template

Os templates base estao em:
- `templates/chat-widget.js` — Widget completo parametrizado
- `templates/schema.sql` — Schema do banco de dados
- `templates/prompt-template.md` — Template do system prompt

## Regras de Ouro

1. **NUNCA inventar depoimentos** — so usar os que o mentorado forneceu
2. **NUNCA abrir o widget automaticamente** — so no clique do botao
3. **SEMPRE gerar UTM nos links** — pra rastrear vendas da vendedora
4. **SEMPRE ter redirecionamento comercial** — quando a IA nao souber, manda pro humano
5. **SEMPRE salvar todas as conversas** — inteligencia de mercado
6. **NUNCA colocar API keys no frontend** — APENAS em .env no backend
7. **Cada produto = 1 vendedora separada** — projetos independentes
