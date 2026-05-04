---
name: briefing-copy-360
description: >
  Briefing 360° de Copy — Framework de Extração Pré-Escrita em 5 níveis
  hierárquicos (Essência → Atores → Contexto → Estratégia → Arsenal).
  FORÇA o copywriter a pensar antes de escrever. Bloqueia a progressão
  sem o nível anterior preenchido. Use quando o usuário quiser "escrever
  copy", "criar página de vendas", "fazer briefing de copy", "antes de
  escrever copy", "preparar copy pra novo produto", "research de copy",
  "extrair essência da copy", "copy pra novo lançamento", ou antes de
  invocar /copywriting, /skill-pagina-vendas, /skill-copy-builder. Output
  final: BRIEFING.md completo + handoff pra /copywriting.
---

# Briefing 360° de Copy — Framework de Extração Pré-Escrita

Este skill é o **filtro obrigatório** antes de qualquer copy ser escrita. Funciona como um funil hierárquico que impede escrita de copy em briefing raso/furado.

## Princípio fundamental

> **80% do trabalho de copy acontece ANTES da primeira palavra ser escrita.**

Copywriter nota 1000 não escreve primeiro e pesquisa depois. Ele pesquisa em 5 níveis hierárquicos até ter clareza absoluta da ESSÊNCIA — só então escreve.

Este skill existe para garantir que a Tata (e qualquer mentorada) **nunca pule essa etapa**.

## Quando usar

- Usuário pede pra escrever copy, página de vendas, VSL, email, anúncio
- Antes de invocar `/copywriting`, `/skill-pagina-vendas`, `/skill-copy-builder`, `/skill-sexy-canvas`
- Quando está começando um novo produto/lançamento
- Quando a copy existente não converte (briefing estava errado)
- Quando a mentorada traz "quero criar copy" sem research feito

## Regra inviolável

**Você NÃO ESCREVE COPY dentro deste skill.** Este skill apenas EXTRAI o briefing. A copy é delegada depois pra `/copywriting` ou skill apropriada com o briefing completo como input.

Se o usuário pedir "me escreve a copy", responda: *"Primeiro vamos preencher o Briefing 360° — sem ele a copy vira chute. Depois eu passo pra skill de escrita com briefing sólido."*

## Hierarquia de 5 níveis

```
NÍVEL 1 — ESSÊNCIA
NÍVEL 2 — ATORES
NÍVEL 3 — CONTEXTO
NÍVEL 4 — ESTRATÉGIA
NÍVEL 5 — ARSENAL
        ↓
    COPY (outra skill)
```

**Ordem é sagrada.** Um nível superior LOCK-a o inferior. Não pode preencher Nível 4 (Framework) sem saber Nível 3 (Consciência do avatar).

## Fluxo de execução

### Passo 0 — Setup

Pergunte ao usuário:
1. **Nome do produto/oferta** (para nomear o arquivo)
2. **Nicho/vertical** (infoproduto, serviço, produto físico, mentoria, SaaS)
3. **Canal principal da copy** (landing page, VSL, email, anúncio, WhatsApp)
4. **Já tem material de research? Onde está?** (PDFs, transcrições, entrevistas, concorrentes mapeados)

Se o usuário não tem NADA de research, avise: *"Vamos precisar fazer research em tempo real. Isso pode demandar leituras, análises de concorrentes, entrevistas com clientes reais. Topa?"*

### Passo 1 — NÍVEL 1: ESSÊNCIA

Este é o fundamento. Se aqui está raso, TUDO DESMORONA.

**Perguntas obrigatórias:**

#### 1.1 — Big Idea
> "Qual é a UMA ideia grande, nova, contrária ao senso comum, que organiza toda a copy? Se você só pudesse transmitir uma frase, qual seria?"

**Critério de aceite:** a resposta deve conter um REFRAME (ex: "Não são seguidores que vendem, são os MODELOS de stories" — quebra a crença de que precisa de muitos seguidores). Se for genérica ("aprenda a vender online"), REJEITE e peça mais profundidade.

#### 1.2 — Transformação prometida
> "De que estado (X) o avatar sai → pra que estado (Y) ele chega? Use palavras concretas, não abstratas."

