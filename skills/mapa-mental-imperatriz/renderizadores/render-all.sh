#!/bin/bash
# render-all.sh — gera os 4 formatos a partir do markdown Mermaid+Markmap
#
# Uso: ./render-all.sh <input.md> <output-base>
# Exemplo: ./render-all.sh ./mapa.md ~/Documents/Obsidian\ Vault/09\ -\ Mapas\ Mentais/2026-04-29-tema
#
# Input esperado: arquivo .md com:
#   - Bloco ```mermaid mindmap ... ``` (pra Mermaid+PNG)
#   - OU markdown com headings (pra Markmap)
#   - Frontmatter YAML opcional
#
# Output: <base>.md (Mermaid) | <base>.html (Markmap) | <base>.png (PNG) | <base>.canvas (Obsidian)

set -e

INPUT="$1"
OUTPUT_BASE="$2"

if [ -z "$INPUT" ] || [ -z "$OUTPUT_BASE" ]; then
  echo "Uso: $0 <input.md> <output-base>"
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "❌ Arquivo não encontrado: $INPUT"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="$(dirname "$OUTPUT_BASE")"
mkdir -p "$OUTPUT_DIR"

echo "🎨 Renderizando 4 formatos..."

# 1. Mermaid (.md) — copia o input já formatado
cp "$INPUT" "${OUTPUT_BASE}.md"
echo "  ✓ Mermaid: ${OUTPUT_BASE}.md"

# 2. Markmap (.html) — gera HTML interativo
if command -v npx >/dev/null 2>&1; then
  npx -y markmap-cli "$INPUT" -o "${OUTPUT_BASE}.html" --no-open 2>/dev/null && \
    echo "  ✓ Markmap: ${OUTPUT_BASE}.html" || \
    echo "  ⚠️  Markmap falhou (instalar: npm i -g markmap-cli)"
else
  echo "  ⚠️  npx não encontrado — instalar Node.js"
fi

# 3. PNG (estático) — extrai mermaid e renderiza
"$SCRIPT_DIR/render-mermaid.sh" "$INPUT" "${OUTPUT_BASE}.png" || \
  echo "  ⚠️  PNG falhou — verificar mermaid no input"

# 4. Obsidian Canvas (.canvas) — gera JSON
if command -v node >/dev/null 2>&1; then
  node "$SCRIPT_DIR/render-canvas.js" "$INPUT" "${OUTPUT_BASE}.canvas" && \
    echo "  ✓ Canvas: ${OUTPUT_BASE}.canvas" || \
    echo "  ⚠️  Canvas falhou"
fi

echo ""
echo "✅ Concluído. Arquivos em: $OUTPUT_DIR"
