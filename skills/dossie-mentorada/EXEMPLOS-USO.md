# EXEMPLOS-USO — 5 Cenários Reais Ponta-a-Ponta

Exemplos práticos cobrindo os fluxos críticos da `dossie-mentorada`. Cada exemplo mostra **comando real, output esperado e estado do dossiê depois**.

---

## ÍNDICE

1. [Criar dossiê novo (Aspirante chegando) — Maria Silva](#exemplo-1)
2. [Gravar output de anamnese e disparar cascata](#exemplo-2)
3. [Ler voz pra abastecer skill de copy (headline-imperatriz)](#exemplo-3)
4. [Sincronizar profiles e detectar inconsistência](#exemplo-4)
5. [Exportar dossiê pra apresentação 1:1 com Tata](#exemplo-5)
6. [BÔNUS — Promoção de nível (Princesa → Duquesa)](#exemplo-6)
7. [BÔNUS — Cross-contamination prevention (slug A protegido de slug B)](#exemplo-7)

---

<a id="exemplo-1"></a>
## EXEMPLO 1 — Criar dossiê novo (Aspirante chegando)

**Contexto:** Maria Silva acabou de assinar a Travessia Imperatriz. Tata vai criar o dossiê dela antes de qualquer skill rodar.

### Comando

```
/dossie-mentorada --criar "Maria Silva dos Santos"
```

### O que acontece nos bastidores

1. Skill recebe nome bruto `"Maria Silva dos Santos"`
2. Sanitiza pra slug: `maria-silva-dos-santos`
3. Verifica se `~/imperio/mentoradas/maria-silva-dos-santos/` já existe
   - Se existe: pergunta se quer sobrescrever (default NÃO)
   - Se não existe: prossegue
4. Cria pasta + 19 arquivos JSON com schema válido + valores nulos
5. Cria pasta `.backups/` vazia
6. Inicializa `14-progresso.json`:
   ```json
   {
     "schema_versao": "1.0",
     "slug": "maria-silva-dos-santos",
     "criado_em": "2026-05-08T19:33:00-03:00",
     "atualizado_em": "2026-05-08T19:33:00-03:00",
     "versao": 1,
     "fonte_skill": "dossie-mentorada",
     "stale": false,
     "dados": {
       "porta_atual": "A0",
       "porta_letra_significado": "Aterrissagem (anamnese pendente)",
       "portas_concluidas": [],
       "portas_pendentes": ["A","P","E","R","A","I","S","S","I","P","F","U","R","A","L","M","I","S","J","I","B","A","C"],
       "data_inicio_travessia": "2026-05-08",
       "data_porta_atual_iniciada": "2026-05-08",
       "dias_na_porta_atual": 0
     }
   }
   ```
7. Inicializa `15-nivel.json` com `nivel_atual: "aspirante"`
8. Cria `04-CLAUDE.md` placeholder com frontmatter mínimo
9. Cria primeira entrada em `18-historico-decisoes.json`:
   ```json
   {
     "id": "dec-001",
     "data": "2026-05-08T19:33:00-03:00",
     "tipo": "criacao-dossie",
     "descricao": "Dossiê criado pra mentorada Maria Silva dos Santos",
     "decidido_por": "tata",
     "skill_usada": "dossie-mentorada"
   }
   ```

### Output

```
Dossiê criado em: ~/imperio/mentoradas/maria-silva-dos-santos/

19 arquivos JSON inicializados (schema versão 1.0):

  00-anamnese.json              vazio — pendente /anamnese-mentorada
  01-perfil.json                vazio — depende de 00
  02-diagnostico.json           vazio — depende de 00, 01
  03-voz-de-marca.json          vazio — pendente /voz-de-marca-builder
  04-CLAUDE.md                  placeholder — re-build automático
  05-persona.json               vazio
  06-mecanismo.json             vazio
  07-historia-metodo.json       vazio
  08-posicionamento.json        vazio
  09-brand.json                 vazio
  10-programa.json              vazio
  11-oferta.json                vazio
  12-infra.json                 vazio
  13-funil.json                 vazio
  14-progresso.json             inicializado: porta A0
  15-nivel.json                 inicializado: aspirante
  16-kpis-dashboard.json        vazio
  17-cases.json                 vazio (array vazio)
  18-historico-decisoes.json    1 entrada (criacao-dossie)

Estado da mentorada:
  Nível: ASPIRANTE
  Porta atual: A0 (Aterrissagem — anamnese pendente)
  Tempo na Travessia: 0 dias

PRÓXIMO PASSO RECOMENDADO:
  /anamnese-mentorada --formulario maria-silva-dos-santos
```

### Estado depois

Pasta criada. Sistema pronto pra receber dados. `tatou-2.0` agora reconhece `maria-silva-dos-santos` como mentorada-em-contexto.

---

<a id="exemplo-2"></a>
## EXEMPLO 2 — Gravar output de anamnese e disparar cascata

**Contexto:** Maria respondeu o formulário de anamnese. A skill `anamnese-mentorada` precisa gravar o resultado e disparar a cascata da Porta A.

### Comando (interno — chamado pela skill `anamnese-mentorada`)

```
/dossie-mentorada --gravar maria-silva-dos-santos 00-anamnese '{
  "identidade": {
    "nome_completo": "Maria Silva dos Santos",
    "nome_publico": "Maria Silva",
    "idade": 38,
    "cidade": "São Paulo - SP",
    "instagram": "@mariasilva.hormonal",
    "site": "https://mariasilva.com.br",
    "whatsapp": "+5511987654321"
  },
  "negocio": {
    "nicho_declarado": "saude feminina hormonal",
    "tempo_atuacao_anos": 6,
    "tipo_negocio": "mentoria + curso digital",
    "esta_solo": false,
    "tamanho_time": 3,
    "faturamento_mensal_atual_brl": 45000,
    "faturamento_meta_12m_brl": 200000
  },
  "historia": {
    "como_chegou_aqui": "Era nutricionista clínica, descobriu nicho hormonal há 4 anos",
    "momento_decisivo": "Caso pessoal de TPM resolvido aos 35"
  },
  "expectativas": {
    "por_que_travessia": "Estruturar pra escalar sem mim no meio",
    "compromisso_horas_semana": 12,
    "investimento_disponivel_brl": 25000
  }
}'
```

### O que acontece nos bastidores

1. Recebe slug + nome do profile + payload JSON
2. Carrega schema de `00-anamnese.json` da skill
3. Valida payload contra schema
   - Campos obrigatórios presentes? ✓
   - Tipos corretos? ✓ (idade é integer, instagram começa com @, etc.)
   - Enums respeitados? ✓
4. Lê arquivo atual `00-anamnese.json` (versao 1, dados null)
5. Faz merge: envelope mantém metadata, `dados` recebe payload
6. Incrementa `versao` (1 → 2)
7. Atualiza `atualizado_em` com timestamp atual
8. Atualiza `fonte_skill` pra `anamnese-mentorada`
9. Salva arquivo
10. **Side-effects automáticos:**
    - Atualiza `14-progresso.json`: porta A0 → A1
    - Cria entrada em `18-historico-decisoes.json` tipo `anamnese-concluida`
    - Re-build de `04-CLAUDE.md` (importa seção de contexto de negócio da anamnese)
    - Backup automático em `.backups/snapshot-2026-05-08.zip`
    - Hook dispara skill `perfil-mentorada` automaticamente (próximo passo da Porta A)

### Output

```
Gravado: 00-anamnese.json (versão 2)

Schema validado. Campos preenchidos: 14/18 (4 opcionais ausentes)

Side-effects executados:
  14-progresso.json     porta_atual: A0 → A1
  18-historico-decisoes 1 entrada criada (anamnese-concluida)
  04-CLAUDE.md          re-build automático (seções: contexto-negocio, identidade)
  .backups/             snapshot-2026-05-08.zip criado

Próxima skill na cascata da Porta A:
  /perfil-mentorada maria-silva-dos-santos
  (executando automaticamente em 3 segundos...)
```

### Estado depois

```
00-anamnese.json       versao 2  (preenchido)
14-progresso.json      versao 2  (porta A1)
18-historico           versao 2  (2 entradas)
04-CLAUDE.md           versao 2  (re-buildado)
demais profiles        versao 1  (ainda vazios)
```

---

<a id="exemplo-3"></a>
## EXEMPLO 3 — Ler voz pra abastecer copy (headline-imperatriz)

**Contexto:** Maria está na Porta J. Quer gerar headlines pra página de vendas. A skill `headline-imperatriz` precisa ler 5 profiles antes de gerar uma única headline.

### Hook automático antes da execução

Quando Tata digita `/headline-imperatriz maria-silva-dos-santos`, o hook `before_skill_execute` dispara:

```
/dossie-mentorada --ler maria-silva-dos-santos todos --modo injetar-contexto
```

### O que acontece nos bastidores

1. Skill recebe slug
2. Verifica se pasta existe
3. Lê os 19 JSONs em sequência (paralelizado)
4. Filtra: só profiles relevantes pra `headline-imperatriz` (declarado no frontmatter):
   - 03-voz-de-marca
   - 05-persona
   - 06-mecanismo
   - 08-posicionamento
   - 11-oferta
5. Verifica se profiles obrigatórios estão preenchidos
   - `06-mecanismo`: `versao >= 2`? ✓ (mentorada chegou na Porta J, mecanismo já está pronto)
   - `11-oferta`: `versao >= 2`? ✓
6. Constrói payload de contexto:
   ```json
   {
     "voz": { /* dados de 03 */ },
     "persona": { /* dados de 05 */ },
     "mecanismo": { /* dados de 06 */ },
     "posicionamento": { /* dados de 08 */ },
     "oferta": { /* dados de 11 */ }
   }
   ```
7. Injeta no contexto da skill `headline-imperatriz`
8. Skill executa com contexto completo

### Output do `--ler` (intermediário, geralmente não exibido)

```
Lido: ~/imperio/mentoradas/maria-silva-dos-santos/

Contexto injetado pra /headline-imperatriz:

  03-voz-de-marca       versao 4  tom: amiga-autoridade
                                  vocabulario_assinatura: 6 termos
                                  vocabulario_banido: 8 termos
                                  frases_assinatura: 3 frases reais

  05-persona            versao 3  Carla 42 advogada-2-filhos
                                  consciência: nivel 3 (sabe da solução)
                                  sofisticação: nivel 4 (mercado saturado)

  06-mecanismo          versao 3  Protocolo Hormônio-Casa
                                  scoring: 13/13 estruturais + 7/10 estratégicos
                                  metafora: cozinha-fogao-receita

  08-posicionamento     versao 2  amiga-autoridade premium-acessível
                                  frase_pos: "...Maria Silva é a nutricionista que..."

  11-oferta             versao 2  Mentoria H-Casa T14 R$8.997
                                  garantia: 7-dias-incondicional
                                  promessas: 3 declaradas

Skill /headline-imperatriz pode prosseguir.
```

### Skill `headline-imperatriz` agora gera

Com o contexto carregado, ela produz:

```
HEADLINE — TEMPERATURA FRIA (público frio, consciência 1-2)

Variação 1:
"O cortisol travesso que rouba sua energia, libido e ciclo aos 38 — e o que
fazer quando dieta, pílula e jejum já falharam"

Variação 2:
"Por que mulher 35-50 não emagrece nem dormindo bem (e a enzima que faz
toda diferença)"

[...]

HEADLINE — TEMPERATURA QUENTE (já viu lead magnet)

Variação 1:
"Protocolo Hormônio-Casa — o método que 347 mulheres usaram pra resolver
TPM em 60 dias sem pílula sintética"

[...]
```

Headlines respeitam:
- Voz da Maria (sem "jornada", sem travessão, com "cortisol travesso")
- Mecanismo embedded (Protocolo Hormônio-Casa)
- Proof real (347 mulheres — vem de 17-cases via 06-mecanismo)
- Posicionamento (amiga-autoridade, não guru-mística)

### Estado depois

Profiles **não modificados** pelo `--ler` (leitura é read-only). Quando Tata escolhe headline finalista, skill chama `/dossie-mentorada --gravar maria-silva-dos-santos 11-oferta` com campo `headlines_aprovadas` atualizado.

---

<a id="exemplo-4"></a>
## EXEMPLO 4 — Sincronizar profiles e detectar inconsistência

**Contexto:** Maria está há 60 dias na Travessia. Já passou pelas Portas A, P, E, R, A, I, S, S, I, P, F, U. Tata quer auditar consistência antes de avançar pra Porta R seguinte.

### Comando

```
/dossie-mentorada --sincronizar maria-silva-dos-santos
```

### O que acontece nos bastidores

1. Carrega TODOS os 19 profiles da mentorada
2. Roda bateria de checks cruzados:

| Check | Lógica | Resultado |
|-------|--------|-----------|
| Voz x Posicionamento | tom em 03 deve casar com tom_premium em 08 | inconsistência detectada |
| Persona x Oferta | ticket aceito por persona em 05 deve >= ticket em 11 | OK |
| Mecanismo x Funil | nome em 06 aparece em copy referenciada em 13? | OK |
| Cases x Mecanismo | proof_stack em 06 vincula a cases em 17? | OK |
| Brand x Voz | voz_visual em 09 casa com tom em 03? | OK |
| KPIs x Funil | métricas em 16 batem com snapshot de 13? | inconsistência (números diferem) |
| Stale check | algum profile com 6m+ sem update? | nenhum |
| LGPD check | cases em uso público têm autorização? | OK |
| Anti-pattern check | proof inventado? credenciais em 12-infra? | OK |

3. Gera relatório

### Output

```
SINCRONIZAÇÃO — maria-silva-dos-santos

Profiles auditados: 19/19
Tempo de auditoria: 1.2s

INCONSISTÊNCIAS DETECTADAS: 2

═══════════════════════════════════════════════════════════════

INCONSISTÊNCIA 1 — Voz x Posicionamento

  03-voz-de-marca      tom_dominante: "amiga-autoridade"
                       registro: "informal-respeitoso"
                       nivel_intimidade: "alta"

  08-posicionamento    tom_premium_ou_acessivel: "premium"
                       categoria_competitiva: "high-ticket-elite"

  Conflito: voz informal-alta-intimidade não casa com posicionamento
  premium-elite. Mentorada pode estar enviando sinais mistos —
  copy informal mas página com cara de luxo.

  Sugestão de resolução:
    OPÇÃO A) Ajustar 08 pra "premium-acessível" (mais coerente com voz)
    OPÇÃO B) Ajustar 03 pra "respeitoso-formal" (mais coerente com elite)
    OPÇÃO C) Manter ambos e declarar tensão proposital
            (ex: "amiga acolhedora que cobra premium")

  Recomendação: rodar /posicionamento-estrategico --revisar
  com argumento explícito da tensão.

═══════════════════════════════════════════════════════════════

INCONSISTÊNCIA 2 — KPIs x Funil

  13-funil.kpis_funil          ROAS: 2.8
                                CPA_compra_brl: 1820
                                ticket_medio_brl: 8997

  16-kpis-dashboard.indicadores ROAS_mes_2026-04: 2.3
                                CPA_brl: 2100
                                ticket_medio_brl: 9200

  Conflito: 13 está stale (snapshot de março). 16 é abril atualizado.

  Sugestão: rodar /maestro-trafego --refresh-funil maria-silva
  pra puxar números atuais do Meta Ads/Google e atualizar 13.

═══════════════════════════════════════════════════════════════

PROFILES OK: 17

  00-anamnese          versao 2   stale: false   última: D-60
  01-perfil            versao 3   stale: false   última: D-58
  02-diagnostico       versao 1   stale: false   última: D-58
  04-CLAUDE.md         versao 8   stale: false   última: D-2
  05-persona           versao 2   stale: false   última: D-50
  06-mecanismo         versao 3   stale: false   última: D-30
  07-historia-metodo   versao 1   stale: false   última: D-45
  09-brand             versao 2   stale: false   última: D-40
  10-programa          versao 2   stale: false   última: D-25
  11-oferta            versao 4   stale: false   última: D-7
  12-infra             versao 3   stale: false   última: D-15
  14-progresso         versao 12  stale: false   última: D-1
  15-nivel             versao 2   stale: false   última: D-30
  17-cases             versao 5   stale: false   última: D-3
  18-historico         versao 18  stale: false   última: D-1

PROFILES VAZIOS (esperado pra estágio atual): 0

═══════════════════════════════════════════════════════════════

CLASSIFICAÇÃO GERAL: AMARELO (2 inconsistências corrigíveis)

Sem bloqueios pra avançar Porta atual, mas resolver antes do Lançamento (Porta L).

Próxima sincronização recomendada: 30 dias ou ao concluir Porta L.
```

### Estado depois

Sincronização **não modifica** profiles diretamente. Cria entrada em `18-historico-decisoes.json` tipo `sincronizacao-executada`. Tata decide se aplica sugestões manualmente.

---

<a id="exemplo-5"></a>
## EXEMPLO 5 — Exportar dossiê pra apresentação 1:1 com Tata

**Contexto:** Tata vai ter call 1:1 com Maria amanhã. Quer dossiê completo em formato denso pra revisar de manhã.

### Comando

```
/dossie-mentorada --exportar maria-silva-dos-santos > ~/Desktop/dossie-maria-silva-2026-05-08.md
```

### O que acontece nos bastidores

1. Carrega 19 profiles
2. Renderiza markdown denso seguindo template de apresentação
3. Inclui seções estratégicas (resumo executivo + sinais de atenção)
4. Exclui campos internos sensíveis (notas privadas de celeste, scoring de risco bruto) por padrão
5. Salva em stdout (Tata redireciona pra arquivo)

### Output (excerpt — markdown gerado)

```markdown
# DOSSIÊ — MARIA SILVA DOS SANTOS

**Slug:** maria-silva-dos-santos
**Última sincronização:** 2026-05-08
**Nível atual:** Princesa (2 meses)
**Porta atual:** L (Lançamento — em andamento)
**Faturamento atual:** R$67.000/mês (meta 12m: R$200k)
**Próxima call recomendada:** 2026-05-15

---

## RESUMO EXECUTIVO

Maria Silva, 38, nutricionista hormonal, São Paulo. 6 anos de mercado.
Time de 3. Faturando R$67k/mês com 7 alunos novos no mês. Está na Princesa
há 2 meses, com Duquesa em vista quando concluir Porta M (Modelagem do
programa). Mecanismo "Protocolo Hormônio-Casa" sólido (13/13 estruturais
+ 7/10 estratégicos). Página live, ROAS 2.3 abaixo da meta de 3.

### Sinais positivos
- 347 alunas concluintes (média -6.3kg em 60d)
- NPS 71
- 7 cases com autorização de uso público
- Margem 58%

### Sinais de atenção
- Tensão entre voz "amiga-autoridade" e posicionamento "premium-elite"
- KPIs de abril abaixo de março (ROAS 2.8 → 2.3)
- 22h/semana ainda no operacional (meta: 10h pra Duquesa)
- Lançamento da T14 em 30 dias — comunicação ainda não start

---

## 00 ANAMNESE

[dump estruturado dos campos preenchidos]

## 01 PERFIL

**Arquétipo:** expert-criadora-conteudo
**Estágio:** estabelecida-pre-escala
**Modelo:** high-ticket-mentoria + curso-evergreen
**Ticket médio:** R$9.571
**LTV/CAC:** 6.3 (saudável)
**Stack tech:** Hotmart, ManyChat, Notion, WhatsApp Business

## 02 DIAGNÓSTICO

**FRIO:** 8/6/4/7 (total 25 — saudável)
**Prioridade 1:** Imperio (autonomia)
**Prioridade 2:** Receita

[continua...]

## 03 VOZ DE MARCA

[seção completa com vocabulario, frases, anti-exemplos]

## 06 MECANISMO

**Nome:** Protocolo Hormônio-Casa
**Causa raiz:** Cortisol noturno elevado bloqueia conversão de progesterona
pela enzima 21-hidroxilase
**Vilão:** indústria-farmacêutica-pílula-sintética
**Metáfora:** "Hormônio é receita de bolo. Cortisol noturno é fogão alto
demais. Receita queima toda."
**Proof stack:** 3 tipos (científico Cleveland Clinic + casuístico Carla +
agregado 347 alunas)

[continua todos os 19 profiles...]

---

## DECISÕES CRÍTICAS — TIMELINE

- 2026-03-10  Promovida pra Princesa
- 2026-04-22  Pivote mecanismo v1 → v2 (nome reformulado)
- 2026-05-01  Diagnóstico FRIO refeito (saiu de 19 → 25)
- 2026-05-07  Bencivenga 8.7 na headline da página
- 2026-05-08  Sincronização: 2 inconsistências detectadas

---

## RECOMENDAÇÕES PRA CALL

1. Discutir tensão voz-posicionamento (resolver antes do lançamento)
2. Revisar plano de saída do operacional (22h/sem é alto pra Duquesa)
3. Confirmar narrativa de lançamento da T14
4. Validar se 17-cases tem proof suficiente pra novo público frio
5. Definir prazo de Porta M (modelagem) pra desbloquear promoção a Duquesa

---

**Dossiê exportado: 2026-05-08T19:33:00-03:00**
**Markdown denso — 8 páginas. Revisar antes da call.**
```

### Estado depois

Profiles **não modificados**. Cria entrada em `18-historico-decisoes.json` tipo `dossie-exportado` com timestamp. Permite auditoria de quem viu o dossiê e quando.

### Variantes do `--exportar`

```bash
# Modo curto (1 página, executive summary)
/dossie-mentorada --exportar maria-silva --modo curto

# Modo mentorada-friendly (filtra notas internas da Tata)
/dossie-mentorada --exportar maria-silva --modo mentorada-friendly

# Modo PDF (renderiza markdown pra PDF via pandoc)
/dossie-mentorada --exportar maria-silva --formato pdf

# Modo JSON (dump cru, sem renderização)
/dossie-mentorada --exportar maria-silva --formato json
```

---

<a id="exemplo-6"></a>
## EXEMPLO 6 (BÔNUS) — Promoção de nível (Princesa → Duquesa)

**Contexto:** Maria concluiu Porta M (Modelagem). Sistema verifica se ela atende critérios de Duquesa.

### Comando (chamado automaticamente após gate da Porta M)

```
/hierarquia-imperatriz --validar maria-silva-dos-santos
```

### O que acontece

`hierarquia-imperatriz` lê:
- `14-progresso.portas_concluidas` — precisa ter `M` ✓
- `16-kpis-dashboard.faturamento_brl` — precisa >= R$50k recorrente por 3+ meses ✓
- `01-perfil.tempo_ela_no_operacional_h_semana` — precisa <= 12h ✗ (Maria ainda está em 22h)
- `15-nivel.tempo_no_nivel_meses` — precisa >= 2 ✓

Critério de operacional FALHOU.

### Output

```
HIERARQUIA — maria-silva-dos-santos

NÍVEL ATUAL: Princesa (2 meses)

CRITÉRIOS DUQUESA — auditoria:

  Porta M concluída                        ✓
  Faturamento >= R$50k 3+ meses            ✓ (R$67k/abril, R$58k/março, R$52k/fev)
  Operacional <= 12h/sem                   ✗ (atual: 22h/sem)
  Tempo no nível atual >= 2 meses          ✓
  Mecanismo nota 1000                      ✓ (13/13 + 7/10)
  Página live com ROAS >= 1.5              ✓ (ROAS 2.3)
  3+ cases novos no nível atual            ✓ (5 cases novos)

CLASSIFICAÇÃO: PROMOÇÃO BLOQUEADA — 1 critério pendente

Bloqueio: redução de horas no operacional
Plano de ação sugerido:
  - Delegar agenda de calls (5h → assistente)
  - Automatizar follow-up DM (4h → bot lara-builder)
  - Sair de produção de aulas semanais (3h → gravadas)

Próxima auditoria automática: 2026-06-08 ou ao concluir delegação

15-nivel.json                               sem alteração
18-historico                                entrada criada (audit-promocao-bloqueada)
```

### Estado depois

Maria continua Princesa. Sistema agendou re-auditoria. Sugere skill `how-to-delegate` pra resolver bloqueio.

---

<a id="exemplo-7"></a>
## EXEMPLO 7 (BÔNUS) — Cross-contamination prevention

**Contexto:** Tata está dentro do diretório `~/imperio/mentoradas/maria-silva-dos-santos/`. Por engano digita comando referenciando outra mentorada.

### Comando

```
cd ~/imperio/mentoradas/maria-silva-dos-santos/
/dossie-mentorada --ler ana-paula 06-mecanismo
```

### O que acontece

1. Skill detecta cwd = `maria-silva-dos-santos`
2. Skill detecta argumento = `ana-paula`
3. CONFLITO: cwd não casa com slug solicitado
4. Bloqueio automático

### Output

```
ALERTA — DETECÇÃO DE CROSS-CONTAMINATION

Você está em:    ~/imperio/mentoradas/maria-silva-dos-santos/
Você pediu:      ler dados de ana-paula

Isso é uma operação CROSS-MENTORADA.

Possíveis razões:
  1. Engano digitando — você queria maria-silva-dos-santos
  2. Comparação proposital entre duas mentoradas (raro)
  3. Você está copiando algo de uma pra outra (anti-pattern)

Pra prosseguir, confirme com flag explícita:

  /dossie-mentorada --ler ana-paula 06-mecanismo --confirmar-cross

Sem a flag, operação BLOQUEADA.

Audit log: tentativa registrada em ~/imperio/.cross-mentorada-attempts.log
```

### Se Tata insiste com `--confirmar-cross`

```
/dossie-mentorada --ler ana-paula 06-mecanismo --confirmar-cross
```

Skill executa, mas registra entrada em `18-historico-decisoes.json` da `ana-paula` tipo `acesso-cross-mentorada` com identificação de quem pediu.

### Estado depois

Operação executada. Mas auditoria preservada. Se Tata copiou conteúdo, sistema rastreia.

---

## RESUMO DE COMANDOS DOS EXEMPLOS

| Exemplo | Comando |
|---------|---------|
| 1 | `/dossie-mentorada --criar "Maria Silva dos Santos"` |
| 2 | `/dossie-mentorada --gravar [slug] 00-anamnese {payload}` |
| 3 | `/dossie-mentorada --ler [slug] todos --modo injetar-contexto` |
| 4 | `/dossie-mentorada --sincronizar [slug]` |
| 5 | `/dossie-mentorada --exportar [slug] --modo [curto/full/mentorada-friendly] --formato [md/pdf/json]` |
| 6 | `/hierarquia-imperatriz --validar [slug]` (lê do dossiê) |
| 7 | `/dossie-mentorada --ler [slug-A] [profile] --confirmar-cross` (raro) |

---

**Exemplos de uso — Dossiê Mentorada v1.0. Propriedade intelectual Tata Gonçalves.**
