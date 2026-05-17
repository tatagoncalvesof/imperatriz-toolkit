---
name: skill-escala-ads
description: >
  Sistema de decisao para escalar, otimizar ou pausar campanhas de ads.
  Inclui decision trees, regras de escala (20%), kill rules (3x), deteccao de fadiga,
  playbooks de otimizacao, e cenarios de escala horizontal e vertical.
  Especializado no mercado brasileiro de infoprodutos e Meta Ads.
  Use quando o usuario pedir "escalar campanha", "otimizar ads", "pausar anuncio",
  "scaling", "kill rule", "escala de trafego", "quando aumentar budget",
  "campanha nao esta performando", "CPA subiu", "como escalar",
  ou qualquer decisao de otimizacao/escala de campanhas pagas.
---

# Sistema de Escala e Otimizacao de Ads

## Contexto
- **Foco:** Meta Ads + Google Ads
- **Mercado:** Infoprodutos, mentorias (Brasil)
- **Moeda:** BRL

## Processo

### 1. Diagnostico
Perguntar ao usuario:
- Campanha/plataforma em questao
- Metricas atuais (CPA, ROAS, CTR, frequencia, gasto)
- Meta de CPA/ROAS
- Budget atual
- Ha quanto tempo esta rodando
- Fase: learning, otimizado, escala

### 2. Decision Trees

#### Arvore Principal: O que Fazer com Esta Campanha?

```
PERGUNTA 1: A campanha tem conversoes?
│
├── NAO → PERGUNTA 2: Gastou mais que 3x CPA alvo?
│   ├── SIM → ❌ KILL (Pausar Imediatamente)
│   │         → Aplicar Kill Rule Protocol (ver secao 4)
│   └── NAO → ⏳ ESPERAR
│             → Campanha pode estar em Learning Phase
│             → Esperar ate gastar 3x CPA antes de decidir
│
└── SIM → PERGUNTA 3: CPA atual vs CPA alvo?
    │
    ├── CPA < Alvo (-10% ou mais) → PERGUNTA 4: Fase de aprendizado?
    │   ├── SIM (em Learning) → ⏳ ESPERAR aprendizado terminar
    │   └── NAO (saiu do Learning) → ✅ ESCALAR
    │       → Aplicar Escala Protocol (ver secao 3)
    │
    ├── CPA = Alvo (±10%) → 🔧 MANTER e OTIMIZAR
    │   → Testar novos criativos
    │   → Testar novos publicos
    │   → NAO mexer no budget
    │
    └── CPA > Alvo (+10% ou mais) → PERGUNTA 5: Ha quanto tempo?
        ├── < 7 dias → ⏳ ESPERAR (pode ser flutuacao)
        ├── 7-14 dias → 🔧 OTIMIZAR (ver secao 5)
        └── > 14 dias → ❌ KILL ou REFORMULAR
```

#### Arvore de Criativos: Manter ou Trocar?

```
PERGUNTA: O criativo esta performando bem?
│
├── CTR > meta E CPA < alvo → ✅ MANTER
│   → Monitorar frequencia
│   → Se frequencia > 4 → Expandir audiencia
│
├── CTR caiu > 20% em 14 dias → ⚠️ FADIGA
│   → Pausar criativo
│   → Substituir por nova versao
│   → Manter conceito mas mudar execucao (novo hook, novo visual)
│
├── CTR OK mas CPA alto → 🔧 PROBLEMA NO FUNIL
│   → Landing page pode ser o gargalo
│   → Testar nova LP antes de trocar criativo
│
└── CTR baixo desde inicio (< 0.5%) → ❌ KILL
    → Criativo nao ressoou
    → Testar conceito totalmente diferente
```

#### Arvore de Audiencia: Expandir ou Trocar?

```
PERGUNTA: A audiencia esta respondendo bem?
│
├── Frequencia < 3 E CPA < alvo → ✅ MANTER/ESCALAR
│
├── Frequencia 3-4 E CPA subindo → ⚠️ SATURANDO
│   → Opcao A: Adicionar novos criativos na mesma audiencia
│   → Opcao B: Expandir audiencia (LAL 1% → 3%)
│   → Opcao C: Escala horizontal (nova campanha mesmo publico)
│
├── Frequencia > 4 E CPA alto → 🔴 SATURADA
│   → Pausar audiencia
│   → Criar nova audiencia
│   → Testar Broad (se >50 conv/semana)
│
└── Audiencia nunca performou → ❌ KILL
    → Publico errado
    → Testar segmentacao diferente
```

