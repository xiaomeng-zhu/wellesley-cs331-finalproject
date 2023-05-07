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
    Output: a list of all the positive vertices of v including v itself
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
    note: the set of vertices V in the formula can be calculated based on G
    """
    
    cluster_set = set(C)
    positive_neighbors = get_all_positive_neighbors(G,v)
    positive_neighbors_set = set(positive_neighbors)

    quantity1 = len(positive_neighbors_set.intersection(cluster_set))
    quantity2 = (1-delta)*len(C)

    # check if it satisfies the first constraint presented on Bansal et al. p.94
    if quantity1 < quantity2:
        return False
    
    all_vertex_set = set(range(len(G)))
    quantity3 = len(positive_neighbors_set.intersection(all_vertex_set-cluster_set))
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
    vertices = list(range(len(G)))
    clusters = [] # list of sets
    continue_loop = True

    while continue_loop:
        v = random.choice(vertices) # choose a random vertex from the set of vertices
        print(v)
        Av = set(get_all_positive_neighbors(G, v))
        print(Av)

        # vertex removal step
        vertices_to_remove = []

        # if x is 3-delta bad w.r.t. A(v), A(v) = A(v) \ {x}
        for x in Av: 
            if not delta_good(3, v, Av, G):
                vertices_to_remove.append(x)

        print(vertices_to_remove)

        Av = Av - set(vertices_to_remove)

        # vertex addition step
        vertices_to_add = []

        # if x is 7-delta good w.r.t. A(v), A(v) = A(v) union set of xs
        for x in vertices:
            if delta_good(7, v, Av, G):
                vertices_to_add.append(x)
        Av = Av.union(set(vertices_to_add))
        print(vertices_to_add)

        if Av == []:
            continue_loop = False
            # if A(v) is empty, output the remaining vertices as singleton nodes
            for v in vertices:
                clusters.append(set(v)) # singleton
        else:
            clusters.append(Av) # a list of sets
            vertices = list(set(vertices) - Av) # delete A(v) from the set of vertices

            # if no vertices are left, stop looping
            if vertices == []: 
                continue_loop = False

    return clusters
            
def bansal_algorithm_divide_choose(G):
    pass



if __name__ == "__main__":
    simple_graph = [[1,1,1],
                    [1,1,0],
                    [1,0,1]]
    # res = bansal_naive(simple_graph)
    res = bansal_algorithm_cautious(simple_graph)
    print(res)