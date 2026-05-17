---
name: criativos-mentorados-setup
description: >
  Onboarding para mentorados configurarem suas fotos de referencia e chave Gemini API
  para usar as skills de criativos (dor-beneficio, urgencia, retargeting, qa-instagram).
  Coleta fotos, API key, descricao fisica, nome e Instagram UMA UNICA VEZ e salva
  em ~/.criativos-mentorados/config.json. Todas as skills de criativos-mentorados leem daqui.
  Use quando o mentorado pedir "configurar criativos", "setup criativos", "cadastrar minhas fotos",
  "minha chave gemini", ou quando qualquer skill de criativos-mentorados detectar que o config nao existe.
user_invocable: true
---

# Onboarding Criativos — Configuracao do Mentorado

Este onboarding coleta e salva as informacoes do mentorado UMA UNICA VEZ para que todas as skills de criativos funcionem com a identidade e chave dele.

## O que e coletado

1. **Fotos de referencia** (1 a 3 fotos) — usadas pelo Gemini para clonar a identidade
2. **Chave Gemini API** — para gerar as fotos com IA
3. **Descricao fisica** — para os prompts de geracao de foto
4. **Nome** — para overlay nos criativos
5. **Instagram** — para overlay nos criativos (opcional)

## Onde salva

```
~/.criativos-mentorados/
  config.json          — todas as configs
  assets/
    foto1.png          — foto de referencia 1
    foto2.png          — foto de referencia 2 (opcional)
    foto3.png          — foto de referencia 3 (opcional)
```

## Processo de Onboarding (SEGUIR EXATAMENTE)

### Passo 1: Verificar se ja existe config

```bash
cat ~/.criativos-mentorados/config.json 2>/dev/null
```

Se existir, mostrar ao mentorado:
- "Voce ja tem um perfil configurado! Aqui estao seus dados:"
- Mostrar nome, instagram, quantas fotos, descricao
- Perguntar: "Quer atualizar algo ou esta tudo certo?"
- Se quiser atualizar, prosseguir com os passos abaixo (so os campos que quer mudar)

Se NAO existir, comecar onboarding completo:

### Passo 2: Criar diretorio

```bash
mkdir -p ~/.criativos-mentorados/assets
```

### Passo 3: Coletar FOTOS de referencia

Dizer ao mentorado:

---
**Suas fotos de referencia**

Preciso de 1 a 3 fotos suas para a IA clonar sua identidade nos criativos.

**Regras das fotos:**
- Rosto bem visivel, boa iluminacao
- De preferencia fotos diferentes (angulos, roupas, cenarios)
- Podem ser selfies ou fotos profissionais
- Formato: PNG ou JPG
- Minimo 1 foto, ideal 3

**Como enviar:**
Arraste as fotos aqui no chat, ou me diga o caminho completo dos arquivos.
Exemplo: `~/Downloads/minha-foto.png`

---

Quando o mentorado fornecer as fotos:
- Copiar cada foto para `~/.criativos-mentorados/assets/foto1.png`, `foto2.png`, `foto3.png`
- Usar `cp` (NUNCA mover, sempre copiar)
- Verificar que os arquivos existem apos copiar

```bash
cp "<caminho-fornecido-1>" ~/.criativos-mentorados/assets/foto1.png
cp "<caminho-fornecido-2>" ~/.criativos-mentorados/assets/foto2.png  # se tiver
cp "<caminho-fornecido-3>" ~/.criativos-mentorados/assets/foto3.png  # se tiver
```

### Passo 4: Coletar CHAVE GEMINI API

Dizer ao mentorado:

---
**Sua chave Gemini API**

Preciso da sua chave de API do Google Gemini para gerar as fotos com IA.

Se voce ainda nao tem uma chave:
1. Acesse: https://aistudio.google.com/apikey
2. Clique em "Create API Key"
3. Copie a chave gerada

Cole sua chave aqui:

---

Quando receber a chave:
- Validar formato (comeca com "AI" e tem ~39 caracteres)
- NAO mostrar a chave de volta no chat (seguranca)
- Salvar no config

### Passo 5: Coletar DESCRICAO FISICA

Dizer ao mentorado:

