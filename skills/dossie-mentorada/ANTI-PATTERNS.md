# ANTI-PATTERNS — 10 Armadilhas Fatais do Dossiê Mentorada

A skill `/dossie-mentorada` bloqueia ativamente esses 10 anti-patterns. Cada um corrompe a confiabilidade do sistema de memória inteiro. Quando detectados, a skill BLOQUEIA a operação e exige correção.

Sistema de memória persistente é frágil: 1 dossiê corrompido envenena ~225 skills que dependem dele.

---

## ANTI-PATTERN 1 — CORROMPER SCHEMA SEM VALIDAÇÃO

**Exemplos que a skill RECUSA:**

- Gravar JSON com tipo errado (`idade: "trinta e oito"` quando schema espera integer)
- Gravar campo enum fora do enum (`nivel_atual: "rainha"` quando enum é aspirante/princesa/duquesa/imperatriz)
- Pular campo obrigatório (`schema_versao` ausente)
- Gravar timestamp em formato não-ISO (`atualizado_em: "08/05/2026"`)

**Por que é fatal:**

- Skills consumidoras quebram em runtime tentando parsear estrutura invalidada
- Cascata: 1 profile inválido vira `--ler` falhar, vira skill quebrar, vira mentorada perder confiança
- Bug fica latente até primeira leitura — pode passar dias

**Antídoto:**

- TODA gravação passa por validação de schema ANTES de escrever em disco
- Skill recusa gravação inválida com mensagem clara:
  ```
  ERRO de schema em 06-mecanismo:
    campo proof_stack[2].fonte: esperado string, recebido null
    campo scoring_23_criterios.estruturais_13: esperado integer 0-13, recebido 14

  Operação NÃO executada. Profile permanece versao 2.
  ```
- Skills produtoras devem rodar dry-run antes de gravar

**Regra dura:**

> **Skill produtora é responsável por validar output ANTES de mandar pra `--gravar`. `--gravar` é a última barreira, não a única.**

---

## ANTI-PATTERN 2 — EXPOR DADOS ENTRE MENTORADAS

**Exemplos que a skill RECUSA:**

- Skill rodando com slug A inclui no contexto dados de slug B
- Cwd em pasta de Maria, pedir `--ler ana-paula` sem flag explícita
- Logs agregados que vazam nome real entre mentoradas
- Skill de IA externa recebe payload com mais de uma mentorada

**Por que é fatal:**

- Quebra LGPD (dado pessoal cruzado sem consentimento)
- Quebra confiança (mentorada descobre que Tata "comparou" dossiê dela com outro)
- Risco de copy-paste cruzado: oferta de Maria virar oferta de Ana
- Auditoria pública possível em call (Tata mostra tela e aparece dado de outra)

**Antídoto:**

- Slug é escopo absoluto. Toda operação exige slug explícito
- Bloqueio cwd: cwd em pasta A + comando referenciando B = bloqueio com flag de confirmação dupla
- Hooks injetam APENAS dados do slug-em-contexto
- Logs agregados anonimizam nomes reais (slug hash)
- Auditoria mensal varre `~/imperio/.cross-mentorada-attempts.log`

**Regra dura:**

> **Mentorada A não existe pra skill rodando em mentorada B. Vazamento de dados é bug crítico, não inconveniente.**

---

## ANTI-PATTERN 3 — ESQUECER AUDIT TRAIL

**Exemplos que a skill RECUSA:**

- Atualizar `06-mecanismo` (pivote crítico) sem registrar em `18-historico-decisoes`
- Promoção de nível sem entrada de audit
- Edição manual direta no JSON (bypassando skill)
- Rollback de versão sem registro

**Por que é fatal:**

- Perde rastreabilidade: 6 meses depois, ninguém sabe POR QUE mecanismo mudou de v1 pra v2
- Não dá pra reproduzir decisão estratégica em call de revisão
- celeste e Tata perdem contexto histórico
- Auditoria externa (LGPD, contábil) fica impossível

