# Crise Imperatriz

**Pilar 5 (Governanca) da Travessia Imperatriz Tata Goncalves.**

Imperio grande tem crises grandes. Sem protocolo, mentorada paralisa, perde dinheiro, perde reputacao. Esta skill entrega o playbook ja decidido — pra quando o cerebro em panico nao consegue decidir bem.

---

## O que faz

- **Ativa playbook de crise em curso** (8 tipos cobertos): ban Meta/Google, processo judicial, vazamento LGPD, saida de socia, post negativo viral, conta zerada (Hotmart/Eduzz/banco), fornecedor critico que some, funcionaria-chave que sai sem aviso.
- **Simula crise** pra stress test do imperio.
- **Audita** quais protecoes ja existem (score 0-100).
- **Previne** com roadmap 90 dias customizado por perfil.

---

## Filosofia

> **Crise nao evitada vira ruina. Crise com protocolo vira historia.**

A skill assume tres verdades:

1. **Cerebro em panico decide mal.** Decisao boa foi tomada antes — pelo playbook.
2. **As primeiras horas valem mais que as proximas semanas.** Janela perdida = guerra perdida.
3. **Crise e teste de governanca, nao de copy.** Vence-se com contrato, advogada de retainer, conta backup, BM secundaria.

---

## Como usar

### Crise EM CURSO (acionamento imediato)
```
/crise-imperatriz --ativar ban-meta
/crise-imperatriz --ativar processo-judicial
/crise-imperatriz --ativar vazamento-dados
/crise-imperatriz --ativar socia-sai
/crise-imperatriz --ativar post-viral
/crise-imperatriz --ativar conta-zerada
/crise-imperatriz --ativar fornecedor-some
/crise-imperatriz --ativar time-quebra
```

A skill cronometra, entrega 3 proximos passos com responsavel sugerido, da templates de comunicacao prontos, lista o que NAO fazer e agenda check-in.

### Stress test (sem crise real, treinando)
```
/crise-imperatriz --simular ban-meta
```

Cenario realista com numeros do imperio, mentorada responde o que faria, skill diagnostica gaps.

### Auditoria preventiva
```
/crise-imperatriz --auditar
```

Roda checklist nas 8 crises. Output: score por crise + score consolidado + top 5 gaps a fechar nos proximos 30 dias.

### Plano preventivo customizado
```
/crise-imperatriz --prevenir
```

Roadmap 90 dias com responsavel, custo e prazo. Le `dossie-mentorada` e `perfil-mentorada` pra customizar.

---

## Os 8 tipos de crise cobertos

| # | Crise | Tempo critico |
|---|-------|---------------|
| 1 | Ban Meta/Google | 24h primeiras |
| 2 | Processo judicial (cliente / trabalhista) | 48h primeiras |
| 3 | Vazamento de dados (LGPD) | 72h legais |
| 4 | Socia/socio sai | 30-90 dias |
| 5 | Post negativo viral | 4h primeiras |
| 6 | Conta zerada (Hotmart/Eduzz/banco) | 7-14 dias |
| 7 | Fornecedor critico some | 7-30 dias |
| 8 | Time interno quebra | 30 dias |

Detalhes em `OS-8-PLAYBOOKS.md`.

---

## Estrutura de arquivos

```
crise-imperatriz/
├── SKILL.md                      # filosofia + 4 modos + regras duras
├── README.md                     # voce esta aqui
├── OS-8-PLAYBOOKS.md             # playbook detalhado por crise
├── PROTOCOLO-COMUNICACAO.md      # templates de mensagem
├── CHECKLIST-PREVENCAO.md        # protecoes a ter ANTES
└── EXEMPLOS-CASOS.md             # 3 simulacoes resolvidas
```

---

## Integracao com a Travessia

```
Disparador automatico:
/tatou-2.0  detecta sintoma  →  /crise-imperatriz --ativar [tipo]

Cadeia preventiva:
/perfil-mentorada + /dossie-mentorada
        ↓
/crise-imperatriz --auditar
        ↓
/crise-imperatriz --prevenir
        ↓
/raci-imperatriz (quem executa)
        ↓
/calendario-imperatriz (plano 90 dias)
```

**Skills adjacentes:**
- `/shield` — protecao tecnica continua (codigo, infra, dados)
- `/security-audit` — auditoria de seguranca pontual
- `/scale-audit` — auditoria de prontidao pra escala
- `/raci-imperatriz` — executor (quem faz cada protecao)
- `/gates-imperatriz` — validacao de portas (Pilar 2)
- `/tatou-2.0` — detector e despachante

---

## Regras duras (a skill nao negocia)

1. **Nao invento conselho juridico.** Em crise judicial/LGPD, manda pra advogada.
2. **Nao recomendo brigar publicamente** com cliente em post viral.
3. **Nao minto** em comunicacao publica.
4. **Nao recomendo apagar prova.**
5. **Nao recomendo usar advogado da familia** em processo de cliente.
6. **Sempre cronometra** o tempo critico.
7. **Sempre separa fato de narrativa.**
8. **Sempre atualiza** `CHECKLIST-PREVENCAO.md` apos cada crise vivida.

---

## Como compartilhar com mentoradas

Copiar a pasta `crise-imperatriz/` pra `~/.claude/skills/` da mentoranda. Skill vira disponivel via `/crise-imperatriz`.

**Atencao:** essa skill so funciona bem se a mentorada ja tiver `dossie-mentorada` e `perfil-mentorada` preenchidos. Caso contrario, rodar primeiro `/anamnese-mentorada`.

---

## Versionamento

- **v1.0** (atual, 2026-05) — 8 crises, 4 modos, integracao Travessia
- **v1.5** (planejado) — banco de casos reais por nicho
- **v2.0** (planejado) — alerta proativo (le sinais fracos antes da crise)

---

**Metodo Imperatriz de Crise — propriedade intelectual Tata Goncalves.**
