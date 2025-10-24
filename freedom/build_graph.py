import csv, os

NODES_OUT = "freedom/graph_nodes.csv"
EDGES_OUT = "freedom/graph_edges.csv"

def read_csv(p):
  if not os.path.exists(p): return []
  with open(p, newline='', encoding='utf-8') as f:
    return list(csv.DictReader(f))

def write_csv(p, rows, fieldnames):
  with open(p, "w", newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader(); w.writerows(rows)

def main():
  entities = read_csv("freedom/entities.csv")
  rels = read_csv("freedom/relations.csv")
  nodes = [{"id":e["entity_id"], "label":e["label"], "type":e["type"], "source_url":e["source_url"]} for e in entities]
  edges = [{"id":r["edge_id"], "source":r["from_id"], "target":r["to_id"], "relation":r["relation"], "date":r["date"], "filing":r["filing"], "source_url":r["source_url"]} for r in rels]
  write_csv(NODES_OUT, nodes, ["id","label","type","source_url"])
  write_csv(EDGES_OUT, edges, ["id","source","target","relation","date","filing","source_url"])
  print("Wrote:", NODES_OUT, EDGES_OUT)

if __name__ == "__main__":
  os.makedirs("freedom", exist_ok=True)
  main()
