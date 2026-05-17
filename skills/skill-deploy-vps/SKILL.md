---
name: skill-deploy-vps
description: Deploy Node.js applications to a Hostinger VPS with Nginx reverse proxy, PM2 process management, and SSL certificates. Use for deploying Express/Fastify backends, React/Vite dashboards, WhatsApp bots, and any Node.js app. Triggers on "deploy", "VPS", "servidor", "Nginx", "PM2", "SSL", "Hostinger", "subdominio", "publicar", "colocar no ar".
---

# Deploy VPS — Hostinger Node.js Apps

## Overview

Deploy Node.js applications to a Hostinger VPS (Ubuntu 24.04) running at `76.13.175.161`. Handles the full lifecycle: local build, file upload via SCP, Nginx reverse proxy configuration, PM2 process management, and SSL certificate provisioning via Certbot.

## Infrastructure Reference

| Component | Detail |
|-----------|--------|
| VPS IP | 76.13.175.161 |
| SSH | `ssh root@76.13.175.161` (key auth) |
| Domain | iacomtata.com.br |
| Apps dir | `/var/www/apps/` |
| Node | 22 (via nvm) |
| Package mgr | pnpm |
| Process mgr | PM2 |
| Reverse proxy | Nginx |
| SSL | Certbot (Let's Encrypt) |
| Databases | SQLite (WAL mode) in app dirs |

### Active Deployments

| App | Port | Subdomain | PM2 Name |
|-----|------|-----------|----------|
| WhatsApp Analyzer | 3003 | whatsapp.iacomtata.com.br | whatsapp-analyzer |
| LuxStudio Bot | 3005 | luxstudio.iacomtata.com.br | luxstudio-whatsapp |
| Podcast Infinito | 3006 | — | podcast-infinito |
| Imperatriz Carroseis | 3010 | iacomtata.com.br/imperatrizdoscarroseis | imperatriz-carroseis |
| Imperio | 18790 | imperio.iacomtata.com.br | imperio |

### Port Allocation

Ports 3003-3006, 3010, 18790 are taken. Use the next available port (3007, 3008, 3009, 3011+).

## Deploy Workflow

Execute these steps sequentially. Each step has a corresponding script in `scripts/`.

### Step 1 — Build Locally

Build the project on the local machine before uploading.

```bash
# For pnpm/turbo monorepo
cd ~/PROJECT_NAME
PATH="$HOME/.npm-global/bin:/usr/bin:/usr/local/bin:$PATH" pnpm run build

# For simple npm project
cd ~/PROJECT_NAME
npm run build
```

Verify the build output exists (`dist/`, `build/`, or `.next/`).

### Step 2 — Upload to VPS

Use SCP to transfer build artifacts. NEVER transfer `node_modules`.

```bash
# Create app directory on VPS
ssh root@76.13.175.161 "mkdir -p /var/www/apps/PROJECT_NAME"

# Upload backend dist
scp -r dist/ root@76.13.175.161:/var/www/apps/PROJECT_NAME/dist/

# Upload package.json and lock file
scp package.json root@76.13.175.161:/var/www/apps/PROJECT_NAME/

# Upload .env (if needed)
scp .env root@76.13.175.161:/var/www/apps/PROJECT_NAME/

# Install production dependencies on VPS
ssh root@76.13.175.161 "cd /var/www/apps/PROJECT_NAME && npm install --production"
```

For apps with a static dashboard (React/Vite):

```bash
# Upload dashboard build to app dir or ~/.imperio/dashboard/
scp -r dashboard/dist/* root@76.13.175.161:/var/www/apps/PROJECT_NAME/dashboard/
```

### Step 3 — Configure Nginx

Generate and install Nginx config for the subdomain. See `references/nginx-templates.md` for all template variants.

```bash
# Run the nginx config generator
bash scripts/nginx-config.sh SUBDOMAIN PORT PROJECT_NAME
```

Standard pattern: Nginx listens on port 80/443, proxies to `127.0.0.1:PORT`.

### Step 4 — Start with PM2

Create or update PM2 process. See `references/pm2-templates.md` for ecosystem config templates.

```bash
# Start new app
ssh root@76.13.175.161 "cd /var/www/apps/PROJECT_NAME && pm2 start dist/index.js --name PROJECT_NAME"

# Or use ecosystem file
ssh root@76.13.175.161 "cd /var/www/apps/PROJECT_NAME && pm2 start ecosystem.config.js"

# Save PM2 process list
ssh root@76.13.175.161 "pm2 save"
```

### Step 5 — SSL Certificate

Provision SSL certificate via Certbot.

```bash
bash scripts/ssl-setup.sh SUBDOMAIN.iacomtata.com.br
```

### Step 6 — Verify

Run health checks to confirm the deploy succeeded.

```bash
bash scripts/health-check.sh PROJECT_NAME PORT SUBDOMAIN.iacomtata.com.br
```

## Full Deploy Script

For a complete automated deploy, use the main deploy script:

```bash
bash scripts/deploy.sh PROJECT_NAME PORT SUBDOMAIN
```

Arguments:
- `PROJECT_NAME` — Name of the project (used for directory, PM2 name)
- `PORT` — Port the app listens on (e.g., 3007)
- `SUBDOMAIN` — Subdomain prefix (e.g., "myapp" for myapp.iacomtata.com.br)

The script executes all 6 steps in sequence with error handling and rollback on failure.

## Rollback

Revert to the previous version if a deploy fails:

```bash
bash scripts/rollback.sh PROJECT_NAME
```

The deploy script automatically creates a backup at `/var/www/apps/PROJECT_NAME.backup/` before uploading new files.

## Troubleshooting

See `references/troubleshooting.md` for common issues:
- Port already in use
- Nginx config syntax errors
- PM2 process crashes
- SSL certificate renewal failures
- Permission issues
- SQLite lock errors

## Quick Reference Commands

```bash
# Check all PM2 processes
ssh root@76.13.175.161 "pm2 list"

# View app logs
ssh root@76.13.175.161 "pm2 logs PROJECT_NAME --lines 50"

# Restart app
ssh root@76.13.175.161 "pm2 restart PROJECT_NAME"

# Test Nginx config
ssh root@76.13.175.161 "nginx -t"

# Reload Nginx
ssh root@76.13.175.161 "systemctl reload nginx"

# Check SSL cert expiry
ssh root@76.13.175.161 "certbot certificates"

# Disk usage
ssh root@76.13.175.161 "df -h && du -sh /var/www/apps/*"
```

## Resources

### scripts/
- `deploy.sh` — Complete deploy workflow (build, upload, configure, start, verify)
- `nginx-config.sh` — Generate and install Nginx reverse proxy config
- `ssl-setup.sh` — Provision SSL certificate via Certbot
- `health-check.sh` — Verify app is running (PM2 + HTTP)
- `rollback.sh` — Revert to previous deploy version

### references/
- `nginx-templates.md` — Nginx config templates for different app types
- `pm2-templates.md` — PM2 ecosystem config templates
- `troubleshooting.md` — Common issues and solutions
