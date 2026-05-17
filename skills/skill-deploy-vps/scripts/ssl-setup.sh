#!/usr/bin/env bash
# =============================================================================
# ssl-setup.sh — Provision SSL certificate via Certbot (Let's Encrypt)
#
# Usage: bash ssl-setup.sh <full-domain>
# Example: bash ssl-setup.sh myapp.iacomtata.com.br
#
# Prerequisites:
# - Nginx must be configured and running for the domain
# - DNS must point to the VPS IP (76.13.175.161)
# - Certbot must be installed on the VPS
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
if [[ $# -lt 1 ]]; then
    echo "Uso: bash ssl-setup.sh <dominio-completo>"
    echo "Exemplo: bash ssl-setup.sh myapp.iacomtata.com.br"
    exit 1
fi

FULL_DOMAIN="$1"

log_info "Configurando SSL para ${FULL_DOMAIN}..."

# Check if certificate already exists
CERT_EXISTS=$(ssh "${VPS_SSH}" "certbot certificates 2>/dev/null | grep '${FULL_DOMAIN}' || true")
if [[ -n "$CERT_EXISTS" ]]; then
    log_warn "Certificado SSL ja existe para ${FULL_DOMAIN}"
    log_info "Verificando validade..."
    ssh "${VPS_SSH}" "certbot certificates 2>/dev/null | grep -A3 '${FULL_DOMAIN}'"
    log_ok "SSL ja configurado — nenhuma acao necessaria"
    exit 0
fi

# Verify DNS resolution points to our VPS
log_info "Verificando DNS para ${FULL_DOMAIN}..."
RESOLVED_IP=$(dig +short "${FULL_DOMAIN}" 2>/dev/null || true)
if [[ "$RESOLVED_IP" != "$VPS_IP" ]]; then
    log_warn "DNS de ${FULL_DOMAIN} resolve para '${RESOLVED_IP}' (esperado: ${VPS_IP})"
    log_warn "O certificado pode falhar se o DNS nao estiver apontando corretamente"
    read -rp "Continuar mesmo assim? (s/N): " confirm
    if [[ "$confirm" != "s" && "$confirm" != "S" ]]; then
        log_error "SSL cancelado pelo usuario"
        exit 1
    fi
fi

# Check if Nginx config exists for this domain
NGINX_EXISTS=$(ssh "${VPS_SSH}" "test -f /etc/nginx/sites-available/${FULL_DOMAIN} && echo yes || echo no")
if [[ "$NGINX_EXISTS" != "yes" ]]; then
    log_error "Configuracao Nginx nao encontrada para ${FULL_DOMAIN}"
    log_error "Execute nginx-config.sh primeiro"
    exit 1
fi

# Run Certbot to obtain certificate
log_info "Obtendo certificado SSL via Certbot..."
CERTBOT_OUTPUT=$(ssh "${VPS_SSH}" "certbot --nginx -d ${FULL_DOMAIN} --non-interactive --agree-tos --email tatagoncalvesoficial@gmail.com --redirect 2>&1")
CERTBOT_EXIT=$?

if [[ $CERTBOT_EXIT -eq 0 ]]; then
    log_ok "Certificado SSL instalado com sucesso!"
    log_info "HTTPS ativo em https://${FULL_DOMAIN}"

    # Verify HTTPS is working
    log_info "Verificando HTTPS..."
    sleep 2
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "https://${FULL_DOMAIN}" --max-time 10 2>/dev/null || echo "000")
    if [[ "$HTTP_CODE" != "000" ]]; then
        log_ok "HTTPS respondendo (HTTP ${HTTP_CODE})"
    else
        log_warn "HTTPS nao respondeu — pode levar alguns segundos para propagar"
    fi

    # Show certificate info
    log_info "Detalhes do certificado:"
    ssh "${VPS_SSH}" "certbot certificates 2>/dev/null | grep -A5 '${FULL_DOMAIN}'" || true
else
    log_error "Falha ao obter certificado SSL:"
    echo "$CERTBOT_OUTPUT"
    log_warn "Verifique: 1) DNS aponta para ${VPS_IP} 2) Nginx esta rodando 3) Porta 80 acessivel"
    exit 1
fi

# Verify auto-renewal is configured
log_info "Verificando renovacao automatica..."
TIMER_ACTIVE=$(ssh "${VPS_SSH}" "systemctl is-active certbot.timer 2>/dev/null || echo inactive")
if [[ "$TIMER_ACTIVE" == "active" ]]; then
    log_ok "Renovacao automatica ativa (certbot.timer)"
else
    log_warn "Timer de renovacao nao esta ativo — ativando..."
    ssh "${VPS_SSH}" "systemctl enable --now certbot.timer 2>/dev/null" || true
fi

log_ok "SSL configurado com sucesso para ${FULL_DOMAIN}"
