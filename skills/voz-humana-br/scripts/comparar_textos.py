#!/usr/bin/env python3
"""
comparar_textos.py — Compara input original e output humanizado.

Mostra métricas antes/depois e palavras/padrões removidos.

Uso:
    python3 comparar_textos.py input_original.txt output_humanizado.txt
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from detectar_ia_ptbr import gerar_relatorio


def diff_contagens(antes: dict, depois: dict) -> dict:
    """Calcula delta de cada contagem."""
    deltas = {}
    for chave in antes["contagens"]:
        a = antes["contagens"][chave]
        d = depois["contagens"][chave]
        deltas[chave] = {
            "antes": a,
            "depois": d,
            "delta": d - a,
        }
    return deltas


def palavras_removidas(antes: dict, depois: dict) -> list[str]:
    """Lista palavras vermelhas que existiam no input e não existem no output."""
    palavras_antes = {p["palavra"] for p in antes["palavras_vermelhas"]}
    palavras_depois = {p["palavra"] for p in depois["palavras_vermelhas"]}
    return sorted(palavras_antes - palavras_depois)


def main() -> int:
    if len(sys.argv) != 3:
        print("Uso: comparar_textos.py <input_original> <output_humanizado>", file=sys.stderr)
        return 1

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        texto_antes = f.read()
    with open(sys.argv[2], "r", encoding="utf-8") as f:
        texto_depois = f.read()

    antes = gerar_relatorio(texto_antes)
    depois = gerar_relatorio(texto_depois)

    print("# Comparação Antes / Depois")
    print()
    print(f"## Resumo geral")
    print(f"- Densidade IA: {antes['densidade_ia']} → {depois['densidade_ia']} (delta: {round(depois['densidade_ia'] - antes['densidade_ia'], 1)})")
    print(f"- Palavras totais: {antes['total_palavras']} → {depois['total_palavras']}")
    print(f"- Frases totais: {antes['total_frases']} → {depois['total_frases']}")
    print(f"- SD tamanho frase: {antes['ritmo']['desvio_padrao']} → {depois['ritmo']['desvio_padrao']}")
    print(f"- Travessão por 500 palavras: {antes['pontuacao']['travessao_por_500_palavras']} → {depois['pontuacao']['travessao_por_500_palavras']}")
    print()

    deltas = diff_contagens(antes, depois)
    print("## Deltas de contagem (antes → depois)")
    for chave, val in deltas.items():
        if val["antes"] > 0 or val["depois"] > 0:
            seta = "↓" if val["delta"] < 0 else ("↑" if val["delta"] > 0 else "=")
            print(f"- {chave}: {val['antes']} → {val['depois']} {seta}")
    print()

    palavras = palavras_removidas(antes, depois)
    if palavras:
        print("## Palavras vermelhas removidas")
        for p in palavras[:30]:
            print(f"- {p}")
        if len(palavras) > 30:
            print(f"- ... e mais {len(palavras) - 30}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
