# Page Builder — Especificacoes de Design & HTML

> Referencia completa de design system, componentes obrigatorios e estrutura HTML
> para gerar paginas de vendas production-ready.

---

## DESIGN SYSTEM PADRAO

Se o usuario nao tiver design system, usar estes defaults:

### Tipografia
- **Primaria:** Inter (Google Fonts)
- **Titulos:** Inter, weight 700
- **Corpo:** Inter, weight 400
- **Texto destaque:** Inter, weight 600

### Paleta de Cores por Industria

| Industria | Cor Primaria | Texto | Fundo |
|-----------|-------------|-------|-------|
| MENTORIA/COACHING | Violet `#7c3aed` | Slate `#1e293b` | White `#ffffff` |
| FITNESS/SAUDE | Emerald `#059669` | Slate | White |
| NEGOCIOS/FINANCAS | Blue `#2563eb` | Slate | White |
| CRIATIVO/DESIGN | Pink `#db2777` | Slate | White |
| TECNOLOGIA/SAAS | Indigo `#4f46e5` | Slate | White |
| EDUCACAO | Teal `#0d9488` | Slate | White |
| BELEZA/MODA | Rose `#e11d48` | Slate | White |
| **PADRAO** | **Violet `#7c3aed`** | **Slate `#1e293b`** | **White `#ffffff`** |

### Espacamento
- **Padding de secao:** `py-16 md:py-24`
- **Container:** `max-w-6xl mx-auto px-4`
- **Entre elementos:** `space-y-6`

### Estilos de Componentes
- **Botoes:** `rounded-xl px-8 py-4 font-semibold shadow-lg hover:shadow-xl transition`
- **Cards:** `rounded-2xl shadow-md p-8 bg-white`
- **Depoimentos:** `rounded-xl` com borda sutil
- **FAQ:** accordion com transicao suave

---

## ELEMENTOS HTML OBRIGATORIOS

### Head Section

```html
<!-- Viewport responsivo -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- SEO -->
<title>[Product Name] — [Tagline]</title>
<meta name="description" content="[Copy-based description 150-160 chars]">
<!-- Open Graph -->
<meta property="og:title" content="[Headline]">
<meta property="og:description" content="[Sub-headline]">
<meta property="og:image" content="[Hero image URL]">
<meta property="og:type" content="website">
<!-- Tailwind CSS CDN -->
<script src="https://cdn.tailwindcss.com"></script>
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<!-- Meta Pixel placeholder -->
<!-- REPLACE: Add your Meta Pixel code here -->
<!-- GTM placeholder -->
<!-- REPLACE: Add your GTM container code here -->
<!-- Google Ads placeholder -->
<!-- REPLACE: Add your Google Ads tag here -->
```

### CTA Fixo (Mobile)

Descricao: Barra fixa no rodape do celular com botao de CTA sempre visivel durante o scroll.

```html
<div class="fixed bottom-0 left-0 right-0 z-50 p-4 bg-white/95 backdrop-blur shadow-2xl border-t md:hidden">
  <a href="#checkout" class="block w-full text-center bg-[PRIMARY] text-white font-bold py-4 rounded-xl text-lg shadow-lg">
    [CTA TEXT]
  </a>
  <p class="text-center text-xs text-slate-500 mt-1">[Sub-CTA text: lembrete de garantia]</p>
</div>
```

### Botao Flutuante WhatsApp

Descricao: Botao verde do WhatsApp fixo no canto inferior direito para contato direto.

```html
<a href="https://wa.me/[PHONE]?text=[ENCODED_MESSAGE]" target="_blank"
   class="fixed bottom-20 md:bottom-6 right-4 z-50 bg-green-500 text-white p-4 rounded-full shadow-xl hover:bg-green-600 transition-all hover:scale-110">
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/>
    <path d="M12 0C5.373 0 0 5.373 0 12c0 2.625.846 5.059 2.284 7.034L.789 23.492a.5.5 0 00.611.611l4.458-1.495A11.952 11.952 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 22c-2.347 0-4.518-.808-6.24-2.159l-.436-.348-2.648.888.888-2.648-.348-.436A9.956 9.956 0 012 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/>
  </svg>
</a>
```

### Timer de Contagem Regressiva (JavaScript)

Descricao: Contador regressivo configuravel que mostra dias, horas, minutos e segundos ate o prazo.

