from bansal import get_all_edges
import random
import numpy

def generate_random_decision_matrix(n):
    """
    Input: The number of vertices in a graph
    Output: A randomly generated symmetric decision matrix
    """
    G = [[] for i in range(n)]
    # print(G)
    for i in range(n):
        for j in range(n):
            # print("ij", i, j)
            if i == j:
                G[i].append(1)
            elif i < j:
                G[i].append(random.choice([0,1]))
            else:
                # print(G)
                G[i].append(G[j][i])
    for row in G:
        print(row)
    return G
                
def generate_dataset(min_vertex, max_vertex, graph_per_size):
    """
    Input: 
    min_vertex - the minimum number of vertices in a generated graph
    max_vertex - the maximum number of vertices in a generated graph
    graph_per_size - how many randomly generated graph per size
    Output: csv files containing generated graphs
    """
    for i in range(min_vertex, max_vertex+1):
        for j in range(graph_per_size):
            G = generate_random_decision_matrix(i)
            numpy.savetxt("{}-complete-{}.csv".format(i, j), G, delimiter=",")

    
if __name__ == "__main__":
    generate_random_decision_matrix(5)
    generate_dataset(3,10,3)
