DROP TABLE IF EXISTS bad_url;

CREATE TABLE bad_url (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host TEXT NOT NULL,
    port INTEGER NOT NULL,
    path TEXT
);