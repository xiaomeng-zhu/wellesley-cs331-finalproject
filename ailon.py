import random

def ailon(G):
  """
  Returns a list of clusters given a complete graph G
  G - a complete graph matrix
  """
  Vt = set([i for i in range(len(G))])
  clusters = []
  while len(Vt) != 0:
    p = random.choice(list(Vt))
    C = set([p])
    edges = G[p]
    for v in range(len(edges)):
      if edges[v] == 1:
        C.add(v)
    Vt = Vt.difference(C)
    clusters.append(C)

  return clusters

if __name__ == "__main__":
  #G = [[1,1,0],[1,1,0],[0,0,1]]
  #G = [[1,1,0,0], [1,1,0,0], [0,0,1,1], [0,0,1,1]]
  G = [[1,1,1,0], [1,1,1,0], [1,1,1,0], [0,0,0,1]]

  print(ailon(G))