# Troubleshooting — VPS Deploy Issues

Common problems and solutions for Node.js apps deployed on the Hostinger VPS.

## Connection Issues

### Cannot SSH into the server

```
ssh: connect to host 76.13.175.161 port 22: Connection refused
```

**Causes:**
- VPS is down or rebooting
- SSH service is not running
- Firewall blocking port 22

**Solutions:**
1. Check VPS status in Hostinger panel
2. Use Hostinger's VPS console to restart SSH: `systemctl restart sshd`
3. Check firewall: `ufw status` — ensure port 22 is allowed

### SSH key authentication fails

```
Permission denied (publickey)
```

**Solutions:**
1. Verify the local SSH key: `ls -la ~/.ssh/id_*`
2. Check authorized_keys on VPS: `cat /root/.ssh/authorized_keys`
3. Fix permissions: `chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys`

---

## Port Issues

### EADDRINUSE — Port already in use

```
Error: listen EADDRINUSE: address already in use :::3007
```

**Solutions:**
1. Find what is using the port:
   ```bash
   ssh root@76.13.175.161 "ss -tlnp | grep :3007"
   ```
2. Kill the process:
   ```bash
   ssh root@76.13.175.161 "fuser -k 3007/tcp"
   ```
3. Or change the port in the app config

### Allocated ports reference

| Port | App |
|------|-----|
| 3003 | whatsapp-analyzer |
| 3005 | luxstudio-whatsapp |
| 3006 | podcast-infinito |
| 3010 | imperatriz-carroseis |
| 18790 | imperio |

Next available: 3007, 3008, 3009, 3011+

---

## Nginx Issues

### Nginx config syntax error

```
nginx: [emerg] unknown directive "proxy_passs"
```

**Solutions:**
1. Test config: `nginx -t`
2. Check the specific file for typos
3. Re-generate with `nginx-config.sh`

### 502 Bad Gateway

The app is not running or not responding on the expected port.

**Solutions:**
1. Check if the app is running: `pm2 list`
2. Check if the port is listening: `ss -tlnp | grep :PORT`
3. Test local connection: `curl -v http://127.0.0.1:PORT`
4. Check app logs: `pm2 logs APP_NAME --lines 50`

### 504 Gateway Timeout

The app is taking too long to respond.

**Solutions:**
1. Increase Nginx timeout values:
   ```nginx
   proxy_connect_timeout 120s;
   proxy_send_timeout 120s;
   proxy_read_timeout 120s;
   ```
2. Check if the app is overloaded: `pm2 monit`
3. Check system resources: `htop`

### 413 Request Entity Too Large

File upload exceeds Nginx default limit (1MB).

**Solution:** Add to the server block:
```nginx
client_max_body_size 50M;
```

### Nginx not starting after config change

```bash
# Check error details
nginx -t

# If config is broken, remove the problematic site
rm /etc/nginx/sites-enabled/PROBLEMATIC_DOMAIN

# Reload
systemctl reload nginx
```

---

## PM2 Issues

### App keeps restarting (restart loop)

**Solutions:**
1. Check logs for the crash reason:
   ```bash
   pm2 logs APP_NAME --err --lines 100
   ```
2. Common causes:
   - Missing environment variables (check `.env`)
   - Missing dependencies (`npm install --production`)
   - Wrong entry point path
   - Database file permissions

3. Stop the loop and debug:
   ```bash
   pm2 stop APP_NAME
   cd /var/www/apps/APP_NAME
   node dist/index.js  # Run directly to see errors
   ```

### PM2 process disappeared after reboot

**Solution:** Set up PM2 startup:
```bash
pm2 startup
pm2 save
```

### PM2 high memory usage

```bash
# Check memory per process
pm2 monit

# Set memory limit in ecosystem config
max_memory_restart: '300M'

# Restart the app
pm2 restart APP_NAME
```

### PM2 logs filling disk

```bash
# Check log sizes
du -sh /root/.pm2/logs/

# Flush all logs
pm2 flush

# Install log rotation
pm2 install pm2-logrotate
pm2 set pm2-logrotate:max_size 50M
pm2 set pm2-logrotate:retain 7
```

