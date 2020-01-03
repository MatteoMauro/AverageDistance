from graph import GraphUndirected
from draw_tree import draw_tree
from BFS import bfs
from math import log, ceil
import random


def count_distance(row_dist, predecessor, V):
    for node in V:
        level = 0
        current = node
        while predecessor[current] is not None:
            level += 1
            current = predecessor[current]
        row_dist[node] = level


def print_matrix(matrix):
    for key in matrix_dist.keys():
        print(key, end=' -> ')
        print(matrix_dist[key])


def sum_all_distances(matrix_dist):
    total = 0
    for node in matrix_dist.keys():
        for v in matrix_dist[node]:
            total += matrix_dist[node][v]
    return total


graph = GraphUndirected()
edges = [["a", "b"],
         ["b", "c"],
         ["c", "d"],
         ["d", "a"],
         ["a", "c"],
         ["b", "d"]]
for e in edges:
    graph.add_edge(e[0], e[1])
V = graph.get_nodes()

# +++ COMPUTE EXACT AVERAGE DISTANCE +++
# 1. compute all pair vertices distances
matrix_dist = {node: dict() for node in V}
for k in range(0, len(V)):
    node = V[k]
    [tree, predecessor] = bfs(node, graph)
    #draw_tree(tree, './grafiPDF/BFS_' + str(node))
    count_distance(matrix_dist[node], predecessor, V)
print_matrix(matrix_dist)
# 2. compute average distance
average_distance = sum_all_distances(matrix_dist)/(len(V)*(len(V)-1))
print("\nAverage distance: " + str(average_distance))



# +++ COMPUTE ESTIMATE AVERAGE DISTANCE +++
# 1. select random sample
eps = 1
K = ceil(log(len(V))/(eps ^ 2))
U = random.sample(V, K)
# 2. compute all pair vertices distances for U
matrix_dist = {node: dict() for node in U}
for i in range(0, K):
    node = U[i]
    [tree, predecessor] = bfs(node, graph)
    count_distance(matrix_dist[node], predecessor, V)
print_matrix(matrix_dist)
# 3. estimate average distance
average_distance = sum_all_distances(matrix_dist)/(len(V)*(len(V)-1))
print("\nEstimated Average distance with " + str(K) + " nodes: " + str(average_distance))