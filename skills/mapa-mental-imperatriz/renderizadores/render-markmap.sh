#!/bin/bash
# render-markmap.sh — gera HTML interativo via markmap-cli
# Uso: ./render-markmap.sh <input.md> <output.html>

set -e

INPUT="$1"
OUTPUT="$2"

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
  echo "Uso: $0 <input.md> <output.html>"
  exit 1
fi

npx -y markmap-cli "$INPUT" -o "$OUTPUT" --no-open 2>/dev/null && \
  echo "  ✓ Markmap: $OUTPUT" || \
  echo "  ⚠️  Falha — instalar: npm i -g markmap-cli"
