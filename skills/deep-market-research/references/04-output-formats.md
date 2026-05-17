# Formatos de Saída — Markdown + JSON + CSV

A skill entrega 3 artefatos em formatos diferentes pra cada caso de uso:

| Artefato | Formato | Pra quê |
|---|---|---|
| Relatório mestre | Markdown | Leitura humana, Obsidian |
| Saída canônica | JSON | Consumo automático por outras skills |
| Tabela acionável | CSV | Importar pra Notion/Sheets/calendário |

---

## 1. Relatório Mestre (Markdown)

Arquivo: `relatorio-mestre.md` em `~/Documents/Obsidian Vault/05 - Pesquisa de Mercado/[nicho-slug]/`

Estrutura obrigatória:

```markdown
# Deep Market Research — [Nicho]
*Pesquisa executada em [data]*
*Produto-alvo: [produto]*
*Cliente ideal: [1 frase]*

## Sumário Executivo

- **Estágio Schwartz dominante:** [inconsciente/consciente da dor/...]
- **Eixo PADC dominante:** [Preço/Autoridade/Dúvida/Condição]
- **Plataforma com mais sinal:** [Google/YT/TikTok/IG/LinkedIn]
- **Tom dominante:** [aspiracional/dor-explícita/comparativo/...]
- **5 insights de alto impacto** [bullet curto cada]

## 1. Briefing

[copiar tabela do briefing inicial]

## 2. Top 50 Termos Exatos

[tabela com 50 linhas: Termo | Plataforma | Frequência | Schwartz | Score]

## 3. Expressões Idiomáticas (20)

[lista]

## 4. Metáforas Recorrentes (15)

[lista]

## 5. Anti-termos (10) — Não usar

[lista]

## 6. Mapa de Objeções (150 linhas)

[tabela: Termo | Objeção | Eixo | Frase-origem | Fonte | Semente de quebra]

## 7. Ideias de Conteúdo (50)

[tabela: # | Termo | Objeção | Formato | Hook | Valor | Ponte | CTA]

## 8. Distribuição por Plataforma

[5 sub-seções, uma por plataforma, com dados específicos]

## 9. Próximos Passos

- [ ] Rodar `/skill-persona-profunda` com este JSON
- [ ] Rodar `/calendario-imperatriz` pra distribuir as 50 ideias
- [ ] Rodar `/headline-imperatriz` pros top 10 termos
- [ ] (etc — ver references/06-integracao-stack.md)

## 10. Fontes Citadas

[lista de URLs/posts/vídeos consultados com data]
```

---

## 2. Saída Canônica (JSON)

Arquivo: `saida-canonica.json` no mesmo diretório. Estrutura:

```json
{
  "$schema": "deep-market-research-v1",
  "metadata": {
    "executed_at": "2026-05-13",
    "nicho": "criação de apps sem código",
    "produto": "Imersão Olimpo",
    "cliente_ideal": "Empreendedora 30-50 anos que quer publicar app sem saber programar",
    "ticket": "R$97-997",
    "schwartz_dominante": "consciente_da_solucao",
    "padc_dominante": "duvida_pessoal",
    "plataformas_pesquisadas": ["google", "youtube", "tiktok", "instagram", "linkedin"],
    "queries_totais_executadas": 47
  },
  "termos_top_50": [
    {
      "id": 1,
      "termo_exato": "como criar app sem programar",
      "plataforma_origem": ["google", "youtube"],
      "frequencia": 18,
      "schwartz": "consciente_da_solucao",
      "score_oportunidade": 9,
      "contexto_dominante": "como_fazer"
    }
  ],
  "expressoes_idiomaticas": [
    {"termo": "to puta de cansada", "fonte": "comentario_tiktok", "data": "2026-04"}
  ],
  "metaforas": [
    {"metafora": "meu negócio é uma vela acesa", "interpretacao": "fragilidade do estágio atual"}
  ],
  "anti_termos": [
    {"termo": "leverage synergies", "razao": "jargão corporativo gringo, público BR rejeita"}
  ],
  "objecoes": [
    {
      "termo_mae": "como criar app sem programar",
      "ranking": 1,
      "objecao_resumida": "Cobra tudo escondido",
      "eixo": "preco",
      "sub_categoria": "custo_escondido",
      "frase_origem": "achei que era grátis mas depois cobra tudo",
      "fonte": {"plataforma": "youtube", "tipo": "comentario", "data": "2026-04-22"},
      "semente_quebra": "Mostrar preço total na primeira tela + comparativo de economia vs alternativa"
    }
  ],
  "ideias_conteudo": [
    {
      "id": 1,
      "termo_mae": "como criar app sem programar",
      "objecao_atacada": "duvida_pessoal_capacidade",
      "formato": "reel",
      "duracao_estimada_s": 60,
      "hook": "Você acha que precisa saber programar pra criar app. Não precisa.",
      "valor": "Demo 20s no Lovable de tela de login",
      "ponte": "Imersão = app publicado em 2 dias",
      "cta": "Link na bio"
    }
  ],
  "fontes": [
    {"url": "https://youtube.com/watch?v=...", "tipo": "video", "consultado_em": "2026-05-13"}
  ]
}
```

