-- ══════════════════════════════════════
-- Schema: Vendedora IA — SQLite
-- Gerado por /lara-builder
-- ══════════════════════════════════════

-- WAL mode pra performance
PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

-- ── Leads (prospects que interagiram) ──
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT UNIQUE NOT NULL,       -- ID unico da sessao do widget
    phone TEXT DEFAULT '',                 -- Numero (se fornecido)
    name TEXT DEFAULT '',                  -- Nome (extraido da conversa)
    email TEXT DEFAULT '',                 -- Email (se fornecido)
    status TEXT DEFAULT 'new',             -- new | warm | hot | checkout_sent | converted | lost
    score INTEGER DEFAULT 0,              -- Score de qualificacao (0-100)
    tags TEXT DEFAULT '[]',               -- JSON array de tags
    source TEXT DEFAULT 'widget',          -- widget | whatsapp | direct
    utm_source TEXT DEFAULT '',            -- UTM de origem
    utm_medium TEXT DEFAULT '',
    utm_campaign TEXT DEFAULT '',
    first_contact_at TEXT DEFAULT (datetime('now')),
    last_message_at TEXT DEFAULT (datetime('now')),
    checkout_sent_at TEXT,                 -- Quando enviou link de compra
    converted_at TEXT,                     -- Quando comprou
    notes TEXT DEFAULT ''
);

-- ── Conversations (historico de mensagens) ──
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lead_id INTEGER NOT NULL,
    session_id TEXT NOT NULL,
    role TEXT NOT NULL,                    -- 'user' | 'bot'
    content TEXT NOT NULL,
    intent TEXT DEFAULT '',               -- purchase | objection | question | whatsapp | positive | churn_risk
    created_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (lead_id) REFERENCES leads(id)
);

-- ── Metrics (eventos de tracking) ──
CREATE TABLE IF NOT EXISTS metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event TEXT NOT NULL,                  -- chat_opened | message_sent | checkout_sent | conversion | whatsapp_redirect
    session_id TEXT DEFAULT '',
    data TEXT DEFAULT '{}',               -- JSON com dados extras
    created_at TEXT DEFAULT (datetime('now'))
);

-- ── Settings (configuracoes do sistema) ──
CREATE TABLE IF NOT EXISTS settings (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- ── Indices ──
CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status);
CREATE INDEX IF NOT EXISTS idx_leads_session ON leads(session_id);
CREATE INDEX IF NOT EXISTS idx_conversations_lead ON conversations(lead_id);
CREATE INDEX IF NOT EXISTS idx_conversations_session ON conversations(session_id);
CREATE INDEX IF NOT EXISTS idx_metrics_event ON metrics(event);
CREATE INDEX IF NOT EXISTS idx_metrics_created ON metrics(created_at);

-- ── Settings defaults ──
INSERT OR IGNORE INTO settings (key, value) VALUES
    ('bot_active', 'true'),
    ('auto_reply', 'true'),
    ('reply_delay_min', '2'),
    ('reply_delay_max', '5'),
    ('max_messages_per_conversation', '50'),
    ('working_hours_start', '08'),
    ('working_hours_end', '22'),
    ('blocked_sessions', '[]'),
    ('manual_takeover_sessions', '[]');
