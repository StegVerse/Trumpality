import os, uuid, requests
def save_pdf(url, out_dir="data/raw"):
  os.makedirs(out_dir, exist_ok=True)
  fn = f"{uuid.uuid4()}.pdf"
  path = os.path.join(out_dir, fn)
  r = requests.get(url, timeout=60); r.raise_for_status()
  with open(path, "wb") as f: f.write(r.content)
  return path
