# Anamnese Mentorada — Skill Proprietaria Tata Goncalves

**Porta de entrada da Travessia Imperatriz.** Primeira skill que roda quando uma mentorada nova fecha contrato. Coleta dados em 8 blocos pra abastecer o ecossistema inteiro de mentoria.

---

## O QUE ELA FAZ

Conduz a coleta estruturada de **37 campos** em **8 blocos** sobre a mentorada nova. Entrega em 4 formatos (formulario HTML, roteiro de call, pre-populacao automatica, auditoria) e salva o resultado em JSON local pra ser consumido por todas as outras skills da Travessia.

**Os 8 blocos:**

1. **Historico pessoal** — quem ela e, de onde veio, como chegou ate a Tata
2. **Negocio atual** — onde ela esta hoje (faturamento, time, produto, audiencia)
3. **Tentativas anteriores** — o que ja tentou (mentorias, cursos, ferramentas IA)
4. **Dores especificas** — o que tira o sono dela (top 3)
5. **Objetivos** — onde quer chegar (curto/medio/longo prazo + vida ideal)
6. **Recursos** — tempo, dinheiro, equipe, background tecnico
7. **Identidade** — nicho, posicionamento, voz, diferencial
8. **Expectativas** — o que espera da Travessia, anima e receia

Resultado: arquivo `~/imperio/mentoradas/[slug]/00-anamnese.json` validado contra schema, com alertas de risco e score de completude.

---

## OS 4 MODOS

### `--formulario` (mentorada preenche offline)
```
/anamnese-mentorada --formulario nome="Carolina Mendes"
```
Gera HTML standalone com voz Tata, entrega por email/WA, mentorada exporta JSON e devolve.

### `--call` (Tata conduz pre-call)
```
/anamnese-mentorada --call nome="Marina Lopes"
```
Roteiro markdown imprimivel pra Tata levar pra call (8 blocos, 35 perguntas, 90 minutos cronometrados).

### `--auto` (deep-research pre-popula)
```
/anamnese-mentorada --auto nome="Renata Ferraz" instagram="@renataferrazpilates"
```
Pre-popula campos via deep-research. O que nao confirma marca como `pendente: true`. Nunca inventa.

### `--validar` (audita anamnese existente)
```
/anamnese-mentorada --validar slug="camila-aguiar"
```
Le o JSON, gera score por bloco, lista gaps, recomenda proxima acao.

---

## PRE-REQUISITOS

- Diretorio `~/imperio/mentoradas/` (cria automatico se nao existir)
- (Opcional) Acesso a `/deep-research` se for usar `--auto`
- (Opcional) Severino logado pra delegar envio de formulario

---

## INTEGRACAO COM O ECOSSISTEMA TATA

Anamnese e a **camada 0** da Travessia. Tudo depende dela.

```
/anamnese-mentorada            ← VOCE ESTA AQUI (ato 0)
       ↓
/perfil-mentorada              (classifica o tipo)
       ↓
/dossie-mentorada              (cria ficha viva)
       ↓
/imperio-diagnostico           (FRIO + DOMINIO + PENTA)
       ↓
/celeste                       (plano estrategico)
       ↓
[execucao 6 meses]
```

**Skills que CONSOMEM anamnese:**
- `/perfil-mentorada`
- `/dossie-mentorada`
- `/imperio-diagnostico`
- `/celeste`
- `/headline-imperatriz` (bloco 7)
- `/copy-conversacional-dm` (blocos 2, 4, 7)

**Skills que ALIMENTAM anamnese (modo `--auto`):**
- `/deep-research`
- `/skill-persona-profunda`

---

## ESTRUTURA DE ARQUIVOS

```
anamnese-mentorada/
├── SKILL.md                  ← Cerebro (sempre carregado)
├── OS-8-BLOCOS.md            ← Perguntas literais + criterio de qualidade
├── FORMULARIO-HTML.md        ← Template HTML standalone (voz Tata)
├── SCHEMA-JSON.md            ← Schema do 00-anamnese.json
├── EXEMPLOS-PREENCHIDOS.md   ← 3 anamneses pra perfis distintos
└── README.md                 ← Este arquivo
```

E o output gerado:

```
~/imperio/mentoradas/
├── [slug-mentorada-1]/
│   └── 00-anamnese.json
├── [slug-mentorada-2]/
│   └── 00-anamnese.json
└── [...]
```

---

## INSTALACAO (USO INTERNO TATA E TIME)

Esta skill e **interna**. Roda na maquina da Tata e nas maquinas do time da Travessia (Severino, etc).

### Opcao 1 — Copiar pasta
```bash
cp -r /Users/tamiresgoncalves/Documents/travessia-imperatriz-site/skills-novas/anamnese-mentorada \
      ~/.claude/skills/anamnese-mentorada
```

### Opcao 2 — Symlink (recomendado pra dev)
```bash
ln -s /Users/tamiresgoncalves/Documents/travessia-imperatriz-site/skills-novas/anamnese-mentorada \
      ~/.claude/skills/anamnese-mentorada
```

### Opcao 3 — Git repo privado (time)
Subir num repo privado da Travessia, time clona com permissao.

Apos instalar, testar com:
```
/anamnese-mentorada --formulario nome="Teste"
```

Deve gerar HTML em `~/imperio/mentoradas/teste/formulario.html`.

---

## COMO COMPARTILHAR COM MENTORADAS

**ATENCAO:** mentoradas NAO instalam essa skill. Elas sao **objeto** dela.

O que vai pra mentorada:
- **HTML do `--formulario`** — ela preenche, exporta JSON, devolve
- **Resumo executivo** (opcional, no segundo encontro, como espelho)

O que NAO vai pra mentorada:
- JSON cru com alertas
- Score de completude
- Notas internas da Tata

---

## REGRAS DURAS

1. **Nao inventa dado.** Se nao tem informacao, marca `pendente: true`.
2. **Nao julga.** Coleta neutra. So fato.
3. **Nao gera plano.** Plano e do `/celeste`.
4. **Nao expoe dado sensivel.** Faturamento, intimidade — local only.
5. **Nao pula bloco.** Os 8 sao obrigatorios.
6. **Nao fecha sem dores top 3 e objetivo de 12 meses.**
7. **Sempre marca data, versao, modo de coleta.**

---

## VERSIONAMENTO

- **v1.0** (atual) — 8 blocos, 4 modos, 6 fases, integracao Travessia
- **v1.1** (planejado) — modo `--reentrar` pra mentorada que refaz
- **v1.5** (planejado) — pre-populacao via transcricao de webinar
- **v2.0** (planejado) — re-coleta automatica a cada 90 dias

---

## FILOSOFIA

> **Anamnese mal feita = mentoria mal feita. A Tata nao chuta. A Tata diagnostica.**

Anamnese vem da medicina: relato do paciente antes do tratamento. Sem anamnese boa, o medico erra remedio. Sem anamnese boa, a Tata erra plano de 6 meses.

Esta skill e o **ato 0** da Travessia Imperatriz. Sem ela, nao tem perfil, nao tem dossie, nao tem diagnostico, nao tem plano.

**Metodo Imperatriz de Anamnese — propriedade intelectual Tata Goncalves. Travessia Imperatriz 2026.**
