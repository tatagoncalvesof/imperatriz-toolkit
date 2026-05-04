# Mecanismo Unico — Skill Proprietaria Tata Goncalves

Motor de criacao e auditoria de **Mecanismo Unico** nota 1000 baseado no **Metodo Imperatriz de Mecanismo Unico** — combinacao proprietaria de:

- **Schwartz** (Breakthrough Advertising — New Mechanism como resposta ao estagio 3+)
- **Bencivenga** (scoring de credibilidade + proof stack)
- **23 criterios proprios** (13 estruturais + 10 estrategicos)
- **Adaptacao Brasil** (estagios de mercado + regulacao + gatilhos culturais)

---

## O QUE ELA FAZ

Recebe briefing do teu negocio/produto e gera **mecanismo unico nota 1000** com:

- **Causa raiz especifica** (nomeavel, falsificavel, contraintuitiva)
- **Vilao externo** (real, legalmente seguro, libertador)
- **Nome proprietario** (testado em 5 validacoes)
- **Metafora explicativa** (6 tipos + Teste da Avo)
- **Proof stack hierarquico** (3+ tipos de evidencia)
- **Sequencia de funcionamento** (3-5 passos ordenados)
- **Razao do fracasso alheio** (por que outros falham mecanicamente)
- **Oponibilidade** (o que nao e)
- **Elevator pitch** (100 palavras, 30 segundos)
- **Diagrama visual** (desenhavel em guardanapo)
- **Storyline de descoberta** (5 atos, 3 minutos falados)
- **Validacao contra 23 criterios**

---

## COMO USAR

### Modo padrao (completo)
```
/mecanismo-unico

[cola copy/briefing ou descreve produto]
```
Entrevista + diagnostico + 10 candidatos + validacao nota 1000.

### Modo express
```
/mecanismo-unico express

[briefing rapido]
```
10 candidatos gerados rapido, sem entrevista extensa.

### Modo auditar (mecanismo existente)
```
/mecanismo-unico auditar

[cola teu mecanismo atual com nome + descricao]
```
Passa teu mecanismo pelos 23 criterios e entrega score + gaps.

### Modo mentoria (pedagogico pra aluna)
```
/mecanismo-unico mentoria

[briefing]
```
Explica cada criterio com profundidade didatica + "aula embutida".

---

## PRE-REQUISITOS IDEAIS

Nao obrigatorios, mas elevam qualidade:

1. **Briefing 360 preenchido** — rodar `/briefing-copy-360` antes
2. **Copy existente** — a skill le e extrai contexto do que ja existe
3. **Entender estagio de sofisticacao do mercado** (`/maestro-trafego` pode ajudar)

Se nada disso existir, a skill entra em **modo entrevista** (15 perguntas em 5 blocos) antes de gerar.

---

## INTEGRACAO COM O ECOSSISTEMA TATA

**Ordem ideal no fluxo de copy:**

```
/briefing-copy-360          (briefing geral)
       ↓
/mecanismo-unico            ← VOCE ESTA AQUI
       ↓
/headline-imperatriz        (headline por temperatura)
       ↓
/copywriting ou /skill-copy-ads-ptbr    (corpo da copy)
       ↓
/bencivenga-method          (scoring final)
       ↓
/analise-anuncio-1000       (diagnostico pos-lancamento)
```

**Por que ANTES de `/headline-imperatriz`:** headline-imperatriz exige mecanismo declarado em mercado estagio 3+. Sem mecanismo, ela recusa gerar headline de promessa simples.

---

## ESTRUTURA DE ARQUIVOS

```
mecanismo-unico/
├── SKILL.md                         ← Cerebro (sempre carregado)
├── OS-13-ELEMENTOS.md               ← 13 criterios estruturais obrigatorios
├── OS-10-ESTRATEGICOS.md            ← 10 criterios de elite
├── OS-7-ARQUETIPOS-NARRATIVOS.md    ← Templates de apresentacao
├── FORMULAS-NOMENCLATURA.md         ← 8 formulas + 5 testes de nome
├── METAFORAS-QUE-CONVERTEM.md       ← 6 tipos + Teste da Avo
├── ANTI-PATTERNS-MECANISMO.md       ← 11 erros fatais + antidoto
├── ADAPTACAO-BR.md                  ← Estagios BR + regulacao
├── TEMPLATE-STORYLINE-DESCOBERTA.md ← 5 atos pra storyline pessoal
└── README.md                        ← Este arquivo
```

