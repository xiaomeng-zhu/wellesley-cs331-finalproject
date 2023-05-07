from bansal import get_all_edges, bansal_naive
def in_same_cluster(u,v,C):
    """
    Given the indices of vertex u and v and a list of sets C, check if u is in the same cluster as
    as v according to the clustering provided by C
    """
    for cluster in C:
        if u in cluster and v in cluster:
            return True
    return False

def calculate_mistakes(G, C):
    """
    Given a clustering assignment C and a graph G, calculate the number of mistakes
    G: a list of lists containing decisions
            0 1 2
    e.g. 0 [[1,1,0],
         1 [1,1,1],
         2 [0,1,1]] is a decision matrix where only (1,3) the only negative edge, all other edges are positive (indexing from 1
    C: a list of sets (C_0, C_1, C_2, ....)
    e.g. [(1,2),(3)] meaning that vertex 1 and vertex 2 are in the same cluster, and vertex 3 is in its singleton cluster
    """
    total_mistakes = 0

    all_edges = get_all_edges(len(G))
    for u,v in all_edges:
        if G[u][v] == 0 and in_same_cluster(u,v,C): # u and v should not be in the same cluster
            total_mistakes += 1
        elif G[u][v] == 1 and (not in_same_cluster(u,v,C)):
            total_mistakes += 1
    
    correctness_index = total_mistakes/len(all_edges)
    return correctness_index

if __name__ == "__main__":
    simple_graph = [[1,1,0],
                    [1,1,1],
                    [0,1,1]]
    clusters = bansal_naive(simple_graph)
    print(clusters)
    print(calculate_mistakes(simple_graph, clusters))


  
