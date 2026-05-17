#!/usr/bin/env bash
# =============================================================================
# rollback.sh — Rollback to previous deploy version
#
# Usage: bash rollback.sh <project-name>
# Example: bash rollback.sh my-app
#
# Restores from /var/www/apps/<project-name>.backup/
# Created automatically by deploy.sh before each deploy
# =============================================================================

set -euo pipefail

# --- Configuration ---
VPS_IP="76.13.175.161"
VPS_USER="root"
VPS_SSH="${VPS_USER}@${VPS_IP}"
APPS_DIR="/var/www/apps"

# --- Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info()  { echo -e "${BLUE}[INFO]${NC} $1"; }
log_ok()    { echo -e "${GREEN}[OK]${NC} $1"; }
log_warn()  { echo -e "${YELLOW}[AVISO]${NC} $1"; }
log_error() { echo -e "${RED}[ERRO]${NC} $1"; }

# --- Validate arguments ---
if [[ $# -lt 1 ]]; then
    echo "Uso: bash rollback.sh <nome-projeto>"
    echo "Exemplo: bash rollback.sh my-app"
    exit 1
fi

PROJECT_NAME="$1"
REMOTE_DIR="${APPS_DIR}/${PROJECT_NAME}"
BACKUP_DIR="${APPS_DIR}/${PROJECT_NAME}.backup"

echo ""
echo "=========================================="
echo "  ROLLBACK: ${PROJECT_NAME}"
echo "=========================================="

# Check if backup exists
log_info "Verificando backup em ${BACKUP_DIR}..."
BACKUP_EXISTS=$(ssh "${VPS_SSH}" "test -d ${BACKUP_DIR} && echo yes || echo no")
if [[ "$BACKUP_EXISTS" != "yes" ]]; then
    log_error "Nenhum backup encontrado em ${BACKUP_DIR}"
    log_error "O backup so e criado durante o deploy (deploy.sh)"
    exit 1
fi

# Show backup info
log_info "Informacoes do backup:"
ssh "${VPS_SSH}" "ls -la ${BACKUP_DIR}/ | head -10"
BACKUP_DATE=$(ssh "${VPS_SSH}" "stat -c %y ${BACKUP_DIR} 2>/dev/null | cut -d. -f1 || echo 'desconhecido'")
log_info "Data do backup: ${BACKUP_DATE}"

# Confirm rollback
echo ""
log_warn "ATENCAO: Isso vai substituir a versao atual pela versao anterior"
read -rp "Confirmar rollback de ${PROJECT_NAME}? (s/N): " confirm
if [[ "$confirm" != "s" && "$confirm" != "S" ]]; then
    log_info "Rollback cancelado"
    exit 0
fi

# Stop PM2 process
log_info "Parando processo PM2..."
ssh "${VPS_SSH}" "pm2 stop ${PROJECT_NAME} 2>/dev/null || true"

# Save current version as .failed (in case we need it)
CURRENT_EXISTS=$(ssh "${VPS_SSH}" "test -d ${REMOTE_DIR} && echo yes || echo no")
if [[ "$CURRENT_EXISTS" == "yes" ]]; then
    log_info "Salvando versao atual como .failed..."
    ssh "${VPS_SSH}" "rm -rf ${REMOTE_DIR}.failed && mv ${REMOTE_DIR} ${REMOTE_DIR}.failed"
fi

# Restore backup
log_info "Restaurando backup..."
ssh "${VPS_SSH}" "cp -a ${BACKUP_DIR} ${REMOTE_DIR}"

# Restart PM2 process
log_info "Reiniciando processo PM2..."
ssh "${VPS_SSH}" "pm2 restart ${PROJECT_NAME} 2>/dev/null || pm2 start ${REMOTE_DIR}/dist/index.js --name ${PROJECT_NAME} 2>/dev/null || pm2 start ${REMOTE_DIR}/index.js --name ${PROJECT_NAME}"
ssh "${VPS_SSH}" "pm2 save"

# Wait for startup
sleep 3

# Verify the rollback
log_info "Verificando rollback..."
PM2_CHECK=$(ssh "${VPS_SSH}" "pm2 list | grep '${PROJECT_NAME}' | grep 'online' || true")
if [[ -n "$PM2_CHECK" ]]; then
    log_ok "Processo reiniciado com sucesso"
    echo "$PM2_CHECK"
else
    log_error "Processo nao reiniciou corretamente"
    log_error "Verifique os logs: ssh ${VPS_SSH} \"pm2 logs ${PROJECT_NAME} --lines 50\""
    exit 1
fi

echo ""
echo "=========================================="
echo -e "  ${GREEN}ROLLBACK CONCLUIDO${NC}"
echo "=========================================="
echo "  Versao restaurada: ${BACKUP_DIR}"
echo "  Versao com falha salva em: ${REMOTE_DIR}.failed/"
echo "  Para limpar: ssh ${VPS_SSH} \"rm -rf ${REMOTE_DIR}.failed\""
echo "=========================================="
echo ""
