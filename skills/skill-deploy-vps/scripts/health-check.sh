#!/usr/bin/env bash
# =============================================================================
# health-check.sh — Verify app is running (PM2 status + HTTP check)
#
# Usage: bash health-check.sh <project-name> <port> [full-domain]
# Example: bash health-check.sh my-app 3007 myapp.iacomtata.com.br
# =============================================================================

set -euo pipefail

# --- Configuration ---
VPS_IP="76.13.175.161"
VPS_USER="root"
VPS_SSH="${VPS_USER}@${VPS_IP}"

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
if [[ $# -lt 2 ]]; then
    echo "Uso: bash health-check.sh <nome-projeto> <porta> [dominio-completo]"
    echo "Exemplo: bash health-check.sh my-app 3007 myapp.iacomtata.com.br"
    exit 1
fi

PROJECT_NAME="$1"
PORT="$2"
FULL_DOMAIN="${3:-}"
ERRORS=0

echo ""
echo "=========================================="
echo "  HEALTH CHECK: ${PROJECT_NAME}"
echo "=========================================="

# --- Check 1: PM2 process status ---
log_info "Verificando processo PM2..."
PM2_GREP=$(ssh "${VPS_SSH}" "pm2 list 2>/dev/null | grep '${PROJECT_NAME}' || true")
if [[ -n "$PM2_GREP" ]]; then
    echo "$PM2_GREP"
    if echo "$PM2_GREP" | grep -q "online"; then
        log_ok "PM2 processo online"
    else
        log_error "PM2 processo nao esta online"
        ERRORS=$((ERRORS + 1))
    fi
else
    log_error "Processo PM2 '${PROJECT_NAME}' nao encontrado"
    ERRORS=$((ERRORS + 1))
fi

# --- Check 2: Port is listening ---
log_info "Verificando porta ${PORT}..."
PORT_CHECK=$(ssh "${VPS_SSH}" "ss -tlnp | grep ':${PORT} ' || true")
if [[ -n "$PORT_CHECK" ]]; then
    log_ok "Porta ${PORT} ativa"
else
    log_error "Porta ${PORT} nao esta escutando"
    ERRORS=$((ERRORS + 1))
fi

# --- Check 3: HTTP response on localhost ---
log_info "Verificando resposta HTTP local (127.0.0.1:${PORT})..."
LOCAL_HTTP=$(ssh "${VPS_SSH}" "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:${PORT}/ --max-time 5 2>/dev/null || echo '000'")
if [[ "$LOCAL_HTTP" == "000" ]]; then
    log_error "Sem resposta HTTP em 127.0.0.1:${PORT}"
    ERRORS=$((ERRORS + 1))
elif [[ "$LOCAL_HTTP" -ge 200 && "$LOCAL_HTTP" -lt 400 ]]; then
    log_ok "HTTP local respondendo (${LOCAL_HTTP})"
elif [[ "$LOCAL_HTTP" -ge 400 ]]; then
    log_warn "HTTP local retornou erro (${LOCAL_HTTP}) — pode ser normal se nao ha rota raiz"
fi

# --- Check 4: External HTTPS (if domain provided) ---
if [[ -n "$FULL_DOMAIN" ]]; then
    log_info "Verificando HTTPS externo (${FULL_DOMAIN})..."
    EXTERNAL_HTTP=$(curl -s -o /dev/null -w "%{http_code}" "https://${FULL_DOMAIN}" --max-time 10 2>/dev/null || echo "000")
    if [[ "$EXTERNAL_HTTP" == "000" ]]; then
        log_warn "Sem resposta HTTPS em ${FULL_DOMAIN}"
        # Try HTTP
        EXTERNAL_HTTP_PLAIN=$(curl -s -o /dev/null -w "%{http_code}" "http://${FULL_DOMAIN}" --max-time 10 2>/dev/null || echo "000")
        if [[ "$EXTERNAL_HTTP_PLAIN" != "000" ]]; then
            log_warn "HTTP respondeu (${EXTERNAL_HTTP_PLAIN}) — SSL pode nao estar configurado"
        else
            log_error "Dominio ${FULL_DOMAIN} nao respondeu (nem HTTP nem HTTPS)"
            ERRORS=$((ERRORS + 1))
        fi
    elif [[ "$EXTERNAL_HTTP" -ge 200 && "$EXTERNAL_HTTP" -lt 400 ]]; then
        log_ok "HTTPS externo respondendo (${EXTERNAL_HTTP})"
    else
        log_warn "HTTPS externo retornou ${EXTERNAL_HTTP}"
    fi
fi

# --- Check 5: Memory and CPU usage ---
log_info "Verificando recursos do processo..."
PM2_SHOW=$(ssh "${VPS_SSH}" "pm2 show ${PROJECT_NAME} 2>/dev/null | grep -E 'memory|cpu|uptime|restarts' || true")
if [[ -n "$PM2_SHOW" ]]; then
    echo "$PM2_SHOW"
fi

# --- Check 6: Recent errors in logs ---
log_info "Verificando logs recentes..."
RECENT_ERRORS=$(ssh "${VPS_SSH}" "pm2 logs ${PROJECT_NAME} --lines 20 --nostream --err 2>/dev/null | grep -i 'error\|fatal\|crash\|EADDRINUSE' | tail -3 || true")
if [[ -n "$RECENT_ERRORS" ]]; then
    log_warn "Erros recentes nos logs:"
    echo "$RECENT_ERRORS"
else
    log_ok "Sem erros recentes nos logs"
fi

# --- Summary ---
echo ""
echo "=========================================="
if [[ $ERRORS -eq 0 ]]; then
    echo -e "  ${GREEN}TUDO OK — ${PROJECT_NAME} esta saudavel${NC}"
else
    echo -e "  ${RED}${ERRORS} PROBLEMA(S) ENCONTRADO(S)${NC}"
    echo "  Verifique os logs: ssh ${VPS_SSH} \"pm2 logs ${PROJECT_NAME} --lines 50\""
fi
echo "=========================================="
echo ""

exit $ERRORS