---
**Sua descricao fisica**

Para a IA gerar fotos que parecam VOCE, preciso de uma descricao detalhada:

- Genero
- Etnia/tom de pele
- Faixa etaria
- Tipo corporal (magro, medio, plus size, atletico)
- Cabelo (cor, comprimento, textura — liso, ondulado, cacheado, crespo)
- Cor dos olhos
- Estilo de roupa habitual (casual, elegante, profissional)
- Maquiagem habitual (se usar)
- Acessorios marcantes (oculos, brincos, colar, relogio)

Exemplo: "Mulher brasileira, pele morena, 35 anos, corpo medio, cabelo castanho ondulado na altura dos ombros, olhos castanhos, estilo casual elegante, maquiagem natural, brincos pequenos dourados"

---

### Passo 6: Coletar NOME e INSTAGRAM

Dizer ao mentorado:

---
**Seu nome e Instagram**

- Seu nome (como quer que apareca nos criativos):
- Seu @ do Instagram (opcional, para overlay):

---

### Passo 7: Salvar config.json

Montar e salvar o arquivo de configuracao:

```bash
cat > ~/.criativos-mentorados/config.json << 'EOF'
{
  "expertName": "<nome>",
  "expertInstagram": "<instagram sem @>",
  "expertDescription": "<descricao fisica em ingles para prompts Gemini>",
  "expertPhotos": [
    "/Users/<username>/.criativos-mentorados/assets/foto1.png",
    "/Users/<username>/.criativos-mentorados/assets/foto2.png",
    "/Users/<username>/.criativos-mentorados/assets/foto3.png"
  ],
  "geminiApiKey": "<chave>",
  "setupDate": "<YYYY-MM-DD>",
  "photoCount": <1|2|3>
}
EOF
```

**IMPORTANTE sobre expertDescription:**
- Traduzir a descricao do mentorado para INGLES (prompts Gemini funcionam melhor em ingles)
- Formato: "Brazilian woman, brown shoulder-length wavy hair, warm brown eyes, medium body type, wearing casual elegant clothing, natural makeup, small gold earrings"
- Incluir TODOS os detalhes fornecidos
- Manter o array expertPhotos APENAS com as fotos que existem (se so tem 1, so 1 entrada)

### Passo 8: Confirmar setup

Mostrar ao mentorado:

---
**Configuracao salva com sucesso!**

- Nome: [nome]
- Instagram: @[instagram]
- Fotos cadastradas: [X] foto(s)
- Chave Gemini: configurada
- Descricao: [resumo em PT-BR]

Agora voce pode usar qualquer uma dessas skills:

- `/criativos-dor-beneficio-mentorados` — Criativos de Dor e Beneficio (6 PNGs)
- `/criativos-urgencia-mentorados` — Criativos de Urgencia/Escassez (8 PNGs)
- `/criativos-retargeting-mentorados` — Criativos de Retargeting (4 PNGs)
- `/criativos-qa-instagram-mentorados` — Q&A Instagram a partir de aula (20 PNGs)

Todas vao usar suas fotos e sua chave automaticamente!

---

## Atualizacao parcial

Se o mentorado quiser atualizar apenas UM campo:
- Ler o config existente
- Alterar APENAS o campo solicitado
- Salvar de volta
- Confirmar a alteracao

Campos atualizaveis individualmente:
- `fotos` — "quero trocar minhas fotos"
- `chave` — "quero trocar minha API key"
- `descricao` — "quero atualizar minha descricao"
- `nome` — "quero mudar meu nome"
- `instagram` — "quero mudar meu instagram"

## Regras

1. **NUNCA** mostrar a chave Gemini completa no chat (mostrar so os primeiros 4 caracteres + "...")
2. **SEMPRE** copiar fotos (nunca mover)
3. **SEMPRE** traduzir descricao para ingles no config
4. **SEMPRE** verificar que os arquivos de foto existem apos copiar
5. **SEMPRE** usar caminhos absolutos no config (com /Users/<username>/)
6. **NUNCA** sobrescrever config sem confirmar com o mentorado
7. Se o mentorado fornecer foto por drag-and-drop no chat, o Claude recebe o caminho temporario — copiar imediatamente para assets/
