# EXEMPLOS DE VALIDAÇÃO — 1 caso por modo + caminho A→K de mentorada fictícia

Mentorada fictícia usada nos exemplos: **Marina Coelho**, nutricionista funcional (PHD-like persona), vende mentoria pra outros nutricionistas viverem só de online. Ticket alvo R$ 8.000. Começou Travessia em 2026-01-10.

Casos abaixo mostram como a skill responde em cada modo, com input e output reais.

---

## EXEMPLO 1 — Modo `--validar [nome] [porta]`

### Input
```
/gates-imperatriz --validar Marina C
```

### Contexto da Marina (lido do dossiê)
- Porta A concluída em 2026-01-15 (dossiê + perfil + voz + plano 90d ok)
- Porta B concluída em 2026-01-28 (persona "Carla Nutri 32a interior SP", ICP, anti-persona declarados)
- Porta C — declarada concluída em 2026-02-22 pela própria Marina
- Mecanismo nomeado: "Método R3 — Reset Ritmo Resultado"
- Storyline: gravou áudio de 60s, não vídeo

### Output da skill

```
# AUDIT PORTA C — Marina Coelho

## Critério objetivo de saída
Mecanismo único passa 13/13 critérios estruturais + storyline da descoberta gravada (vídeo, mínimo 90s).

## Checklist
- [X] Mecanismo construído via /mecanismo-unico — output salvo em 2026-02-18
- [~] Score estruturais: 11/13 (faltam: hierarquia de evidência, oponibilidade)
- [ ] Storyline em vídeo — Marina gravou só áudio de 60s
- [X] Nome "Método R3" passa nos 5 testes (WhatsApp ok, Google ok, fonético ok)

## Dependências upstream
- Porta B PASSOU (persona articulada em call de 2026-01-28)
- Porta A PASSOU

## Veredito
**PARCIAL — não pode declarar concluída**

## Ação seguinte
1. Rodar /mecanismo-unico modo auditar pra fechar os 2 critérios faltantes:
   - Hierarquia de evidência: precisa proof stack hierárquico (mín 3 tipos)
   - Oponibilidade: precisa frase "não é X, não é Y, não é Z. É R3."
2. Gravar storyline em vídeo de 90s+ (não áudio).
3. Re-submeter audit com /gates-imperatriz --validar Marina C

## Skill seguinte
/mecanismo-unico --auditar
```

---

## EXEMPLO 2 — Modo `--sintomas [nome]`

### Input
```
/gates-imperatriz --sintomas Marina

Marina diz: "Tata, meu CPA disparou. Estava em R$ 38, foi pra R$ 96 em 3 semanas.
ROAS caiu pra 1.4x. Página converte 2.1%. O que faço?"
```

### Output da skill

```
# DIAGNÓSTICO POR SINTOMA — Marina Coelho

## Sintomas declarados
- CPA passou de R$ 38 pra R$ 96 em 3 semanas
- ROAS caiu pra 1.4x (alvo 3x+)
- Conversão de página: 2.1%

## Sintoma-âncora identificado
Sintoma 1 — Tráfego caro / CPA alto / ROAS < 3x

## Portas-fonte candidatas

### ALTA confiança
- **Porta C (Causa)** — Mecanismo R3 está com PARCIAL (audit anterior identificou 11/13). Sem oponibilidade + hierarquia de evidência, copy não diferencia, leilão pune.
  → ação: fechar C primeiro (ver audit anterior)

- **Porta J (Jornada)** — Página com conversão 2.1% sugere Bencivenga < 8. Vale auditoria.
  → ação: rodar /bencivenga-method na página atual

### MÉDIA confiança
- **Porta H (Habitar)** — Tracking pode estar subestimando conversão. Validar Pixel + CAPI.
  → ação: 30min de check de tracking antes de mexer em ads

### BAIXA confiança
- **Porta K (Kombate)** — Otimização ruim de campanhas (provavelmente sintoma, não causa)
  → ação: só mexer depois de C e J

## Recomendação imediata
PAUSAR ESCALA por 7 dias. Fechar C (oponibilidade + hierarquia + storyline em vídeo). Re-rodar /mecanismo-unico --auditar. Em paralelo, validar tracking H (30min). Só voltar pra K depois.

## Próximo modo recomendado
/gates-imperatriz --rollback Marina "tráfego caro"
```

---

## EXEMPLO 3 — Modo `--rollback [nome] [sintoma]`

### Input
```
/gates-imperatriz --rollback Marina "tráfego caro"
```

### Output da skill

