
CREATE TABLE IF NOT EXISTS interactions (
  id TEXT PRIMARY KEY,
  connection_id TEXT,
  notes TEXT,
  date_created DATETIME,
  date_interaction DATETIME,
  FOREIGN KEY (connection_id) REFERENCES connections(id)
);

