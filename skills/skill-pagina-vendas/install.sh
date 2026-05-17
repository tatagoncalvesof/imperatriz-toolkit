#!/usr/bin/env bash
set -euo pipefail

REPO="https://github.com/tatagoncalvesof/skill-pagina-vendas.git"
DEST="$HOME/.claude/skills/skill-pagina-vendas"
TMP="$(mktemp -d)"

echo ""
echo "==============================================="
echo "  PageCraft — Sales Page Factory by Tata"
echo "  Instalando skill-pagina-vendas..."
echo "==============================================="
echo ""

if ! command -v git >/dev/null 2>&1; then
  echo "ERRO: git nao encontrado. Instale com: xcode-select --install"
  exit 1
fi

git clone --depth 1 "$REPO" "$TMP/skill" >/dev/null 2>&1

if [ -d "$DEST" ]; then
  BACKUP="$DEST.backup.$(date +%Y%m%d-%H%M%S)"
  echo "Skill ja existe — backup em:"
  echo "  $BACKUP"
  mv "$DEST" "$BACKUP"
  echo ""
fi

mkdir -p "$(dirname "$DEST")"
mkdir -p "$DEST"
cp -R "$TMP/skill/." "$DEST/"

rm -rf "$DEST/.git" "$DEST/install.sh" "$DEST/README.md" 2>/dev/null || true

rm -rf "$TMP"

echo "OK — skill instalada em:"
echo "  $DEST"
echo ""
echo "Como usar no Claude Code:"
echo "  /skill-pagina-vendas"
echo ""
echo "Pra atualizar no futuro, rode esse mesmo comando de novo."
echo ""
