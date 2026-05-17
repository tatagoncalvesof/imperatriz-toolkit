# Nginx Config Templates

Reference templates for different Node.js application types deployed on the Hostinger VPS.

All configs follow the same base pattern:
- Nginx listens on port 80 (HTTP) and 443 (HTTPS after Certbot)
- Proxies to `127.0.0.1:PORT`
- WebSocket support included by default
- Certbot handles the HTTPS configuration automatically

## Template 1: Standard Node.js App (Express/Fastify)

The most common pattern. Single backend with optional static file serving.

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name APP_NAME.iacomtata.com.br;

    location / {
        proxy_pass http://127.0.0.1:PORT;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_buffering off;
        proxy_cache_bypass $http_upgrade;
    }

    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml application/json application/javascript application/xml+rss image/svg+xml;
}
```

## Template 2: Backend + Static Dashboard (React/Vite)

Backend API on `/api/` and `/ws/`, static dashboard files served directly by Nginx.

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name APP_NAME.iacomtata.com.br;

    # Dashboard (static files)
    root /var/www/apps/APP_NAME/dashboard;
    index index.html;

    # SPA fallback — serve index.html for client-side routing
    location / {
        try_files $uri $uri/ /index.html;
    }

    # API proxy
    location /api/ {
        proxy_pass http://127.0.0.1:PORT;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # WebSocket proxy
    location /ws {
        proxy_pass http://127.0.0.1:PORT;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    # Socket.IO
    location /socket.io/ {
        proxy_pass http://127.0.0.1:PORT;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    # Static asset caching
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml application/json application/javascript application/xml+rss image/svg+xml;
}
```

## Template 3: Path-Based App (subpath instead of subdomain)

For apps served under a path like `iacomtata.com.br/appname/`.

```nginx
# Add this inside the main iacomtata.com.br server block

location /APP_PATH/ {
    proxy_pass http://127.0.0.1:PORT/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

**Used by:** Imperatriz dos Carroseis at `/imperatrizdoscarroseis/`.

## Template 4: WhatsApp Bot (Express + Socket.IO + whatsapp-web.js)

Specific pattern for WhatsApp bots that need long-lived WebSocket connections and file uploads.

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name BOT_NAME.iacomtata.com.br;

    # Increase upload limit for media files
    client_max_body_size 50M;

    location / {
        proxy_pass http://127.0.0.1:PORT;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Longer timeouts for WhatsApp connections
        proxy_connect_timeout 300s;
        proxy_send_timeout 300s;
        proxy_read_timeout 300s;

        proxy_buffering off;
        proxy_cache_bypass $http_upgrade;
    }

    # Socket.IO specific
    location /socket.io/ {
        proxy_pass http://127.0.0.1:PORT;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_read_timeout 86400s;
    }

    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml application/json application/javascript application/xml+rss image/svg+xml;
}
```

## Template 5: Imperio (Fastify + WebSocket + Dashboard at custom path)

Specific to the Imperio platform deployment.

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name imperio.iacomtata.com.br;

    location / {
        proxy_pass http://127.0.0.1:18790;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_buffering off;
    }

    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml application/json application/javascript application/xml+rss image/svg+xml;
}
```

**Note:** The Imperio dashboard is served from `/root/.imperio/dashboard/` by the Fastify server itself, NOT by Nginx.

## After Certbot

After running `certbot --nginx -d DOMAIN`, Certbot automatically:
1. Adds `listen 443 ssl` directives
2. Adds `ssl_certificate` and `ssl_certificate_key` paths
3. Adds an HTTP-to-HTTPS redirect block
4. Sets SSL parameters (protocols, ciphers)

Do NOT manually edit the SSL sections — let Certbot manage them.

## Nginx Management Commands

```bash
# Test config syntax
nginx -t

# Reload config (no downtime)
systemctl reload nginx

# Restart Nginx (brief downtime)
systemctl restart nginx

# View error logs
tail -50 /var/log/nginx/error.log

# View access logs for specific domain
grep "APP_NAME.iacomtata.com.br" /var/log/nginx/access.log | tail -50
```
