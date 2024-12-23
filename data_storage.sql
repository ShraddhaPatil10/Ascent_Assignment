CREATE TABLE IF NOT EXISTS binance_account (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data JSON NOT NULL
);

CREATE TABLE IF NOT EXISTS binance_trades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data JSON NOT NULL
);

CREATE TABLE IF NOT EXISTS binance_income (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data JSON NOT NULL
);

CREATE TABLE IF NOT EXISTS crypto_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    currency VARCHAR(255),
    date DATE,
    open DECIMAL(18, 8),
    close DECIMAL(18, 8),
    volume DECIMAL(18, 8)
);