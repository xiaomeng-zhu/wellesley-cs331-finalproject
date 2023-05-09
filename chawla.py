import random
from evaluation import import_graph

def chawla(G, lp_sol):
  """
  Input: a decision matrix G, LP solution lp_sol
  Output: clusters result of Chawla et. al. algorithm
  """
  active_vertices = list(range(len(G)))
  clusters = [] # list of sets

  while len(active_vertices) > 0:
    v = random.choice(active_vertices) # choose a random vertex from the set of vertices
    print("the pivot vertex is")
    print(v)
    s = set()
    print(G)
    for vertex in active_vertices:
      print(vertex)
      uv = G[v][vertex]
      if uv == 1:
        x_uv = lp_sol[v][vertex]
        p_uv = positive_function(x_uv)
      if uv == 0:
        x_uv = lp_sol[v][vertex]
        p_uv = negative_function(x_uv)
      p_uv = 1 - p_uv
      prob = random.uniform(0, 1)
      if prob < p_uv:
        s.add(vertex)
        active_vertices.remove(vertex)
    s.add(v)
    active_vertices.remove(v)
    clusters.append(s)

  return clusters

def positive_function(x):
  if x < 0.19:
    return 0
  if x > 0.5094:
    return 1

def negative_function(x):
  return x

#TESTING
G = import_graph("data/4-complete-2.csv")
lp_sol = [[1, 0, 1, 1], [0, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]
clus = chawla(G, lp_sol)
print(clus)