ALTER TABLE records ADD COLUMN archive_wayback TEXT;
ALTER TABLE records ADD COLUMN archive_local_path TEXT;
ALTER TABLE records ADD COLUMN checksum_sha256 TEXT;
ALTER TABLE records ADD COLUMN last_verified_at TEXT;
ALTER TABLE records ADD COLUMN last_status_code INTEGER;
ALTER TABLE records ADD COLUMN link_ok INTEGER DEFAULT 1;
