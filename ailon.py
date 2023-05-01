import random

def ailon(V, edges):
  """
  For now:
  V - a set of vertices in the graph
  edges - an adjacency matrix (dict of lists)
  """
  Vt = V
  #t = 1
  clusters = set()
  while len(Vt) != 0:
    p = random.choice(Vt)
    C = set()
    C.add(p)
    for v in edges[p]:
      C.add(v)
    Vt = Vt.difference(C)
    clusters.add(C)

  return clusters
