# Cases Imperatriz — Skill Proprietária Tata Gonçalves

Operadora do **Pilar 7 (Tribo)** da Travessia Imperatriz. Motor de captação, validação e ativação de cases reais de mentoradas, com proof stack auditável e copy pronta pra cada canal.

---

## FILOSOFIA

> **Caso real > promessa. Número específico > adjetivo. Print autorizado > storytelling. Frase da mentorada > frase da Tata.**

Sem cases, narrativa é só promessa. Com cases, narrativa vira convicção. Em mercado estágio 4+ (que é o caso da Tata em 2026), cases estruturados são o ativo #2 de copy — atrás só do mecanismo único.

Cases não são depoimento solto. São **ativos estruturais de império** que viram:
- Seção de página de vendas
- Capítulo de livro
- VSL de 8-12 minutos
- Ad de retargeting
- E-mail de objeção
- Carrossel de Instagram
- Slide de palco

---

## O QUE A SKILL FAZ

Recebe trigger de proof point (KPI verde, mudança de nível, pipeline completo) e:

1. **Capta** case completo via formulário dos 8 blocos
2. **Valida** proof stack contra hierarquia de 7 níveis
3. **Estrutura** em formato reutilizável e versionado
4. **Cruza** com objeções pra construir biblioteca de proof
5. **Gera copy** pronta pra qualquer canal (página, e-mail, VSL, ad, carrossel, livro)
6. **Audita** termo de uso e canais autorizados
7. **Versiona** (v1 → v2 → v3 conforme mentorada evolui)

---

## QUANDO USAR

Disparar quando:

- Mentorada **muda de nível** na Hierarquia (Princesa → Duquesa → Marquesa → Imperatriz)
- Mentorada atinge **KPI verde** declarado (faturamento dobrou, NPS ≥ 80, recompra ≥ 40%)
- Mentorada completa **pipeline** (porta A até a meta destravada)
- Mentorada conquista **proof point qualitativo** (palco, mídia, citação por autoridade)
- Tata vai escrever **copy nova** e precisa de prova social específica
- Tata quer **auditar** se cases existentes têm proof stack robusto
- Tata quer **biblioteca** de proof organizada por objeção

---

## COMO USAR

### Modo captar (novo case)
```
/cases-imperatriz --captar [nome da mentorada]
```
Envia formulário dos 8 blocos pra mentorada. Aguarda preenchimento. Valida completude.

### Modo validar (auditoria)
```
/cases-imperatriz --validar [nome]
```
Audita case existente contra hierarquia de proof. Devolve score (Bronze/Prata/Ouro/Diamante) + gaps.

### Modo gerar-copy (transforma case em copy)
```
/cases-imperatriz --gerar-copy [nome] [canal]
```
Canais: pagina, email, vsl, ad-estatico, ad-video, carrossel, stories, livro, palco, webinar.

### Modo listar (visão de ecossistema)
```
/cases-imperatriz --listar
```
Lista todos cases com filtros: nicho, nível Hierarquia, objeção quebrada, canais autorizados.

### Modo biblioteca (proof por objeção)
```
/cases-imperatriz --biblioteca
```
Exporta biblioteca cruzando cases × objeções. Trecho pronto pra colar em copy.

---

## ESTRUTURA DOS 8 BLOCOS

1. **Apresentação** — nome, nicho, cidade/estado, foto, tempo na Travessia
2. **ANTES** — faturamento, horas trabalhadas, dor central, o que tentou
3. **Virada** — porta destravada, skill chave, tempo até primeiro resultado
4. **DEPOIS** — faturamento atual, multiplicador, horas, NPS, recompra, time
5. **Proof stack** — prints, vídeos, mensagens, reconhecimento público
6. **Frase-pegada** — 1 frase original da mentorada, sem retoque
7. **Aplicação** — em qual copy vira proof, qual objeção quebra, pra qual público
8. **Autorização** — termo de uso assinado, canais autorizados, prazo, anonimato

Detalhamento completo em `ESTRUTURA-CASE-PADRAO.md`.

---

## HIERARQUIA DE PROOF (7 NÍVEIS)

Do mais fraco ao mais forte:

1. Texto puro
2. Texto + número
3. Texto + número + data
4. Print autorizado da fonte oficial (Stripe/Hotmart/Kiwify/banco)
5. Vídeo curto da mentorada (15-60s)
6. Vídeo longo + storytelling (3-10 min)
7. Reconhecimento público externo (palco, mídia, citação por autoridade)

Case nota 1000 tem **3+ níveis simultâneos**, sendo pelo menos 1 do nível 4+.