```javascript
// Configurable countdown
const COUNTDOWN_END = new Date('[DATE]T[TIME]:00').getTime();

function updateCountdown() {
  const now = new Date().getTime();
  const distance = COUNTDOWN_END - now;

  if (distance < 0) {
    document.getElementById('countdown').innerHTML = '<span class="text-red-600 font-bold">ENCERRADO</span>';
    return;
  }

  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById('countdown').innerHTML =
    `<span class="text-3xl font-bold">${days}</span><span class="text-sm">d</span> ` +
    `<span class="text-3xl font-bold">${hours}</span><span class="text-sm">h</span> ` +
    `<span class="text-3xl font-bold">${minutes}</span><span class="text-sm">m</span> ` +
    `<span class="text-3xl font-bold">${seconds}</span><span class="text-sm">s</span>`;
}

setInterval(updateCountdown, 1000);
updateCountdown();
```

### Notificacao de Prova Social

Descricao: Pop-up que aparece no canto inferior esquerdo simulando inscricoes recentes para gerar urgencia.

```javascript
// Rotates through names
const socialProofNames = [
  { name: 'Maria S.', city: 'Sao Paulo' },
  { name: 'Carlos R.', city: 'Rio de Janeiro' },
  { name: 'Ana L.', city: 'Belo Horizonte' },
  // Add more...
];

function showSocialProof() {
  const person = socialProofNames[Math.floor(Math.random() * socialProofNames.length)];
  const notification = document.getElementById('social-proof');
  notification.innerHTML = `<strong>${person.name}</strong> de ${person.city} acabou de se inscrever`;
  notification.classList.remove('hidden');
  notification.classList.add('animate-slide-in');

  setTimeout(() => {
    notification.classList.add('hidden');
  }, 5000);
}

// Random interval: 15-45 seconds
function scheduleSocialProof() {
  const delay = (Math.random() * 30 + 15) * 1000;
  setTimeout(() => {
    showSocialProof();
    scheduleSocialProof();
  }, delay);
}

scheduleSocialProof();
```

### Popup de Intencao de Saida

Descricao: Modal que aparece quando o usuario move o mouse para fora da pagina (desktop) ou apos 60s (mobile).

```html
<!-- Triggers when mouse moves to top of viewport (desktop) -->
<!-- Triggers after 60s on mobile -->
<!-- Shows: lead capture or last-chance offer -->
<!-- Cookie-based: only shows once per session -->
<div id="exit-popup" class="hidden fixed inset-0 z-[200] bg-black/60 flex items-center justify-center p-4">
  <div class="bg-white rounded-2xl shadow-2xl max-w-lg w-full p-8 relative">
    <button onclick="closeExitPopup()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600">&times;</button>
    <h3 class="text-2xl font-bold text-slate-900 mb-4">[HEADLINE DE RETENCAO]</h3>
    <p class="text-slate-600 mb-6">[COPY DE ULTIMA CHANCE]</p>
    <a href="#checkout" class="block w-full text-center bg-[PRIMARY] text-white font-bold py-4 rounded-xl">
      [CTA TEXT]
    </a>
  </div>
</div>

<script>
// Desktop: mouse leave
document.addEventListener('mouseout', (e) => {
  if (e.clientY <= 0 && !sessionStorage.getItem('exitShown')) {
    document.getElementById('exit-popup').classList.remove('hidden');
    sessionStorage.setItem('exitShown', 'true');
  }
});

// Mobile: after 60s
if (window.innerWidth < 768) {
  setTimeout(() => {
    if (!sessionStorage.getItem('exitShown')) {
      document.getElementById('exit-popup').classList.remove('hidden');
      sessionStorage.setItem('exitShown', 'true');
    }
  }, 60000);
}

function closeExitPopup() {
  document.getElementById('exit-popup').classList.add('hidden');
}
</script>
```

### Banner LGPD (Cookies)

Descricao: Banner de conformidade com a LGPD para consentimento de cookies.

```html
<div id="lgpd-banner" class="fixed bottom-0 left-0 right-0 z-[100] bg-slate-900 text-white p-4" style="display: none;">
  <div class="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
    <p class="text-sm">Este site usa cookies para melhorar sua experiencia. Ao continuar navegando, voce concorda com nossa <a href="#" class="underline">Politica de Privacidade</a>.</p>
    <button onclick="acceptCookies()" class="bg-white text-slate-900 px-6 py-2 rounded-lg font-semibold text-sm whitespace-nowrap">Aceitar</button>
  </div>
</div>

<script>
if (!localStorage.getItem('lgpdAccepted')) {
  document.getElementById('lgpd-banner').style.display = 'block';
}

function acceptCookies() {
  localStorage.setItem('lgpdAccepted', 'true');
  document.getElementById('lgpd-banner').style.display = 'none';
}
</script>
```

