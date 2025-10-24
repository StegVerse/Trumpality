import requests, sqlite3, time, datetime

DB = "data/processed/records.sqlite"
HEADERS = {"User-Agent": "StegArchive-Monitor/1.0"}

def check(url):
    try:
        r = requests.head(url, headers=HEADERS, timeout=30, allow_redirects=True)
        code = r.status_code
        ok = 200 <= code < 400
        if code >= 400:
            r = requests.get(url, headers=HEADERS, timeout=30, allow_redirects=True)
            code = r.status_code
            ok = 200 <= code < 400
        return ok, code
    except Exception:
        return False, 0

def main(limit=200):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    rows = cur.execute("SELECT id, source_url, archive_wayback FROM records ORDER BY created_at DESC LIMIT ?", (limit,)).fetchall()
    now = datetime.datetime.utcnow().isoformat()
    broken = 0
    for rid, src, wb in rows:
        ok, code = check(src)
        if not ok and wb:
            ok_wb, code_wb = check(wb)
            ok = ok or ok_wb
        cur.execute("UPDATE records SET last_verified_at=?, last_status_code=?, link_ok=? WHERE id=?", (now, code, 1 if ok else 0, rid))
        if not ok: broken += 1
        time.sleep(1)
    conn.commit(); conn.close()
    print(f"Checked {len(rows)} records; broken/unreachable: {broken}")

if __name__ == "__main__":
    main()
