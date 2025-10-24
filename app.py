from fastapi import FastAPI
import sqlite3

DB = "data/processed/records.sqlite"
app = FastAPI(title="Trumpality API", version="0.1" )

def rows(sql, args=()):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    cur = con.execute(sql, args)
    r = [dict(x) for x in cur.fetchall()]
    con.close()
    return r

@app.get("/records")
def get_records(limit: int = 100, category: str | None = None):
    q = "SELECT * FROM records"
    a = []
    if category:
        q += " WHERE category=?"
        a.append(category)
    q += " ORDER BY date_published DESC LIMIT ?"
    a.append(limit)
    return rows(q, tuple(a))

@app.get("/records/{rid}")
def get_record(rid: str):
    r = rows("SELECT * FROM records WHERE id=?", (rid,))
    return r[0] if r else {}

@app.get("/stats")
def stats():
    by_cat = rows("SELECT category, COUNT(*) as n FROM records GROUP BY category")
    return {"by_category": by_cat, "total": sum(x["n"] for x in by_cat)}
