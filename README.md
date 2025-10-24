# Trumpality (StegBiography Module)

Neutral, evidence-first documentation of **Donald J. Trump**, using verifiable public sources
(court filings, government records, reputable journalism). Includes a **FREE-DOM (involvement)** layer
to map entities, events, dates, and filings.

## Quick Start (no laptop needed)
1) In the GitHub app, create a repo named **Trumpality** (public).
2) Upload the contents of this ZIP to the root of that repo.
3) Go to **Actions** → run **weekly-ingest** once to populate the database.

### Optional (if you open Codespaces later)
```bash
uvicorn api.app:app --reload --port 8080
```

See `freedom/` for the involvement graph files (edit the CSVs, then run `build_graph.py` in Codespaces later).
