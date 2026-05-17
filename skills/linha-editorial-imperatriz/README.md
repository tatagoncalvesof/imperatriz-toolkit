# Linha Editorial Imperatriz — Skill Proprietária Tata Gonçalves

Operadora do **Pilar Editorial da Travessia Imperatriz**. Define a LINHA EDITORIAL canônica da mentorada — não calendário, não copy avulsa: a **régua editorial que governa TUDO que sai da boca da marca**.

---

## O QUE ELA FAZ

Cruza 4 fundações (posicionamento, voz de marca, marca sistêmica, Porta atual da Travessia) e gera **8 ativos**:

1. **Manifesto editorial** (o que essa marca defende publicamente)
2. **3-5 pilares temáticos** com proporção
3. **Matriz TEAM** (Teach/Engage/Authority/Monetize/Story) com mix por canal
4. **Cadência por canal** (frequência + horário + voz)
5. **Vocabulário ON/OFF** (palavras-âncora + banidas)
6. **Boundaries** (o que SIM e o que NÃO publica)
7. **Matriz Porta × Conteúdo** (como muda a linha em cada Porta da Travessia)
8. **Gabarito de auditoria**

---

## OS 4 MODOS

| Modo | Quando usar |
|---|---|
| `--gerar` | Linha editorial do zero, cruzando todas as fundações |
| `--auditar` | Avalia conteúdo existente contra a linha — detecta drift, canibalização, voz fora |
| `--evoluir` | Recalibra quando muda de Porta ou de Princesa → Marquesa → Imperatriz |
| `--exportar` | Manifesto + dashboard HTML + JSON canônico |

---

## INTEGRAÇÃO COM O ECOSSISTEMA TATA

Output JSON em `~/imperio/mentoradas/[nome]/04-linha-editorial.json` é lido **automaticamente** por:

- `/calendario-imperatriz`
- `/linkedin-empire`
- `/social-content`
- `/skill-carrossel-instagram`
- `/email-sequence`

```
/posicionamento-estrategico → /voz-de-marca-builder → /linha-editorial-imperatriz ← AQUI
                                                              ↓
                                                      /calendario-imperatriz
```

---

## INSTALAÇÃO

```bash
cd ~/.claude/skills
git clone https://github.com/tatagoncalvesof/skill-linha-editorial-imperatriz.git linha-editorial-imperatriz
```

---

Pilar Editorial da Travessia Imperatriz — propriedade intelectual Tata Gonçalves.
