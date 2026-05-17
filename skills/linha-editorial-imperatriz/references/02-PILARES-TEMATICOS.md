# 02 — Pilares Temáticos

## Regra de ouro

**3 a 5 pilares. Nem mais, nem menos.**

- Menos de 3 → marca monotemática, audiência cansa em 30 dias
- Mais de 5 → marca dispersa, audiência não sabe quem você é
- Sweet spot operacional: **4 pilares com proporção 40-30-20-10**

## Como descobrir os pilares (não inventar)

Pilar **bom** vem do cruzamento de 4 fontes que a skill já tem em mãos:

```
Pilar = (Dor real do cliente ideal)
        ∩ (Transformação prometida no posicionamento)
        ∩ (Mecanismo único nomeado)
        ∩ (Território onde a mentorada tem autoridade declarada)
```

Pilar **ruim** vem de:
- ❌ "Conteúdo de valor" (genérico, todo mundo posta)
- ❌ "Bastidores" (formato, não tema)
- ❌ "Inspiração" (vazio)
- ❌ "Educacional" (categoria, não pilar)
- ❌ Colado de competidor (não é teu)

## Anatomia de um pilar bem-formado

Cada pilar entregue pela skill tem:

| Campo | Regra | Exemplo bom | Exemplo ruim |
|---|---|---|---|
| **Nome** | 1-3 palavras, evocativo | "Câmara da Conversão" | "Conversão" |
| **Descrição** | 1 frase que explica o território | "Como o que você fala determina quem entra na sala" | "Sobre conversão" |
| **Proporção** | % do volume mensal (soma=100) | 40% | "Bastante" |
| **Cliente que serve** | Qual recorte do cliente ideal | "Mentorada que vende high-ticket e perde lead na proposta" | "Todo mundo" |
| **Dor que cura** | Dor específica nomeada | "Mandar áudio pra cliente e não fechar" | "Ajuda em vendas" |
| **Mecanismo que ativa** | Qual peça do método entra | "Etapa 3 do Sistema Imperatriz de Vendas" | "Meu método" |
| **5 micro-temas** | Sub-tópicos pra postar | (lista de 5) | Lista vazia |
| **Formato dominante** | Qual canal/formato performa pra esse pilar | "Carrossel IG + post LinkedIn" | "Tudo serve" |
| **Não-objetivo** | O que esse pilar NÃO faz (pra não inflar) | "Não faz teoria de vendas. Só execução." | (em branco) |

## Distribuição típica por Porta

A proporção entre pilares **muda** dependendo da Porta atual da Travessia:

| Porta | Pilar Autoridade | Pilar Cliente | Pilar Mecanismo | Pilar Cultura |
|---|---|---|---|---|
| **A-D** (Descoberta/Identidade/Marca/Posicionamento) | 50% | 30% | 10% | 10% |
| **E-H** (Oferta/Promessa/Pitch/Preço) | 30% | 30% | 30% | 10% |
| **I-N** (Funil/Tráfego/Lançamento/Calendário) | 20% | 30% | 35% | 15% |
| **O-T** (Vendas/Operação/Time/Receita) | 25% | 25% | 30% | 20% |
| **U-Z** (Escala/Sucessão) | 30% | 20% | 20% | 30% |

A skill calibra automaticamente baseado na Porta lida do dossiê.

## Pilar-cultura (o quarto pilar quase esquecido)

A maioria das mentoradas para em 3 pilares (autoridade + cliente + mecanismo) e esquece do **pilar cultura** — que é o que diferencia uma marca de uma "produtora de conteúdo".

Pilar cultura inclui:
- Manifesto declarado em ação (não em texto bonito)
- Bastidor de decisão estratégica (com aprendizado nomeado)
- Posicionamento sobre temas adjacentes (sem virar opinião sobre tudo)
- Linguagem própria sendo construída (nomenclatura, ritual, símbolo)
- Time aparecendo em ação

A skill **força** o pilar cultura na Porta U+ (escala) — sem ele, a marca trava em "pessoa que ensina X" e nunca vira movimento.

## Validação dos pilares antes de prosseguir

Antes de fechar os pilares (etapa 3 do `--gerar`), a skill checa:

1. ✅ Cada pilar passa no teste do "alguém me confunde com X" — se o pilar é tão genérico que serve pra 10 concorrentes, refazer
2. ✅ Soma das proporções = 100% (sem arredondamento errado)
3. ✅ Nenhum pilar começa com "Conteúdo de", "Sobre", "Tudo sobre"
4. ✅ Pelo menos 1 pilar nomeia o mecanismo único da mentorada
5. ✅ Pelo menos 1 pilar fala diretamente da dor do cliente ideal (não da solução)
6. ✅ Cliente da mentorada conseguiria identificar qual pilar serve pra ele em 5 segundos

Se algum check falha, a skill **não avança** — pede ajuste.

## Exemplo de pilares mal-formados → bem-formados

| ❌ Antes (genérico) | ✅ Depois (específico) |
|---|---|
| "Educacional" | "Câmara da Conversão" — como o que você fala na proposta decide a venda |
| "Bastidores" | "Decretos da Imperatriz" — decisões estratégicas que mudaram a operação esse mês |
| "Inspiração" | "Outras Imperatrizes" — mentoradas que romperam teto + o que destravou |
| "Vendas" | "O Pitch que Vendeu" — anatomia de uma venda real da semana, frase a frase |
| "Vida pessoal" | "Bastidor de Soberana" — escolhas de tempo, dinheiro e relação que sustentam o trono |

## Saída esperada da etapa de pilares

JSON parcial gravado durante `--gerar`:

```json
"pilares": [
  {
    "nome": "Câmara da Conversão",
    "descricao": "Como o que você fala na proposta decide a venda",
    "proporcao_pct": 40,
    "cliente_que_serve": "Mentorada high-ticket que perde lead na proposta",
    "dor_que_cura": "Mandar áudio pra cliente e não fechar",
    "mecanismo_que_ativa": "Etapa 3 — Pitch Imperatriz",
    "micro_temas": ["...", "...", "...", "...", "..."],
    "formato_dominante": "Carrossel IG + post LinkedIn",
    "nao_objetivo": "Não faz teoria. Só execução."
  },
  ...
]
```