### FAQ Accordion

Descricao: Componente de perguntas frequentes com abertura/fechamento suave. Apenas um item aberto por vez.

```html
<div class="space-y-3" id="faq-container">
  <!-- Repeat for each FAQ item -->
  <div class="border border-slate-200 rounded-xl overflow-hidden">
    <button onclick="toggleFaq(this)" class="w-full flex items-center justify-between p-5 text-left font-semibold text-slate-900 hover:bg-slate-50 transition">
      <span>[PERGUNTA]</span>
      <svg class="faq-icon w-5 h-5 text-slate-400 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
      </svg>
    </button>
    <div class="faq-answer max-h-0 overflow-hidden transition-all duration-300">
      <p class="px-5 pb-5 text-slate-600">[RESPOSTA]</p>
    </div>
  </div>
</div>

<script>
function toggleFaq(btn) {
  const answer = btn.nextElementSibling;
  const icon = btn.querySelector('.faq-icon');
  const isOpen = answer.style.maxHeight && answer.style.maxHeight !== '0px';

  // Close all
  document.querySelectorAll('.faq-answer').forEach(a => a.style.maxHeight = '0px');
  document.querySelectorAll('.faq-icon').forEach(i => i.style.transform = 'rotate(0deg)');

  // Open clicked if was closed
  if (!isOpen) {
    answer.style.maxHeight = answer.scrollHeight + 'px';
    icon.style.transform = 'rotate(180deg)';
  }
}
</script>
```

### Integracao de Checkout

Descricao: Botoes de CTA com URL configuravel e passagem automatica de UTM para plataformas de pagamento.

```html
<!-- CTA buttons use configurable URL -->
<!-- Supports UTM passthrough: ?utm_source=...&utm_medium=...&utm_campaign=... -->
<!-- Platforms: Hotmart, Eduzz, Kiwify, Monetizze -->
<!-- Format: href="[CHECKOUT_URL]" with data-platform="hotmart" -->

<script>
// UTM passthrough to checkout links
document.addEventListener('DOMContentLoaded', () => {
  const params = new URLSearchParams(window.location.search);
  const utmKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
  const utmParams = {};

  utmKeys.forEach(key => {
    if (params.get(key)) utmParams[key] = params.get(key);
  });

  if (Object.keys(utmParams).length > 0) {
    document.querySelectorAll('a[href*="checkout"], a[data-platform]').forEach(link => {
      const url = new URL(link.href);
      Object.entries(utmParams).forEach(([k, v]) => url.searchParams.set(k, v));
      link.href = url.toString();
    });
  }
});
</script>
```

---

## ESTRUTURA DA PAGINA (Ordem das Secoes)

```
1.  Navegacao (minima: logo + CTA)
2.  Hero section (headline + sub + CTA + trust badges)
3.  Secao Problema/Dor
4.  Secao Historia/Autoridade
5.  Secao Transformacao/Futuro
6.  Secao Revelacao da Oferta
7.  Value Stack / O Que Esta Incluso
8.  Secao de Bonus
9.  Preco + Opcoes de Pagamento
10. Secao de Garantia
11. Secao de Depoimentos (carrossel ou grid)
12. FAQ accordion
13. Secao CTA Final
14. Footer (minimo: links + legal)
```

---

## BREAKPOINTS RESPONSIVOS

| Dispositivo | Tamanho | Layout |
|-------------|---------|--------|
| Mobile | < 640px | Coluna unica, empilhado |
| Tablet | 640-1024px | 2 colunas onde apropriado |
| Desktop | > 1024px | Layout completo, container com max-width |

---

## PERFORMANCE

- **Imagens:** lazy loading com `loading="lazy"`
- **Fontes:** `display=swap` para nao bloquear renderizacao
- **CSS:** Tailwind CDN (aceitavel para paginas unicas)
- **Sem jQuery** ou bibliotecas pesadas
- **SVGs inline** para icones criticos (sem biblioteca de icones necessaria)
