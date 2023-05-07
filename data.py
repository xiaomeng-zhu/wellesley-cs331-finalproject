from bansal import get_all_edges

def distance_to_decision(G):
    """
    Input: A complete distance matrix G
    Output: the corresponding decision matrix G' where edges whose length 
    above average are rounded up and rounded down otherwise
    """
    all_edges = get_all_edges(len(G))
    sum_edges = 0
    for u,v in all_edges:
        dist = G[u][v]
        sum_edges += dist
    average_distance = sum_edges/len(all_edges)

    D = []
    for row in G:
        D_row = []
        for item in row:
            if item >= average_distance:
                D_row.append(1)
            else:
                D_row.append(0)
        D.append(D_row)

    return D
    
if __name__ == "__main__":
    simple_dist_matrix = [[0, 1, 3],
                          [1, 0, 9],
                          [3, 9, 0]]
    resulting_decision_matrix = distance_to_decision(simple_dist_matrix)
    print(resulting_decision_matrix)