**Formato esperado:** `De [estado atual concreto] → para [estado desejado concreto]`
Ex: "De 'posta stories e ninguém compra' → para 'posta stories e cliente chega no direct pedindo pagamento'"

**Critério de aceite:** ambos os estados devem ser CONCRETOS. "Sem sucesso → com sucesso" é inaceitável.

#### 1.3 — Inimigo comum
> "Contra QUEM ou O QUÊ a copy vai lutar? Qual é o vilão?"

Pode ser: um concorrente, uma crença limitante, uma indústria, um comportamento. Ex: gurus que ensinam "precisa de 100k seguidores", algoritmo do Instagram, estratégias de "engajamento tóxico".

**Se algum desses 3 itens estiver vazio ou raso, PARE. Não avance pro Nível 2.** Mande o usuário pesquisar mais (leituras, entrevistas, análise de copy que converte no nicho — pode invocar `/analise-anuncio-1000` em concorrentes).

---

### Passo 2 — NÍVEL 2: ATORES

#### 2.1 — Produto
Capture EXATAMENTE:
- Nome do produto + subtítulo
- Formato (curso, mentoria, serviço, produto físico)
- Entregáveis concretos (módulos, sessões, volume de aulas, duração)
- Bônus reais (lista completa, com valor individual se for ancorar)
- Preço + parcelamento + preço à vista
- Garantia (prazo + condições)
- Mecanismo proprietário (o MÉTODO único — tem nome? tem etapas?)
- Suporte (grupo, comunidade, acompanhamento)
- Resultados esperados em X tempo

#### 2.2 — Criador/Autoridade
- Nome completo + como é conhecido
- História de origem (o "por que você pode ensinar isso")
- Números relevantes (seguidores, alunos, faturamento, anos)
- Onde já esteve (mídia, palcos, podcasts, MBAs, citações)
- Posicionamento em 1 frase ("eu sou o especialista em ____")
- Tom de voz natural (formal, casual, ácido, maternal, educador, provocador)

#### 2.3 — Avatar
Use dimensões de persona profunda (pode invocar `/skill-persona-profunda` se precisar de mais profundidade):
- Demografia (idade, gênero, profissão, renda, localização)
- Estado atual concreto (o que ele FAZ hoje — não adjetivos)
- 3 dores específicas (não "ser frustrada" — mas "posta stories e só 5 pessoas respondem")
- 3 desejos específicos (não "ter sucesso" — mas "fazer R$10k em 90 dias só pelos stories")
- 3 coisas que ele JÁ TENTOU e falharam
- 3 medos + 3 objeções
- Linguagem literal que ele usa (palavras exatas, gírias, termos)
- Crença limitante central ("eu não vendo porque...")
- Transformação que busca

**Critério de aceite:** resposta com "mulheres empreendedoras" é INSUFICIENTE. Precisa ter especificidade de "médicas que vendem consulta particular no Instagram, faturam R$8-15k/mês, querem escalar pra R$30k sem se expor mais". Se for genérico, invoque `/skill-persona-profunda`.

---

### Passo 3 — NÍVEL 3: CONTEXTO

#### 3.1 — Mercado
- Top 3-5 concorrentes diretos (nome + oferta + preço)
- Top 3 promessas que o mercado JÁ CANSOU de ouvir
- Espaço vazio que ninguém está ocupando
- Se possível, invocar `/analise-anuncio-1000` em 1-2 copies de concorrentes pra mapear padrões

#### 3.2 — Consciência (Eugene Schwartz)
Em que estágio ESTÁ O AVATAR no momento em que encontra a copy?

- **Nível 1 — Unaware:** não sabe que tem problema → copy precisa EDUCAR e criar consciência
- **Nível 2 — Problem Aware:** sabe que tem problema, não sabe solução → copy apresenta o mecanismo
- **Nível 3 — Solution Aware:** sabe que existe solução, não conhece seu produto → copy diferencia o seu
- **Nível 4 — Product Aware:** conhece seu produto, não comprou → copy justifica o preço e reduz risco
- **Nível 5 — Most Aware:** só precisa do empurrão → copy curta, oferta + escassez + CTA

**A copy MUDA completamente baseada nisso.** Registre o estágio e justifique.

#### 3.3 — Sofisticação do mercado (Schwartz)

