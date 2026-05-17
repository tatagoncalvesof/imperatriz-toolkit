#!/usr/bin/env bash
# =============================================================================
# deploy.sh — Complete deploy workflow for Node.js apps to Hostinger VPS
#
# Usage: bash deploy.sh <project-name> <port> <subdomain>
# Example: bash deploy.sh my-app 3007 myapp
#
# This deploys to: /var/www/apps/<project-name>/
# Accessible at: https://<subdomain>.iacomtata.com.br
# =============================================================================

set -euo pipefail

# --- Configuration ---
VPS_IP="76.13.175.161"
VPS_USER="root"
VPS_SSH="${VPS_USER}@${VPS_IP}"
DOMAIN="iacomtata.com.br"
APPS_DIR="/var/www/apps"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --- Colors ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# --- Functions ---
log_info()  { echo -e "${BLUE}[INFO]${NC} $1"; }
log_ok()    { echo -e "${GREEN}[OK]${NC} $1"; }
log_warn()  { echo -e "${YELLOW}[AVISO]${NC} $1"; }
log_error() { echo -e "${RED}[ERRO]${NC} $1"; }

usage() {
    echo "Uso: bash deploy.sh <nome-projeto> <porta> <subdominio>"
    echo ""
    echo "Argumentos:"
    echo "  nome-projeto  Nome do projeto (ex: my-app)"
    echo "  porta         Porta da aplicacao (ex: 3007)"
    echo "  subdominio    Prefixo do subdominio (ex: myapp para myapp.iacomtata.com.br)"
    echo ""
    echo "Exemplo:"
    echo "  bash deploy.sh podcast-infinito 3006 podcast"
    exit 1
}

check_ssh() {
    log_info "Verificando conexao SSH com o servidor..."
    if ! ssh -o ConnectTimeout=5 -o BatchMode=yes "${VPS_SSH}" "echo ok" &>/dev/null; then
        log_error "Nao foi possivel conectar ao servidor ${VPS_IP}"
        log_error "Verifique se a chave SSH esta configurada: ssh ${VPS_SSH}"
        exit 1
    fi
    log_ok "Conexao SSH OK"
}

check_port() {
    local port="$1"
    log_info "Verificando se a porta ${port} esta disponivel..."
    local in_use
    in_use=$(ssh "${VPS_SSH}" "ss -tlnp | grep ':${port} ' || true")
    if [[ -n "$in_use" ]]; then
        log_warn "Porta ${port} ja esta em uso:"
        echo "$in_use"
        read -rp "Continuar mesmo assim? (s/N): " confirm
        if [[ "$confirm" != "s" && "$confirm" != "S" ]]; then
            log_error "Deploy cancelado pelo usuario"
            exit 1
        fi
    else
        log_ok "Porta ${port} disponivel"
    fi
}

