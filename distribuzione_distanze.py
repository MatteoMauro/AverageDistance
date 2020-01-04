from graph import GraphUndirected
from draw_tree import draw_tree
from BFS import bfs
from math import log, ceil
import random
import operator
from graphviz import Graph


def draw_graph(graph, edges):
    g = Graph()
    for node in graph.get_nodes():
        g.node(node)
    for edge in edges:
        g.edge(edge[0], edge[1], minlen='2')
    g.view("./grafiPDF/grafo")


def count_distance(row_dist, predecessor, V):
    for node in V:
        level = 0
        current = node
        while predecessor[current] is not None:
            level += 1
            current = predecessor[current]
        row_dist[node] = level


def print_matrix(matrix):
    print("MATRIX: ADJACENCY LISTS")
    for key in sorted(matrix_dist.keys()):
        print(key, end=' -> ')
        print(matrix_dist[key])


def sum_all_distances(matrix_dist):
    total = 0
    for node in matrix_dist.keys():
        for v in matrix_dist[node]:
            total += matrix_dist[node][v]
    return total


def compute_freq_distr(matrix_dist, h, K, V):
    total = 0
    for node in matrix_dist.keys():
        for v in matrix_dist[node]:
            if matrix_dist[node][v] == h:
                total += 1
    return total/(K*V-1)


graph = GraphUndirected()
#edges = [["a", "b"], ["b", "c"], ["c", "d"], ["d", "a"], ["a", "c"], ["b", "d"]]
edges = open("random_edges.txt").readlines()
for i in range(0, len(edges)):
    edges[i] = edges[i].replace('\n', '').split(' ', 1)

for e in edges:
    graph.add_edge(e[0], e[1])
draw_graph(graph, edges)
V = graph.get_nodes()

# +++ COMPUTE EXACT AVERAGE DISTANCE +++
# 1. compute all pair vertices distances
matrix_dist = {node: dict() for node in V}
diameter = 0
for k in range(0, len(V)):
    node = V[k]
    [tree, predecessor] = bfs(node, graph)
    #draw_tree(tree, './grafiPDF/BFS_' + str(node))
    count_distance(matrix_dist[node], predecessor, V)
    # compute diameter so far
    d = max(matrix_dist[node].items(), key=operator.itemgetter(1))[1]
    if diameter < d:
        diameter = d
print_matrix(matrix_dist)
print('diameter = ' + str(diameter))
# 2. compute average distance
average_distance = sum_all_distances(matrix_dist)/(len(V)*(len(V)-1))
print("Average distance: " + str(average_distance), end='\n\n')



# +++ COMPUTE ESTIMATE AVERAGE DISTANCE +++
# 1. select random sample
print("CLASSICAL SAMPLING")
eps = 1
K = ceil(log(len(V))/(eps ** 2))
U = random.sample(V, K)
# 2. compute all pair vertices distances for U
matrix_dist = {node: dict() for node in U}
sample_diameter = 0
for i in range(0, K):
    node = U[i]
    [tree, predecessor] = bfs(node, graph)
    count_distance(matrix_dist[node], predecessor, V)
    # compute diameter so far
    d = max(matrix_dist[node].items(), key=operator.itemgetter(1))[1]
    if sample_diameter < d:
        sample_diameter = d
print_matrix(matrix_dist)
print('sample diameter = ' + str(sample_diameter))
# 3. estimate average distance
N = {}
average_distance = 0
for h in range(1, sample_diameter):
    N[h] = compute_freq_distr(matrix_dist, h, K, len(V))
for h in range(1, sample_diameter):
    average_distance += h*N[h]
print("Estimated Average distance with " + str(K) + " nodes: " + str(average_distance))