**Antídoto:**

- Toda mudança em campo crítico (mecanismo, oferta, nível, posicionamento) gera entrada automática em `18-historico-decisoes.json`
- Skill `--gravar` detecta diff entre versão antiga e nova e classifica:
  - Diff < 5% campos: change menor (sem audit)
  - Diff em campo crítico: change estratégico (audit obrigatório)
- Edição manual via editor de texto bloqueada por permissão (cron checa hash)

**Regra dura:**

> **Decisão crítica sem audit = decisão que não aconteceu. Se não tá em 18-historico, não foi decidido.**

---

## ANTI-PATTERN 4 — ARMAZENAR CREDENCIAIS NO DOSSIÊ

**Exemplos que a skill RECUSA:**

- `12-infra.dados.api_key_meta_ads: "EAA..."` (credencial bruta)
- `01-perfil.dados.senha_hotmart: "..."` (senha)
- `12-infra.dados.token_whatsapp_business: "..."` (token de API)

**Por que é fatal:**

- Dossiê é versionado em backup (snapshot diário) — credencial vaza pro backup
- Se um único backup vaza, credencial fica comprometida historicamente
- LGPD: credencial financeira em backup não-encriptado é violação grave
- Skill produtora pode logar campo (logs em texto puro)

**Antídoto:**

- Schema bloqueia campos com nome `password|senha|api_key|secret|token|access_key|client_secret`
- Dossiê só armazena PONTEIROS pra credencial:
  ```json
  {
    "credencial_em": "1password://maria/hotmart/senha",
    "rotacao_em": "2026-08-15"
  }
  ```
- Skills que precisam da credencial buscam direto no 1Password (op CLI)
- Auditoria mensal varre dossiês em busca de strings que parecem credencial (regex)

**Regra dura:**

> **Dossiê armazena METADADOS de credencial, NUNCA a credencial. Quem viola, skill recusa e alerta.**

---

## ANTI-PATTERN 5 — TRATAR DOSSIÊ VAZIO COMO ERRO

**Exemplos errados:**

- Skill consumidora retorna erro quando profile tem `dados: null`
- Página de vendas é gerada com placeholders genéricos quando 06-mecanismo está vazio
- Skill silenciosamente substitui campo vazio por valor default (sem avisar Tata)

**Por que é fatal:**

- Mentorada Aspirante tem 19 profiles vazios — é estado normal, não erro
- Erro de runtime em estado válido quebra fluxo da Porta A
- Defaults silenciosos contaminam dados (gerou copy fake e ninguém percebeu)

**Antídoto:**

- Skills consumidoras tratam `dados: null` como SINAL pra:
  - OPÇÃO A: retornar mensagem amigável pedindo skill anterior
  - OPÇÃO B: rodar com defaults explícitos + flag de aviso
  - OPÇÃO C: bloquear se profile é OBRIGATÓRIO pra função (ex: headline-imperatriz exige 06)
- Nunca usar default silencioso. Sempre avisar.

**Exemplo correto:**

```
/headline-imperatriz maria-silva-aspirante

ALERTA: 06-mecanismo está vazio (mentorada Aspirante).

Em mercado estágio 3+ headline sem mecanismo nomeável tem CTR < 0.5%.

Opções:
  1. Rodar /mecanismo-unico maria-silva-aspirante primeiro (recomendado)
  2. Gerar headlines genéricas com flag --aceito-risco
     (output será marcado como "rascunho-pre-mecanismo" em 13-funil)

Skill aguardando decisão.
```

**Regra dura:**

> **Vazio é estado válido. Erro é silenciar a ausência.**

---

## ANTI-PATTERN 6 — APAGAR HISTÓRICO

**Exemplos que a skill RECUSA:**

