class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.next = None
        self.is_traversed = False

    def __str__(self):
        return "[ " + self.source + ", " + self.destination + ", " + str(self.is_traversed) + "]"


class GraphUndirected:

    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dest):
        if self.graph.get(src) is None:
            self.graph[src] = None
        if self.graph.get(dest) is None:
            self.graph[dest] = None

        edge = Edge(src, dest)
        edge.next = self.graph[src]
        self.graph.update({src: edge})
        edge = Edge(dest, src)
        edge.next = self.graph[dest]
        self.graph.update({dest: edge})

    def print_graph(self):
        for i in self.graph.keys():
            print("Adjacency list of vertex {}:\n[".format(i), end="")
            temp = self.graph.get(i)
            while temp:
                print(" -> (" + temp.destination + ") ", end="")
                temp = temp.next
            print("] \n")

    def get_nodes(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for i in self.graph.keys():
            temp = self.graph.get(i)
            while temp:
                edges.append(temp)
                temp = temp.next
        return edges

    def get_neighbors(self, node):
        neighbors = []
        temp = self.graph.get(node)
        while temp:
            neighbors.append(temp.destination)
            temp = temp.next
        # Remove duplications
        neighbors = list(dict.fromkeys(neighbors))
        neighbors.sort()
        return neighbors