# --- Validate arguments ---
if [[ $# -lt 3 ]]; then
    usage
fi

PROJECT_NAME="$1"
PORT="$2"
SUBDOMAIN="$3"
FULL_DOMAIN="${SUBDOMAIN}.${DOMAIN}"
REMOTE_DIR="${APPS_DIR}/${PROJECT_NAME}"
LOCAL_DIR="$(pwd)"

echo ""
echo "=========================================="
echo "  DEPLOY: ${PROJECT_NAME}"
echo "=========================================="
echo "  Servidor:   ${VPS_IP}"
echo "  Diretorio:  ${REMOTE_DIR}"
echo "  Porta:      ${PORT}"
echo "  Dominio:    ${FULL_DOMAIN}"
echo "  Origem:     ${LOCAL_DIR}"
echo "=========================================="
echo ""

# --- Pre-flight checks ---
check_ssh
check_port "$PORT"

# --- Step 1: Build locally ---
log_info "=== PASSO 1/6: Build local ==="

if [[ -f "pnpm-lock.yaml" ]]; then
    log_info "Detectado pnpm — executando build..."
    PATH="$HOME/.npm-global/bin:/usr/bin:/usr/local/bin:$PATH" pnpm run build
elif [[ -f "package-lock.json" ]] || [[ -f "package.json" ]]; then
    log_info "Detectado npm — executando build..."
    npm run build
else
    log_error "Nenhum package.json encontrado em ${LOCAL_DIR}"
    exit 1
fi

# Detect build output directory
BUILD_DIR=""
for dir in dist build .next; do
    if [[ -d "$dir" ]]; then
        BUILD_DIR="$dir"
        break
    fi
done

if [[ -z "$BUILD_DIR" ]]; then
    log_error "Nenhum diretorio de build encontrado (dist/, build/, .next/)"
    exit 1
fi

log_ok "Build concluido — diretorio: ${BUILD_DIR}/"

# --- Step 2: Backup existing deploy and upload ---
log_info "=== PASSO 2/6: Upload para o servidor ==="

# Create backup of existing deploy
BACKUP_EXISTS=$(ssh "${VPS_SSH}" "test -d ${REMOTE_DIR} && echo yes || echo no")
if [[ "$BACKUP_EXISTS" == "yes" ]]; then
    log_info "Criando backup da versao anterior..."
    ssh "${VPS_SSH}" "rm -rf ${REMOTE_DIR}.backup && cp -a ${REMOTE_DIR} ${REMOTE_DIR}.backup"
    log_ok "Backup criado em ${REMOTE_DIR}.backup"
fi

# Create remote directory
ssh "${VPS_SSH}" "mkdir -p ${REMOTE_DIR}"

# Upload build files
log_info "Enviando arquivos de build..."
scp -r "${BUILD_DIR}/" "${VPS_SSH}:${REMOTE_DIR}/${BUILD_DIR}/"

# Upload package.json
if [[ -f "package.json" ]]; then
    scp package.json "${VPS_SSH}:${REMOTE_DIR}/"
fi

# Upload lock file
for lockfile in pnpm-lock.yaml package-lock.json yarn.lock; do
    if [[ -f "$lockfile" ]]; then
        scp "$lockfile" "${VPS_SSH}:${REMOTE_DIR}/"
        break
    fi
done

# Upload .env if it exists
if [[ -f ".env" ]]; then
    log_info "Enviando arquivo .env..."
    scp .env "${VPS_SSH}:${REMOTE_DIR}/"
fi

# Upload ecosystem.config.js if it exists
if [[ -f "ecosystem.config.js" ]]; then
    scp ecosystem.config.js "${VPS_SSH}:${REMOTE_DIR}/"
fi

# Upload static dashboard if it exists
for dashboard_dir in dashboard/dist public/dist frontend/dist; do
    if [[ -d "$dashboard_dir" ]]; then
        log_info "Enviando dashboard estatico (${dashboard_dir})..."
        ssh "${VPS_SSH}" "mkdir -p ${REMOTE_DIR}/dashboard"
        scp -r "${dashboard_dir}/"* "${VPS_SSH}:${REMOTE_DIR}/dashboard/"
        break
    fi
done

# Install production dependencies on VPS
log_info "Instalando dependencias de producao no servidor..."
ssh "${VPS_SSH}" "cd ${REMOTE_DIR} && npm install --production --ignore-scripts 2>&1 | tail -3"

log_ok "Upload concluido"

# --- Step 3: Configure Nginx ---
log_info "=== PASSO 3/6: Configuracao Nginx ==="
bash "${SCRIPT_DIR}/nginx-config.sh" "$SUBDOMAIN" "$PORT" "$PROJECT_NAME"

# --- Step 4: Start/restart with PM2 ---
log_info "=== PASSO 4/6: PM2 ==="

# Determine entry point
ENTRY_POINT=""
if ssh "${VPS_SSH}" "test -f ${REMOTE_DIR}/${BUILD_DIR}/index.js"; then
    ENTRY_POINT="${BUILD_DIR}/index.js"
elif ssh "${VPS_SSH}" "test -f ${REMOTE_DIR}/${BUILD_DIR}/server.js"; then
    ENTRY_POINT="${BUILD_DIR}/server.js"
elif ssh "${VPS_SSH}" "test -f ${REMOTE_DIR}/server.js"; then
    ENTRY_POINT="server.js"
elif ssh "${VPS_SSH}" "test -f ${REMOTE_DIR}/index.js"; then
    ENTRY_POINT="index.js"
else
    log_error "Nenhum entry point encontrado (index.js, server.js)"
    log_error "Arquivos no servidor:"
    ssh "${VPS_SSH}" "ls -la ${REMOTE_DIR}/${BUILD_DIR}/"
    exit 1
fi

log_info "Entry point: ${ENTRY_POINT}"

# Check if PM2 process already exists
PM2_EXISTS=$(ssh "${VPS_SSH}" "pm2 list | grep '${PROJECT_NAME}' || true")
if [[ -n "$PM2_EXISTS" ]]; then
    log_info "Reiniciando processo PM2 existente..."
    ssh "${VPS_SSH}" "cd ${REMOTE_DIR} && pm2 restart ${PROJECT_NAME}"
else
    log_info "Criando novo processo PM2..."
    if ssh "${VPS_SSH}" "test -f ${REMOTE_DIR}/ecosystem.config.js"; then
        ssh "${VPS_SSH}" "cd ${REMOTE_DIR} && pm2 start ecosystem.config.js"
    else
        ssh "${VPS_SSH}" "cd ${REMOTE_DIR} && PORT=${PORT} pm2 start ${ENTRY_POINT} --name ${PROJECT_NAME}"
    fi
fi

# Save PM2 process list for startup persistence
ssh "${VPS_SSH}" "pm2 save"
log_ok "PM2 configurado e salvo"

# --- Step 5: SSL Certificate ---
log_info "=== PASSO 5/6: Certificado SSL ==="
bash "${SCRIPT_DIR}/ssl-setup.sh" "$FULL_DOMAIN"

# --- Step 6: Health check ---
log_info "=== PASSO 6/6: Verificacao ==="
sleep 3
bash "${SCRIPT_DIR}/health-check.sh" "$PROJECT_NAME" "$PORT" "$FULL_DOMAIN"

# --- Done ---
echo ""
echo "=========================================="
echo -e "  ${GREEN}DEPLOY CONCLUIDO COM SUCESSO!${NC}"
echo "=========================================="
echo "  App:     ${PROJECT_NAME}"
echo "  URL:     https://${FULL_DOMAIN}"
echo "  PM2:     pm2 logs ${PROJECT_NAME}"
echo "  Backup:  ${REMOTE_DIR}.backup/"
echo "=========================================="
echo ""
