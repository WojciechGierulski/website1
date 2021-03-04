CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
login TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
gallery_code INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS admins (
id INTEGER PRIMARY KEY,
login TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS photos (
id INTEGER PRIMARY KEY,
login TEXT NOT NULL,
photo_name TEXT NOT NULL,
photo_code TEXT NOT NULL,
upload_date TEXT NOT NULL
);