---

## OS 23 CRITERIOS AVALIADOS

### 13 Estruturais (obrigatorios — sem qualquer, mecanismo e fraco)
1. Causa raiz especifica
2. Vilao externo
3. Nome proprietario
4. Metafora explicativa
5. Prova cientifica/empirica
6. Sequencia de funcionamento
7. Razao do fracasso alheio
8. Especificidade ultra-granular
9. Hierarquia de evidencia (proof stack)
10. Diagrama visual
11. Oponibilidade
12. Acessibilidade (teste do elevador)
13. Proprietariedade

### 10 Estrategicos (elevam pra elite)
14. Arquetipo narrativo declarado
15. Linguagem-ancora (binding language)
16. Storyline de descoberta
17. Gatilhos psicologicos embedded
18. Compatibilidade Schwartz
19. Encaixabilidade no funil
20. Pattern interrupt mensuravel
21. Defensibilidade juridica
22. Arquitetura de versionamento
23. Vinculacao ao posicionamento pessoal

### Scoring
- 13/13 estruturais = **mecanismo pronto pra rodar**
- 13 + 5 estrategicos = **mecanismo nota 1000**
- 13 + 10 estrategicos = **mecanismo lendario** (ativo de imperio)

---

## REGRAS DURAS (a skill nao negocia)

1. **Nao inventa estudo, dado ou caso** — se nao existe, sinaliza gap
2. **Nao gera mecanismo vago** ("metodo revolucionario")
3. **Nao nomeia antes de testar** os 5 testes de nomenclatura
4. **Nao entrega sem causa especifica**
5. **Nao entrega sem vilao real**
6. **Nao recomenda** mecanismo que viola regulacao BR
7. **Nao copia** gringo literal — adapta
8. **Nao gera** que contradiz cultura do publico
9. **Sempre le** contexto existente antes de entrevistar
10. **Sempre sinaliza** gaps quando score < 13/13 estrutural
11. **Sempre valida** nome contra busca Google + INPI
12. **Sempre oferece** storyline de descoberta

---

## COMO COMPARTILHAR COM MENTORANDAS

### Opcao 1 — Copiar pasta
```bash
cp -r ~/.claude/skills/mecanismo-unico /caminho/da/mentoranda/.claude/skills/
```

### Opcao 2 — Zipar e enviar
```bash
cd ~/.claude/skills/
zip -r mecanismo-unico.zip mecanismo-unico/
```
Envia o zip, mentoranda extrai em `~/.claude/skills/`.

### Opcao 3 — Git repo privado
Subir num repo privado, mentorandas clonam com permissao.

---

## PAR COM HEADLINE IMPERATRIZ

Essa skill e a **irma gemea** de `/headline-imperatriz`:
- `/mecanismo-unico` gera o **COMO** (mecanismo)
- `/headline-imperatriz` gera **como apresentar** (headlines por temperatura)

Juntas sao o motor completo de copy nota 1000 da Tata.

---

## VERSIONAMENTO

- **v1.0** (atual) — 23 criterios, 4 modos, 9 fases, integracao Tata ecosystem
- **v1.5** (planejado) — base de mecanismos vencedores BR por nicho
- **v2.0** (planejado) — feedback loop com performance de ads
- **v3.0** (planejado) — auto-sugestao de evolucao v1 → v2 → v3

---

## FILOSOFIA DA SKILL

> **Promessa diz O QUE. Mecanismo diz COMO. No Brasil 2026, so o COMO converte.**

Mecanismo Unico nao e marketing. E **ativo estrutural de marca**. Quem tem mecanismo paga 1/3 do CPA de quem nao tem. Quem tem mecanismo registrado e defendido escala sem limite.

Metodo Imperatriz de Mecanismo Unico — propriedade intelectual Tata Goncalves.
