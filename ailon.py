import random

def ailon(V, edges):
  """
  For now:
  V - a set of vertices in the graph
  edges - an adjacency matrix (dict of lists)
  """
  Vt = V
  #clusters = set()
  clusters = []
  while len(Vt) != 0:
    p = random.choice(list(Vt))
    C = set()
    C.add(p)
    for v in edges[p]:
      C.add(v)
    Vt = Vt.difference(C)
    clusters.append(C)

  return clusters


V = {1, 2, 3, 4}
edges = {1: [2, 4], 2: [1, 4], 3:[], 4:[1, 2]}

print(ailon(V, edges))