- Tata pede pra "limpar" 18-historico que ficou grande
- Skill faz overwrite de `versao` em vez de incrementar
- Profile sobrescrito perde campo `versao` (volta a 1)
- Backup deleta snapshots antigos sem retenção mínima

**Por que é fatal:**

- Audit trail é base de auditoria fiscal/legal/LGPD
- Reconstrução de timeline impossível depois de perda
- Pivotes estratégicos perdem contexto (porque mudou? não sabe mais)
- celeste e Tata perdem capacidade de aprender com decisões anteriores

**Antídoto:**

- 18-historico é APPEND-ONLY. Skill recusa qualquer operação de delete/update
- Versão sempre incrementa. Nunca volta atrás
- Backup tem retenção mínima 90 dias (cron `tatou-2.0`)
- Se 18-historico ficar grande, oferecer arquivamento (move pra `~/imperio/mentoradas/[slug]/.archive/historico-2025.json`) mas NUNCA delete

**Regra dura:**

> **Tudo que entra fica. Apagar histórico é apagar memória, é apagar mentorada.**

---

## ANTI-PATTERN 7 — CONFIAR EM PROFILE STALE

**Exemplos errados:**

- Skill de copy usa 03-voz que não foi atualizada há 8 meses (mentorada já evoluiu voz)
- Página de vendas é gerada com 11-oferta de 6 meses atrás (preço mudou)
- Persona de 2 anos atrás abastece copy nova (público mudou)

**Por que é fatal:**

- Output de copy fica "fora do tempo" — soa datado
- Preço em página pode estar errado (mentorada reajustou e esqueceu de atualizar)
- Persona desatualizada gera copy pra público que mentorada não atende mais

**Antídoto:**

- Profile com `atualizado_em` > 6 meses recebe `stale: true` automaticamente (cron mensal)
- Skills consumidoras verificam `stale` antes de usar:
  ```
  AVISO: 03-voz-de-marca está stale (última atualização: 2025-09-12).

  Voz pode ter evoluído. Recomendado:
    /voz-de-marca-builder --refresh maria-silva

  Prosseguir com voz stale? [s/N]
  ```
- Tata pode marcar profile como "ainda válido" manualmente (campo `stale_revisado_em` reseta o stale)

**Regra dura:**

> **Profile velho não é confiável. Skill que não checa stale é skill que gera output errado em silêncio.**

---

## ANTI-PATTERN 8 — DUPLICAR INFORMAÇÃO ENTRE PROFILES

**Exemplos que a skill RECUSA:**

- `01-perfil.publico_alvo_resumo` e `05-persona.persona_principal` divergem
- Mecanismo nome em `06-mecanismo.nome_proprietario` e `08-posicionamento.diferenciador_principal` ficam fora de sincronia
- Preço em `10-programa.preco` e `11-oferta.preco_brl` divergem
- Cores em `09-brand.paleta` e em outro profile (acidentalmente)

**Por que é fatal:**

- Cada dado vive em UM lugar canônico. Duplicação cria conflito de fonte
- Atualização em um lugar não propaga pro outro
- Skills consomem o errado e geram inconsistência
- Sincronização passa a falhar com falsos positivos

**Antídoto:**

- Schema declara campo CANÔNICO de cada dado
- Outros profiles fazem REFERÊNCIA, não cópia:
  ```json
  {
    "diferenciador_principal": "{{ref:06-mecanismo.nome_proprietario}}"
  }
  ```
- Skill `--ler` resolve referências automaticamente
- `--sincronizar` detecta cópias literais entre profiles e alerta

**Regra dura:**

> **Cada dado tem dono. Outros profiles linkam. Cópia é bug.**

---

## ANTI-PATTERN 9 — IGNORAR LGPD EM CASES E DEPOIMENTOS

**Exemplos que a skill RECUSA:**

- Case em `17-cases` sendo usado em copy SEM `autorizacao_uso_publico: true`
- Foto/vídeo de aluna sem `data_autorizacao` registrada
- Nome real de aluna em depoimento sem consentimento documentado
- Compartilhamento cross-mentorada de case (case da Maria virando proof da Ana)

