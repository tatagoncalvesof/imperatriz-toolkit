#!/usr/bin/env python3
"""
detectar_ia_ptbr.py — Detector de padrões de IA em texto PT-BR.

Varre texto em busca de todos os tiques conhecidos de IA em português brasileiro
e produz um relatório estruturado (JSON ou Markdown). Zero dependência externa,
só stdlib Python 3.10+.

Uso:
    python3 detectar_ia_ptbr.py input.txt
    python3 detectar_ia_ptbr.py input.txt --formato json
    python3 detectar_ia_ptbr.py input.txt --formato markdown
    cat input.txt | python3 detectar_ia_ptbr.py

Baseado em:
    - reference/palavras-proibidas-ptbr.md
    - reference/frases-proibidas-ptbr.md
    - reference/padroes-estruturais-ptbr.md
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from typing import Any

# ============================================================================
# SEÇÃO 1 — LISTAS DE PALAVRAS VERMELHAS E AMARELAS
# ============================================================================

VERBOS_VERMELHOS = [
    "mergulhar", "mergulhamos", "mergulhou", "mergulha", "mergulhando",
    "sublinhar", "sublinha", "sublinhou", "sublinhando",
    "alavancar", "alavanca", "alavancou", "alavancando",
    "potencializar", "potencializa", "potencializou", "potencializando",
    "maximizar", "maximiza", "maximizou", "maximizando",
    "facilitar", "facilita", "facilitou", "facilitando",
    "viabilizar", "viabiliza", "viabilizou", "viabilizando",
    "propiciar", "propicia", "propiciou", "propiciando",
    "oportunizar", "oportuniza", "oportunizou",
    "fomentar", "fomenta", "fomentou", "fomentando",
    "desencadear", "desencadeia", "desencadeou", "desencadeando",
    "desbloquear", "desbloqueia", "desbloqueou",
    "transcender", "transcende", "transcendeu",
    "embarcar", "embarca", "embarcou", "embarcando",
    "abraçar", "abraça", "abraçou", "abraçando",
    "elevar", "eleva", "elevou", "elevando",
    "aprimorar", "aprimora", "aprimorou", "aprimorando",
    "iluminar", "ilumina", "iluminou",
    "revolucionar", "revoluciona", "revolucionou", "revolucionando",
    "inovar", "inova", "inovou", "inovando",
    "entrelaçar", "entrelaça", "entrelaçou", "entrelaçando",
    "reimaginar", "reimagina", "reimaginou",
    "descortinar", "descortina",
    "desvendar", "desvenda", "desvendou", "desvendando",
    "cativar", "cativa", "cativou", "cativando",
    "encantar", "encanta", "encantou",
    "otimizar", "otimiza", "otimizou", "otimizando",
    "empoderar", "empodera", "empoderou", "empoderando",
    "catalisar", "catalisa", "catalisou",
    "impulsionar", "impulsiona", "impulsionou", "impulsionando",
    "encapsular", "encapsula", "encapsulou",
    "exemplificar", "exemplifica", "exemplificou",
    "personificar", "personifica", "personificou",
    "galvanizar", "galvaniza",
    "propelir", "propele",
    "utilizar", "utiliza", "utilizou", "utilizando", "utilizamos",
    "realizar", "realiza", "realizou", "realizando", "realizamos",
    "efetuar", "efetua", "efetuou",
    "demonstrar", "demonstra", "demonstrou", "demonstrando",
    "elucidar", "elucida", "elucidou",
    "averiguar", "averigua", "averiguou",
    "necessitar", "necessita", "necessitou", "necessitando",
    "possuir", "possui", "possuíram", "possuindo",
    "obter", "obtém", "obteve", "obtendo",
    "adquirir", "adquire", "adquiriu", "adquirindo",
    "indagar", "indaga", "indagou",
    "residir", "reside", "residiu",
    "abranger", "abrange", "abrangeu", "abrangendo",
    "englobar", "engloba", "englobou",
    "ostentar", "ostenta", "ostentou",
    "constituir", "constitui", "constituiu", "constituindo",
    "encarnar", "encarna", "encarnou",
    "contemplar", "contempla", "contemplou", "contemplando",
    "liberar", "libera", "liberou",
]

ADJETIVOS_VERMELHOS = [
    "crucial", "cruciais",
    "vital", "vitais",
    "imprescindível", "imprescindíveis",
    "indispensável", "indispensáveis",
    "nuançado", "nuançada", "nuançados", "nuançadas",
    "multifacetado", "multifacetada", "multifacetados", "multifacetadas",
    "holístico", "holística", "holísticos", "holísticas",
    "impecável", "impecáveis",
    "inovador", "inovadora", "inovadores", "inovadoras",
    "inédito", "inédita", "inéditos", "inéditas",
    "revolucionário", "revolucionária", "revolucionários", "revolucionárias",
    "transformador", "transformadora", "transformadores", "transformadoras",
    "disruptivo", "disruptiva", "disruptivos", "disruptivas",
    "compelativo", "compelativa",
    "profundo", "profunda", "profundos", "profundas",
    "meticuloso", "meticulosa", "meticulosos", "meticulosas",
    "intrincado", "intrincada", "intrincados", "intrincadas",
    "inestimável", "inestimáveis",
    "exemplar", "exemplares",
    "elusivo", "elusiva",
    "pungente", "pungentes",
    "vibrante", "vibrantes",
    "vívido", "vívida", "vívidos", "vívidas",
    "vanguardista", "vanguardistas",
    "louvável", "louváveis",
    "imersivo", "imersiva",
    "impactante", "impactantes",
    "magnânimo", "magnânima",
    "descomplicado", "descomplicada",
    "exponencial", "exponenciais",
]

SUBSTANTIVOS_VERMELHOS_METAFORAS = [
    "jornada", "jornadas",
    "panorama", "panoramas",
    "paisagem", "paisagens",
    "esfera",
    "reino", "reinos",
    "farol",
    "testemunho", "testemunhos",
    "sinfonia",
    "mosaico",
    "nexo", "nexus",
    "paradigma", "paradigmas",
    "sinergia", "sinergias",
    "catalisador", "catalisadores",
    "alicerce", "alicerces",
    "tapeçaria",
    "caleidoscópio",
    "labirinto",
    "ecossistema", "ecossistemas",
    "miríade", "miríades",
    "gama", "gamas",
    "arsenal",
    "vertente", "vertentes",
    "prisma",
    "ótica",
    "patamar", "patamares",
    "mindset",
    "deliverável",
]

ADVERBIOS_VERMELHOS = [
    "ademais",
    "outrossim",
    "destarte",
    "doravante",
    "notadamente",
    "adicionalmente",
    "crucialmente",
    "meticulosamente",
    "impecavelmente",
    "aptamente",
    "dinamicamente",
    "indelevelmente",
    "vibrantemente",
    "vividamente",
    "indubitavelmente",
    "inegavelmente",
    "ostensivamente",
    "deveras",
    "sobremaneira",
    "mormente",
    "outrora",
    "porventura",
]

PALAVRAS_AMARELAS = [
    "abrangente", "significativo", "significativa", "significativos", "significativas",
    "fundamental", "fundamentais",
    "essencial", "essenciais",
    "dinâmico", "dinâmica", "dinâmicos", "dinâmicas",
    "estratégico", "estratégica", "estratégicos", "estratégicas",
    "robusto", "robusta", "robustos", "robustas",
    "notável", "notáveis",
    "potencial", "potenciais",
]

TRANSICOES_BANIDAS = [
    "contudo,", "entretanto,", "todavia,", "não obstante,",
    "por conseguinte,", "haja vista", "mediante",
    "visando ", "a fim de ", "com o intuito de ", "com o objetivo de ",
    "em virtude de ", "tendo em vista que ", "pelo fato de ",
    "no presente momento", "neste momento",
    "anteriormente a ", "posteriormente a ",
    "subsequentemente",
    "no que tange a ", "no que se refere a ", "no que diz respeito a ",
    "diversos ", "diversas ", "inúmeros ", "inúmeras ",
]

# ============================================================================
# SEÇÃO 2 — FRASES BANIDAS (regex)
# ============================================================================

ABERTURAS_BANIDAS = [
    r"no mundo atual",
    r"nos dias de hoje",
    r"no cenário atual",
    r"no cenário em constante evolução",
    r"em um cenário em que",
    r"em um mundo onde",
    r"num mundo cada vez mais",
    r"na era (da|digital|do)",
    r"vivemos em uma época",
    r"estamos vivendo um momento",
    r"mais do que nunca",
    r"hoje mais do que nunca",
    r"agora mais do que nunca",
    r"diante desse cenário",
    r"não é novidade que",
    r"não é segredo que",
    r"você já deve ter ouvido",
    r"todo mundo sabe que",
    r"vamos mergulhar",
    r"vamos explorar",
    r"vamos descobrir",
    r"vamos desvendar",
    r"prepare-se para",
    r"abaixo, compartilho",
    r"neste artigo, vamos",
    r"neste post, vou",
    r"imagina o seguinte cenário",
    r"imagina isso",
    r"antes de mais nada",
    r"sem mais delongas",
    r"sem enrolação",
]

FECHAMENTOS_BANIDOS = [
    r"em conclusão",
    r"em resumo",
    r"em suma",
    r"em síntese",
    r"pra concluir",
    r"pra finalizar",
    r"concluindo,",
    r"finalizando,",
    r"em última análise",
    r"ao fim e ao cabo",
    r"no final das contas",
    r"no final do dia",
    r"o futuro é promissor",
    r"só o tempo dirá",
    r"uma coisa é certa",
    r"as possibilidades são infinitas",
    r"o céu é o limite",
    r"daqui pra frente",
    r"olhando pra frente",
    r"a jornada continua",
    r"isso é só o começo",
]

HYPE_VENDAS = [
    r"desbloqueie o poder",
    r"libere o potencial",
    r"libere seu potencial",
    r"acelere seu",
    r"turbine seu",
    r"potencialize seu",
    r"maximize seus resultados",
    r"divisor de águas",
    r"game[- ]changer",
    r"é aí que entra",
    r"revolucionando a forma",
    r"transformando x em y",
    r"prepare-se para uma revolução",
    r"saia na frente",
    r"empresas visionárias",
    r"simplesmente não consegue",
    r"vantagem estratégica",
    r"vantagem competitiva",
    r"elevar a outro patamar",
    r"levar a outro nível",
    r"estamos felizes em anunciar",
    r"com imenso orgulho",
    r"é com satisfação que",
    r"integra-se perfeitamente",
    r"na vanguarda da inovação",
    r"sucesso garantido",
    r"resultados extraordinários",
    r"vida que você merece",
    r"você merece mais",
]

HEDGING = [
    r"é importante (notar|ressaltar|lembrar)",
    r"vale (a pena|mencionar|ressaltar)",
    r"cabe destacar",
    r"convém observar",
    r"é preciso (entender|lembrar) que",
    r"não daria pra falar de .* sem mencionar",
    r"de maneira geral",
    r"de um modo amplo",
    r"pode potencialmente",
    r"talvez possivelmente",
    r"poderia vir a",
    r"teoricamente falando",
    r"pode-se argumentar",
    r"alguém poderia dizer",
    r"há quem diga",
    r"não é exagero dizer",
]

ATRIBUICAO_VAGA = [
    r"especialistas afirmam",
    r"especialistas do mercado",
    r"observadores apontam",
    r"analistas acreditam",
    r"relatórios da indústria",
    r"pesquisas recentes mostram",
    r"estudos indicam",
    r"estudos mostram",
    r"segundo especialistas",
    r"muitos acreditam",
    r"muitas pessoas",
    r"cada vez mais pessoas",
    r"é amplamente aceito",
    r"como é do conhecimento de todos",
    r"diz-se que",
    r"comenta-se que",
    r"dizem por aí",
    r"grande parte das pessoas",
    r"maioria esmagadora",
]

SICOFANCIA = [
    r"ótima pergunta",
    r"excelente pergunta",
    r"que pergunta (incrível|ótima)",
    r"com certeza!",
    r"absolutamente!",
    r"será um prazer",
    r"fico feliz em ajudar",
    r"espero que (isso )?ajude",
    r"espero ter ajudado",
    r"me avisa se precisar",
    r"fico à disposição",
    r"estou à disposição",
    r"quer que eu detalhe",
    r"posso elaborar",
    r"você está absolutamente (certo|certa)",
    r"esse é um ótimo ponto",
    r"excelente observação",
    r"espero que este e-mail te encontre",
]

CONVERSA_FALSA = [
    r"vamos ser sinceros",
    r"vamos ser honestos",
    r"vou te contar a verdade",
    r"aqui vai a verdade nua e crua",
    r"aqui está o que ninguém te conta",
    r"vamos encarar",
    r"mas vamos ao que importa",
    r"o que isso significa pra você",
    r"mas por que isso importa",
    r"nem todos os .* são iguais",
    r"a boa notícia\?",
    r"a má notícia\?",
    r"a grande sacada",
    r"o grande segredo",
    r"a chave está em",
    r"está na hora de",
    r"chegou a hora de",
    r"aqui está o que você precisa saber",
    r"faça .* para que você possa",
    r"essa é a diferença entre quem .* e quem",
]

PARALELISMO_NEGATIVO = [
    r"não é só .*?\. é ",
    r"não é apenas .*?\. é ",
    r"não se trata apenas de .*? mas",
    r"não é sobre .*?\. é sobre",
    r"isso não é .*?\. é ",
    r"não é mais um .*?\. é ",
    r"não é teoria\. é prática",
    r"não é promessa\. é resultado",
]

# Gerúndios "de cauda" (vêm DEPOIS de vírgula no fim da frase)
GERUNDIOS_CAUDA = [
    "gerando", "criando", "causando", "provocando",
    "destacando", "enfatizando", "sublinhando",
    "mostrando", "demonstrando", "evidenciando",
    "refletindo", "simbolizando", "representando",
    "preparando", "pavimentando",
    "garantindo", "assegurando",
    "fomentando", "incentivando",
    "permitindo", "possibilitando",
    "impulsionando", "fortalecendo",
    "revelando", "transformando",
]

FAIXAS_FALSAS_REGEX = r"\bde\s+\w+\s+(?:a|até)\s+\w+"

CORRELATIVOS = [
    r"não só .* mas também",
    r"não apenas .* como também",
    r"seja .* seja",
    r"tanto .* quanto",
]

GANGORRA_HEDGE = [
    r"embora .* tenha",
    r"apesar de .* também",
    r"se por um lado .* por outro",
    r"ainda que .* apresente",
]

TRAVESSAO = "—"
TRAVESSAO_DUPLO = "--"

# ============================================================================
# SEÇÃO 3 — FUNÇÕES DE VARREDURA
# ============================================================================

def tokenizar_frases(texto: str) -> list[str]:
    """Divide texto em frases simples por pontuação terminal."""
    frases = re.split(r'(?<=[.!?])\s+', texto.strip())
    return [f.strip() for f in frases if f.strip()]


def contar_palavras(frase: str) -> int:
    """Conta palavras em uma frase (ignora pontuação)."""
    return len(re.findall(r"\b\w+\b", frase))


def detectar_palavras(texto: str, lista: list[str], severidade: str) -> list[dict]:
    """Detecta ocorrências de palavras da lista (word-boundary)."""
    achados = []
    texto_lower = texto.lower()
    for palavra in lista:
        for match in re.finditer(r"\b" + re.escape(palavra.lower()) + r"\b", texto_lower):
            achados.append({
                "palavra": palavra,
                "posicao": match.start(),
                "severidade": severidade,
            })
    return achados


def detectar_frases(texto: str, padroes: list[str], categoria: str) -> list[dict]:
    """Detecta ocorrências de padrões regex de frase."""
    achados = []
    for padrao in padroes:
        for match in re.finditer(padrao, texto, flags=re.IGNORECASE):
            achados.append({
                "padrao": padrao,
                "trecho": match.group(0)[:100],
                "posicao": match.start(),
                "categoria": categoria,
            })
    return achados


def detectar_paralelismo_negativo(texto: str) -> list[dict]:
    """Detecta padrões 'não é só X. É Y.' etc."""
    achados = []
    for padrao in PARALELISMO_NEGATIVO:
        for match in re.finditer(padrao, texto, flags=re.IGNORECASE):
            achados.append({
                "padrao": padrao,
                "trecho": match.group(0)[:120],
                "posicao": match.start(),
            })
    # Busca adicional: "Não é [palavra]. É [palavra]."
    for match in re.finditer(r"Não\s+é\s+\w+[\.;]\s+É\s+\w+", texto):
        achados.append({
            "padrao": "não é X. é Y.",
            "trecho": match.group(0)[:120],
            "posicao": match.start(),
        })
    return achados


def detectar_gerundio_cauda(texto: str) -> list[dict]:
    """Detecta gerúndio na cauda de frase (vírgula + gerúndio + ...)."""
    achados = []
    for gerundio in GERUNDIOS_CAUDA:
        # vírgula + espaços + gerúndio + qualquer coisa até ponto
        padrao = r",\s+" + re.escape(gerundio) + r"\b[^.!?]*[.!?]"
        for match in re.finditer(padrao, texto, flags=re.IGNORECASE):
            achados.append({
                "gerundio": gerundio,
                "trecho": match.group(0)[:120],
                "posicao": match.start(),
            })
    return achados


def detectar_faixas_falsas(texto: str) -> list[dict]:
    """Detecta 'de X a Y' construções."""
    achados = []
    # Pega "de [palavra] a/até [palavra]"
    for match in re.finditer(r"\bde\s+(\w+)\s+(a|até)\s+(\w+)", texto, flags=re.IGNORECASE):
        palavra1 = match.group(1).lower()
        palavra2 = match.group(3).lower()
        # Filtra falsos positivos comuns (ex: "de 10 a 20")
        if palavra1.isdigit() or palavra2.isdigit():
            continue
        # Filtra verbos comuns
        if palavra1 in {"mim", "ti", "nós", "vocês", "onde", "quando"}:
            continue
        achados.append({
            "trecho": match.group(0),
            "posicao": match.start(),
        })
    return achados


def detectar_correlativos(texto: str) -> list[dict]:
    """Detecta 'não só X mas também Y' e similares."""
    achados = []
    for padrao in CORRELATIVOS:
        for match in re.finditer(padrao, texto, flags=re.IGNORECASE):
            achados.append({
                "padrao": padrao,
                "trecho": match.group(0)[:120],
                "posicao": match.start(),
            })
    return achados


def detectar_gangorra_hedge(texto: str) -> list[dict]:
    """Detecta 'embora X tenha Y' balanceados."""
    achados = []
    for padrao in GANGORRA_HEDGE:
        for match in re.finditer(padrao, texto, flags=re.IGNORECASE):
            achados.append({
                "padrao": padrao,
                "trecho": match.group(0)[:120],
                "posicao": match.start(),
            })
    return achados


def detectar_tricolon(texto: str) -> list[dict]:
    """Detecta regra de três (três itens separados por vírgula + 'e')."""
    achados = []
    # Padrão: palavra, palavra e palavra (com virgulas)
    padrao = r"\b(\w+),\s+(\w+)\s+e\s+(\w+)\b"
    for match in re.finditer(padrao, texto):
        palavras = [match.group(1), match.group(2), match.group(3)]
        # Filtra ruído: só conta se as 3 são adjetivos/substantivos parecidos em tamanho
        if all(len(p) >= 4 for p in palavras):
            achados.append({
                "trecho": match.group(0),
                "posicao": match.start(),
            })
    return achados


def analisar_ritmo(frases: list[str]) -> dict:
    """Calcula métricas de ritmo de frase."""
    if not frases:
        return {
            "n_frases": 0,
            "tamanho_medio": 0,
            "desvio_padrao": 0,
            "distribuicao": {},
            "status_ritmo": "sem dados",
        }
    tamanhos = [contar_palavras(f) for f in frases]
    media = statistics.mean(tamanhos)
    sd = statistics.stdev(tamanhos) if len(tamanhos) > 1 else 0
    # Distribuição por faixa
    distr = {"1-5": 0, "6-14": 0, "15-22": 0, "23+": 0}
    for t in tamanhos:
        if t <= 5:
            distr["1-5"] += 1
        elif t <= 14:
            distr["6-14"] += 1
        elif t <= 22:
            distr["15-22"] += 1
        else:
            distr["23+"] += 1
    status = "bom" if sd >= 6 else ("razoável" if sd >= 4 else "monotonia-IA")
    return {
        "n_frases": len(frases),
        "tamanho_medio": round(media, 1),
        "desvio_padrao": round(sd, 2),
        "distribuicao": distr,
        "tamanhos": tamanhos,
        "status_ritmo": status,
    }


def analisar_paragrafos(texto: str) -> dict:
    """Conta parágrafos, tamanhos, uniformidade."""
    paragrafos = [p.strip() for p in re.split(r"\n\s*\n", texto) if p.strip()]
    if not paragrafos:
        return {"n_paragrafos": 0, "status_paragrafo": "sem dados"}
    tamanhos_frases = [len(tokenizar_frases(p)) for p in paragrafos]
    media = statistics.mean(tamanhos_frases)
    sd = statistics.stdev(tamanhos_frases) if len(tamanhos_frases) > 1 else 0
    status = "variado" if sd >= 2 else "uniforme-IA"
    return {
        "n_paragrafos": len(paragrafos),
        "tamanho_medio_frases": round(media, 1),
        "desvio_padrao_paragrafos": round(sd, 2),
        "status_paragrafo": status,
    }


def analisar_pontuacao(texto: str) -> dict:
    """Conta travessão, dois-pontos, negrito, etc."""
    total_palavras = contar_palavras(texto)
    n_travessao = texto.count(TRAVESSAO) + texto.count(TRAVESSAO_DUPLO)
    n_dois_pontos = texto.count(":")
    n_negrito_md = len(re.findall(r"\*\*[^*]+\*\*", texto))
    n_emoji = len(re.findall(
        r"[\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF"
        r"\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F900-\U0001F9FF"
        r"\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002600-\U000026FF"
        r"\U00002700-\U000027BF]+",
        texto
    ))
    # Travessões por 500 palavras
    travessao_por_500 = (n_travessao / max(total_palavras, 1)) * 500
    return {
        "travessao": n_travessao,
        "travessao_por_500_palavras": round(travessao_por_500, 2),
        "dois_pontos": n_dois_pontos,
        "negrito_markdown": n_negrito_md,
        "emoji": n_emoji,
        "status_travessao": "ok" if travessao_por_500 <= 1 else "excesso-IA",
    }


def analisar_aberturas_paragrafo(texto: str) -> dict:
    """Checa se parágrafos começam com 'O/A/Esse/Isso' em sequência."""
    paragrafos = [p.strip() for p in re.split(r"\n\s*\n", texto) if p.strip()]
    aberturas_preguiçosas = {"o", "a", "os", "as", "esse", "essa", "esses", "essas",
                              "isso", "isto", "este", "esta", "um", "uma"}
    primeiras_palavras = []
    for p in paragrafos:
        palavras = re.findall(r"\b\w+", p)
        if palavras:
            primeiras_palavras.append(palavras[0].lower())
    n_preguiçosas = sum(1 for p in primeiras_palavras if p in aberturas_preguiçosas)
    total = len(primeiras_palavras)
    pct = (n_preguiçosas / total * 100) if total > 0 else 0
    status = "ok" if pct <= 40 else "repetitivo-IA"
    return {
        "n_paragrafos": total,
        "aberturas_preguiçosas": n_preguiçosas,
        "pct": round(pct, 1),
        "primeiras_palavras": primeiras_palavras,
        "status_aberturas": status,
    }


def calcular_densidade_ia(relatorio: dict, total_palavras: int) -> float:
    """Calcula score 0-100 de densidade de IA."""
    if total_palavras == 0:
        return 0.0

    score = 0.0

    # Vermelhas pesam 2 pontos por palavra
    n_vermelhas = len(relatorio["palavras_vermelhas"])
    score += n_vermelhas * 2

    # Amarelas pesam 0.5
    n_amarelas = len(relatorio["palavras_amarelas"])
    score += n_amarelas * 0.5

    # Frases banidas pesam 3
    n_frases_banidas = sum([
        len(relatorio["aberturas_vazias"]),
        len(relatorio["fechamentos_vazios"]),
        len(relatorio["hype_vendas"]),
        len(relatorio["hedging"]),
        len(relatorio["atribuicao_vaga"]),
        len(relatorio["sicofancia"]),
        len(relatorio["conversa_falsa"]),
    ])
    score += n_frases_banidas * 3

    # Estruturas pesam 2
    score += len(relatorio["paralelismo_negativo"]) * 2
    score += len(relatorio["gerundios_cauda"]) * 1
    score += len(relatorio["tricolons"]) * 0.5
    score += len(relatorio["faixas_falsas"]) * 1
    score += len(relatorio["correlativos"]) * 1
    score += len(relatorio["gangorra_hedge"]) * 1.5

    # Travessão: 1.5 ponto por travessão acima do limite
    n_travessao = relatorio["pontuacao"]["travessao"]
    limite_travessao = total_palavras / 500
    if n_travessao > limite_travessao:
        score += (n_travessao - limite_travessao) * 1.5

    # Ritmo: se SD < 4, adiciona pontos
    sd = relatorio["ritmo"]["desvio_padrao"]
    if sd < 4:
        score += (4 - sd) * 3

    # Normalizar pelo tamanho do texto (palavras). Limite: 100.
    densidade = (score / total_palavras) * 100
    return min(round(densidade, 1), 100.0)


def gerar_relatorio(texto: str) -> dict:
    """Varre o texto e devolve o relatório completo."""
    total_palavras = contar_palavras(texto)
    frases = tokenizar_frases(texto)

    palavras_vermelhas = []
    palavras_vermelhas += detectar_palavras(texto, VERBOS_VERMELHOS, "vermelho")
    palavras_vermelhas += detectar_palavras(texto, ADJETIVOS_VERMELHOS, "vermelho")
    palavras_vermelhas += detectar_palavras(texto, SUBSTANTIVOS_VERMELHOS_METAFORAS, "vermelho")
    palavras_vermelhas += detectar_palavras(texto, ADVERBIOS_VERMELHOS, "vermelho")

    palavras_amarelas = detectar_palavras(texto, PALAVRAS_AMARELAS, "amarelo")

    relatorio = {
        "total_palavras": total_palavras,
        "total_frases": len(frases),
        "palavras_vermelhas": palavras_vermelhas,
        "palavras_amarelas": palavras_amarelas,
        "aberturas_vazias": detectar_frases(texto, ABERTURAS_BANIDAS, "abertura"),
        "fechamentos_vazios": detectar_frases(texto, FECHAMENTOS_BANIDOS, "fechamento"),
        "hype_vendas": detectar_frases(texto, HYPE_VENDAS, "hype"),
        "hedging": detectar_frases(texto, HEDGING, "hedging"),
        "atribuicao_vaga": detectar_frases(texto, ATRIBUICAO_VAGA, "atribuicao_vaga"),
        "sicofancia": detectar_frases(texto, SICOFANCIA, "sicofancia"),
        "conversa_falsa": detectar_frases(texto, CONVERSA_FALSA, "conversa_falsa"),
        "paralelismo_negativo": detectar_paralelismo_negativo(texto),
        "gerundios_cauda": detectar_gerundio_cauda(texto),
        "tricolons": detectar_tricolon(texto),
        "faixas_falsas": detectar_faixas_falsas(texto),
        "correlativos": detectar_correlativos(texto),
        "gangorra_hedge": detectar_gangorra_hedge(texto),
        "ritmo": analisar_ritmo(frases),
        "paragrafos": analisar_paragrafos(texto),
        "pontuacao": analisar_pontuacao(texto),
        "aberturas_paragrafo": analisar_aberturas_paragrafo(texto),
    }

    relatorio["densidade_ia"] = calcular_densidade_ia(relatorio, total_palavras)

    # Contadores resumidos
    relatorio["contagens"] = {
        "palavras_vermelhas": len(palavras_vermelhas),
        "palavras_amarelas": len(palavras_amarelas),
        "aberturas_vazias": len(relatorio["aberturas_vazias"]),
        "fechamentos_vazios": len(relatorio["fechamentos_vazios"]),
        "hype_vendas": len(relatorio["hype_vendas"]),
        "hedging": len(relatorio["hedging"]),
        "atribuicao_vaga": len(relatorio["atribuicao_vaga"]),
        "sicofancia": len(relatorio["sicofancia"]),
        "conversa_falsa": len(relatorio["conversa_falsa"]),
        "paralelismo_negativo": len(relatorio["paralelismo_negativo"]),
        "gerundios_cauda": len(relatorio["gerundios_cauda"]),
        "tricolons": len(relatorio["tricolons"]),
        "faixas_falsas": len(relatorio["faixas_falsas"]),
        "correlativos": len(relatorio["correlativos"]),
        "gangorra_hedge": len(relatorio["gangorra_hedge"]),
    }

    return relatorio


def formatar_markdown(rel: dict) -> str:
    """Formata o relatório em markdown legível."""
    out = []
    out.append(f"# Relatório Voz Humana BR")
    out.append("")
    out.append(f"**Densidade IA:** {rel['densidade_ia']}/100")
    out.append(f"**Total de palavras:** {rel['total_palavras']}")
    out.append(f"**Total de frases:** {rel['total_frases']}")
    out.append("")
    out.append("## Contagens")
    for chave, valor in rel["contagens"].items():
        if valor > 0:
            out.append(f"- {chave}: {valor}")
    out.append("")
    out.append("## Ritmo")
    r = rel["ritmo"]
    out.append(f"- Frase média: {r['tamanho_medio']} palavras")
    out.append(f"- Desvio padrão: {r['desvio_padrao']}")
    out.append(f"- Status: {r['status_ritmo']}")
    out.append(f"- Distribuição: {r['distribuicao']}")
    out.append("")
    out.append("## Pontuação")
    p = rel["pontuacao"]
    out.append(f"- Travessões: {p['travessao']} ({p['travessao_por_500_palavras']} por 500 palavras)")
    out.append(f"- Dois-pontos: {p['dois_pontos']}")
    out.append(f"- Negrito markdown: {p['negrito_markdown']}")
    out.append(f"- Emoji: {p['emoji']}")
    out.append(f"- Status travessão: {p['status_travessao']}")
    out.append("")
    out.append("## Parágrafos")
    pa = rel["paragrafos"]
    out.append(f"- Total: {pa.get('n_paragrafos', 0)}")
    out.append(f"- Status: {pa.get('status_paragrafo', 'N/A')}")
    out.append("")
    out.append("## Aberturas de parágrafo")
    ab = rel["aberturas_paragrafo"]
    out.append(f"- {ab['aberturas_preguiçosas']}/{ab['n_paragrafos']} começam com 'O/A/Esse/Isso' ({ab['pct']}%)")
    out.append(f"- Status: {ab['status_aberturas']}")

    if rel["palavras_vermelhas"]:
        out.append("")
        out.append("## Palavras vermelhas encontradas")
        for pv in rel["palavras_vermelhas"][:20]:
            out.append(f"- `{pv['palavra']}` @ {pv['posicao']}")

    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Detector de padrões IA em PT-BR"
    )
    parser.add_argument("arquivo", nargs="?", help="Arquivo de input (ou stdin)")
    parser.add_argument("--formato", "-f", choices=["json", "markdown"], default="markdown")
    args = parser.parse_args()

    if args.arquivo:
        with open(args.arquivo, "r", encoding="utf-8") as f:
            texto = f.read()
    else:
        texto = sys.stdin.read()

    if not texto.strip():
        print("ERRO: texto vazio", file=sys.stderr)
        return 1

    rel = gerar_relatorio(texto)

    if args.formato == "json":
        print(json.dumps(rel, ensure_ascii=False, indent=2))
    else:
        print(formatar_markdown(rel))

    return 0


if __name__ == "__main__":
    sys.exit(main())
