from urllib.parse import urlparse

TRUSTED = {
  "apnews.com": 0.95, "reuters.com": 0.95, "bbc.com": 0.9, "npr.org": 0.85,
  "nytimes.com": 0.85, "washingtonpost.com": 0.85, "wsj.com": 0.85,
  "courtlistener.com": 1.0, "uscourts.gov": 1.0, "congress.gov": 1.0
}

def source_confidence(url: str) -> float:
  host = urlparse(url).netloc.lower()
  return max((score for dom, score in TRUSTED.items() if host.endswith(dom)), default=0.5)

def verification_label(source_type: str, conf: float) -> str:
  if source_type in ("pdf", "docket", "gov"):
    return "verified_primary"
  if conf >= 0.9:
    return "corroborated_secondary"
  if conf >= 0.7:
    return "secondary_report"
  return "unverified"
