#!/usr/bin/env python3
"""
deep-market-research — Validador do JSON canônico

Uso:
    python3 research_engine.py <path-do-saida-canonica.json>

Roda os 10 validadores anti-AI-slop sobre o JSON gerado pela skill e
retorna PASS / FAIL com detalhes. Use depois de gerar o relatorio
e antes de salvar no vault.

Nao faz pesquisa (a pesquisa e feita pelo Claude via WebSearch/WebFetch).
Apenas valida o output canonico.
"""

import json
import sys
from collections import Counter
from pathlib import Path


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERRO: arquivo nao encontrado: {path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERRO: JSON invalido em {path}: {e}")
        sys.exit(1)


def v1_termos_literais(data):
    termos = data.get("termos_top_50", [])
    abstratos = ["ferramenta de", "estrategia de", "solucao de", "abordagem", "metodo"]
    suspeitos = []
    for t in termos:
        termo = t.get("termo_exato", "").lower()
        if any(a in termo for a in abstratos):
            if not any(nome in termo for nome in [" para ", " com ", " sem ", " de "]):
                suspeitos.append(t.get("termo_exato"))
    ok = len(termos) >= 20 and len(suspeitos) <= 5
    return ok, f"{len(termos)} termos, {len(suspeitos)} suspeitos de abstracao"


def v2_objecoes_com_origem(data):
    objs = data.get("objecoes", [])
    sem_frase = sum(1 for o in objs if not o.get("frase_origem", "").strip())
    sem_fonte = sum(1 for o in objs if not (o.get("fonte") or {}).get("plataforma"))
    ok = sem_frase == 0 and sem_fonte <= len(objs) * 0.2
    return ok, f"{len(objs)} objecoes, {sem_frase} sem frase-origem, {sem_fonte} sem fonte"


def v3_plataformas_min_3(data):
    plats = data.get("metadata", {}).get("plataformas_pesquisadas", [])
    ok = len(plats) >= 3
    return ok, f"{len(plats)} plataformas: {plats}"


def v4_sem_abstracoes(data):
    termos = data.get("termos_top_50", [])
    abstratos_proibidos = [
        "ferramenta de produtividade",
        "solucao completa",
        "estrategia eficaz",
        "abordagem holistica",
    ]
    encontrados = [
        t["termo_exato"] for t in termos
        if any(a in t.get("termo_exato", "").lower() for a in abstratos_proibidos)
    ]
    ok = len(encontrados) == 0
    return ok, f"{len(encontrados)} termos abstratos proibidos: {encontrados[:3]}"


def v5_sugestoes_especificas(data):
    ideias = data.get("ideias_conteudo", [])
    incompletas = []
    for i in ideias:
        if not all([
            i.get("hook", "").strip(),
            i.get("valor", "").strip(),
            i.get("ponte", "").strip(),
            i.get("cta", "").strip(),
            i.get("formato", "").strip(),
        ]):
            incompletas.append(i.get("id"))
        elif len(i.get("hook", "")) < 30:
            incompletas.append(i.get("id"))
    ok = len(incompletas) == 0
    return ok, f"{len(ideias)} ideias, {len(incompletas)} incompletas/curtas: {incompletas[:5]}"


def v6_pontes_variadas(data):
    pontes = [i.get("ponte", "").lower().strip() for i in data.get("ideias_conteudo", [])]
    counter = Counter(pontes)
    if not counter:
        return False, "sem ideias_conteudo"
    mais_comum, freq = counter.most_common(1)[0]
    ok = freq <= 5
    return ok, f"ponte mais repetida: '{mais_comum[:60]}...' aparece {freq}x"


def v7_scores_com_racional(data):
    termos = data.get("termos_top_50", [])[:10]
    sem_racional = sum(1 for t in termos if not t.get("score_racional", "").strip())
    ok = sem_racional == 0
    return ok, f"top 10: {sem_racional} sem score_racional"


def v8_registro_coerente(data):
    palavras_ia = [
        "abordagem holistica", "ecossistema vibrante", "insights acionaveis",
        "experiencia frictionless", "alavancar sinergias", "mindset",
        "jornada do cliente", "delivers value", "unlock potential",
    ]
    encontrados = []
    for campo in ["termos_top_50", "expressoes_idiomaticas", "metaforas"]:
        for item in data.get(campo, []):
            texto = json.dumps(item, ensure_ascii=False).lower()
            for p in palavras_ia:
                if p in texto:
                    encontrados.append(p)
    ok = len(encontrados) == 0
    return ok, f"{len(encontrados)} palavras-IA detectadas: {list(set(encontrados))[:3]}"


def v9_anti_termos_listados(data):
    anti = data.get("anti_termos", [])
    sem_razao = sum(1 for a in anti if not a.get("razao", "").strip())
    ok = len(anti) >= 10 and sem_razao == 0
    return ok, f"{len(anti)} anti-termos, {sem_razao} sem razao"


def v10_passou_voz_humana(data):
    v = data.get("validacao_anti_slop", {})
    ok = v.get("v10_passou_voz_humana", False) is True
    return ok, f"flag v10_passou_voz_humana: {v.get('v10_passou_voz_humana')}"


VALIDADORES = [
    ("V1", "Termos literais (nao parafraseados)", v1_termos_literais),
    ("V2", "Objecoes com frase-origem", v2_objecoes_com_origem),
    ("V3", "Minimo 3 plataformas representadas", v3_plataformas_min_3),
    ("V4", "Sem termos abstratos genericos", v4_sem_abstracoes),
    ("V5", "Sugestoes de conteudo especificas", v5_sugestoes_especificas),
    ("V6", "Pontes variadas (sem repetir CTA >5x)", v6_pontes_variadas),
    ("V7", "Scores com racional documentado", v7_scores_com_racional),
    ("V8", "Registro linguistico coerente (sem AI-slop)", v8_registro_coerente),
    ("V9", "10 anti-termos com razao", v9_anti_termos_listados),
    ("V10", "Passou por /voz-humana-br", v10_passou_voz_humana),
]


def run(path):
    data = load_json(path)
    print(f"\nValidando: {path}\n")
    print(f"Nicho: {data.get('metadata', {}).get('nicho', '?')}")
    print(f"Produto: {data.get('metadata', {}).get('produto', '?')}\n")
    print("-" * 70)

    falhas = 0
    for codigo, descricao, fn in VALIDADORES:
        try:
            ok, detalhe = fn(data)
        except Exception as e:
            ok, detalhe = False, f"ERRO no validador: {e}"
        marca = "ok" if ok else "XX"
        print(f"  [{marca}] {codigo}: {descricao}")
        print(f"        {detalhe}")
        if not ok:
            falhas += 1

    print("-" * 70)
    if falhas == 0:
        print(f"\n10/10 validadores PASSARAM. Pode salvar no vault.\n")
        return 0
    print(f"\n{falhas}/10 validadores FALHARAM. Corrija antes de entregar.\n")
    return 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 research_engine.py <path-do-saida-canonica.json>")
        sys.exit(2)
    sys.exit(run(Path(sys.argv[1]).expanduser()))
