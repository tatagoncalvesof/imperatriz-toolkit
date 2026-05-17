# Validador — 7 princípios Buzan

Aplica este checklist ANTES de renderizar. Se algum falhar, corrige o mapa.

## Os 7 princípios

### 1. Centro forte (1-3 palavras OU emoji+palavra)

❌ Falha:
- "Estratégia completa de marketing para 2026"
- "Como vender mais usando funis"

✅ Passa:
- "🎯 Marketing 2026"
- "Funil"
- "💜 Império IA"

**Como corrigir:** identifica a essência. Se o tema é frase longa, extrai 1-3 palavras-chave.

---

### 2. Uma palavra-chave por nó (em ramos e sub-ramos)

❌ Falha:
- "Como criar uma página de captura que converte"
- "Estratégia de aquecimento durante 7 dias"

✅ Passa:
- "Página de captura" → sub: "converte"
- "Aquecimento" → sub: "7 dias"

**Exceção:** folhas finais (último nível) podem ter frase se for citação, dado, ou exemplo concreto.

**Como corrigir:** quebra frase em pai + filho.

---

### 3. Hierarquia balanceada

Nenhum ramo principal pode ter:
- 3x mais sub-ramos que outro
- Sub-ramos quando outros ramos não têm

❌ Falha:
```
Ramo A: 12 sub-ramos
Ramo B: 2 sub-ramos
Ramo C: 1 sub-ramo
```

✅ Passa:
```
Ramo A: 5 sub-ramos
Ramo B: 4 sub-ramos
Ramo C: 4 sub-ramos
```

**Como corrigir:** quebra ramo gigante em 2 ou agrupa ramos pequenos.

---

### 4. Máximo 7 ramos principais

Lei de Miller (7±2 itens na memória de trabalho).

❌ Falha: 9 ramos principais
✅ Passa: 5-7 ramos principais

**Como corrigir:** agrupa ramos relacionados em categorias mais amplas.

---

### 5. Máximo 4 níveis de profundidade

Acima disso, vira organograma — perde função de mapa mental.

❌ Falha:
```
Root → Ramo → Sub → Sub-sub → Sub-sub-sub → Folha
```

✅ Passa:
```
Root → Ramo → Sub → Folha
```

**Como corrigir:** se nível 5+ existe, simplifica ou move pra nota separada.

---

### 6. Cor por ramo principal

Cada ramo principal ganha cor única. Sub-ramos herdam a cor do pai.

❌ Falha: tudo na mesma cor
✅ Passa: 5-7 cores únicas, uma por ramo

**Como corrigir:** atribui paleta:
- Vermelho: problema/dor
- Laranja: atenção/objeção
- Amarelo: oportunidade/idea
- Verde: resultado/positivo
- Azul: informação/dados
- Roxo: centro/identidade
- Turquesa: ação/próximos passos

---

### 7. Conexões cruzadas (mínimo 2 quando faz sentido)

Mapa sem conexões é só árvore. Insight emerge das conexões.

❌ Falha: nenhuma conexão cruzada
✅ Passa: 2+ conexões com label explicando relação

**Como corrigir:** roda validador `conexoes-cruzadas.md` (separado).

## Output do validador

Reporte assim:

```
Buzan 7 princípios:
  ✓ Centro forte (1-3 palavras)
  ✓ Palavras-chave únicas
  ✗ Hierarquia balanceada — Ramo "Tráfego" tem 12 sub, "Oferta" tem 2
  ✓ Máximo 7 ramos
  ✓ Máximo 4 níveis
  ✓ Cor por ramo
  ✗ Conexões cruzadas — apenas 0 identificadas

Status: ❌ FALHA — corrigir antes de renderizar
```

Se status = FALHA, **corrige automaticamente** e re-valida.