### 3. Protocolo de Escala

#### Escala Vertical (Aumentar Budget)

```
PRE-REQUISITOS:
✅ Campanha fora da fase de aprendizado
✅ CPA < CPA alvo em > 10% por pelo menos 7 dias
✅ Minimo 50 conversoes na ultima semana
✅ Frequencia < 3 (audiencia nao saturada)
✅ Criativos com CTR estavel

REGRA DOS 20%:
→ Aumentar budget em EXATAMENTE 20%
→ Esperar 3-5 dias
→ Se CPA se manteve: repetir +20%
→ Se CPA subiu < 10%: repetir +20%
→ Se CPA subiu > 15%: PARAR e voltar ao budget anterior

EXEMPLO:
Budget atual: R$200/dia
Aumento 1 (Dia 1): R$240/dia → esperar 5 dias
Aumento 2 (Dia 6): R$288/dia → esperar 5 dias
Aumento 3 (Dia 11): R$346/dia → esperar 5 dias
...e assim por diante
```

**ATENCAO META ADS:**
- NUNCA aumentar mais que 20% de uma vez
- Aumento > 20% RESETA a fase de aprendizado
- Fim de semana: NAO mexer em budget (comportamento diferente)

#### Escala Horizontal (Diversificar)

```
QUANDO USAR:
→ Escala vertical atingiu teto (CPA sobe a cada aumento)
→ Audiencia principal saturada (frequencia > 4)
→ Quer testar novos angulos mantendo o que funciona

COMO FAZER:
1. DUPLICAR campanha vencedora
2. MUDAR 1 variavel:
   → Nova audiencia (ex: LAL 3% em vez de 1%)
   → Novo criativo (mesmo publico, diferente ad)
   → Novo posicionamento (Reels-only, Stories-only)
   → Nova geo (expandir estados/regioes)
3. Budget IGUAL ou menor que a original
4. Esperar 7 dias antes de julgar
5. Se funcionar: escalar verticalmente
```

#### Escala com Advantage+ (Meta)

```
PRE-REQUISITOS:
→ 50+ conversoes/semana na conta
→ Catalogo de produtos (se e-commerce)
→ Pixel + CAPI funcionando

COMO:
1. Criar campanha Advantage+ Shopping
2. Definir cap de clientes existentes (ex: 30%)
3. Budget inicial: 20% do budget total da conta
4. Subir TODOS os melhores criativos (nao filtrar)
5. Deixar o algoritmo otimizar
6. Avaliar apos 7 dias
```

### 4. Protocolo Kill (Pausar)

#### 3x Kill Rule
```
REGRA: Se gastou 3x o CPA alvo sem NENHUMA conversao → PAUSAR

EXEMPLO:
CPA alvo: R$50
Gasto sem conversao: R$150 → PAUSAR

APOS PAUSAR:
1. Identificar causa provavel:
   □ Criativo fraco (CTR < 0.5%)
   □ Audiencia errada (sem relevancia)
   □ Landing page com problema (bounce > 80%)
   □ Tracking quebrado (0 eventos no Pixel)
   □ Oferta sem atratividade

2. Corrigir a causa ANTES de reativar

3. NAO reativar a mesma campanha
   → Criar NOVA campanha com a correcao aplicada

4. Se 3 tentativas falharam com mesmo conceito:
   → Mudar abordagem completamente
   → Revisar oferta, publico, ou produto
```

#### Kill por Fadiga Criativa
```
REGRA: CTR caiu > 20% em 14 dias → PAUSAR criativo

APOS PAUSAR:
1. Anotar o que funcionou (hook, formato, conceito)
2. Criar nova versao mantendo o conceito mas mudando:
   → Novo hook (primeiros 3 segundos)
   → Nova thumbnail (imagem diferente)
   → Novo angulo visual (cenario, roupa)
   → Mesmo script, diferente entrega
3. Subir como AD NOVO (nao editar o antigo)
```

### 5. Protocolo de Otimizacao

#### Quando CPA Esta Alto (mas nao pra Kill)

