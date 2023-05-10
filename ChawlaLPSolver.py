from scipy.optimize import linprog
import numpy as np
import itertools

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


def get_LP_solution(length):
    print("----------")

    #define vertices
    vertices = [i for i in range(0, length)]
    edges = [] #this is var_list
    num_vertices = len(vertices)
    for i in range(0, num_vertices):
        for i in range (0, i):
            edges.append(1)
    cost = [1 for each in edges]
    A_ineq = []
    B_ineq = []

    mapping = create_mapping(len(vertices))
    mapping = mapping.astype(int)
    #make A_ineq
    #run for each triangle
    for triplet in itertools.combinations(vertices, 3):
        A_ineq_row1 = [0] * len(edges)
        A_ineq_row1[mapping[triplet[0]][triplet[1]]] = -1
        A_ineq_row1[mapping[triplet[1]][triplet[2]]] = -1
        A_ineq_row1[mapping[triplet[0]][triplet[2]]] = 1
        A_ineq.append(A_ineq_row1)
        B_ineq_row1 = [0]
        B_ineq.append(B_ineq_row1)

        A_ineq_row2 = [0] * len(edges)
        A_ineq_row2[mapping[triplet[0]][triplet[1]]] = -1
        A_ineq_row2[mapping[triplet[1]][triplet[2]]] = 1
        A_ineq_row2[mapping[triplet[0]][triplet[2]]] = -1
        A_ineq.append(A_ineq_row2)
        B_ineq_row2 = [0]
        B_ineq.append(B_ineq_row2)

        A_ineq_row3 = [0] * len(edges)
        A_ineq_row3[mapping[triplet[0]][triplet[1]]] = 1
        A_ineq_row3[mapping[triplet[1]][triplet[2]]] = -1
        A_ineq_row3[mapping[triplet[0]][triplet[2]]] = -1
        A_ineq.append(A_ineq_row3)
        B_ineq_row3 = [0]
        B_ineq.append(B_ineq_row3)


    for pair in itertools.combinations(vertices, 2):
        A_ineq_row1 = [0] * len(edges)
        A_ineq_row1[mapping[pair[0]][pair[1]]] = 1
        A_ineq.append(A_ineq_row1)
        B_ineq_row1 = [1]
        B_ineq.append(B_ineq_row1)

        A_ineq_row2 = [0] * len(edges)
        A_ineq_row2[mapping[pair[0]][pair[1]]] = -1
        A_ineq.append(A_ineq_row2)
        B_ineq_row2 = [0]
        B_ineq.append(B_ineq_row2)


    print('WITHOUT BOUNDS')
    # # pass these matrices to linprog, use the method 'interior-point'. '_ub' implies the upper-bound or
    # # inequality matrices and '_eq' imply the equality matrices
    res_no_bounds = linprog(cost, A_ub=A_ineq, b_ub=B_ineq, method='interior-point')
    print(res_no_bounds['x'])
    print(LPsolution_to_matrix(len(vertices), res_no_bounds['x']))
    return LPsolution_to_matrix(len(vertices), res_no_bounds['x'])

def create_mapping(int):
    matrix = np.empty([int, int]) 
    count = 0
    for i in range(0, int):
        matrix[i][i] = -1
        j = i+1
        for ind in range(j, int):
            matrix[i][ind] = count
            matrix[ind][i] = count
            count += 1
    return matrix

def LPsolution_to_matrix(int, soln):
    matrix = np.empty([int, int])
    index = 0 
    for i in range(0, int):
        matrix[i][i] = 0
        j = i+1
        for ind in range(j, int):
            matrix[i][ind] = soln[index]
            matrix[ind][i] = soln[index]
            index += 1
    return matrix

#TESTING
#get_LP_solution("data/4-complete-2.csv")
#create_mapping(10)
#get_LP_solution(4)