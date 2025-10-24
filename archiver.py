import os, time, hashlib, requests, sqlite3
from urllib.parse import urlparse

DB = "data/processed/records.sqlite"
RAW_DIR = "data/raw"
HEADERS = {"User-Agent": "StegArchive/1.0 (+github actions)"}

def sha256_bytes(b):
    h = hashlib.sha256(); h.update(b); return h.hexdigest()

def save_local_snapshot(url, content):
    host = urlparse(url).netloc.replace(":", "_")
    digest = sha256_bytes(content)[:16]
    fn = f"{host}_{digest}.html"
    path = os.path.join(RAW_DIR, fn)
    os.makedirs(RAW_DIR, exist_ok=True)
    with open(path, "wb") as f: f.write(content)
    return path

def wayback_save(url):
    try:
        r = requests.get("https://web.archive.org/save/" + url, headers=HEADERS, timeout=60, allow_redirects=False)
        loc = r.headers.get("Content-Location", "")
        if loc and not loc.startswith("http"): loc = "https://web.archive.org" + loc
        if not loc and r.is_redirect and r.headers.get("Location"): loc = r.headers["Location"]
        return loc
    except Exception as e:
        print("Wayback save failed:", e)
        return ""

def archive_record(rec_id, url):
    r = requests.get(url, headers=HEADERS, timeout=60)
    r.raise_for_status()
    content = r.content
    checksum = sha256_bytes(content)
    local_path = save_local_snapshot(url, content)
    wb = wayback_save(url)
    conn = sqlite3.connect(DB)
    conn.execute("UPDATE records SET archive_local_path=?, archive_wayback=?, checksum_sha256=? WHERE id=?", (local_path, wb, checksum, rec_id))
    conn.commit(); conn.close()
    print("Archived:", rec_id, "->", bool(wb))

def main(limit=50):
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT id, source_url FROM records ORDER BY created_at DESC LIMIT ?", (limit,)).fetchall()
    conn.close()
    for row in rows:
        try:
            archive_record(row["id"], row["source_url"])
            time.sleep(3)
        except Exception as e:
            print("skip:", row["id"], e)

if __name__ == "__main__":
    main()