Detalhamento em `PROOF-STACK-HIERARQUIA.md`.

---

## CLASSIFICAÇÃO DE CASES

| Classe | Critério | Onde pode usar |
|--------|----------|----------------|
| **Diamante** | 5+ níveis de proof, vídeo longo, palco | Tudo (ad, VSL, livro, palco principal) |
| **Ouro** | 4 níveis, print + vídeo curto | Página, e-mail, VSL, carrossel |
| **Prata** | 3 níveis, print autorizado | Página, e-mail, post |
| **Bronze** | 2-3 níveis sem print | Apenas e-mail interno e WhatsApp morno |
| **Depoimento** | < 3 níveis, sem proof robusto | Não rotular como case — usar como side-quote |

---

## INTEGRAÇÃO COM O ECOSSISTEMA TATA

```
gates-imperatriz / tatou-2.0
        ↓ (detecta proof point)
cases-imperatriz --captar
        ↓
cases-imperatriz --validar
        ↓
dossie-mentorada (atualiza profile 17-cases)
        ↓
        ├── bestseller-book (case → capítulo)
        ├── skill-pagina-vendas (case → seção)
        ├── analise-anuncio-1000 (case → VSL)
        ├── email-sequence (case → e-mail)
        ├── linkedin-empire (case → post)
        └── palco-digital (case → slide)
```

**Skills relacionadas:**
- `dossie-mentorada` — armazena cases no profile 17-cases
- `tatou-2.0` — dispara captação
- `gates-imperatriz` — valida pipeline e proof point
- `analise-anuncio-1000` — analisa VSL pronta com case
- `headline-imperatriz` — usa frase-pegada como hook
- `mecanismo-unico` — case prova mecanismo
- `voz-humana-br` — valida voz da mentorada na frase-pegada

---

## ESTRUTURA DE ARQUIVOS

```
cases-imperatriz/
├── SKILL.md                          ← Cérebro (sempre carregado)
├── README.md                         ← Este arquivo
├── ESTRUTURA-CASE-PADRAO.md          ← 8 blocos detalhados com perguntas
├── PROOF-STACK-HIERARQUIA.md         ← 7 níveis de proof + critérios
├── APLICACAO-POR-CANAL.md            ← Templates de copy por canal
├── FORMULARIO-AUTORIZACAO.md         ← Termo de uso de imagem
└── EXEMPLOS-CASES-COMPLETOS.md       ← 3 cases ficcionais nota 1000
```

---

## REGRAS DURAS (a skill não negocia)

1. **Nunca inventa** case ou número
2. **Nunca arredonda** pra cima
3. **Nunca publica** sem termo assinado
4. **Nunca retoca** frase-pegada
5. **Nunca rotula** depoimento como case
6. **Nunca mistura** cases ("uma aluna minha…") — sempre nominal
7. **Nunca usa** case fora do canal autorizado no termo
8. **Nunca extrapola** prazo declarado
9. **Sempre cruza** por nicho pra evitar repetição
10. **Sempre marca** objeções quebradas
11. **Sempre versiona** quando mentorada evolui
12. **Sempre confirma** proof point antes de captar

---

## COMPARTILHAMENTO

Skill de **uso interno do escritório Tata**. Mentoradas não recebem cópia — mas **resultam** dela como protagonistas. Cases prontos podem ser entregues à mentorada como ativo dela (presente do programa).

---

## VERSIONAMENTO

- **v1.0** (atual) — 8 blocos, 7 níveis de proof, 5 modos, integração ecossistema
- **v1.5** (planejado) — auto-deteção de KPI verde via dashboard-imperatriz
- **v2.0** (planejado) — biblioteca cruzada por mecanismo único + temperatura
- **v3.0** (planejado) — tracking de qual case converteu em qual canal (loop ROI)

---

## PILAR 7 NA TRAVESSIA

Cases-imperatriz é a operadora do **Pilar 7 (Tribo)**. Os 7 pilares da Travessia Imperatriz:

1. Identidade
2. Fluxo (gates-imperatriz)
3. Execução (raci-imperatriz)
4. Receita
5. Time
6. Narrativa
7. **Tribo (cases-imperatriz)** ← este pilar

Sem Tribo viva e documentada, os outros 6 pilares não convertem em escala — porque mercado estágio 4+ não compra mais promessa, compra prova.

---

**Método Imperatriz de Cases — propriedade intelectual Tata Gonçalves.**

> Caso real > promessa. Sem cases, narrativa é fé. Com cases, narrativa é convicção.
