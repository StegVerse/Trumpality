# FREE-DOM Rules (Global — apply to all StegBiography repos)

**FREE-DOM = Factually Recounted Epstein Era — Destruction Of Morality**

These rules **govern all data** in StegBiography repos (Trumpality, Epsteinality, Maxwellality, etc.).
We index verifiable information first and maintain a neutral, evidence-first tone.

## Verification Classes
- **verified_primary** — court/gov docs, official filings/releases, authenticated scans (with link or archived copy).
- **corroborated_secondary** — 2+ reputable outlets that cite or align with primaries (or carry identical material detail).
- **secondary_report** — one reputable outlet; primary not accessible.
- **unverified** — claims with unclear provenance; allowed only in **quarantine** for matching purposes.
- **debunked** — credible refutation (fact-check, correction, retraction).

## Movement Rules
- **Promote** only with added evidence (URL, snapshot, hash) via Pull Request.
- **Demote** automatically if links die and no archive exists; if an archive exists, keep status but flag `link_ok=0`.
- **Minors**: never add PII beyond publicly available court documents.
- **No memes/rumors** as records. They may be parked in **quarantine** (below) for co-occurrence matching only.

## Co-Occurrence & Promotion
- Items in _quarantine_ can be **matched** to windows of time/place where verified items occur.
- If multiple independent sources (different domains) and/or identical signals (e.g., photo pHash) co-occur in the same window,
  a **strength score** is computed; maintainers may promote via PR.

## Archival & Integrity
- Every source URL should have: **Wayback snapshot + local HTML snapshot + SHA-256 hash**.
- Link monitoring runs on schedule; broken links are flagged and the archived copy is retained.
