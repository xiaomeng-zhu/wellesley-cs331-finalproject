import os
from bansal import get_all_edges, bansal_naive, bansal_algorithm_cautious
from ailon import ailon
from chawla import chawla
import csv

# import all functions here
FUNCS = {
    "BansalNaive": bansal_naive,
    "BansalAlgorithmCautious": bansal_algorithm_cautious,
    "KwikCluster": ailon,
    "Chawla": chawla
}


def import_graph(file_name):
    """
    Input: the relative filepath of the csv
    Output: the graph stored in a list of lists
    """
    graph = []
    with open(file_name, "r") as f:
        for row in f:
            graph.append([int(float(i)) for i in row.strip().split(",")])
    return graph

def is_valid_decision_matrix(G):
    """
    Given a graph G, check if it is valid decision matrix (condition 1 and 2 must all be satisfied)
    condition 1: the diagonal line from top left to bottom right must all be ones
    condition 2: the matrix must be symmetric based on the diagonal lines in condition 1
    """
    num_v = len(G)

    # check condition 1
    for i in range(num_v):
        if G[i][i] != 1: # if numbers on the diagonal line is not 1
            return False
    
    # check condition 2
    all_edges = get_all_edges(len(G))
    for u,v in all_edges:
        if G[u][v] != G[v][u]: # if it is not symmetric
            return False
    return True

def is_in_same_cluster(u,v,C):
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
        if G[u][v] == 0 and is_in_same_cluster(u,v,C): # u and v should not be in the same cluster
            total_mistakes += 1
        elif G[u][v] == 1 and (not is_in_same_cluster(u,v,C)):
            total_mistakes += 1
    
    correctness_index = total_mistakes/len(all_edges)
    return correctness_index

def calculate_mistakes_under_alg(func_name, G):
    """
    Given a function name and a Graph, calculate its correctness index
    """
    clusters = func_name(G)
    # print(clusters)
    correctness_index = calculate_mistakes(G, clusters)
    return clusters, correctness_index

def calculate_mistakes_under_alg_for_all(dir):
    """
    Given a function name, calculate its correctness index for all graphs in data folder, 
    and output a csv summarizing the results
    """
    all_res = []

    # generate all data entries
    for filename in os.listdir(dir):
        if filename.endswith(".csv"):
            
            file_path = os.path.join(dir, filename)
            G = import_graph(file_path)

            if is_valid_decision_matrix(G): # only proceed if G is a valid decision matrix
                for func_name in FUNCS:
                    func = FUNCS[func_name] # store the function in the func variable
                    entry = {"filename": filename}
                    entry["func_name"] = func_name
                    clusters, index = calculate_mistakes_under_alg(func, G)
                    entry["clusters"] = clusters
                    entry["index"] = index

                    all_res.append(entry)
            else: # print alert message and move onto the next file
                print("The graph in", file_path, "is not a valid decision matrix")

    # output to csv
    #with open('res.csv', 'w', newline='') as output_file:
    with open('res.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, all_res[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(all_res)




if __name__ == "__main__":
    dir = "data"
    calculate_mistakes_under_alg_for_all(dir)

  