**Por que é fatal:**

- Multa LGPD (até 2% do faturamento, máx R$50M)
- Processo da aluna por uso indevido de imagem/dados
- Destruição da marca ao ser exposta
- Risco contagioso: 1 case sem autorização compromete credibilidade de TODOS

**Antídoto:**

- Schema de 17-cases EXIGE `autorizacao_uso_publico: true` antes de campo `destacavel_em_pagina_vendas: true`
- Schema EXIGE `data_autorizacao` quando autorizacao é true
- Skills consumidoras (página de vendas, ads, depoimentos) FILTRAM cases sem autorização
- Tata recebe alerta mensal: cases sem autorização que estão "esquecidos" no dossiê
- Auditoria de uso público: log de cada vez que case é usado em material exposto

**Regra dura:**

> **Sem autorização documentada, case existe no dossiê pra registro interno mas NUNCA pra uso público. Skills que consomem 17-cases filtram automaticamente.**

---

## ANTI-PATTERN 10 — EXPOR DOSSIÊ INTEIRO PRA MENTORADA SEM FILTRAR

**Exemplos que a skill RECUSA:**

- `--exportar maria-silva` enviado direto pra mentorada com seções internas da Tata
- Mentorada vê notas de celeste tipo "burnout-iminente" ou "sinal-vermelho-financeiro"
- Mentorada vê scoring de risco bruto ("probabilidade-churn: 78%")
- Mentorada vê comentários estratégicos de Tata pra time

**Por que é fatal:**

- Quebra confiança absoluta (mentorada lê crítica interna sobre ela e processo termina)
- Notas internas existem PRA serem internas — Tata precisa de espaço pra avaliar friamente
- Mentorada pode contestar avaliação fora de contexto
- Risco reputacional pra Tata se algum trecho vazar

**Antídoto:**

- Modo `--exportar [slug]` tem 2 perfis:
  - `--modo full` (default — só Tata e celeste)
  - `--modo mentorada-friendly` (filtrado — pra compartilhar com mentorada)
- Modo mentorada-friendly remove:
  - Campos com prefixo `_interno_` em qualquer profile
  - Seções `notas_celeste`, `bandeira_alerta` críticas
  - Scoring de risco bruto
  - Comparação com outras mentoradas
  - Comentários informais de Tata
- Skill avisa antes de exportar full pra terceiros

**Exemplo de bloqueio:**

```
/dossie-mentorada --exportar maria-silva > /tmp/dossie.md

ATENÇÃO: você está exportando em modo FULL.

Esse export contém seções internas (notas Tata, scoring de risco,
bandeiras de alerta). NÃO compartilhar com a mentorada.

Pra exportar versão filtrada (segura pra mentorada ver), use:
  /dossie-mentorada --exportar maria-silva --modo mentorada-friendly

Confirma exportar FULL? [digite "FULL CONFIRMADO" pra prosseguir]
```

**Regra dura:**

> **O dossiê tem 2 leitores: Tata (vê tudo) e mentorada (vê filtrado). Confundir é quebra de contrato.**

---

## ANTI-PATTERN BONUS #11 — SKILL GRAVA DIRETO NO JSON BYPASSANDO `--gravar`

**Exemplos que a skill DETECTA:**

- Script bash que faz `jq` direto no arquivo
- Skill mal feita que usa `fs.writeFile` em vez de chamar `dossie-mentorada --gravar`
- Edição manual no editor de texto

**Por que é fatal:**

- Pula validação de schema
- Pula incremento de `versao`
- Pula registro em audit
- Pula side-effects (re-build de CLAUDE.md, backup)
- Cria divergência entre estado real e estado declarado

**Antídoto:**

