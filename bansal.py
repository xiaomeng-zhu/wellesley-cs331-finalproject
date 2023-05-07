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

def delta_good(v, C, n):
    pass

def bansal_algorithm_cautious(graph):
    pass

if __name__ == "__main__":
    simple_graph = [[1,0,0],
                    [0,1,1],
                    [0,1,1]]
    res = bansal_naive(simple_graph)
    print(res)