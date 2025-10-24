def consolidate_score(ver_status: str, confidence: float, replications: int) -> float:
  base = {"verified_primary":1.0,"corroborated_secondary":0.85,
          "secondary_report":0.7,"unverified":0.4,"debunked":0.0}.get(ver_status,0.4)
  bonus = min(replications * 0.03, 0.12)
  return round(min(1.0, base*0.8 + confidence*0.2 + bonus), 3)
