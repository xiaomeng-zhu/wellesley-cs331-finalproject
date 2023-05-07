import random

def get_all_edges(n):
    """
    Input: number of vertices in a complete graph
    Output: a list of all edges indicing from 0
    Example: With an input of 3, the function outputs [(0,1), (0,2), (1,2)]
    """
    all_edges = []
    for i in range(n):
       for j in range(n):
            if i < j:
               all_edges.append((i,j))
    return all_edges

def get_all_positive_neighbors(G,v):
    """
    Input: a decision matrix G and a vertex v
    Output: a list of all the positive vertices of v
    """
    positive_neighbors = []
    for idx, decision in enumerate(G[v]):
        if decision == 1:
            positive_neighbors.append(idx)
    return positive_neighbors


def bansal_naive(graph):
    """
    Input: a decision matrix of graph G
    Algorithm: If the number of positive edges is greater than the number of negative edges,
    return a cluster with every vertex; otherwise, return singleton sets of all vertices
    Output: return a set of sets (clusterings)
    """
    # Assuming all input graphs are complete graphs
    n = len(graph)
    all_edges = get_all_edges(n)
    
    num_pos = 0
    num_neg = 0
    
    for u,v in all_edges:
        if graph[u][v] == 0: # if it is a negative edge
            num_neg += 1 # increment the num_neg counter by 1
        else:
           num_pos += 1
           
    if num_pos >= num_neg:
        all_vertices = list(range(n))
        # print(all_vertices)
        return [set(all_vertices)]
    else:
        # print([[u] for u in list(range(n))])
        return [{u} for u in list(range(n))]

def delta_good(delta, v, C, G):
    """
    Given a vertex, cluster C, set of vertices V, check if v is delta-good
    note: set of vertices V can be calculated based on G
    """
    
    cluster_set = set(C)
    positive_neighbors = get_all_positive_neighbors(G,v)
    positive_neighbors_set = set(positive_neighbors)

    quantity1 = len(positive_neighbors_set.intersect(cluster_set))
    quantity2 = (1-delta)*len(C)

    # check if it satisfies the first constraint presented on Bansal et al. p.94
    if quantity1 < quantity2:
        return False
    
    all_vertex_set = set(range(len(G)))
    quantity3 = len(positive_neighbors_set.intersect(all_vertex_set-cluster_set))
    quantity4 = delta*len(C)

    # check if it satisfies the second constraint presented on Bansal et al. p.94
    if quantity3 > quantity4:
        return False
    
    return True
    

def bansal_algorithm_cautious(G):
    """
    Input: a decision matrix G
    Output: clusters under Algorithm Cautious in Bansal et al. p.97
    """
    random_start = random.choice(list(range(len(G))))
    Av = get_all_positive_neighbors(G, random_start)

    # vertex removal step
    vertices_to_remove = []
    for x in Av:
        if not delta_good(3, random_start, Av, G):
            vertices_to_remove.append(x)

    Av = list(set(Av) - set(vertices_to_remove))

    # vertex addition step
    vertices_to_add = []
    for x in len(G):
        if delta_good(7, random_start, Av, G):
            vertices_to_add.append(x)
    Av = list(set(Av) + set(vertices_to_add))
    

if __name__ == "__main__":
    simple_graph = [[1,0,0],
                    [0,1,1],
                    [0,1,1]]
    res = bansal_naive(simple_graph)
    print(res)