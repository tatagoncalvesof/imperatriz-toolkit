# MAPA DE DEPENDÊNCIAS — Upstream / Downstream / Cascata de contaminação

A Travessia Imperatriz é um grafo direcional. Algumas portas são INDEPENDENTES (rodam quando a mentorada quer). Outras são DEPENDENTES (não rodam sem upstream concluído). E todas as portas viram FONTE potencial de contaminação pra portas downstream — quando a mentorada força uma porta, ela paga o juro depois.

A skill usa este mapa pra:
1. Bloquear avanço quando upstream falhou
2. Calcular cascata reversa quando rollback é acionado
3. Identificar porta-fonte real quando sintoma aparece downstream

---

## REGRA DE LEITURA

- **→** significa "depende de" (esquerda depende da direita)
- Depender significa: a porta da esquerda NÃO PODE ser declarada concluída sem a porta da direita estar concluída antes
- Dependência soft (gera juros mas não bloqueia) é marcada com `(soft)`
- Dependência temporal (precisa de N dias rodando) é marcada com `(+Nd)`

---

## DEPENDÊNCIAS DURAS (bloqueiam avanço)

```
A — independente (porta de entrada)
B — independente (pode rodar em paralelo a A)
C — independente (mas idealmente após B)
D — independente (mas idealmente após C)
E → C, D
F → B, C
G → F
H — independente (técnica, pode rodar a qualquer momento)
I — independente (mas idealmente após E)
J → C, E, G
K → J, H
L → K (+30d)
M → J, K, O
N — independente (mas vira ciclo recorrente eterno após primeira execução)
O → F (soft) — fica obrigatório antes de M
P → E (soft) — pode rodar antes mas perde força
Q → F, G — não fecha sem programa pra time vender
R → F, G — não fecha sem oferta + programa pra avaliar
S → M, Q — só consegue trabalhar < 40h se funil + time autônomos
T → R (+90d)
U → F, P (soft) — comunidade só vira orgânica com programa + evento
V → M, Q (+6 meses)
W → C, J — termos próprios viram busca quando mecanismo + página rodam
X — independente (auditoria trimestral; pode rodar a qualquer momento depois de K)
Y → K (+12 meses) — margem só estabiliza com aquisição rodando há 12 meses
Z — independente (ciclo mensal; ativa após X primeira)
```

---

## GRAFO VISUAL (ASCII)

```
                  A (entrada)
                  |
                  v
                  B
                 / \
                v   v
                C    F  (F precisa de B+C)
               /|    |
              v v    |
              D E    G  (G precisa de F)
                |    |
                +----+
                     |
                     v
                     J  (J precisa de C+E+G)
                     |
            H -------+
                     |
                     v
                     K  (K precisa de J+H)
                    /|
                   v |
                   L (+30d) 
                   M (precisa também de O)
                  /|
            O ---+ |
                   v
                   Q (precisa de F+G)
                   R (precisa de F+G)
                   |
                   v
                   S (precisa de M+Q)
                   T (R+90d)
                   V (M+Q+6m)
                   Y (K+12m)
```

---

## CASCATA DE CONTAMINAÇÃO

Quando a mentorada força uma porta, a contaminação se propaga downstream. A skill detecta o padrão:

### Cascata C contaminada
- C força → E genérica → J fraca → K caro → L sem ajuste → M impossível
- Sintoma final: "tráfego não converte e não sei por que"
- Rollback: até C

### Cascata B contaminada
- B genérica → F mira público errado → G erra preço → R reembolso alto → T impossível
- Sintoma final: "vendi mas reembolsou tudo"
- Rollback: até B

### Cascata G contaminada
- G força (sem venda real teste) → J vende mal → K não fecha ROAS → L distorcido
- Sintoma final: "página converte mas não fecho preço"
- Rollback: até G

### Cascata F contaminada
- F sem piloto real → Q time treina errado → R onboarding falha → S burnout
- Sintoma final: "time não fecha e eu trabalho mais que antes"
- Rollback: até F

### Cascata J contaminada
- J com Bencivenga < 8 → K caro → L gargalo no clique → M sem maestria
- Sintoma final: "CPA disparou mês 2"
- Rollback: até J

### Cascata K contaminada
- K declarada antes de 30d → L mente sobre gargalo → M impossível
- Sintoma final: "achei que estava bem mas nada escala"
- Rollback: até K (espera os 30d)

### Cascata O contaminada
- O sem rotina firme → mentorada volta a responder → M volta atrás → S burnout
- Sintoma final: "não consigo desconectar"
- Rollback: até O

### Cascata R contaminada
- R sem onboarding → reembolso > 5% → T não funciona → Y instável
- Sintoma final: "margem oscila e cliente não volta"
- Rollback: até R

---

## CASCATA REVERSA (quando rollback é acionado)

Quando a skill manda voltar pra porta-fonte, ela também precisa avisar **quais portas downstream serão re-validadas** depois do rollback.

### Voltou pra C
- Re-validar: D, E, J, K, L, M, W

### Voltou pra B
- Re-validar: F, Q, R

### Voltou pra G
- Re-validar: J, R, T

### Voltou pra F
- Re-validar: G, Q, R, U

### Voltou pra J
- Re-validar: K, L, M

### Voltou pra K
- Apenas espera 30d e re-mede

### Voltou pra O
- Re-validar: M

### Voltou pra R
- Re-validar: T, Y

---

## PORTAS QUE VIRAM CICLO RECORRENTE

Algumas portas, depois de fechadas pela primeira vez, viram ciclo eterno:

| Porta | Cadência (após primeira execução) | Skill recorrente |
|---|---|---|
| N | Semanal | conteúdo do calendário editorial |
| L | Mensal | revisão de funil |
| Z | Mensal | melhoria + check de regresso |
| T | Trimestral | campanha de reativação |
| X | Trimestral | audit completo |
| Y | Anual | revisão de margem 12m |

Detalhes em `CICLOS-RECORRENTES.md`.

---

## INDEPENDENTES (podem rodar quando a mentorada quer)

- A, B, C, D, H, I, N, X (não dependem de upstream)

Mas atenção: **independente** ≠ **bom rodar antes**. C antes de B é tecnicamente possível mas a mentorada vai reescrever C depois. A skill avisa se a sequência for ineficiente.

---

## SEQUÊNCIA RECOMENDADA (caminho ótimo)

```
A → B → C → D → E → F → G → H → I → J → K → L → M
                                  ↘     ↘
                                   O    N (ciclo)
                                   ↓
                                   P → Q → R → S → T
                                                 ↓
                                                 U → V → W → X → Y → Z
```

Mas a skill respeita ordem que a mentorada já seguiu. Não força reset.

---

## REGRA DURA

A skill **não declara porta dependente como concluída** se a porta de upstream está parcial ou não passou. Não importa quão bonito o output downstream pareça. Upstream contaminado contamina tudo.

---

**Travessia Imperatriz — Pilar 2 (Fluxo). Propriedade intelectual Tata Gonçalves.**
