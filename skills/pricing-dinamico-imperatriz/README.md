# Pricing Dinamico Imperatriz

Skill da **Porta G (Garantia)** + **Porta Y (Yield)** da Travessia Imperatriz Tata Goncalves.

> **Preco nao e tabela. E sistema vivo.**

Trata pricing como camada estrategica viva — recomenda janelas de aumento, splits de oferta, ancoragens R$X-R$Y-R$Z, simula receita esperada e entrega 3 cenarios (Conservador/Realista/Agressivo) calibrados por capacidade, posicionamento, concorrencia, custos, sazonalidade e elasticidade historica.

---

## O que essa skill faz (e o que NAO faz)

### Faz
- Diagnostica saude do pricing atual (taxa de ocupacao, margem, revenue gap)
- Gera 3 cenarios de preco com formulas explicitas
- Calcula janela de aumento ativa (gatilho automatico em slot >80%)
- Monta tabela de ancoragens (R$X alvo, R$Y valor real, R$Z concorrencia)
- Simula receita esperada aplicando elasticidade historica
- Cruza com `dossie-mentorada` profile 11 (oferta) + 16 (KPIs)
- Salva output estruturado em JSON pra reuso

### NAO faz
- Nao calcula custo unitario do zero (e papel de `/pricing-strategy`)
- Nao escreve copy de oferta (e papel de `/skill-oferta-irresistivel`)
- Nao reposiciona marca (e papel de `/luxe-empire`)
- Nao monta pitch de fechamento (e papel de `/high-ticket-strategist`)
- Nao inventa elasticidade ou caso (regra dura)

---

## Quando usar

| Situacao | Modo |
|----------|------|
| Mentorada chegou na Porta G — primeira oferta | `--gerar` |
| Revisita anual (Porta Y) | `--gerar` |
| Agenda 80%+ cheia | `--janela` |
| "E se eu cobrar R$X?" | `--simular` |
| "Como ancoro o preco em copy?" | `--ancorar` |
| Bateu meta de receita, quer recalibrar | `--gerar` |
| Ex-cliente quer renovar | `--janela` (consulta stock pricing) |

---

## Modos de uso

```bash
/pricing-dinamico-imperatriz --gerar [nome]
# 3 cenarios completos (conservador/realista/agressivo)

/pricing-dinamico-imperatriz --simular [nome] [preco]
# Simula receita esperada num preco-alvo

/pricing-dinamico-imperatriz --janela [nome]
# Calcula proxima janela de aumento ativa

/pricing-dinamico-imperatriz --ancorar [nome]
# Gera tabela de ancoragens R$X-R$Y-R$Z pra copy
```

---

## Inputs obrigatorios (8 variaveis)

A skill **nao gera cenario sem essas 8 variaveis**. Le do `dossie-mentorada` se existir, senao pergunta:

1. **Capacidade** (slots/mes que aguenta entregar)
2. **Faturamento atual** (media 3 ultimos meses)
3. **Meta** (12 meses)
4. **Posicionamento** (Princesa/Duquesa/Marquesa/Condessa)
5. **Concorrencia direta** (3-5 nomes + precos + diferenciais)
6. **Custos fixos + variaveis** (pra calcular margem minima)
7. **Sazonalidade** (mes forte / mes fraco)
8. **Elasticidade historica** (subiu preco antes? perdeu quanto volume?)

Bonus: **stock pricing** (cliente antigo paga preco antigo? renovacao tem desconto?).

---

## Output

Salvo em `~/imperio/mentoradas/[nome]/pricing-dinamico-[trimestre].json`.

Resumo legivel impresso na tela com:
- Diagnostico (3 indicadores)
- 3 cenarios lado a lado
- Janela ativa
- Tabela de ancoragens
- Stock pricing (cliente novo / renovacao / ex-cliente)
- Recomendacao final + 4 proximos passos

---

## Filosofia central

> Tabela estatica e foto. Sistema vivo e filme.

Tres principios:
1. **Capacidade dita preco** — slot >80% = +10% automatico
2. **Ancoragem precede numero** — R$X sozinho e caro; R$X depois de R$Y parece barato
3. **Elasticidade revela teto** — historico mostra quanto o publico aguenta antes de cair volume

---

## Integracao com a Travessia

```
/dossie-mentorada (profile 11 + 16)
       v
/pricing-strategy (base mecanica — 1 vez)
       v
/pricing-dinamico-imperatriz   <-
       v
/luxe-empire (se agressivo)
       v
/skill-oferta-irresistivel (atualizar copy)
       v
/high-ticket-strategist (pitch)
       v
/gates-imperatriz (validar Porta G ou Y)
```

**Ciclos:**
- **Porta G inicial** — 1 vez (ao construir oferta)
- **Porta Y** — revisita anual obrigatoria
- **Sob demanda** — capacidade cheia / bate meta / sazonalidade / ex-cliente retorna

---

## Diferenca vs /pricing-strategy

| Skill | Foco | Output |
|-------|------|--------|
| `/pricing-strategy` | Base mecanica (custos, modelos) | Tabela fundamentada |
| `/pricing-dinamico-imperatriz` | Camada estrategica (janelas, splits, ancoragens) | Sistema vivo |

Sempre rode `/pricing-strategy` antes (uma vez). Depois rode `/pricing-dinamico-imperatriz` em ciclos.

---

## Como compartilhar com mentorandas

Copie a pasta `pricing-dinamico-imperatriz/` pra `~/.claude/skills/` da mentorada. Skill vira disponivel via `/pricing-dinamico-imperatriz`.

Pre-requisitos no ambiente da mentorada:
- `/dossie-mentorada` instalado e profile 11 + 16 preenchidos
- `/pricing-strategy` instalado (base)
- Pasta `~/imperio/mentoradas/[nome]/` existe

---

## Arquivos de referencia

- `SKILL.md` — instrucoes principais (filosofia, 4 modos, 7 fases, regras duras)
- `OS-3-CENARIOS.md` — formulas detalhadas dos 3 cenarios
- `JANELAS-DE-AUMENTO.md` — matriz de gatilhos + cadencia + comunicacao
- `ANCORAGENS-ESTRATEGICAS.md` — 12 tecnicas de ancoragem premium BR
- `EXEMPLOS-PRICING.md` — 3 casos resolvidos completos

---

**Metodo Imperatriz de Pricing — propriedade intelectual Tata Goncalves.**
