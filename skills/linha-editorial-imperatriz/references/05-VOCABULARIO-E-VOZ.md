# 05 — Vocabulário e Voz

## De onde vem o vocabulário ON/OFF

A skill **não inventa** vocabulário. Sintetiza a partir de três fontes que **já existem** no ecossistema da mentorada:

| Fonte | O que extrai | Skill que produziu |
|---|---|---|
| `03-voz-de-marca.json` | Palavras-âncora, palavras banidas, abertura padrão, fechamento padrão, exemplos canônicos | `/voz-de-marca-builder` |
| Vocabulário oficial da Marca Sistêmica (se existir) | Linguagem ritualística da Corte, termos próprios do método | `/marca-sistemica-imperatriz` |
| Pilares temáticos (etapa 02 desta skill) | Termos que aparecem em cada pilar (mecanismo, dor, transformação) | (esta skill) |

A skill **agrega**, **deduplica**, **prioriza por frequência** e **devolve** uma lista canônica de vocabulário ON/OFF.

## Estrutura do vocabulário

### Palavras-âncora (mínimo 30)

Palavras que **devem aparecer** no conteúdo da marca pra reforçar identidade. Exemplos por tipo:

- **Termos do método** (proprietários da mentorada): "Sistema Imperatriz", "Etapa 3", "Pitch Soberano"
- **Termos do mecanismo único**: o nome próprio + variações
- **Verbos da transformação**: o que a mentorada faz acontecer ("destrava", "abre", "investe")
- **Palavras que viraram identidade da pessoa**: gírias autorizadas, expressões recorrentes
- **Vocabulário do nicho** (sem virar jargão): termos que o cliente ideal usa

### Palavras banidas (mínimo 30)

Tudo que **não pode aparecer**, organizado em categorias:

#### 1. Cara de IA (sempre banidas)
- `ecossistema` (sem ser tech)
- `jornada` (genérico)
- `framework` (sem ser técnico)
- `abraçar` (mudança, transformação)
- `desbloquear` (potencial)
- `sinergia`, `holístico`, `disruptivo`, `escalável` (sem contexto técnico)
- `mergulhar` (em qualquer coisa)
- `navegar` (pelos desafios)

#### 2. Travessões (—, –, --) e seus substitutos forçados
A skill marca travessões como banidos. Substitui por: ponto final, vírgula, parênteses ou nova frase.

#### 3. Hedging tóxico
- `talvez`, `pode ser`, `acho que`, `meio que`, `de certa forma`
- (mentorada Imperatriz não fala em "talvez" sobre o próprio método)

#### 4. Sicofancia
- `excelente pergunta`, `ótimo ponto`, `que insight incrível`
- (qualquer adjetivo gratuito sobre o leitor)

#### 5. Jargão de copy ruim
- `transformar sua vida`, `mudar o jogo`, `próximo nível`, `unlock`, `boost`
- `verdade incômoda`, `segredo que ninguém te conta`
- `não é mais um curso`

#### 6. Termos do nicho que viraram cliché
A skill puxa do nicho específico:
- Mentoria: "minha alma sabia", "se permita", "se autorize"
- Marketing: "alavancar", "potencializar", "engajamento real"
- Coaching: "tirar do estado", "elevar a frequência"

#### 7. Palavras genéricas sem ancoragem
- `amor`, `gratidão`, `propósito` — banidas SE usadas sozinhas, sem ancoragem em ato

#### 8. Termos da concorrência direta
A skill marca termos que **outras** mentoradas/concorrentes usam — pra a marca não virar eco.

## Abertura e fechamento padrão

### Abertura padrão (max 3 variações)

Como a marca **começa** um post/email/story. Puxado da voz-de-marca. Exemplos:

- "Vou te contar uma coisa que..."
- "Tem uma frase que eu falo demais aqui dentro:"
- "Toda semana acontece isso:"

### Fechamento padrão (max 3 variações)

Como a marca **fecha** um post/email/story. Não é CTA — é assinatura. Exemplos:

- "É isso. Boa semana."
- "Conta pra mim quando aplicar."
- "Imperatriz não pede licença. Bora."

## Voz × Forma (a regra que não se viola)

| Constante | Variável |
|---|---|
| Voz da mentorada (sempre a mesma) | Forma por canal (calibra) |
| Vocabulário-âncora (sempre presente) | Densidade do vocabulário (mais técnico no LinkedIn, mais íntimo no WhatsApp) |
| Palavras banidas (sempre banidas) | — |
| Abertura/fechamento padrão | Pode variar entre as 3 versões registradas |

## Cruzamento com `voz-humana-br`

Esta skill **declara** o vocabulário. A skill `/voz-humana-br` **valida** que ele foi respeitado depois da escrita.

Fluxo:
1. Linha editorial declara `palavras_banidas`
2. Mentorada (ou outra skill) escreve a peça
3. `/voz-humana-br` checa: peça usou alguma palavra banida? Removeu travessão? Manteve voz?
4. Se sim, devolve corrigida. Se não, aprova.

**Sem essa skill, voz-humana-br trabalha com lista genérica.** Com essa skill, voz-humana-br trabalha com a lista PERSONALIZADA da mentorada.

## Exemplo de vocabulário ON/OFF gerado

```json
"vocabulario": {
  "palavras_ancora": [
    "Imperatriz", "Travessia", "Soberana", "Decreto", "Câmara",
    "destravar", "investir em si", "ato político", "pitch soberano",
    "sala", "trono", "sucessão", "dossiê", "ritual", "porta",
    "marquesa", "princesa", "estação", "porta atual", "salto",
    "abrir conta", "fechar conta", "sentar na mesa", "tomar lugar",
    "conduzir", "audiência", "investidura", "coroação", "protocolo"
  ],
  "palavras_banidas": [
    "ecossistema", "jornada", "framework", "abraçar mudança",
    "desbloquear potencial", "—", "talvez", "acho que",
    "excelente pergunta", "transformar sua vida", "mudar o jogo",
    "próximo nível", "verdade incômoda", "segredo", "alma sabia",
    "se permita", "se autorize", "alavancar", "potencializar",
    "engajamento real", "elevar a frequência", "amor universal",
    "gratidão genuína", "propósito divino", "mergulhar fundo",
    "navegar pelos desafios", "sinergia", "holístico", "disruptivo"
  ],
  "abertura_padrao": [
    "Vou te contar uma coisa que...",
    "Toda semana acontece isso aqui:",
    "Tem uma frase que eu repito muito:"
  ],
  "fechamento_padrao": [
    "É isso. Boa semana.",
    "Conta pra mim quando aplicar.",
    "Imperatriz não pede licença. Bora."
  ]
}
```

## Validação obrigatória

Antes de a skill aprovar a linha (e exportar), checa que:

1. ✅ Mínimo 30 palavras-âncora
2. ✅ Mínimo 30 palavras banidas
3. ✅ Travessão (`—`, `–`, `--`) está nas banidas
4. ✅ Pelo menos 1 abertura e 1 fechamento padrão
5. ✅ Nenhuma palavra está nas duas listas (ON e OFF)
6. ✅ Manifesto editorial (próximo arquivo) **não usa** nenhuma palavra banida — se usar, é falha de skill, refazer
