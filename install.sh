#!/usr/bin/env bash
# Imperatriz Toolkit — instalador automático (Mac/Linux)
# Uso: ./install.sh

set -e

SKILLS_DIR="$HOME/.claude/skills"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ""
echo "👑 Imperatriz Toolkit — instalando 71 skills no Claude Code"
echo ""

if [ ! -d "$SKILLS_DIR" ]; then
  echo "📁 Criando $SKILLS_DIR (não existia)"
  mkdir -p "$SKILLS_DIR"
fi

INSTALLED=0
SKIPPED=0

for skill in "$REPO_DIR"/skills/*/; do
  name=$(basename "$skill")
  target="$SKILLS_DIR/$name"

  if [ -d "$target" ]; then
    read -r -p "⚠️  '$name' já existe em ~/.claude/skills/. Sobrescrever? [s/N] " resp
    if [[ "$resp" =~ ^[SsYy]$ ]]; then
      rm -rf "$target"
      cp -R "$skill" "$target"
      echo "  ✅ $name (sobrescrita)"
      INSTALLED=$((INSTALLED+1))
    else
      echo "  ⏭️  $name (pulada)"
      SKIPPED=$((SKIPPED+1))
    fi
  else
    cp -R "$skill" "$target"
    echo "  ✅ $name"
    INSTALLED=$((INSTALLED+1))
  fi
done

echo ""
echo "🎉 Concluído: $INSTALLED instalada(s), $SKIPPED pulada(s)"
echo ""
echo "Abre o Claude Code e digite '/' pra ver as 71 skills."
echo ""
echo "Trio mestre:"
echo "  /briefing-copy-360  →  /mecanismo-unico  →  /headline-imperatriz"
echo ""
echo "Orquestrador de conteúdo (uma skill, 5 fases):"
echo "  /maestro-de-conteudo"
echo ""
echo "Lista completa de categorias: veja o README.md"
echo ""
