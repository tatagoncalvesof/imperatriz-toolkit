# Pausas e Validações (UX entre fases)

## Por que pausa importa

Cinco fases de captura intensa em sequência matam a qualidade. Mentorada cansada responde no automático, e voz capturada vira voz neutra de IA. Pausa não é luxo — é proteção da qualidade do output.

## Os dois modos de execução

### Modo MARATONA (sessão única ~2h30min)

3 pausas obrigatórias:
- **Pausa 1**: depois da Fase 2 (Voz de Marca foi exigente — 5min de respiro)
- **Pausa 2**: depois da Fase 3 (10min)
- **Pausa 3**: depois da Fase 4 (10min — antes do calendário pra mentorada chegar fresca)

Maestro força as pausas. Se mentorada disser "pula a pausa", Maestro insiste:

> Pausa não é negociável aqui. Cinco minutos. Levanta, bebe água, olha pela janela. Volta em 5min ou avisa que prefere parar agora e continuar amanhã. Não tem pressa.

### Modo SESSÃO POR SESSÃO

Cada fase é uma sessão separada. Maestro ao terminar uma fase **não pergunta "vamos pra próxima?"** — ele combina:

> ✅ Fase X concluída.
>
> Quando você quer fazer a próxima fase? Não precisa marcar agora — mas quando voltar, é só digitar `/maestro-de-conteudo continuar` que eu retomo de onde paramos.

E **encerra a sessão**.

## Como Maestro retoma uma sessão

Quando mentorada volta e digita `/maestro-de-conteudo continuar` (ou só `/maestro-de-conteudo` de novo), Maestro:

1. Lê `~/imperio/mentoradas/[nome]/_progresso.json` (estado salvo)
2. Identifica última fase concluída
3. Anuncia retomada:

```
Bem-vinda de volta.

Última vez você terminou: Fase 2 (Voz de Marca) ✓
Próxima fase: Fase 3 (Porta da Travessia) — ~10min

Bora?
- Sim, vamos pra Fase 3
- Quero revisar o que já foi capturado antes
- Quero parar (você fica com o que já tem)
```

## Estado salvo (`_progresso.json`)

Após cada fase, Maestro grava:

```json
{
  "mentorada": "Marina Faria",
  "iniciado_em": "2026-05-09T14:00:00-03:00",
  "modo": "sessao_por_sessao",
  "fases": {
    "1_posicionamento": {"status": "concluida", "concluida_em": "2026-05-09T14:32:00-03:00"},
    "2_voz_de_marca": {"status": "concluida", "concluida_em": "2026-05-09T15:18:00-03:00"},
    "3_porta": {"status": "pendente"},
    "4_linha_editorial": {"status": "pendente"},
    "5_calendario": {"status": "pendente"}
  },
  "ultima_atualizacao": "2026-05-09T15:18:00-03:00"
}
```

## Validações entre fases

Cada transição entre fases tem **validação dupla**:

### Validação técnica (automática)

Maestro checa que o arquivo da fase anterior:
- Existe no caminho correto
- Tem schema válido (campos esperados preenchidos)
- Mínimos quantitativos atingidos (ex: ≥10 palavras-âncora)

Se falha, Maestro NÃO prossegue. Pede pra rodar a fase de novo.

### Validação humana (pausa de confirmação)

Maestro mostra resumo do que saiu da fase + pergunta:

```
Tudo certo? Vamos pra próxima?
- Sim, próxima
- Quero revisar essa fase
- Pausa
```

Mentorada precisa **clicar** numa opção. Maestro não atropela.

## Estados que param o Maestro

Maestro **encerra a sessão** (sem culpar a mentorada) quando:

- Mentorada digita `parar`, `pausa longa`, `volto depois`, `desisto`
- Skill filha falha 2x seguidas e mentorada não quer rodar 3ª vez
- Mentorada não responde por > 30min na mesma fase (timeout de cuidado — Maestro avisa: "tô vendo que parou. Salva tudo e volta quando puder.")

Em qualquer caso, Maestro **salva o progresso** e mostra:

```
Sessão pausada. Tudo que a gente fez está salvo.

Quando voltar: digita /maestro-de-conteudo continuar.

Volta quando der. Sem pressa.
```

## Anti-patterns de UX

- ❌ Perguntar "tudo bem?" entre cada bloco — vira ruído
- ❌ Forçar continuação ("vamos terminar logo")
- ❌ Mostrar % de progresso ("você está 60% pronto") — vira competição com si mesma
- ❌ Comparar com outras mentoradas ("a maioria termina em 2h")
- ❌ Celebrar excessivamente ("PARABÉNS!! VOCÊ É INCRÍVEL!!") — sicofancia
- ❌ Mandar mensagem motivacional na pausa — pausa é silêncio