```
# ROLLBACK — Marina Coelho — sintoma: tráfego caro

## Porta-fonte
**Porta C (Causa)** — mecanismo R3 com 11/13 estruturais. Cascata C → J → K confirmada.

## Caminho de volta
1. **PAUSAR ESCALA em K imediatamente.** Mantém só campanhas-âncora com 30% do budget atual pra não perder dados.
2. **Refazer C** aplicando /mecanismo-unico --auditar:
   - Construir hierarquia de evidência (proof stack: lógico + científico + casuístico + autoridade)
   - Escrever oponibilidade ("Método R3 não é dieta, não é coaching, não é nutri tradicional. É reset hormonal por 3 fases.")
   - Gravar storyline em vídeo de 90s+
3. **Re-validar C** com /gates-imperatriz --validar Marina C → precisa sair PASSOU
4. **Revisitar J** (página deve absorver mecanismo atualizado): nova headline + bloco de mecanismo + diagrama. Re-score Bencivenga (alvo 8+).
5. **Voltar pra K** com criativo + página atualizados, esperar 30 dias pra re-medir.

## Critério de saída do rollback
- C com 13/13 estruturais
- J com Bencivenga ≥ 8
- 7 dias de tracking validado em H

## Esforço estimado
**Médio** — 10-14 dias de trabalho concentrado:
- C refazer: 2-3 dias (auditar + ajustar + gravar storyline)
- J reescrever: 3-4 dias (página + headline + revisão)
- Validar tracking: 0,5 dia
- Pausa em K: contínua durante o rollback

## Cascata reversa (downstream a re-validar)
- Porta D (Diferenciação) — depende de C atualizado
- Porta E (Estandarte) — ativos públicos provavelmente precisam refresh
- Porta J — re-audit obrigatório
- Porta K — espera +30 dias após J ok
- Porta W — termos do mecanismo atualizado entram no Google

## Skills a acionar nessa ordem
1. /mecanismo-unico --auditar
2. /headline-imperatriz (nova headline da J)
3. /skill-pagina-vendas (refresh página)
4. /bencivenga-method (re-score)
5. /maestro-trafego (relançar K depois)
```

---

## EXEMPLO 4 — Modo `--proxima [nome]`

### Input
```
/gates-imperatriz --proxima Marina
```

### Contexto
- A, B PASSOU
- C PARCIAL (audit anterior)
- D não rodou ainda
- E não rodou ainda
- F PARCIAL (programa estruturado mas piloto não rodou de ponta a ponta)
- G não rodou
- H PASSOU (site + tracking ok)
- J em PROGRESSO (rascunho de página)
- K em PROGRESSO (campanhas pausadas pelo rollback)

### Output da skill

```
# PRÓXIMA PORTA — Marina Coelho

## Status atual
- Última porta concluída sem ressalvas: H (2026-02-10)
- Portas em PARCIAL: C, F
- Portas em PROGRESSO: J, K
- Próxima porta óbvia (sequência): D

## Análise de dependências
- D não tem dependência dura, mas ganha força com C concluída — C ainda PARCIAL
- E depende de C + D — bloqueado
- F PARCIAL — piloto não rodou de ponta a ponta
- J depende de C + E + G — TRIPLO BLOQUEIO

## Recomendação
**NÃO AVANÇAR pra D ainda.** Caminho ótimo:

1. **Fechar C primeiro** (audit identificou 2 gaps — ver `--validar Marina C`)
2. **Fechar F** (rodar piloto de ponta a ponta — Marina mencionou ter 1 candidata pronta)
3. Depois D fica trivial (motivos vão sair direto do C atualizado)
4. E vira plug-and-play (brand book com mecanismo C + diferenciação D)
5. G entra
6. J relança com Bencivenga 8+
7. K destrava

## Ciclo recorrente vencido (pré-requisito antes de avançar)
- N (semanal) — última publicação 2026-04-25, atrasado 9 dias
  → rodar /voz-humana-br + publicar 3 peças esta semana ANTES de avançar travessia

## Skill seguinte
/mecanismo-unico --auditar (pra fechar C)

## Janela estimada
Se Marina executar com foco: 14-21 dias até K voltar a rodar com lastro.
```

---

## EXEMPLO 5 — Modo `--ciclos [nome]`

### Input
```
/gates-imperatriz --ciclos Marina
```

### Output da skill

