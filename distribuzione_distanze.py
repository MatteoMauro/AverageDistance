from graph import GraphUndirected
from draw_tree import draw_tree
from BFS import bfs

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
[tree, count_edges] = bfs(V[0], graph)
draw_tree(tree, 'BFS')

average_distance = count_edges/(len(V)*(len(V)-1))
print("Number of edges: " + str(count_edges))
print("Average distance: " + str(average_distance))