```
PASSO 1: Diagnosticar onde esta o gargalo

METRICAS A CHECAR:
→ CTR baixo? → Problema no CRIATIVO
→ CTR ok mas bounce alto? → Problema na LANDING PAGE
→ CTR ok, bounce ok, mas sem conversao? → Problema na OFERTA
→ Tudo ok mas CPA alto? → Problema no PUBLICO (saturacao/relevancia)

PASSO 2: Aplicar correcao especifica

SE CRIATIVO:
→ Testar 3-5 novos criativos com hooks diferentes
→ Manter conceito vencedor, mudar execucao
→ Testar formato diferente (video → carrossel, imagem → video)

SE LANDING PAGE:
→ A/B test: headline, CTA, layout
→ Verificar velocidade (PageSpeed > 80)
→ Verificar mobile (60%+ do trafego)
→ Simplificar (menos campos, menos fricao)

SE OFERTA:
→ Testar preco diferente
→ Adicionar bonus
→ Mudar garantia (7 → 15 → 30 dias)
→ Testar angulo diferente (dor vs aspiracao)

SE PUBLICO:
→ Excluir sub-audiencias de baixa performance
→ Testar lookalike de compradores recentes (30d vs 180d)
→ Narrow: adicionar interesses extras
→ Expand: remover restricoes e deixar Advantage+
```

### 6. Cenarios Comuns + Solucoes

| Cenario | Diagnostico | Solucao |
|---------|-------------|---------|
| "CPA subiu 50% de repente" | Possivel fadiga, sazonalidade, ou competicao | Pausar criativos antigos, subir novos, verificar frequencia |
| "CPM disparou" | Sazonalidade (Nov-Dez), competicao, ou audiencia pequena | Expandir audiencia, verificar calendario, ajustar bid |
| "Muitos leads mas poucas vendas" | Qualidade do lead baixa ou funil de nurture fraco | Restringir audiencia, melhorar sequencia pos-lead, qualificar |
| "ROAS negativo no primeiro mes" | Normal para infoprodutos — backend compensa | Medir MER incluindo upsells e email, dar tempo |
| "Learning Limited" | Budget insuficiente ou muitos ad sets | Consolidar ad sets, aumentar budget, simplificar conta |
| "Frequencia > 5" | Audiencia esgotada | Renovar criativos, expandir audiencia, pausar 7 dias |
| "CTR alto mas CPA alto" | LP ou oferta com problema | A/B test LP, simplificar checkout, testar preco |
| "Campanha boa parou de funcionar" | Fadiga ou algoritmo reset | Duplicar em nova campanha, novos criativos, same publico |

### 7. Checklist de Otimizacao Semanal

```
TODA SEGUNDA-FEIRA:
□ Verificar CPA vs meta por campanha
□ Verificar frequencia por ad set
□ Identificar criativos com CTR caindo
□ Pausar o que gastou 3x CPA sem converter
□ Verificar budget: gastou tudo ou sobrou?
□ Anotar top 3 e bottom 3 performers
□ Decidir: escalar, manter, otimizar, ou kill

TODA SEXTA-FEIRA:
□ Subir criativos novos (se necessario)
□ Ajustar budget pra fim de semana (se aplicavel)
□ Revisar sequencias de email/WhatsApp
□ Preparar relatorio semanal
```

### 8. Tabela de Decisao Rapida

| CPA vs Meta | Frequencia | CTR Trend | Decisao |
|-------------|-----------|-----------|---------|
| < meta -10% | < 3 | Estavel/Subindo | ✅ ESCALAR +20% |
| < meta -10% | 3-4 | Estavel | ✅ Escalar + Novos criativos |
| < meta -10% | > 4 | Caindo | ⚠️ Escala horizontal (novo ad set) |
| ± meta 10% | < 3 | Estavel | 🔧 Manter + Testar novos criativos |
| ± meta 10% | 3-4 | Caindo | 🔧 Renovar criativos |
| ± meta 10% | > 4 | Caindo | ⚠️ Pausar audiencia, expandir |
| > meta +10% | Qualquer | Qualquer (< 7 dias) | ⏳ Esperar |
| > meta +10% | Qualquer | Caindo (> 7 dias) | 🔧 Otimizar (ver protocolo) |
| > meta +50% | Qualquer | Qualquer | ❌ KILL / Reformular |
| 3x meta | Zero conv. | Qualquer | ❌ KILL IMEDIATO |

## Output

Para cada analise de otimizacao/escala:
- `DECISAO-[CAMPANHA]-[DATA].md` — Diagnostico + decisao + plano de acao
- Justificativa baseada em dados
- Proximos passos claros e acionaveis
- Timeline de implementacao
