# Perfil Mentorada — Skill Travessia Imperatriz

> Motor de classificação proprietário da Travessia Imperatriz. Lê `00-anamnese.json` + pesquisa pública (deep-research), aplica algoritmo de 12 sinais e devolve o perfil correto da mentorada (1 de 8) + a rota A-Z customizada das 26 portas.

**Método Travessia Imperatriz — propriedade Tata Gonçalves.**

---

## O QUE FAZ

A skill `/perfil-mentorada` resolve UM problema crítico: **toda mentorada que entra na Travessia precisa de uma rota — mas nenhuma percorre as 26 portas na mesma ordem**.

Ela lê os dados da mentorada, classifica em 1 dos 8 perfis canônicos e devolve:
- Perfil principal (e secundário se híbrido)
- Score 0-100 por perfil
- Rota A-Z customizada
- Kit de skills indicado
- Lista NÃO-USAR
- Tempo estimado de travessia
- Nível inicial sugerido
- Justificativa em sinais concretos

Resultado é gravado em `01-perfil.json` (validado pela Tata e pela mentorada).

---

## OS 8 PERFIS CANÔNICOS

| # | Perfil | Faixa | Sinal-âncora |
|---|--------|-------|--------------|
| 1 | Iniciante Zero | R$ 0 | Sem produto, sem audiência |
| 2 | Vendedora Avulsa | R$ 5-30k | Vende 1:1 sem digital |
| 3 | Mentora Estabelecida | R$ 30-100k | Mentoria/curso 1+ ano |
| 4 | Infoprodutora | R$ 30-200k+ | Curso digital + lançamentos |
| 5 | Empresa Física → Mentora | R$ 30-200k físico | Quer empacotar conhecimento |
| 6 | Especialista Técnica | varia | Dev/programadora quer criar produto IA |
| 7 | Empresa B2B | R$ 100k-1M+ | Vende pra outras empresas |
| 8 | Coach/Terapeuta | R$ 5-50k | Transformação pessoal, sensível a copy |

Detalhamento profundo em [`OS-8-PERFIS.md`](OS-8-PERFIS.md).

---

## INSTALAÇÃO

### Para a Tata (uso interno)

```bash
# clonar/copiar a pasta da skill pra pasta global de skills do Claude Code
cp -r ~/Documents/travessia-imperatriz-site/skills-novas/perfil-mentorada ~/.claude/skills/

# verificar
ls ~/.claude/skills/perfil-mentorada/
```

A skill fica disponível como `/perfil-mentorada` em qualquer sessão Claude Code.

### Para uma mentorada/multiplicadora (futuro)

Quando publicada como repo isolado (modelo Tata):

```bash
git clone https://github.com/tatagoncalvesof/skill-perfil-mentorada ~/.claude/skills/perfil-mentorada
```

---

## USO

### Modo padrão — classificar nova mentorada

```
/perfil-mentorada --classificar
```

A skill vai:
1. Pedir caminho do `00-anamnese.json` (ou inferir da pasta atual)
2. Rodar deep-research público (Insta, site, LinkedIn, Google)
3. Extrair os 12 sinais
4. Calcular scores dos 8 perfis
5. Apresentar classificação + justificativa
6. Esperar validação da Tata
7. Gravar `01-perfil.json` validado

### Modo reclassificar — mentorada que evoluiu

```
/perfil-mentorada --reclassificar
```

Usa o `00-anamnese.json` atualizado + `01-perfil.json` antigo. Compara, gera nova versão, arquiva a anterior.

### Modo listar — calibragem mental

```
/perfil-mentorada --listar-perfis
```

Mostra os 8 perfis com sinais distintivos resumidos. Útil antes de uma reunião 1:1 ou pra explicar pra mentorada nova.

### Modo simular — treinamento e materiais

```
/perfil-mentorada --simular vendedora-avulsa
/perfil-mentorada --simular coach-terapeuta
```

Gera mentorada fictícia daquele perfil com dados verossímeis. Usado pra:
- Treinar multiplicadoras novas
- Criar carrossel/conteúdo explicando os perfis
- Calibrar a skill (rodar e ver se classifica certo)

---

## ANATOMIA DA SKILL (7 ARQUIVOS)

| Arquivo | O que tem |
|---------|-----------|
| [`SKILL.md`](SKILL.md) | Coração da skill — frontmatter, fases, modos, regras duras |
| [`README.md`](README.md) | Você está aqui — instalação, uso, FAQ |
| [`OS-8-PERFIS.md`](OS-8-PERFIS.md) | Detalhamento profundo dos 8 perfis (sinais, dor, rota, kit, NÃO usar, tempo, nível, frase-pegada, risco de errar) |
| [`LOGICA-CLASSIFICACAO.md`](LOGICA-CLASSIFICACAO.md) | Algoritmo dos 12 sinais com tabelas de pontuação por perfil + boosts especiais + pseudocódigo |
| [`CASOS-HIBRIDOS.md`](CASOS-HIBRIDOS.md) | Combinações comuns + tratamento detalhado dos 6 híbridos mais frequentes |
| [`EXEMPLOS-CLASSIFICACOES.md`](EXEMPLOS-CLASSIFICACOES.md) | 8 casos resolvidos (1 por perfil) com sinais, scoring, justificativa |
| [`SCHEMA-JSON.md`](SCHEMA-JSON.md) | Estrutura completa do `01-perfil.json` com vocabulário controlado |

