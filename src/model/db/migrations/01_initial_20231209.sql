
-- Creates connection table ot my database 

CREATE TABLE IF NOT EXISTS connections (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name TEXT NOT NULL,
  linkedin TEXT NOT NULL,
);