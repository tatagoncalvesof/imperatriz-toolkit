# Hierarquia Imperatriz

Operadora do **Pilar 7 (Tribo)** da Travessia Imperatriz Tata Goncalves. Gerencia os 6 niveis hierarquicos da Corte e os 5 ritos de passagem.

> **Marca sem ritual e logo. Marca com ritual e cultura.**

---

## O que essa skill faz

- Audita em qual nivel cada mentorada esta (Aspirante, Princesa, Duquesa, Marquesa, Condessa, Imperatriz Plena)
- Lista criterios objetivos pra subir de nivel
- Identifica quem esta pronta pra subir agora
- Prepara o **rito de passagem** (preparacao, cerimonia, comunicacao publica, kit fisico)
- Aplica matriz de **direitos + deveres** por nivel
- Atualiza `15-nivel.json` no dossie da mentorada com versao
- Notifica dashboard, tatou-2.0 e gates-imperatriz
- Audita **distribuicao da Corte** (piramide saudavel?)
- Prepara **Coroacao Imperial** (cerimonia anual, Condessa → Imperatriz Plena)

---

## O que essa skill NAO faz

- Nao escreve copy de venda (use `/copywriting` ou `/skill-copy-ads-ptbr`)
- Nao define preco de mentoria (use `/pricing-dinamico-imperatriz`)
- Nao desenha a jornada da mentorada (use `/tatou-2.0`)
- Nao audita porta especifica (use `/gates-imperatriz`)
- Nao sobe ninguem sem criterio objetivo cumprido — **nao negocia**

---

## Os 6 niveis (visao rapida)

| # | Nivel | Emoji | Cor | Coroa | Tempo medio |
|---|-------|-------|-----|-------|-------------|
| 1 | Aspirante | 🌱 | Verde claro + botao de rosa | (sem coroa) | 60-90 dias |
| 2 | Princesa | 👸 | Rosa perola | 3 pontas | 6-9 meses |
| 3 | Duquesa | 🦄 | Roxo realeza | 5 pontas | 6-12 meses |
| 4 | Marquesa | 💎 | Azul zafira | 7 pontas | 12-18 meses |
| 5 | Condessa | 🌟 | Dourado real | 9 pontas + pedras | 12-24 meses |
| 6 | Imperatriz Plena | 👑 | Purpura imperial | Coroa imperial completa | (vitalicio) |

Detalhamento em [`OS-6-NIVEIS-DETALHADO.md`](./OS-6-NIVEIS-DETALHADO.md).

---

## Os 5 ritos de passagem

| # | Rito | De | Pra | Cerimonia |
|---|------|-----|-----|-----------|
| 1 | Investidura da Princesa | Aspirante | Princesa | Call mensal |
| 2 | Investidura da Duquesa | Princesa | Duquesa | Imersao trimestral |
| 3 | Investidura da Marquesa | Duquesa | Marquesa | Encontro presencial |
| 4 | Investidura da Condessa | Marquesa | Condessa | Evento aberto |
| 5 | Coroacao Imperial | Condessa | Imperatriz Plena | Evento anual |

Roteiro completo em [`OS-5-RITOS.md`](./OS-5-RITOS.md).

---

## Como usar

### Modo padrao
```
/hierarquia-imperatriz --status [nome da mentorada]
```
Ve em qual nivel ela esta + criterios pendentes pro proximo.

### Preparar rito de passagem
```
/hierarquia-imperatriz --investidura [nome]
```
Gera roteiro da cerimonia + comunicacao + kit + atualizacao de dossie.

### Listar Corte por nivel
```
/hierarquia-imperatriz --listar Princesa
/hierarquia-imperatriz --listar Duquesa
```

### Auditoria global (quem esta pronta)
```
/hierarquia-imperatriz --prontas
```
Lista todas mentoradas que cumpriram criterio mas ainda nao subiram.

### Coroacao Imperial (anual)
```
/hierarquia-imperatriz --coroar [nome]
```
Prepara cerimonia maxima + contrato societario.

---

## Arquivos da skill

- [`SKILL.md`](./SKILL.md) — operacao completa e modos
- [`OS-6-NIVEIS-DETALHADO.md`](./OS-6-NIVEIS-DETALHADO.md) — cada nivel com tudo
- [`OS-5-RITOS.md`](./OS-5-RITOS.md) — cerimonias detalhadas
- [`DIREITOS-DEVERES.md`](./DIREITOS-DEVERES.md) — matriz completa
- [`DISTRIBUICAO-ESPERADA.md`](./DISTRIBUICAO-ESPERADA.md) — piramide saudavel
- [`EXEMPLOS-INVESTIDURAS.md`](./EXEMPLOS-INVESTIDURAS.md) — 3 casos com roteiro

---

## Integracao no ecossistema

```
dossie-mentorada (15-nivel + 14-progresso)
        ↓
hierarquia-imperatriz  ← VOCE ESTA AQUI (Pilar 7 Tribo)
        ↓
        ├─ atualiza 15-nivel.json (versionado)
        ├─ notifica dashboard-imperatriz (metrica)
        ├─ notifica tatou-2.0 (handoff de jornada)
        └─ notifica gates-imperatriz (revalida portas)
```

Disparada por:
- `tatou-2.0` quando gate critico e atingido
- `gates-imperatriz` quando porta especifica destrava
- Auditoria mensal manual da Tata
- Pos-evento (call mensal, imersao, presencial, anual)

---

## Regra dura

**Hierarquia visivel = comunidade real.**

Sem hierarquia, comunidade vira lista de e-mail. Mentoradas precisam:
1. Saber em que nivel estao
2. Saber o que falta pra subir
3. Ver as outras subindo (efeito tribo)
4. Ter cerimonia simbolica (memorabilidade)
5. Ter direitos crescentes (motivacao)
6. Ter deveres crescentes (responsabilidade)

---

## Distribuicao saudavel (1000 mentoradas)

- Aspirante: 30-40% (300-400) — base larga, recem-chegadas
- Princesa: 25-30% (250-300) — primeiro resultado validado
- Duquesa: 15-20% (150-200) — funil opera sem ela
- Marquesa: 8-12% (80-120) — time fecha sem ela
- Condessa: 3-5% (30-50) — autoridade publica
- Imperatriz Plena: 1-2% (10-20) — socia formal

Sinais de desbalanceamento + diagnostico em [`DISTRIBUICAO-ESPERADA.md`](./DISTRIBUICAO-ESPERADA.md).

---

## Versionamento

**v1.0** (atual) — 6 niveis, 5 ritos, 5 modos, integracao Travessia.

---

**Pilar 7 (Tribo) da Travessia Imperatriz — propriedade intelectual Tata Goncalves.**