```
# CICLOS RECORRENTES — Marina Coelho

## Vencidos (atenção imediata)

### N — Narrativa (semanal) — RISCO ALTO
- Última publicação: 2026-04-25
- Atrasado: 9 dias
- Cadência declarada: 3x/semana no Instagram
- Sintoma associado: 6 (conteúdo travado)
- Ação: rodar /voz-humana-br em 3 rascunhos guardados + publicar HOJE

### L — Laboratório (mensal) — RISCO MÉDIO
- Última revisão de funil: 2026-03-15
- Atrasado: 24 dias
- Sintoma associado: 1 (tráfego caro — JÁ APARECEU)
- Ação: rodar /ads-meta + /page-cro esta semana — confirma diagnóstico do rollback C/J

## Em dia
- Z (mensal) — última: 2026-04-30 — próxima: 2026-05-31
- X (trimestral) — primeira execução prevista: 2026-06-30 (fim do trimestre)

## Bloqueados (porta ainda não fechou primeira vez)
- T — depende de R+90d (Marina ainda não está em R)
- Y — depende de K+12 meses (Marina está em K há 4 meses)

## Recomendação de ordem
1. **N HOJE** (cadência crítica + relação com sintoma 6 latente)
2. **L esta semana** — vai confirmar gargalo do tráfego com dado e dar respaldo ao rollback
3. **Z no fluxo normal** (último útil do mês)

## Observação
Vencido em N + L + sintoma de tráfego caro = padrão clássico de mentorada que pulou C. O ciclo vencido aqui é sintoma do rollback necessário. Resolve C, ressincroniza N e L automaticamente.

## Skills por ciclo
- N: /voz-humana-br + /headline-imperatriz + /skill-mentoria-tata
- L: /ads-meta + /page-cro
- Z: /reuniao-de-resultado + /kaizen-improvement + /gates-imperatriz --validar
```

---

## CASO COMPLETO — Caminho A→K de Marina (linha do tempo fictícia)

Mentorada fictícia: **Marina Coelho** — nutricionista funcional, ticket alvo R$ 8.000.

### Linha do tempo

| Data | Porta | Evento | Status final |
|---|---|---|---|
| 2026-01-10 | A | Inicia Travessia, dossiê + perfil + voz + plano 90d | PASSOU |
| 2026-01-28 | B | Persona "Carla Nutri 32a interior SP" + ICP + Anti | PASSOU |
| 2026-02-22 | C | Marina declara mecanismo "Método R3" — audit acusa 11/13 | PARCIAL |
| 2026-02-25 | (skill recomenda voltar a C, Marina ignora) | Avança pra D | risco assumido |
| 2026-03-05 | D | 3 motivos definidos, mas 2 derivam de C incompleto | PARCIAL |
| 2026-03-12 | E | Brand book pronto, ativos no ar | PASSOU (mas vai precisar refresh) |
| 2026-03-20 | F | Programa estruturado, piloto começou mas não terminou | PARCIAL |
| 2026-03-30 | G | Stack + garantia + 3 preços + 1 venda real | PASSOU |
| 2026-04-02 | H | Site + tracking ok | PASSOU |
| 2026-04-08 | I | Atinge 52 leads/mês orgânico (1 mês só, falta o segundo) | PARCIAL |
| 2026-04-15 | J | Página no ar — Bencivenga 6.5 (abaixo de 8) | PARCIAL |
| 2026-04-20 | K | Lança campanhas, ROAS bom 7 dias | em PROGRESSO |
| 2026-05-01 | K | CPA dobra. ROAS cai pra 1.4x. SOS pra Tata | sintoma ativo |
| 2026-05-08 | (HOJE) | Skill diagnostica: rollback até C | aguardando ação |

### Onde a skill entra

A cada porta declarada concluída, Marina deveria ter rodado `--validar`. A skill teria sinalizado os PARCIAL antes de Marina avançar. Custo do não-uso: 3 semanas de tráfego pago no escuro + ROAS 1.4x.

### Próximos passos sugeridos pela skill (5 de maio)

1. `/gates-imperatriz --rollback Marina "tráfego caro"` — caminho de volta
2. Pausa K. Mantém 30% budget em campanhas-âncora.
3. Fecha C (2-3 dias). Fecha F (1 semana — termina piloto).
4. Refresh em D, E. Re-audit J pra Bencivenga 8+.
5. Ressincroniza ciclos N e L vencidos.
6. Volta pra K com lastro. Espera 30d pra declarar K PASSOU.
7. Janela total: 14-21 dias até voltar ao status de avanço seguro.

---

## REGRA DURA OBSERVADA

Em todos os exemplos, a skill:
- Não inventou métricas que não estavam no dossiê
- Não declarou porta concluída sem evidência
- Não otimizou sintoma diretamente — sempre buscou porta-fonte
- Sempre devolveu próxima skill a executar
- Sempre integrou com `/tatou-2.0` no final (input pra construção)

---

**Travessia Imperatriz — Pilar 2 (Fluxo). Propriedade intelectual Tata Gonçalves.**
