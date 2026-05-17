# gates-imperatriz

Skill que opera o **Pilar 2 (Fluxo)** da Travessia Imperatriz da Tata Gonçalves. Audita as 26 portas (A-Z) com critério objetivo, devolve diagnóstico por sintoma e recomenda rollback quando upstream está contaminado.

> Não é a Travessia. É o cobrador da Travessia.

## O que ela faz

- **Valida** se uma porta foi concluída de fato (não no achismo)
- **Diagnostica** sintomas e aponta porta-fonte upstream
- **Recomenda rollback** quando porta foi pulada/forçada
- **Calcula próxima porta** respeitando dependências
- **Lista ciclos recorrentes** vencidos (semanal, mensal, trimestral, anual)

## O que ela não faz

- Não escreve copy
- Não cria oferta
- Não monta funil
- Não dá coaching emocional
- Não substitui as skills de execução do ecossistema (delega pra elas)

## Modos

| Modo | Para quê |
|---|---|
| `--validar [nome] [porta]` | Auditar porta específica de uma mentorada |
| `--sintomas [nome]` | Receber sintomas e devolver porta-fonte provável |
| `--rollback [nome] [sintoma]` | Caminho de volta pra porta upstream contaminada |
| `--proxima [nome]` | Próxima porta liberada (respeitando dependências) |
| `--ciclos [nome]` | Ciclos recorrentes vencidos / em dia |

## Exemplos rápidos

```
/gates-imperatriz --validar Marina C
/gates-imperatriz --sintomas Joana
/gates-imperatriz --rollback Joana "tráfego caro"
/gates-imperatriz --proxima Marina
/gates-imperatriz --ciclos Joana
```

Ver `EXEMPLOS-VALIDACAO.md` pra um caso completo A→K de mentorada fictícia.

## Arquivos

- `SKILL.md` — manual operacional, modos, regras duras
- `GATES-POR-PORTA.md` — todas 26 portas com checklist objetivo
- `MAPA-DEPENDENCIAS.md` — grafo upstream/downstream + cascata
- `TROUBLESHOOTING-REVERSO.md` — 8 sintomas-âncora + matriz de confiança
- `CICLOS-RECORRENTES.md` — cadência + skill associada
- `EXEMPLOS-VALIDACAO.md` — casos reais por modo

## Integração

**Lê:** `/dossie-mentorada`
**Alimenta:** `/tatou-2.0`
**Coordena:** `/perfil-mentorada`, `/anamnese-mentorada`, `/voz-de-marca-builder`
**Aciona:** `/mecanismo-unico` (C), `/headline-imperatriz` (J), `/skill-pagina-vendas` (J), `/maestro-trafego` (K), `/copy-conversacional-dm` (G), `/imperatriz-das-vendas` (Q), `/reuniao-de-resultado` (Z)

## Como instalar

Copia a pasta `gates-imperatriz/` pra `~/.claude/skills/` da Tata ou da mentorada. Vira disponível via `/gates-imperatriz`.

```bash
cp -R gates-imperatriz ~/.claude/skills/
```

## Filosofia

> **Porta só fecha com evidência mensurável. Sintoma é sintoma, causa é porta. Pular porta gera dívida composta.**

Diagnóstico seco, próximo passo concreto, sem hype. A skill é o gate — a Travessia é a estrada.

---

**Travessia Imperatriz — propriedade intelectual Tata Gonçalves.**
