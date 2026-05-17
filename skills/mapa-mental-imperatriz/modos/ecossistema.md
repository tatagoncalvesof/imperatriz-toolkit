# Modo: ECOSSISTEMA

## Quando usar

- Mapear sistema complexo (skills, agentes, ferramentas)
- Visualizar arquitetura de stack
- Onboarding técnico (mostrar o todo)
- Inventário de ativos
- Documentação de império/operação

## Estratégia

Mapa de ecossistema é **anatomia visual** — mostra peças, função de cada uma, e como se conectam.

3 movimentos:

1. **Identificar peças** (skills, ferramentas, agentes, processos)
2. **Agrupar por função** (categorias funcionais)
3. **Desenhar conexões** (o que alimenta o quê) — aqui as cross-connections explodem

## Hierarquia base

```
NÍVEL 0: Nome do sistema/ecossistema
NÍVEL 1: Categorias funcionais (5-7)
NÍVEL 2: Peças específicas
NÍVEL 3: Função de cada peça (1 frase)
```

## Templates por tipo

### Mapa de skills/agentes

```
ROOT: <Império IA — meu arsenal>
├── Copy
│   ├── briefing-copy-360
│   ├── headline-imperatriz
│   ├── mecanismo-unico
│   └── voz-humana-br
├── Funil
│   ├── funil-completo
│   ├── funil-novela
│   └── funil-registro
├── Ads
│   ├── ads (orquestrador)
│   ├── ads-meta
│   ├── ads-google
│   └── analise-anuncio-1000
├── Conteúdo
│   ├── stories-pergunta-resposta
│   ├── skill-carrossel-instagram
│   └── linkedin-empire
├── Mentoria
│   ├── transcricao-mentoradas
│   ├── editordeaulas
│   └── celeste
└── Infra
    ├── imperio-infra
    ├── shield
    └── guardian
```

### Stack técnico

```
ROOT: <Stack do projeto>
├── Frontend
├── Backend
├── Banco
├── Infra/Deploy
├── Integrações externas
└── Observabilidade
```

### Time/operação

```
ROOT: <Operação>
├── Time
├── Processos
├── Ferramentas
├── Métricas
└── Ritmos (reuniões, ciclos)
```

## Adaptação ao input

- **Lista de skills do `~/.claude/skills/`:** lê os SKILL.md, agrupa por descrição
- **Stack a partir de package.json/requirements:** extrai dependências
- **Sistema complexo descrito em texto:** identifica entidades + relações

## Conexões cruzadas (CRÍTICAS neste modo)

Mapa de ecossistema SEM conexões cruzadas é catálogo, não mapa. As conexões são o ouro.

Tipos de conexão a procurar:

- **Alimentação:** A produz X que B consome (briefing → copy → página)
- **Dependência:** B só funciona se A existe
- **Substituição:** A e B fazem coisa parecida (escolha)
- **Composição:** A + B juntos = C

Marca no Mermaid com linha tracejada e label.

## Exemplo de conexões cruzadas

```
briefing-copy-360 -.alimenta.-> headline-imperatriz
mecanismo-unico -.compõe.-> skill-pagina-vendas
voz-humana-br -.valida saída de.-> headline-imperatriz
transcricao-mentoradas -.produz input pra.-> mapa-mental-imperatriz
```

## Erros a evitar

- Listar peças sem função (só nome = catálogo)
- Esquecer conexões (perde o "ecossistema", vira lista)
- Hierarquia plana (todas no nível 1) — agrupa em categorias
- Misturar peças funcionais com peças de infra (separa)

## Output adicional sugerido

Quando o mapa for grande (>30 peças), gera também:

- **Lista priorizada:** peças core vs auxiliares
- **Gaps:** o que falta no ecossistema (categoria sem peça)
- **Sobreposições:** peças que fazem coisa parecida
