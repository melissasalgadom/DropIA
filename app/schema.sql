CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    external_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    cost REAL NOT NULL,
    image_url TEXT,
    platform TEXT,
    supplier TEXT,
    category TEXT,
    status TEXT DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    external_id TEXT,
    customer_name TEXT,
    customer_email TEXT,
    total_amount REAL NOT NULL,
    status TEXT DEFAULT 'pending',
    platform TEXT,
    shipping_address TEXT,
    tracking_number TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
);

CREATE TABLE IF NOT EXISTS settings (
    key TEXT PRIMARY KEY,
    value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS scheduled_tasks (
    id TEXT PRIMARY KEY,
    type TEXT,
    frequency TEXT,
    params TEXT,
    created_at TEXT,
    last_run TEXT,
    status TEXT,
    last_result TEXT,
    error TEXT
);

CREATE TABLE IF NOT EXISTS market_analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    trending_products TEXT,
    growth_rate TEXT,
    popularity_score REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar configuración inicial
INSERT OR IGNORE INTO settings (key, value) VALUES ('app_settings', '{"dsers_username":"", "dsers_password":"", "update_frequency":"daily", "price_margin":"0.4"}');