### Validação do JSON

Antes de salvar, valide:
- [ ] `metadata.nicho` não vazio
- [ ] `termos_top_50.length === 50` (modo full) ou 20 (modo rápido)
- [ ] `objecoes.length === termos_top_50.length × 3`
- [ ] Toda `objecao.frase_origem` tem aspas
- [ ] Todo `ideias_conteudo[].hook` contém ≥1 palavra do `termo_mae` (regra: hook usa termo exato)

---

## 3. Tabela Acionável (CSV)

Arquivo: `pauta-50-ideias.csv` no mesmo diretório.

Estrutura (importável direto pra Notion/Sheets/Airtable):

```csv
id,termo_exato,objecao_principal,eixo_padc,formato,hook,valor,ponte,cta,data_sugerida,canal_principal,prioridade
1,"como criar app sem programar","capacidade",D,"reel","Você acha que precisa saber programar...","Demo Lovable 20s","Imersão = app em 2 dias","Link bio",2026-05-14,instagram,alta
```

---

## 4. Recortes por Canal (Markdown)

5 arquivos adicionais:
- `recorte-google.md` — termos + autocompletes + people-also-ask
- `recorte-youtube.md` — vídeos top + 30 comentários top de cada + objeções
- `recorte-tiktok.md` — hashtags cluster + 20 Reels analisados + hooks padrão
- `recorte-instagram.md` — perfis-referência + carrosséis salvos + comentários
- `recorte-linkedin.md` — posts virais + linguagem B2B + comentários contrarian

Cada recorte segue estrutura:
```markdown
# Recorte [Plataforma] — [Nicho]

## Queries executadas
[lista]

## Termos capturados
[tabela]

## Padrões detectados
[3-5 padrões específicos da plataforma]

## Linguagem literal
[citações curtas com fonte]

## Objeções dominantes (nessa plataforma)
[top 5]

## Ideias de conteúdo específicas (10)
[direcionadas pra essa plataforma]
```

---

## 5. Convenções de nomenclatura

- **Nicho-slug:** kebab-case, sem acento, sem espaço. Ex: `criacao-apps-sem-codigo`, `estetica-facial`, `consultoria-rh-b2b`
- **Diretório:** `~/Documents/Obsidian Vault/05 - Pesquisa de Mercado/[nicho-slug]/`
- **Versionamento:** se rodar `--atualizar`, salvar como `relatorio-mestre-v2.md` (não sobrescrever)
- **Arquivo de diff temporal:** `diff-vs-v1.md` mostra o que mudou

---

## 6. Tags Obsidian no frontmatter

Cada arquivo `.md` da skill começa com:

```yaml
---
tags: [pesquisa-mercado, deep-market-research, voc, nicho/[nicho-slug]]
created: 2026-05-13
nicho: [nicho]
produto: [produto]
status: ativo
---
```

Isso permite buscas no Obsidian por:
- `tag:pesquisa-mercado` → toda pesquisa já feita
- `tag:nicho/estetica` → pesquisas de estética
- `path:"05 - Pesquisa de Mercado"` → todas

---

## 7. Output mínimo do modo `--rapido`

No modo rápido, entregue **APENAS**:
- `relatorio-rapido.md` (1 arquivo, sem recortes)
- `saida-canonica.json` (truncado: 20 termos, 20 objeções, 20 ideias)

Tempo: <1h.
