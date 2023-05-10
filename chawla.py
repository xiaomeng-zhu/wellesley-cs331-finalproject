import random
from evaluation import import_graph
from ChawlaLPSolver import get_LP_solution

def chawla(G):
  """
  Input: a decision matrix G
  Output: clusters result of Chawla et. al. algorithm
  """
  active_vertices = list(range(len(G)))
  lp_sol = get_LP_solution(len(G))
  clusters = [] # list of sets

  while len(active_vertices) > 0:
    v = random.choice(active_vertices) # choose a random vertex from the set of vertices
    s = set()
    active_vertices.remove(v)
    for vertex in active_vertices:
      edge_val = G[v][vertex]
      if edge_val == 1:
        x_uv = lp_sol[v][vertex]
        p_uv = positive_function(x_uv)
      if edge_val == 0:
        x_uv = lp_sol[v][vertex]
        p_uv = negative_function(x_uv)
      p_uv = 1 - p_uv
      prob = random.uniform(0, 1)
      if prob < p_uv:
        s.add(vertex)
        active_vertices.remove(vertex)
    s.add(v)
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
G = import_graph("data/4-complete-1.csv")
clus = chawla(G)
print(clus)