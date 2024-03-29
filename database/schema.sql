CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
login TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS photos (
id INTEGER PRIMARY KEY,
login TEXT NOT NULL,
photo_name TEXT NOT NULL,
upload_date TEXT NOT NULL,
album_id INTEGER
);

CREATE TABLE IF NOT EXISTS albums (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);