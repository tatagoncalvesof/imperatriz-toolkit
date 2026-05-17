#!/usr/bin/env bash
# Imperatriz Toolkit — instalador automático (Mac/Linux)
# Uso: ./install.sh

set -e

SKILLS_DIR="$HOME/.claude/skills"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ""
echo "👑 Imperatriz Toolkit — instalando 13 skills no Claude Code"
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
echo "Abre o Claude Code e usa as skills:"
echo ""
echo "  COPY:        /briefing-copy-360  /mecanismo-unico  /headline-imperatriz"
echo "  VISUAL:      /texto-em-visual  /mapa-mental-imperatriz"
echo "  ANÁLISE:     /analise-anuncio-1000"
echo "  ESTRATÉGIA:  /maestro-de-conteudo  /linha-editorial-imperatriz  /calendario-imperatriz"
echo "  CONTEÚDO:    /linkedin-empire  /stories-pergunta-resposta"
echo "  PESQUISA:    /deep-market-research"
echo "  REUNIÃO:     /reuniao-de-resultado"
echo ""