---

## SSL / Certbot Issues

### Certbot fails: "Could not automatically find a matching server block"

**Solution:** Ensure Nginx config has `server_name DOMAIN;` that matches exactly.

### Certbot fails: "Challenge failed for domain"

The domain DNS is not pointing to the VPS, or port 80 is blocked.

**Solutions:**
1. Check DNS: `dig +short DOMAIN.iacomtata.com.br`
2. Must resolve to `76.13.175.161`
3. Ensure Nginx is running on port 80: `ss -tlnp | grep :80`
4. Ensure no firewall blocking port 80: `ufw allow 80/tcp`

### SSL certificate expired

```bash
# Check all certificates
certbot certificates

# Renew all
certbot renew

# Renew specific domain
certbot renew --cert-name DOMAIN.iacomtata.com.br

# Force renewal
certbot renew --force-renewal

# Ensure auto-renewal timer is active
systemctl enable --now certbot.timer
systemctl status certbot.timer
```

### Mixed content warnings (HTTPS page loading HTTP resources)

The app is generating HTTP URLs instead of HTTPS.

**Solution:** Ensure the proxy headers are set so the app knows it is behind HTTPS:
```nginx
proxy_set_header X-Forwarded-Proto $scheme;
```
And the app trusts the proxy (Express: `app.set('trust proxy', 1)`).

---

## SQLite Issues

### Database locked

```
SQLITE_BUSY: database is locked
```

**Solutions:**
1. Ensure WAL mode is enabled:
   ```sql
   PRAGMA journal_mode=WAL;
   ```
2. Check for zombie processes holding the lock:
   ```bash
   fuser /var/www/apps/APP_NAME/data.db
   ```
3. Restart the app: `pm2 restart APP_NAME`

### Database file permissions

```
SQLITE_CANTOPEN: unable to open database file
```

**Solutions:**
1. Check permissions:
   ```bash
   ls -la /var/www/apps/APP_NAME/*.db
   ```
2. Fix ownership:
   ```bash
   chown root:root /var/www/apps/APP_NAME/*.db
   chmod 644 /var/www/apps/APP_NAME/*.db
   ```

### Database corrupted after crash

```bash
# Create backup of corrupted db
cp data.db data.db.corrupted

# Try to recover
sqlite3 data.db ".dump" | sqlite3 data_recovered.db
mv data_recovered.db data.db
```

---

## Node.js / npm Issues

### Module not found after deploy

```
Error: Cannot find module 'express'
```

**Solution:** Install dependencies on the VPS:
```bash
cd /var/www/apps/APP_NAME
npm install --production
```

### Wrong Node.js version

```bash
# Check current version
node -v

# Switch via nvm
nvm use 22
nvm alias default 22
```

### Build fails on VPS (out of memory)

Always build locally and SCP the dist files. The VPS has limited RAM.

---

## Disk Space Issues

```bash
# Check disk usage
df -h

# Find large directories
du -sh /var/www/apps/* | sort -hr

# Clean PM2 logs
pm2 flush

# Clean npm cache
npm cache clean --force

# Remove old backups
rm -rf /var/www/apps/*.backup
rm -rf /var/www/apps/*.failed

# Clean apt cache
apt clean
```

---

## Quick Diagnostic Script

Run this to get a full system overview:

```bash
ssh root@76.13.175.161 bash -c '
echo "=== DISK ==="
df -h /
echo ""
echo "=== MEMORY ==="
free -h
echo ""
echo "=== PM2 ==="
pm2 list
echo ""
echo "=== NGINX ==="
nginx -t 2>&1
echo ""
echo "=== PORTS ==="
ss -tlnp | grep -E ":(80|443|300[0-9]|301[0-9]|18790) "
echo ""
echo "=== SSL CERTS ==="
certbot certificates 2>/dev/null | grep -E "(Certificate Name|Expiry)" || echo "certbot not found"
'
```