- **Stage 1:** mercado virgem — promessa simples funciona ("emagreça")
- **Stage 2:** mercado aceita promessa maior ("emagreça 10kg em 30 dias")
- **Stage 3:** precisa de mecanismo único ("com método japonês de 5 min")
- **Stage 4:** mecanismo + nova variação ("método japonês melhorado com ciência")
- **Stage 5:** experiência completa (identidade + filosofia + comunidade)

Brasil infoproduto geralmente está em Stage 4-5. Luana SPE está em Stage 4 (mecanismo "modelos validados" + nova variação do mercado de stories).

#### 3.4 — Mapa de objeções
Liste no mínimo 8 objeções específicas do nicho. Não genéricas. Formate:

| # | Objeção literal (como o avatar pensa) | Gatilho por trás | Como vai ser quebrada na copy |
|---|---------------------------------------|------------------|-------------------------------|
| 1 | "Não tenho tempo pra mais um curso" | Sobrecarga / procrastinação | Com prova "1 cliente converte paga o curso" |
| 2 | "Meu nicho é diferente" | Exceção / ceticismo | Lista diversa de nichos atendidos |
| ... | ... | ... | ... |

---

### Passo 4 — NÍVEL 4: ESTRATÉGIA

#### 4.1 — Ângulo de ataque
Qual é a PRIMEIRA coisa que a copy vai dizer? Qual é o gancho que para o scroll/atenção?

Tipos de ângulos clássicos:
- Contraste ("enquanto todos fazem X, faça Y")
- Segredo ("o que ninguém te contou sobre X")
- Provocação ("você está fazendo X errado")
- História ("a história de [alguém] que [resultado específico]")
- Pergunta ("você sabia que...?")
- Número ("os 3 erros que impedem X")

**Escolha 1 ângulo principal.** Justifique por que esse ângulo converge com o Nível 3 (consciência do avatar).

#### 4.2 — Jornada emocional
Qual o mapa emocional do leitor do topo ao fundo da página?

```
Estado inicial: [ex: cética, cansada, já decepcionada com cursos]
    ↓
Abertura: [gancho que a faz parar]
    ↓
Identificação: [ela se reconhece no problema]
    ↓
Epifania: [momento "a-ha" com a Big Idea]
    ↓
Esperança + prova: [depoimentos mostram que é possível]
    ↓
Desejo: [ela se vê com o resultado]
    ↓
Objeção quebrada: [FAQ + garantia]
    ↓
Decisão: [CTA final]
```

Marque os 3-5 picos emocionais da jornada (surpresa, medo, esperança, urgência, alívio).

#### 4.3 — Framework escolhido

Qual estrutura vai reger a copy?

- **AIDA** (Attention, Interest, Desire, Action) — copy curta
- **PAS** (Problem, Agitate, Solution) — direct response clássico
- **PASTOR** (Problem, Agitate, Solution, Testimony, Offer, Response) — landing completa
- **4Ps** (Promise, Picture, Proof, Push) — emocional
- **StoryBrand** — narrativa com o avatar como herói
- **Bencivenga** — 40 princípios de direct response
- **Sexy Canvas** — método brasileiro de tráfego direto (7 pecados)

**Escolha 1.** Justifique por que ele serve ao Nível 3 + 4.1.

---

### Passo 5 — NÍVEL 5: ARSENAL

#### 5.1 — Prova
Inventário completo de provas disponíveis:
- Depoimentos (quantidade, formato — vídeo/print/texto, autor nominal ou anônimo)
- Cases detalhados (antes → depois, com números)
- Screenshots (conversas no direct, pagamentos, resultados, dashboards)
- Números do criador (seguidores, alunos, faturamento, anos)
- Menções na mídia
- Certificações ou selos

Se a prova é ESCASSA, apontar: "aumentar depoimentos antes da copy virar é prioridade 1."

#### 5.2 — Oferta completa
- Stack de valor (tabela com o que entra na oferta + valor individual + valor total empilhado)
- Ancoragem de preço (valor total → preço real → parcelamento)
- Urgência/escassez (vaga limitada, bônus expirando, preço subindo, data limite)
- Garantia (prazo + condição + nome criativo se tiver)
- Bônus de ação rápida (se tem, quais)

