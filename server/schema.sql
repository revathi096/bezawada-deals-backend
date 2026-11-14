
-- BEZAWADADEALS DATABASE

-- 1. USERS
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'customer'
      CHECK (role IN ('customer', 'seller', 'admin')),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. CATEGORIES
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    icon VARCHAR(20),
    active BOOLEAN DEFAULT TRUE
);

INSERT INTO categories (name, icon) VALUES
('Vegetables', '🥬'),
('Fruits', '🍎'),
('Shopping Malls & Brands', '🛍️'),
('Restaurants', '🍽️'),
('Grocery', '🛒'),
('Medical', '💊')
ON CONFLICT (name) DO NOTHING;

-- 3. DEALS
CREATE TABLE IF NOT EXISTS deals (
    id SERIAL PRIMARY KEY,
    seller_id INTEGER REFERENCES users(id),
    category_id INTEGER REFERENCES categories(id),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    price NUMERIC(12,2),
    discount VARCHAR(50),
    image_url TEXT,
    area VARCHAR(100),
    ward_number INTEGER CHECK (ward_number BETWEEN 1 AND 86),
    status VARCHAR(20) DEFAULT 'pending'
      CHECK (status IN ('pending', 'approved', 'rejected')),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. EXISTING DATABASE WARD COLUMN UPDATE
ALTER TABLE deals
ADD COLUMN IF NOT EXISTS ward_number INTEGER
CHECK (ward_number BETWEEN 1 AND 86);

-- 5. MARKET PRICES
CREATE TABLE IF NOT EXISTS market_prices (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(120) NOT NULL,
    telugu_name VARCHAR(120),
    price NUMERIC(12,2) NOT NULL CHECK (price >= 0),
    unit VARCHAR(30) NOT NULL,
    market_name VARCHAR(150),
    area VARCHAR(100),
    ward_number INTEGER CHECK (ward_number BETWEEN 1 AND 86),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 6. MARKET PRICE HISTORY
CREATE TABLE IF NOT EXISTS market_price_history (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(120) NOT NULL,
    price NUMERIC(12,2) NOT NULL,
    unit VARCHAR(30) NOT NULL,
    market_name VARCHAR(150),
    area VARCHAR(100),
    recorded_at TIMESTAMPTZ DEFAULT NOW()
);

-- 7. FAVORITES
CREATE TABLE IF NOT EXISTS favorites (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    deal_id INTEGER REFERENCES deals(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, deal_id)
);

-- 8. INDEXES
CREATE INDEX IF NOT EXISTS deals_status_idx
ON deals(status, created_at DESC);

CREATE INDEX IF NOT EXISTS deals_area_idx
ON deals(area);

CREATE INDEX IF NOT EXISTS deals_ward_idx
ON deals(ward_number);

CREATE INDEX IF NOT EXISTS prices_updated_idx
ON market_prices(updated_at DESC);

CREATE INDEX IF NOT EXISTS prices_area_idx
ON market_prices(area);
