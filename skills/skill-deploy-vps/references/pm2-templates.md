# PM2 Ecosystem Config Templates

Reference templates for PM2 process management on the Hostinger VPS.

## Template 1: Simple Node.js App

Minimal config for a single process.

```javascript
// ecosystem.config.js
module.exports = {
  apps: [{
    name: 'APP_NAME',
    script: 'dist/index.js',
    cwd: '/var/www/apps/APP_NAME',
    env: {
      NODE_ENV: 'production',
      PORT: 3007
    },
    // Restart on crash
    autorestart: true,
    // Max restarts before stopping
    max_restarts: 10,
    // Restart if memory exceeds limit
    max_memory_restart: '300M',
    // Log configuration
    error_file: '/var/www/apps/APP_NAME/logs/error.log',
    out_file: '/var/www/apps/APP_NAME/logs/out.log',
    log_date_format: 'YYYY-MM-DD HH:mm:ss',
    // Merge stdout and stderr
    merge_logs: true
  }]
};
```

## Template 2: Express + Socket.IO (WhatsApp Bot)

Config for WhatsApp bots that need stable long-running connections.

```javascript
// ecosystem.config.js
module.exports = {
  apps: [{
    name: 'BOT_NAME',
    script: 'dist/index.js',
    cwd: '/var/www/apps/BOT_NAME',
    env: {
      NODE_ENV: 'production',
      PORT: 3005
    },
    autorestart: true,
    max_restarts: 15,
    max_memory_restart: '500M',
    // Graceful restart (send SIGINT, wait 5s, then SIGKILL)
    kill_timeout: 5000,
    // Wait before considering app as started
    wait_ready: true,
    listen_timeout: 10000,
    // Exponential backoff restart delay
    exp_backoff_restart_delay: 1000,
    // Log files
    error_file: '/var/www/apps/BOT_NAME/logs/error.log',
    out_file: '/var/www/apps/BOT_NAME/logs/out.log',
    log_date_format: 'YYYY-MM-DD HH:mm:ss',
    merge_logs: true
  }]
};
```

## Template 3: Monorepo / Multi-Service

For projects that run multiple services (e.g., backend + cron worker).

```javascript
// ecosystem.config.js
module.exports = {
  apps: [
    {
      name: 'APP_NAME-api',
      script: 'dist/server.js',
      cwd: '/var/www/apps/APP_NAME',
      env: {
        NODE_ENV: 'production',
        PORT: 3007
      },
      autorestart: true,
      max_restarts: 10,
      max_memory_restart: '300M'
    },
    {
      name: 'APP_NAME-worker',
      script: 'dist/worker.js',
      cwd: '/var/www/apps/APP_NAME',
      env: {
        NODE_ENV: 'production'
      },
      autorestart: true,
      max_restarts: 10,
      max_memory_restart: '200M',
      // Cron-like restart (restart daily at 3am)
      cron_restart: '0 3 * * *'
    }
  ]
};
```

## Template 4: Imperio (Fastify + Dashboard)

Specific to the Imperio platform.

```javascript
// ecosystem.config.js
module.exports = {
  apps: [{
    name: 'imperio',
    script: 'dist/index.js',
    cwd: '/var/www/apps/imperio',
    env: {
      NODE_ENV: 'production',
      PORT: 18790,
      IMPERIO_HOME: '/root/.imperio'
    },
    autorestart: true,
    max_restarts: 10,
    max_memory_restart: '500M',
    kill_timeout: 5000,
    error_file: '/root/.imperio/logs/error.log',
    out_file: '/root/.imperio/logs/out.log',
    log_date_format: 'YYYY-MM-DD HH:mm:ss',
    merge_logs: true
  }]
};
```

## Template 5: App with Environment File

Load environment variables from `.env` file.

```javascript
// ecosystem.config.js
const dotenv = require('dotenv');
const path = require('path');

// Load .env file
const envConfig = dotenv.config({
  path: path.resolve(__dirname, '.env')
}).parsed || {};

module.exports = {
  apps: [{
    name: 'APP_NAME',
    script: 'dist/index.js',
    cwd: '/var/www/apps/APP_NAME',
    env: {
      NODE_ENV: 'production',
      ...envConfig
    },
    autorestart: true,
    max_restarts: 10,
    max_memory_restart: '300M'
  }]
};
```

**Note:** Most apps read `.env` directly (via `dotenv`), so the PM2 ecosystem config does not usually need to load it. Use this template only when environment variables must be injected by PM2.

## PM2 Management Commands

```bash
# List all processes
pm2 list

# Start app
pm2 start ecosystem.config.js

# Restart app
pm2 restart APP_NAME

# Stop app
pm2 stop APP_NAME

# Delete app from PM2
pm2 delete APP_NAME

# View logs (real-time)
pm2 logs APP_NAME

# View last 100 lines of logs
pm2 logs APP_NAME --lines 100

# View error logs only
pm2 logs APP_NAME --err --lines 50

# Monitor (CPU/memory dashboard)
pm2 monit

# Save current process list (persists across reboots)
pm2 save

# Resurrect saved processes (run after reboot)
pm2 resurrect

# Setup PM2 startup script (run once)
pm2 startup

# Reload all apps (zero-downtime)
pm2 reload all

# Flush all logs
pm2 flush

# Show detailed info for an app
pm2 show APP_NAME
```

## PM2 Log Rotation

Install the log rotation module to prevent logs from filling the disk:

```bash
pm2 install pm2-logrotate

# Configure rotation
pm2 set pm2-logrotate:max_size 50M
pm2 set pm2-logrotate:retain 7
pm2 set pm2-logrotate:compress true
pm2 set pm2-logrotate:workerInterval 60
```

## Resource Limits per App Type

| App Type | Max Memory | Max Restarts |
|----------|-----------|-------------|
| Simple API | 200-300M | 10 |
| WhatsApp Bot | 400-500M | 15 |
| Dashboard + API | 300-400M | 10 |
| Imperio | 500M | 10 |
| Worker/Cron | 150-200M | 10 |
