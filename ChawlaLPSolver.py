from scipy.optimize import linprog
import numpy as np
from evaluation import import_graph


d = [[1,1,0],
        [1,1,1],
        [0,1,1]]

# This is the function you should edit.
def get_LP_solution(file_name):
    print("----------")

    #imports graph
    data_matrix = import_graph(file_name)

    #define vertices
    vertices = [i for i in range(0, len(data_matrix[0]))]
    edges = [i for i in range(0, len(data_matrix[0]) * len(data_matrix[0]))] #this is var_list
    cost = [1 for each in edges]
    A_ineq = []
    B_ineq = []
    print(vertices)
    #make A_ineq
    #run for each triangle
    for i, j, k in vertices:
        A_ineq_row = []
        # add x_uv + x_vw - x_uw > 0

        var_edges = []
        #var_list is each edge
        var_list = [data_matrix[i][j], data_matrix[i][k], data_matrix[j][k]]

       

       



    #define num_edges
    #num_edges = sum(row.len() for row in data_matrix)


    # # X matrix and Cost function
    # edges = []
    # c = []
    # for i in range(0, num_edges):
    #     edges.append(str(i))
    #     c.append(1)

    # # Inequality equations
    # A_ineq = []
    # B_ineq = []


    # # add x_uv + x_vw - x_uw > 0
    # for edge in in_graph:
    #     mat = [0] * num_edges
    #     #mat = [0 for i in range(num_vertices)]
    #     mat[edge[0]] = -1.
    #     mat[edge[1]] = -1.
    #     mat[edge[2]] = 1.
    #     A_ineq.append(mat)
    #     B_ineq.append(0.)
    # #add x_u > 0
    # for i in range(0, num_vertices):
    #     new_mat = [0] * num_vertices
    #     new_mat[i] = -1.
    #     A_ineq.append(new_mat)
    #     B_ineq.append(0.)


    # print('WITHOUT BOUNDS')
    # # pass these matrices to linprog, use the method 'interior-point'. '_ub' implies the upper-bound or
    # # inequality matrices and '_eq' imply the equality matrices
    # res_no_bounds = linprog(c, A_ub=A_ineq, b_ub=B_ineq, method='revised simplex')
    # print(res_no_bounds)

    # #rounding algorithm
    # min_vc = set()
    # for i in range(len(res_no_bounds['x'])):
    #     if res_no_bounds['x'][i] < 0.499999: 
    #     #if res_no_bounds['x'][i] < 0.5:
    #         res_no_bounds['x'][i] = 0
    #     else:
    #         res_no_bounds['x'][i] = 1

    # for i in range(len(res_no_bounds['x'])):
    #     if res_no_bounds['x'][i] == 1:
    #         min_vc.add(i)

    # # Checks if min_vc is a valid vertex cover and if so, prints it
    # # and its size.
    # # You may want to comment this out if you're working on getting
    # # the LP solution and haven't implemented the rounding step yet.
    # is_valid_vc(in_graph, min_vc)
    # return res_no_bounds['x']


#TESTING
get_LP_solution("data/4-complete-2.csv")