- Hash de cada arquivo salvo em `.checksums.json`
- Cron `tatou-2.0` verifica hashes a cada 6h
- Hash diferente sem update via skill = ALERTA crítico:
  ```
  ALERTA — modificação fora-de-skill detectada

  Arquivo: ~/imperio/mentoradas/maria-silva/06-mecanismo.json
  Hash anterior: a3f4...
  Hash atual:    b2e1...
  Última gravação registrada: 2026-05-07 (skill: mecanismo-unico)
  Modificação detectada: 2026-05-08 11:23 (sem entrada em audit)

  Investigar: quem editou? por quê? rollback possível via .backups/
  ```
- Permissão de arquivo: leitura livre, escrita só via skill (bit setuid no script)

**Regra dura:**

> **Edição direta = corrupção. Sempre via `--gravar`. Sem exceção.**

---

## PROTOCOLO DE BLOQUEIO

Quando a skill detecta qualquer dos 11 anti-patterns:

1. **Operação NÃO executada**
2. **Mensagem clara** explicando qual anti-pattern foi detectado
3. **Sugestão de caminho correto**
4. **Log da tentativa** em `~/imperio/.skill-violations.log`
5. **Se reincidência** (3+ no mesmo dia): notificação pra Tata via Telegram-bot
6. **Override manual** disponível com flag `--override-anti-pattern` (registrado em audit)

### Exemplo de bloqueio com override

```
/dossie-mentorada --gravar maria-silva 17-cases '{"id":"case-005","aluno_nome":"...","autorizacao_uso_publico":false,"destacavel_em_pagina_vendas":true}'

BLOQUEIO — Anti-pattern 9 detectado (LGPD em cases)

Conflito de schema: case marcado como `destacavel_em_pagina_vendas: true`
mas `autorizacao_uso_publico: false`.

Cases sem autorização não podem ser destacados publicamente.

CAMINHOS:
  1. Coletar autorização da aluna (recomendado)
     → atualize autorizacao_uso_publico: true + data_autorizacao
  2. Desmarcar destacavel_em_pagina_vendas: false (registro interno apenas)
  3. Forçar com override (NÃO recomendado, registrado em audit)
     → adicione --override-anti-pattern "lgpd-explicitamente-aceito"

Operação NÃO executada.
```

---

## CHECKLIST DE CONFORMIDADE

Antes de toda gravação, skill `--gravar` roda checklist:

- [ ] Schema validado (anti-pattern 1)
- [ ] Slug match com pasta (anti-pattern 2)
- [ ] Audit trail criado se decisão crítica (anti-pattern 3)
- [ ] Sem credencial em campos sensíveis (anti-pattern 4)
- [ ] Tratamento explícito de campos vazios (anti-pattern 5)
- [ ] Versão incrementada, histórico preservado (anti-pattern 6)
- [ ] Stale flag respeitado (anti-pattern 7)
- [ ] Sem duplicação de dado canônico (anti-pattern 8)
- [ ] LGPD verificado em cases (anti-pattern 9)
- [ ] Modo de exportação correto se aplicável (anti-pattern 10)
- [ ] Hash atualizado em `.checksums.json` (anti-pattern 11)

Se passar todos os 11 → operação autorizada.
Se falhar 1+ → bloqueio automático.

---

## FILOSOFIA DOS ANTI-PATTERNS

Sistema de memória persistente é base de confiança. Quando 1 dossiê corrompe, ~225 skills geram output errado em silêncio. Mentorada perde fé, Tata perde tempo descobrindo onde quebrou.

Os 10 anti-patterns acima cobrem 95% dos modos de falha observados em ecossistemas de skills. Skill `dossie-mentorada` foi projetada pra ser PARANOICA — bloquear primeiro, perguntar depois.

> **Melhor bloquear operação válida e fazer Tata explicar do que aceitar operação inválida e descobrir 6 meses depois que dossiê está corrompido.**

---

**Anti-patterns — Dossiê Mentorada v1.0. Propriedade intelectual Tata Gonçalves.**
