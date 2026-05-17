# Modo: ESTRUTURA

## Quando usar

- Conteúdo já existe mas está bagunçado
- Currículo de curso/mentoria
- Sumário de ebook/livro próprio
- Lista de skills/ferramentas pra organizar
- Documentação/processo

## Estratégia

Não cria conteúdo novo — **revela a hierarquia que já está lá**. Você é arqueólogo: cava, agrupa, hierarquiza.

3 movimentos:

1. **Inventário:** lista TUDO que está no input
2. **Agrupamento:** categoriza por afinidade
3. **Hierarquização:** define o que é nível 1, 2, 3

## Hierarquia base

```
NÍVEL 0: Nome da estrutura
NÍVEL 1: Seções/módulos/áreas (3-7)
NÍVEL 2: Subseções/aulas/itens
NÍVEL 3: Detalhes/checklists
```

## Templates por tipo

### Currículo de curso

```
ROOT: <nome do curso>
├── Módulo 1: <nome>
│   ├── Aula 1.1
│   ├── Aula 1.2
│   └── Material complementar
├── Módulo 2: <nome>
└── ...
```

### Mentoria

```
ROOT: <nome da mentoria>
├── Onboarding
├── Pilares (5-7 áreas)
├── Encontros
├── Materiais
└── Suporte/comunidade
```

### Documentação/processo

```
ROOT: <nome do processo>
├── Pré-requisitos
├── Passos (numerados)
├── Validações
├── Erros comuns
└── Referências
```

## Adaptação ao input

- **Lista numerada existente:** mantém ordem como ramos
- **Texto corrido:** extrai listas implícitas (palavras como "primeiro", "depois", "também")
- **Múltiplos arquivos:** cada arquivo vira um ramo principal
- **Notas Obsidian:** usa tags como ramos

## Conexões cruzadas típicas

- Pré-requisitos ↔ Validações (o que precisa virar o que checar)
- Módulo X ↔ Módulo Y (dependência de conteúdo)
- Aulas ↔ Materiais complementares

## Erros a evitar

- Manter ordem do input quando agrupamento melhor existe
- Ramo "Outros" — força agrupar tudo em categoria nomeada
- Hierarquia plana (tudo no nível 1) — força desdobrar
