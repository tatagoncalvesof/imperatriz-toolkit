# Copy Analyzer — Sistema de Scoring

> Sistema completo de analise e pontuacao de copy de vendas.
> Baseado na Equacao de Persuasao de Bencivenga + analise secao por secao.

---

## EQUACAO DE PERSUASAO BENCIVENGA

**Score = (Urgencia x Relevancia x Prova x Desejo) / Friccao**

Cada elemento pontuado de 1 a 10:

---

### URGENCIA (1-10)

| Faixa | Descricao |
|-------|-----------|
| 1-3 | Sem pressao de tempo, prazos vagos |
| 4-6 | Alguma escassez mas generica ("vagas limitadas" sem numero) |
| 7-8 | Escassez especifica com numeros e prazo real |
| 9-10 | Multiplas camadas de urgencia (prazo + vagas limitadas + bonus expirando + aumento de preco) |

**Como aumentar:** Adicionar numeros especificos, prazos reais, timer de contagem regressiva, secao "custo de esperar"

---

### RELEVANCIA (1-10)

| Faixa | Descricao |
|-------|-----------|
| 1-3 | Generica, poderia ser para qualquer pessoa |
| 4-6 | Menciona publico-alvo mas de forma ampla |
| 7-8 | Especifica para segmento do publico, usa a linguagem deles |
| 9-10 | Parece escrita pessoalmente para UMA pessoa, usa frases exatas que ela diria internamente |

**Como aumentar:** Usar tecnica de "leitura de mente", verbalizar pensamentos internos entre aspas, descrever rotina diaria com precisao

---

### PROVA (1-10)

| Faixa | Descricao |
|-------|-----------|
| 1-3 | Afirmacoes sem evidencias |
| 4-6 | Alguns depoimentos, numeros vagos |
| 7-8 | Depoimentos especificos com resultados, exibicao de credenciais, estudos de caso |
| 9-10 | Multiplos tipos de prova sobrepostos (social + autoridade + resultados + logica + demonstracao) |

**Como aumentar:** Adicionar numeros especificos, antes/depois, depoimentos com nome, prints, logos de credenciais

---

### DESEJO (1-10)

| Faixa | Descricao |
|-------|-----------|
| 1-3 | Features listadas, sem conexao emocional |
| 4-6 | Beneficios mencionados mas genericos |
| 7-8 | Visualizacao vivida do futuro, gatilhos emocionais, transformacao de identidade |
| 9-10 | Leitor SENTE a transformacao, multiplos angulos do Sexy Canvas ativados, resultado dos sonhos cristalino |

**Como aumentar:** Adicionar secoes de visualizacao, angulos Sexy Canvas, transformacao de identidade, "um dia na vida" depois

---

### FRICCAO (1-10, MENOR E MELHOR)

| Faixa | Descricao |
|-------|-----------|
| 1-3 | Processo facil, garantia forte, multiplas opcoes de pagamento, sem confusao |
| 4-6 | Alguns passos pouco claros, garantia fraca, opcoes de pagamento limitadas |
| 7-8 | Processo complexo, sem garantia, unica opcao de pagamento |
| 9-10 | CTA confuso, custos ocultos, sem garantia, checkout complicado |

**Como diminuir:** Simplificar CTA, adicionar garantia, adicionar opcoes de pagamento, adicionar FAQ abordando duvidas do processo

---

## SCORING SECAO POR SECAO

Para cada secao da pagina, pontuar:

1. **Clareza** (1-10): A mensagem e entendida instantaneamente?
2. **Emocao** (1-10): Dispara a emocao-alvo?
3. **Especificidade** (1-10): Ha detalhes concretos, nao afirmacoes vagas?
4. **Fluxo** (1-10): Leva naturalmente a proxima secao?
5. **Objecao** (1-10): Aborda/quebra uma objecao especifica?

---

## CHECKLIST DE OBJECOES

Toda pagina de vendas DEVE abordar estas objecoes:

- [ ] **"E caro demais"** → Ancoragem de preco + projecao de ROI + opcoes de pagamento
- [ ] **"Nao sei se funciona pra mim"** → Depoimentos de perfis similares + garantia
- [ ] **"Nao tenho tempo"** → Mostrar que o investimento de tempo e pequeno / mostrar tempo ECONOMIZADO
- [ ] **"Ja tentei outras coisas"** → Explicar POR QUE isso e diferente (mecanismo)
- [ ] **"Nao confio em voce"** → Autoridade + credenciais + prova social
- [ ] **"Posso fazer sozinho"** → Mostrar custo/tempo do DIY vs. caminho guiado
- [ ] **"Preciso pensar"** → Urgencia + custo de esperar + garantia remove risco
- [ ] **"Meu [conjuge/socio] nao vai concordar"** → Matematica de ROI + resumo facil de compartilhar

---

## MAPA DE EMOCOES

Mapeamento da jornada emocional. O padrao ideal:

```
Secao 1 (Hero):        CURIOSIDADE + ESPERANCA    ████████░░
Secao 2 (Problema):    RECONHECIMENTO + DOR       ██████████
Secao 3 (Amplificar):  URGENCIA + MEDO            █████████░
Secao 4 (Historia):    EMPATIA + CONFIANCA        ████████░░
Secao 5 (Transformar): DESEJO + ASPIRACAO         █████████░
Secao 6 (Oferta):      CLAREZA + VALOR            ████████░░
Secao 7 (Preco):       ALIVIO + LOGICA            ███████░░░
Secao 8 (Garantia):    SEGURANCA + CONFIANCA      ████████░░
Secao 9 (CTA):         URGENCIA + DECISAO         █████████░
```

---

## CHECK DE LEGIBILIDADE

- **Frases:** Media de 15-20 palavras (PT-BR)
- **Paragrafos:** Maximo 3-4 linhas
- **Nivel de leitura:** Equivalente a 6o-8o ano
- **Espacamento:** Generoso entre secoes
- **Negrito/destaques:** Apenas frases-chave, sem exagero
- **CTAs:** Minimo 3 ao longo da pagina, maximo 6

---

## INTERPRETACAO DO SCORE FINAL

| Score | Significado |
|-------|-------------|
| 9-10 | Excepcional — pronta para deploy e teste |
| 7-8 | Forte — ajustes menores melhorariam |
| 5-6 | Media — precisa de melhorias especificas (listar quais) |
| 3-4 | Fraca — reescrita significativa necessaria em secoes especificas |
| 1-2 | Problemas fundamentais — estrategia pode estar errada, reconsiderar framework |
