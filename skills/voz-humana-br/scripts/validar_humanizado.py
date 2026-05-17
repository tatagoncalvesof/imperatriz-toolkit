#!/usr/bin/env python3
"""
validar_humanizado.py — Verifica se texto humanizado passa nos critérios.

Compara input original e output humanizado. Devolve PASSOU/FALHOU com detalhes
de cada critério.

Uso:
    python3 validar_humanizado.py input_original.txt output_humanizado.txt
"""

from __future__ import annotations

import sys
import os
import json

# Permite importar o detector do mesmo diretório
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from detectar_ia_ptbr import gerar_relatorio, contar_palavras


CRITERIOS = {
    "densidade_ia_max": 15,
    "palavras_vermelhas_max": 0,
    "palavras_amarelas_max": 1,
    "sd_frases_min": 5,
    "travessao_por_500_max": 1,
    "paralelismo_negativo_max": 0,
    "gerundios_cauda_max": 2,
    "sicofancia_max": 0,
    "aberturas_vazias_max": 0,
    "fechamentos_vazios_max": 0,
}


def validar(rel_input: dict, rel_output: dict) -> dict:
    """Compara os dois relatórios e devolve resultado da validação."""
    c = rel_output["contagens"]
    p = rel_output["pontuacao"]
    r = rel_output["ritmo"]

    resultados = []

    # Critério 1: densidade IA
    densidade = rel_output["densidade_ia"]
    resultados.append({
        "criterio": "Densidade IA <= 15",
        "valor": densidade,
        "limite": CRITERIOS["densidade_ia_max"],
        "passou": densidade <= CRITERIOS["densidade_ia_max"],
    })

    # Critério 2: zero palavras vermelhas
    resultados.append({
        "criterio": "Zero palavras vermelhas",
        "valor": c["palavras_vermelhas"],
        "limite": 0,
        "passou": c["palavras_vermelhas"] == 0,
    })

    # Critério 3: máximo 1 palavra amarela
    resultados.append({
        "criterio": "Máximo 1 palavra amarela",
        "valor": c["palavras_amarelas"],
        "limite": 1,
        "passou": c["palavras_amarelas"] <= 1,
    })

    # Critério 4: desvio padrão de tamanho de frase >= 5
    sd = r["desvio_padrao"]
    resultados.append({
        "criterio": "Desvio padrão tamanho frase >= 5",
        "valor": sd,
        "limite": 5,
        "passou": sd >= 5,
    })

    # Critério 5: travessão controlado
    trav = p["travessao_por_500_palavras"]
    resultados.append({
        "criterio": "Travessão <= 1 por 500 palavras",
        "valor": trav,
        "limite": 1,
        "passou": trav <= 1,
    })

    # Critério 6: zero paralelismo negativo
    resultados.append({
        "criterio": "Zero paralelismo negativo",
        "valor": c["paralelismo_negativo"],
        "limite": 0,
        "passou": c["paralelismo_negativo"] == 0,
    })

    # Critério 7: gerúndios na cauda sob controle
    resultados.append({
        "criterio": "Gerúndio cauda <= 2",
        "valor": c["gerundios_cauda"],
        "limite": 2,
        "passou": c["gerundios_cauda"] <= 2,
    })

    # Critério 8: zero sicofancia
    resultados.append({
        "criterio": "Zero sicofancia",
        "valor": c["sicofancia"],
        "limite": 0,
        "passou": c["sicofancia"] == 0,
    })

    # Critério 9: zero abertura vazia
    resultados.append({
        "criterio": "Zero abertura vazia",
        "valor": c["aberturas_vazias"],
        "limite": 0,
        "passou": c["aberturas_vazias"] == 0,
    })

    # Critério 10: zero fechamento vazio
    resultados.append({
        "criterio": "Zero fechamento vazio",
        "valor": c["fechamentos_vazios"],
        "limite": 0,
        "passou": c["fechamentos_vazios"] == 0,
    })

    todos_passaram = all(r["passou"] for r in resultados)

    return {
        "status": "PASSOU" if todos_passaram else "FALHOU",
        "densidade_input": rel_input["densidade_ia"],
        "densidade_output": rel_output["densidade_ia"],
        "delta_densidade": round(rel_input["densidade_ia"] - rel_output["densidade_ia"], 1),
        "criterios": resultados,
    }


def main() -> int:
    if len(sys.argv) != 3:
        print("Uso: validar_humanizado.py <input_original> <output_humanizado>", file=sys.stderr)
        return 1

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        texto_input = f.read()
    with open(sys.argv[2], "r", encoding="utf-8") as f:
        texto_output = f.read()

    rel_input = gerar_relatorio(texto_input)
    rel_output = gerar_relatorio(texto_output)

    resultado = validar(rel_input, rel_output)

    # Print resumo formatado
    print(f"# Validação: {resultado['status']}")
    print(f"")
    print(f"Densidade IA: {resultado['densidade_input']} → {resultado['densidade_output']} (delta: -{resultado['delta_densidade']})")
    print(f"")
    print(f"## Critérios")
    for c in resultado["criterios"]:
        emoji = "OK" if c["passou"] else "FALHA"
        print(f"[{emoji}] {c['criterio']}: {c['valor']} (limite: {c['limite']})")

    return 0 if resultado["status"] == "PASSOU" else 1


if __name__ == "__main__":
    sys.exit(main())
