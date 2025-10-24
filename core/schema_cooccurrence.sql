-- Co-occurrence and Quarantine tables (idempotent for SQLite)
CREATE TABLE IF NOT EXISTS cooccurrence (
  id TEXT PRIMARY KEY,
  window_start TEXT,     -- ISO timestamp
  window_end   TEXT,     -- ISO timestamp
  place_id     TEXT,     -- normalized place/venue
  signals      TEXT,     -- JSON: ["photo_hash:abc","text:...","handle:@x","file:..."]
  entities     TEXT,     -- JSON array: ["e_trump","e_maxwell"]
  source_urls  TEXT,     -- JSON array
  strength     REAL,     -- 0..1 heuristic score
  created_at   TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS quarantine (
  id TEXT PRIMARY KEY,
  claim TEXT,               -- raw text / caption / snippet
  extracted_entities TEXT,  -- JSON array
  time_hint TEXT,           -- ISO if known
  place_hint TEXT,          -- string/geo if known
  source_url TEXT,          -- where this came from
  evidence TEXT,            -- JSON: weak signals (pHash, OCR text)
  status TEXT,              -- unverified | matched | promoted | rejected
  notes TEXT,
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);