---

## FLUXO DE INTEGRAÇÃO COM A TRAVESSIA

```
/anamnese-mentorada           (coleta dados brutos da mentorada)
       ↓
/deep-research                (pesquisa pública: Insta, site, LinkedIn)
       ↓
/perfil-mentorada             ← VOCE ESTA AQUI
       ↓
/dossie-mentorada             (gera dossiê executivo já com perfil)
       ↓
/voz-de-marca-builder         (calibra voz pra rota dela)
       ↓
[Rota A-Z customizada começa]
```

---

## DEPENDÊNCIAS

### Necessárias

- `00-anamnese.json` preenchido (skill `/anamnese-mentorada`)
- Acesso a deep-research público (skill `/deep-research`)

### Recomendadas (mas não obrigatórias)

- Acesso ao Obsidian Vault `~/Documents/Obsidian Vault/03 - Projetos/Travessia-Imperatriz/`
- Skills downstream instaladas pra ações imediatas após classificação

---

## REGRAS DE OURO (a skill não negocia)

1. **Não classifica sem anamnese mínima** — pede pra rodar `/anamnese-mentorada` antes
2. **Não grava `01-perfil.json` sem validação humana** — Tata aprova
3. **Não inventa sinais** — marca como "desconhecido" e redistribui peso
4. **Não força perfil único quando é híbrido** — Δ < 15 = híbrido
5. **Não recomenda kit completo sem checar NÃO-USAR**
6. **Empresa B2B é "Empresa do Império"** — denominação correta
7. **Coach com copy agressivo = NUNCA** — sensibilidade ao tom é fundadora
8. **Especialista Técnica precisa intenção declarada de monetizar** via skills/agentes/apps
9. **Vendedora Avulsa ≠ Iniciante Zero** — Vendedora já fatura R$ 5-30k 1:1
10. **Justificativa sempre em sinais concretos** — não basta "achei"

---

## FAQ

### Pergunta: A mentorada pode pular a classificação e ir direto pra rota?

**Não.** Sem perfil definido, a rota é tiro no escuro. A skill é pré-requisito de tudo que vem depois.

### Pergunta: E se a mentorada não se reconhecer no perfil classificado?

A skill **NUNCA** grava `01-perfil.json` sem validação humana. Se a mentorada não se reconhece, a Tata investiga: pode ser sinal mal extraído, anamnese incompleta ou caso híbrido mal identificado. Skill regenera com inputs corrigidos.

### Pergunta: Quantas vezes posso reclassificar?

Quantas precisar. A cada reclassificação, a skill arquiva versão anterior (`01-perfil-v1.json`, `01-perfil-v2.json`...) e mantém `01-perfil.json` como atual. **Recomendação:** reclassificar a cada 90 dias na Travessia.

### Pergunta: Como sei se uma mentorada é híbrida?

A skill detecta automaticamente: se Δ < 15 entre top 1 e top 2, declara híbrido e mostra a combinação. Detalhes em [`CASOS-HIBRIDOS.md`](CASOS-HIBRIDOS.md).

### Pergunta: A skill pode classificar errado?

Pode. Por isso ela:
- Sempre apresenta justificativa em sinais concretos (auditável)
- Calcula confiança (alta/média/baixa)
- Pede validação humana
- Permite reclassificação fácil
- Aceita correções da Tata

### Pergunta: Mentorada Coach pode receber recomendação de ads?

Pode — mas com **filtro Coach**: ads sem urgência forçada, sem escassez agressiva, sem "ÚLTIMAS HORAS". Ver lista NÃO-USAR do perfil Coach em [`OS-8-PERFIS.md`](OS-8-PERFIS.md).

### Pergunta: Posso criar um 9º perfil?

A versão atual fixa 8 perfis canônicos. Roadmap v2.0 contempla extensão. Se aparecer caso real que não cabe em nenhum dos 8 nem em híbrido, abrir issue/RFC pra Tata avaliar.

---

## ROADMAP

- **v1.0** *(atual)* — 8 perfis, 12 sinais, 4 modos, 7 fases, integração Travessia
- **v1.5** — banco de mentoradas reais classificadas (benchmark anônimo)
- **v2.0** — auto-detecção de evolução (skill flagga "essa mentorada mudou de perfil")
- **v3.0** — feedback loop com resultado real após 90 dias na Travessia (acerto da classificação valida o algoritmo)

---

## LICENÇA E COMPARTILHAMENTO

**Skill PRIVADA** — uso interno Tata Gonçalves + multiplicadoras autorizadas da Travessia Imperatriz.

NÃO distribuir publicamente sem autorização. Conteúdo é propriedade intelectual:
- Os 8 perfis canônicos
- O algoritmo de 12 sinais
- A rota A-Z customizada
- Os híbridos mapeados

São métodos proprietários da Travessia Imperatriz.

---

## SUPORTE E EVOLUÇÃO

Encontrou caso de classificação errada? Mentorada que não cabe em nenhum perfil? Híbrido novo?

Reportar pra Tata via:
- Issue interno na pasta `~/Documents/Obsidian Vault/03 - Projetos/Travessia-Imperatriz/Skills/feedback/`
- Ou direto numa reunião de calibragem

A cada calibragem, a skill evolui — versionada e documentada.

---

**Travessia Imperatriz — onde cada mentorada encontra a rota dela.**
**Método proprietário Tata Gonçalves — 2026.**
