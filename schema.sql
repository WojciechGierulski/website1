CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
login TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
)