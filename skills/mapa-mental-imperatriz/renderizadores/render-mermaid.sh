#!/bin/bash
# render-mermaid.sh — extrai bloco mermaid de um .md (ou gera a partir do markdown limpo) e renderiza PNG
# Uso: ./render-mermaid.sh <input.md> <output.png>

set -e

INPUT="$1"
OUTPUT="$2"

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
  echo "Uso: $0 <input.md> <output.png>"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TMP_MMD="$(mktemp).mmd"

# Tenta extrair bloco mermaid existente
awk '/^```mermaid/{flag=1; next} /^```$/{flag=0} flag' "$INPUT" > "$TMP_MMD"

# Se não achou, gera a partir das headings + listas do markdown
if [ ! -s "$TMP_MMD" ]; then
  node "$SCRIPT_DIR/md-to-mermaid.js" "$INPUT" > "$TMP_MMD"
fi

if [ ! -s "$TMP_MMD" ]; then
  echo "  ⚠️  Não foi possível extrair nem gerar mermaid de $INPUT"
  rm -f "$TMP_MMD"
  exit 1
fi

# Renderiza com mermaid-cli
npx -y -p @mermaid-js/mermaid-cli mmdc \
  -i "$TMP_MMD" \
  -o "$OUTPUT" \
  -t default \
  -b transparent \
  --width 2400 \
  --height 1800 \
  --scale 2 \
  2>/dev/null && echo "  ✓ PNG: $OUTPUT" || \
  echo "  ⚠️  Falha ao gerar PNG"

rm -f "$TMP_MMD"