Pode invocar `/stack-closer`, `/skill-oferta-irresistivel` e `/garantia-irresistivel` pra aprofundar.

#### 5.3 — CTAs + tom + gatilhos táticos
- CTAs principais (variações por intenção: descoberta, ação, garantia)
- Micro-copy de CTAs (ex: "Acesso imediato. Garantia de 7 dias.")
- Gatilhos de identidade ("mesmo sem X", "mesmo sendo Y")
- Palavras-chave do avatar (literais — tiradas de entrevistas)
- Palavras proibidas (termos que o avatar REJEITA)
- Pronomes dominantes (você / eu / nós)
- Tempo verbal dominante (presente urgente / futuro concreto)

---

## Passo 6 — CHECKLIST FINAL "Está pronto pra escrever?"

Só avance pra copy se todos esses itens tiverem resposta FIRME:

- [ ] Big Idea em 1 frase clara e provocativa
- [ ] Transformação concreta (X → Y) com palavras específicas
- [ ] Inimigo comum identificado
- [ ] Produto 100% mapeado (entregáveis, preço, bônus, garantia, mecanismo)
- [ ] Criador com autoridade documentada (números + provas)
- [ ] Avatar com 3 dores + 3 desejos + 3 objeções específicas + linguagem literal
- [ ] Concorrentes mapeados (top 3 + promessas saturadas)
- [ ] Nível de consciência definido (1-5 Schwartz)
- [ ] Nível de sofisticação definido (1-5 Schwartz)
- [ ] Mapa de objeções com 8+ itens
- [ ] Ângulo de ataque escolhido + justificado
- [ ] Jornada emocional com 6-8 pontos + 3-5 picos
- [ ] Framework de copy escolhido + justificado
- [ ] Inventário de prova feito (mesmo que com gaps apontados)
- [ ] Stack de valor + ancoragem + urgência + garantia definidos
- [ ] CTAs + tom + gatilhos táticos listados

**Se algum item tiver "não sei", "depois", "geral" — PARE. Não escreva.**

## Passo 7 — Geração do arquivo BRIEFING.md

Depois de preencher todos os níveis, gere o arquivo `BRIEFING-<slug-do-produto>.md` no diretório de trabalho do projeto. Use o template em `template.md` (mesma pasta desta skill).

## Passo 8 — Handoff

Pergunte ao usuário:
> "Briefing completo. Quer que eu chame `/copywriting` agora pra escrever a copy com esse briefing como input? Ou outra skill (/skill-pagina-vendas, /skill-copy-builder, /skill-sexy-canvas, /bencivenga-method)?"

Nunca escreva a copy dentro deste skill. Delegue.

## Skills parceiras (para aprofundar cada nível)

| Nível | Skill complementar |
|-------|-------------------|
| 2.3 Avatar | `/skill-persona-profunda` |
| 3.1 Mercado | `/analise-anuncio-1000` (em concorrentes) |
| 3.4 Objeções | `/skill-copy-builder` (investigativa) |
| 4.3 Framework Bencivenga | `/bencivenga-method` |
| 4.3 Framework Sexy Canvas | `/skill-sexy-canvas` |
| 5.2 Stack | `/stack-closer` + `/skill-oferta-irresistivel` |
| 5.2 Garantia | `/garantia-irresistivel` |

## Casos de referência

Dois briefings completos preenchidos (engenharia reversa) para consulta:

- **`exemplo-luana-spe.md`** — Story para Enriquecer (Luana Carolina) — infoproduto evergreen, Schwartz 3, avatar feminino, framework PASTOR
- **`exemplo-operacao-claude-code.md`** — Operação Claude Code (Thales Laray) — evento ao vivo B2B, Schwartz 2-3, avatar empresário, framework PASTOR + ancoragem financeira dupla

Quando preencher um briefing novo, consulte os dois casos pra entender diferentes arquétipos de copy (B2C emocional vs. B2B racional).

## Ética da skill

- Nunca pule níveis mesmo que o usuário peça
- Nunca aceite respostas rasas só pra avançar
- Sempre questione quando algo estiver genérico
- Sempre lembre: se o briefing é raso, a copy é chute, a conversão é baixa, a mentorada perde dinheiro
