/**
 * {{NOME_VENDEDORA}} — Chat Widget Vendedora IA v6
 * Gerado por /lara-builder (Instituto Tata Goncalves)
 * Mobile-first: fullscreen + keyboard handling para TODOS os browsers
 * (Safari, Chrome, Instagram, Facebook, TikTok in-app)
 *
 * Embed na sua pagina:
 * <script src="https://SEU_DOMINIO/chat-widget.js"></script>
 *
 * CONFIGURACOES (editar abaixo):
 */
(function () {
  // ══════════════════════════════════════
  // CONFIGURACOES — EDITAR AQUI
  // ══════════════════════════════════════
  const CONFIG = {
    name: '{{NOME_VENDEDORA}}',           // Nome da vendedora
    subtitle: '{{SUBTITULO}}',             // Ex: "Assistente do [Seu Negocio]"
    apiUrl: '{{API_URL}}',                 // URL do backend (ex: /api ou https://dominio.com)
    primaryColor: '{{COR_PRIMARIA}}',      // Hex da cor principal (ex: #7C3AED)
    secondaryColor: '{{COR_SECUNDARIA}}',  // Hex da cor secundaria (gradiente)
    textOnPrimary: '{{COR_TEXTO_BOTAO}}',  // Cor do texto no botao (ex: white ou #0d0d0d)
    bgDark: '{{COR_FUNDO}}',              // Cor de fundo do chat (ex: #0D0B15 ou #111)
    welcomeMessage: '{{MENSAGEM_BOAS_VINDAS}}',
    quickReplies: {{QUICK_REPLIES_JSON}},  // Array de strings
    avatarLetter: '{{AVATAR_LETRA}}',      // Primeira letra do nome
    whatsappUrl: '{{WHATSAPP_URL}}',       // Link WhatsApp do time comercial
    tooltipText: '{{TOOLTIP_TEXT}}',       // Texto do tooltip (ex: "Tem duvida? Me pergunta!")
    tooltipDelay: 5000,                    // Delay pra mostrar tooltip (ms)
    tooltipDuration: 12000,                // Quanto tempo tooltip fica visivel (ms)
    btnPosition: { bottom: '24px', right: '24px' },  // Posicao do botao desktop
    btnPositionMobile: { bottom: '16px', right: '16px' },  // Posicao do botao mobile
  };
  // ══════════════════════════════════════

  const SESSION_ID = CONFIG.name.toLowerCase().replace(/\s/g, '_') + '_' + Math.random().toString(36).slice(2, 10);
  const isMobile = () => window.innerWidth <= 480;
  const P = CONFIG.primaryColor;
  const S = CONFIG.secondaryColor;
  const T = CONFIG.textOnPrimary || 'white';
  const BG = CONFIG.bgDark || '#0D0B15';

  const css = `
    /* ═══ BOTAO FLUTUANTE ═══ */
    #lara-chat-btn {
      position: fixed;
      bottom: ${CONFIG.btnPosition.bottom};
      right: ${CONFIG.btnPosition.right};
      z-index: 9999;
      width: 56px; height: 56px; border-radius: 50%;
      background: linear-gradient(135deg, ${P}, ${S});
      border: none; cursor: pointer;
      box-shadow: 0 4px 20px ${P}66;
      display: flex; align-items: center; justify-content: center;
      transition: transform 0.2s, box-shadow 0.2s;
      animation: lara-pulse 3s ease-in-out infinite;
    }
    #lara-chat-btn:hover { transform: scale(1.08); box-shadow: 0 6px 28px ${P}80; }
    #lara-chat-btn svg { width: 26px; height: 26px; fill: ${T}; }
    @keyframes lara-pulse {
      0%,100% { box-shadow: 0 4px 20px ${P}66; }
      50% { box-shadow: 0 4px 20px ${P}66, 0 0 0 8px ${P}00; }
    }
    #lara-chat-btn.hidden { display: none !important; }

    #lara-badge {
      position: absolute; top: -3px; right: -3px;
      width: 18px; height: 18px; border-radius: 50%;
      background: #ef4444; color: white;
      font-size: 10px; font-weight: 700;
      display: flex; align-items: center; justify-content: center;
      font-family: system-ui, sans-serif;
    }

    /* ═══ TOOLTIP ═══ */
    #lara-tooltip {
      position: fixed;
      bottom: calc(${CONFIG.btnPosition.bottom} + 64px);
      right: ${CONFIG.btnPosition.right};
      z-index: 9998;
      background: ${BG}; color: #f5f0eb;
      border: 1px solid ${P}40;
      border-radius: 12px; padding: 10px 14px;
      font-family: 'Inter', system-ui, sans-serif;
      font-size: 13px; line-height: 1.4;
      max-width: 220px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.4);
      display: none; cursor: pointer;
    }
    #lara-tooltip::after {
      content: ''; position: absolute; bottom: -6px; right: 24px;
      width: 12px; height: 12px; background: ${BG};
      border-right: 1px solid ${P}40;
      border-bottom: 1px solid ${P}40;
      transform: rotate(45deg);
    }
    #lara-tooltip .close-tip {
      position: absolute; top: 4px; right: 8px;
      background: none; border: none; color: #64748B;
      cursor: pointer; font-size: 14px; line-height: 1; padding: 2px;
    }
    #lara-tooltip.show { display: block; }

    /* ═══ OVERLAY ═══ */
    #lara-overlay {
      position: fixed; inset: 0; z-index: 9997;
      background: rgba(0,0,0,0.6); display: none;
    }
    #lara-overlay.show { display: block; }

    /* ═══ CHAT BOX — DESKTOP ═══ */
    #lara-chat-box {
      position: fixed; z-index: 9998;
      bottom: calc(${CONFIG.btnPosition.bottom} + 68px);
      right: ${CONFIG.btnPosition.right};
      width: 360px; max-width: calc(100vw - 32px);
      height: 480px; max-height: calc(100vh - 140px);
      background: ${BG};
      border: 1px solid ${P}26;
      border-radius: 16px;
      box-shadow: 0 16px 48px rgba(0,0,0,0.5);
      display: none; flex-direction: column;
      overflow: hidden;
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      animation: lara-slide-up 0.3s ease;
    }
    @keyframes lara-slide-up {
      0% { opacity: 0; transform: translateY(16px); }
      100% { opacity: 1; transform: translateY(0); }
    }
    #lara-chat-box.open { display: flex; }

    /* ═══ HEADER ═══ */
    #lara-header {
      padding: 14px 16px;
      background: linear-gradient(135deg, ${BG}, ${BG}ee);
      border-bottom: 1px solid ${P}1F;
      display: flex; align-items: center; gap: 10px;
      flex-shrink: 0;
    }
    #lara-avatar {
      width: 36px; height: 36px; border-radius: 50%;
      background: linear-gradient(135deg, ${P}, ${S});
      display: flex; align-items: center; justify-content: center;
      font-size: 15px; font-weight: 800; color: ${T};
      flex-shrink: 0;
    }
    #lara-header-info { flex: 1; min-width: 0; }
    #lara-header-info h3 { margin: 0; font-size: 13px; font-weight: 700; color: #f5f0eb; }
    #lara-header-info p {
      margin: 1px 0 0; font-size: 10px; color: #22C55E;
      display: flex; align-items: center; gap: 4px;
    }
    #lara-header-info p::before {
      content: ''; width: 5px; height: 5px; border-radius: 50%;
      background: #22C55E; display: inline-block;
    }
    #lara-close {
      background: rgba(245,240,235,0.08); border: none;
      color: #f5f0eb; cursor: pointer;
      width: 36px; height: 36px; border-radius: 8px;
      font-size: 20px; line-height: 1;
      display: flex; align-items: center; justify-content: center;
      transition: background 0.2s; flex-shrink: 0;
    }
    #lara-close:hover { background: rgba(245,240,235,0.12); }

    /* ═══ MESSAGES ═══ */
    #lara-messages {
      flex: 1; overflow-y: auto; padding: 14px 12px 8px;
      display: flex; flex-direction: column; gap: 8px;
      -webkit-overflow-scrolling: touch;
      overscroll-behavior: contain;
    }
    .lara-msg {
      max-width: 82%; padding: 10px 12px;
      border-radius: 14px; font-size: 13px;
      line-height: 1.5; word-wrap: break-word;
      overflow-wrap: break-word; white-space: pre-wrap;
    }
    .lara-msg.bot {
      background: ${P}14;
      border: 1px solid ${P}1A;
      color: #e0ddd8; align-self: flex-start;
      border-bottom-left-radius: 4px;
    }
    .lara-msg.user {
      background: linear-gradient(135deg, ${P}, ${S});
      color: ${T}; align-self: flex-end;
      border-bottom-right-radius: 4px; font-weight: 500;
    }
    .lara-msg a { color: ${P}; text-decoration: underline; }
    .lara-msg.bot a { color: ${P}; font-weight: 600; }

    .lara-typing {
      display: flex; gap: 4px; padding: 10px 14px; align-self: flex-start;
    }
    .lara-typing span {
      width: 6px; height: 6px; border-radius: 50%;
      background: ${P}; opacity: 0.4;
      animation: lara-dot 1.2s ease-in-out infinite;
    }
    .lara-typing span:nth-child(2) { animation-delay: 0.2s; }
    .lara-typing span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes lara-dot {
      0%,100% { opacity: 0.3; transform: scale(0.8); }
      50% { opacity: 1; transform: scale(1.1); }
    }

    /* ═══ INPUT ═══ */
    #lara-input-area {
      padding: 10px 12px;
      border-top: 1px solid ${P}14;
      background: ${BG};
      display: flex; gap: 8px; align-items: flex-end;
      flex-shrink: 0;
    }
    #lara-input {
      flex: 1; background: ${P}0A;
      border: 1px solid ${P}1F;
      border-radius: 10px; padding: 9px 12px;
      color: #f5f0eb; font-size: 16px;
      font-family: inherit; outline: none;
      transition: border-color 0.2s;
      resize: none; min-height: 20px; max-height: 72px;
      -webkit-appearance: none;
    }
    #lara-input:focus { border-color: ${P}59; }
    #lara-input::placeholder { color: #64748B; }
    #lara-send {
      width: 38px; height: 38px; border-radius: 10px;
      background: linear-gradient(135deg, ${P}, ${S});
      border: none; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      transition: transform 0.15s, opacity 0.15s; flex-shrink: 0;
    }
    #lara-send:hover { transform: scale(1.05); }
    #lara-send:disabled { opacity: 0.3; cursor: default; transform: none; }
    #lara-send svg { width: 16px; height: 16px; fill: ${T}; }

    /* ═══ QUICK REPLIES ═══ */
    .lara-quick {
      display: flex; gap: 6px; padding: 4px 12px 6px;
      flex-shrink: 0; overflow-x: auto;
      -webkit-overflow-scrolling: touch; scrollbar-width: none;
    }
    .lara-quick::-webkit-scrollbar { display: none; }
    .lara-quick button {
      background: ${P}14;
      border: 1px solid ${P}2E;
      color: ${P}; border-radius: 16px;
      padding: 5px 12px; font-size: 12px;
      font-family: inherit; cursor: pointer;
      transition: all 0.2s; white-space: nowrap; flex-shrink: 0;
    }
    .lara-quick button:hover {
      background: ${P}26;
      border-color: ${P}59; color: #f5f0eb;
    }

    /* ═══ MOBILE — FULLSCREEN + KEYBOARD ═══ */
    @media (max-width: 480px) {
      #lara-chat-box {
        top: 0; left: 0; right: 0; bottom: 0;
        width: 100%; max-width: 100%;
        height: 100%; max-height: 100%;
        border-radius: 0; border: none;
      }
      #lara-header {
        padding-top: max(12px, env(safe-area-inset-top));
      }
      #lara-input-area {
        padding-bottom: max(10px, env(safe-area-inset-bottom));
      }
      #lara-chat-btn {
        bottom: ${CONFIG.btnPositionMobile.bottom};
        right: ${CONFIG.btnPositionMobile.right};
        width: 52px; height: 52px;
      }
      #lara-chat-btn svg { width: 24px; height: 24px; }
      #lara-tooltip {
        bottom: calc(${CONFIG.btnPositionMobile.bottom} + 60px);
        right: ${CONFIG.btnPositionMobile.right};
        max-width: 200px; font-size: 12px;
      }
      .lara-msg { font-size: 14px; }
      #lara-overlay { display: none !important; }
    }

    @media (min-width: 481px) {
      #lara-overlay { display: none !important; }
    }
  `;

  // ── DOM ──
  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  const overlay = document.createElement('div');
  overlay.id = 'lara-overlay';
  document.body.appendChild(overlay);

  const btn = document.createElement('button');
  btn.id = 'lara-chat-btn';
  btn.innerHTML = `
    <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H5.2L4 17.2V4h16v12z"/><path d="M7 9h2v2H7zm4 0h2v2h-2zm4 0h2v2h-2z"/></svg>
    <div id="lara-badge">1</div>
  `;
  document.body.appendChild(btn);

  const tooltip = document.createElement('div');
  tooltip.id = 'lara-tooltip';
  tooltip.innerHTML = (CONFIG.tooltipText || 'Tem duvida? Me pergunta!') + ' <button class="close-tip">&times;</button>';
  document.body.appendChild(tooltip);
  tooltip.querySelector('.close-tip').onclick = (e) => { e.stopPropagation(); tooltip.classList.remove('show'); };

  const box = document.createElement('div');
  box.id = 'lara-chat-box';
  box.innerHTML = `
    <div id="lara-header">
      <div id="lara-avatar">${CONFIG.avatarLetter}</div>
      <div id="lara-header-info">
        <h3>${CONFIG.name} — ${CONFIG.subtitle}</h3>
        <p>Online agora</p>
      </div>
      <button id="lara-close">\u2715</button>
    </div>
    <div id="lara-messages"></div>
    <div class="lara-quick" id="lara-quick"></div>
    <div id="lara-input-area">
      <textarea id="lara-input" placeholder="Digite sua duvida..." rows="1"></textarea>
      <button id="lara-send">
        <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
      </button>
    </div>
  `;
  document.body.appendChild(box);

  const messagesEl = box.querySelector('#lara-messages');
  const inputEl = box.querySelector('#lara-input');
  const sendBtn = box.querySelector('#lara-send');
  const quickEl = box.querySelector('#lara-quick');
  const badge = btn.querySelector('#lara-badge');
  let isOpen = false;
  let firstOpen = true;
  let savedScrollY = 0;
  let keyboardPoll = null;
  let baseHeight = 0;

  // Tooltip with configurable timing
  setTimeout(() => { if (!isOpen) tooltip.classList.add('show'); }, CONFIG.tooltipDelay);
  setTimeout(() => { tooltip.classList.remove('show'); }, CONFIG.tooltipDelay + CONFIG.tooltipDuration);

  // ══════════════════════════════════════
  // OPEN / CLOSE
  // ══════════════════════════════════════
  function openChat() {
    isOpen = true;
    tooltip.classList.remove('show');
    badge.style.display = 'none';

    if (isMobile()) {
      savedScrollY = window.scrollY;
      document.body.style.overflow = 'hidden';
      document.body.style.position = 'fixed';
      document.body.style.top = -savedScrollY + 'px';
      document.body.style.width = '100%';
      baseHeight = window.innerHeight;
    }

    box.classList.add('open');
    overlay.classList.add('show');
    btn.classList.add('hidden');

    if (firstOpen) {
      firstOpen = false;
      addBot(CONFIG.welcomeMessage);
      showQuickReplies(CONFIG.quickReplies);
    }

    // NO auto-focus on mobile — user reads first, taps when ready
    if (!isMobile()) inputEl.focus();
  }

  function closeChat() {
    isOpen = false;
    inputEl.blur();
    resetKeyboard();

    box.classList.remove('open');
    overlay.classList.remove('show');
    btn.classList.remove('hidden');

    if (isMobile()) {
      document.body.style.overflow = '';
      document.body.style.position = '';
      document.body.style.top = '';
      document.body.style.width = '';
      window.scrollTo(0, savedScrollY);
    }
  }

  btn.onclick = openChat;
  tooltip.onclick = (e) => { if (!e.target.classList.contains('close-tip')) openChat(); };
  box.querySelector('#lara-close').onclick = closeChat;
  overlay.onclick = closeChat;

  // Swipe down on header to close (mobile)
  let touchStartY = 0;
  const header = box.querySelector('#lara-header');
  header.addEventListener('touchstart', (e) => { touchStartY = e.touches[0].clientY; }, { passive: true });
  header.addEventListener('touchmove', (e) => {
    if (touchStartY > 0 && e.touches[0].clientY - touchStartY > 50) { closeChat(); touchStartY = 0; }
  }, { passive: true });
  header.addEventListener('touchend', () => { touchStartY = 0; }, { passive: true });

  // ══════════════════════════════════════
  // KEYBOARD HANDLING
  // Works in ALL browsers including:
  // Safari, Chrome, Instagram, Facebook,
  // TikTok, Twitter in-app WebViews
  // ══════════════════════════════════════
  function getVisibleHeight() {
    if (window.visualViewport) return window.visualViewport.height;
    return window.innerHeight;
  }

  function getVisibleTop() {
    if (window.visualViewport) return window.visualViewport.offsetTop;
    return 0;
  }

  function adjustForKeyboard() {
    if (!isOpen || !isMobile()) return;
    const vh = getVisibleHeight();
    const top = getVisibleTop();

    if (vh < baseHeight - 100) {
      // Keyboard is open
      box.style.position = 'fixed';
      box.style.top = top + 'px';
      box.style.height = vh + 'px';
      box.style.bottom = 'auto';
    } else {
      // Keyboard is closed
      box.style.top = '0';
      box.style.height = '100%';
      box.style.bottom = '0';
    }
    requestAnimationFrame(() => { messagesEl.scrollTop = messagesEl.scrollHeight; });
  }

  function resetKeyboard() {
    if (keyboardPoll) { clearInterval(keyboardPoll); keyboardPoll = null; }
    box.style.top = '0';
    box.style.height = '100%';
    box.style.bottom = '0';
  }

  // Focus: start aggressive polling to catch keyboard in any browser
  inputEl.addEventListener('focus', () => {
    if (!isMobile()) return;
    let attempts = 0;
    if (keyboardPoll) clearInterval(keyboardPoll);
    keyboardPoll = setInterval(() => {
      adjustForKeyboard();
      attempts++;
      if (attempts > 40) {
        clearInterval(keyboardPoll);
        keyboardPoll = setInterval(adjustForKeyboard, 200);
      }
    }, 50);
  });

  inputEl.addEventListener('blur', () => {
    if (!isMobile()) return;
    setTimeout(() => {
      if (document.activeElement !== inputEl) resetKeyboard();
    }, 150);
  });

  // Also use visualViewport events if available
  if (window.visualViewport) {
    window.visualViewport.addEventListener('resize', adjustForKeyboard);
    window.visualViewport.addEventListener('scroll', adjustForKeyboard);
  }
  window.addEventListener('resize', () => { if (isOpen && isMobile()) adjustForKeyboard(); });

  // ══════════════════════════════════════
  // MESSAGES
  // ══════════════════════════════════════
  function cleanMarkdown(text) {
    return text
      .replace(/\*\*([^*]+)\*\*/g, '$1')
      .replace(/\*([^*]+)\*/g, '$1')
      .replace(/^[\s]*[-\u2022]\s/gm, '\u2192 ')
      .replace(/^[\s]*\d+\.\s/gm, '\u2192 ')
      .replace(/#{1,3}\s/g, '')
      .replace(/`([^`]+)`/g, '$1');
  }

  function addMsg(text, type) {
    const div = document.createElement('div');
    div.className = 'lara-msg ' + type;
    const clean = type === 'bot' ? cleanMarkdown(text) : text;
    div.innerHTML = clean.replace(
      /(https?:\/\/[^\s<]+)/g,
      '<a href="$1" target="_blank" rel="noopener">$1</a>'
    ).replace(/\n/g, '<br>');
    messagesEl.appendChild(div);
    requestAnimationFrame(() => { messagesEl.scrollTop = messagesEl.scrollHeight; });
    return div;
  }

  function addBot(text) { return addMsg(text, 'bot'); }
  function addUser(text) { return addMsg(text, 'user'); }

  function showTyping() {
    const div = document.createElement('div');
    div.className = 'lara-typing';
    div.innerHTML = '<span></span><span></span><span></span>';
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
    return div;
  }

  function showQuickReplies(options) {
    quickEl.innerHTML = '';
    for (const opt of options) {
      const b = document.createElement('button');
      b.textContent = opt;
      b.onclick = () => { quickEl.innerHTML = ''; sendMessage(opt); };
      quickEl.appendChild(b);
    }
  }

  // ══════════════════════════════════════
  // SEND
  // ══════════════════════════════════════
  async function sendMessage(text) {
    if (!text.trim()) return;
    addUser(text);
    inputEl.value = '';
    inputEl.style.height = 'auto';
    sendBtn.disabled = true;

    const typing = showTyping();

    try {
      const res = await fetch(CONFIG.apiUrl + '/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text, sessionId: SESSION_ID })
      });
      const data = await res.json();
      typing.remove();
      addBot(data.reply || 'Desculpe, tive um probleminha. Tenta de novo?');

      if (data.quickReplies && data.quickReplies.length > 0) {
        showQuickReplies(data.quickReplies);
      } else if (data.intent === 'purchase') {
        showQuickReplies(['Quero comprar!', 'Ainda tenho duvidas', 'Falar no WhatsApp']);
      } else if (data.intent === 'whatsapp' && CONFIG.whatsappUrl) {
        showQuickReplies(['Voltar pro chat', 'Quero comprar']);
      } else {
        showQuickReplies(CONFIG.quickReplies);
      }
    } catch (err) {
      typing.remove();
      addBot('Ops, nao consegui conectar. Tenta de novo ou fala com a equipe no WhatsApp!');
      showQuickReplies(['Tentar de novo', 'Falar no WhatsApp']);
    }
    sendBtn.disabled = false;
  }

  sendBtn.onclick = () => sendMessage(inputEl.value);

  inputEl.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage(inputEl.value);
    }
  });

  inputEl.addEventListener('input', () => {
    inputEl.style.height = 'auto';
    inputEl.style.height = Math.min(inputEl.scrollHeight, 72) + 'px';
  });

  // Scroll to bottom when input gets focus on mobile
  inputEl.addEventListener('focus', () => {
    if (isMobile()) {
      setTimeout(() => { messagesEl.scrollTop = messagesEl.scrollHeight; }, 300);
    }
  });

})();
