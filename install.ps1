# Imperatriz Toolkit — instalador automático (Windows PowerShell)
# Uso: .\install.ps1

$ErrorActionPreference = "Stop"

$SkillsDir = Join-Path $HOME ".claude\skills"
$RepoDir = $PSScriptRoot

Write-Host ""
Write-Host "👑 Imperatriz Toolkit — instalando 6 skills no Claude Code" -ForegroundColor Magenta
Write-Host ""

if (-not (Test-Path $SkillsDir)) {
  Write-Host "📁 Criando $SkillsDir (não existia)"
  New-Item -ItemType Directory -Path $SkillsDir -Force | Out-Null
}

$Installed = 0
$Skipped = 0

Get-ChildItem -Path (Join-Path $RepoDir "skills") -Directory | ForEach-Object {
  $name = $_.Name
  $target = Join-Path $SkillsDir $name

  if (Test-Path $target) {
    $resp = Read-Host "⚠️  '$name' já existe em ~/.claude/skills/. Sobrescrever? [s/N]"
    if ($resp -match '^[sSyY]$') {
      Remove-Item -Path $target -Recurse -Force
      Copy-Item -Path $_.FullName -Destination $target -Recurse
      Write-Host "  ✅ $name (sobrescrita)" -ForegroundColor Green
      $Installed++
    } else {
      Write-Host "  ⏭️  $name (pulada)" -ForegroundColor Yellow
      $Skipped++
    }
  } else {
    Copy-Item -Path $_.FullName -Destination $target -Recurse
    Write-Host "  ✅ $name" -ForegroundColor Green
    $Installed++
  }
}

Write-Host ""
Write-Host "🎉 Concluído: $Installed instalada(s), $Skipped pulada(s)" -ForegroundColor Magenta
Write-Host ""
Write-Host "Abre o Claude Code e usa as skills:"
Write-Host "  /briefing-copy-360"
Write-Host "  /mecanismo-unico"
Write-Host "  /headline-imperatriz"
Write-Host "  /texto-em-visual"
Write-Host "  /analise-anuncio-1000"
Write-Host "  /stories-pergunta-resposta"
Write-Host ""
