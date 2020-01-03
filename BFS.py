from TreeNode import TreeNode


def build_tree(source, predecessor):
    find_children = lambda vertex: predecessor[vertex] == source.name
    children = list(filter(find_children, predecessor.keys()))
    if children:
        for node in children:
            new_node = TreeNode(node)
            source.add_node(new_node)
            build_tree(new_node, predecessor)


def bfs(source, graph):
    count_edges = 0
    V = graph.get_nodes()
    visited = {node: False for node in V}
    predecessor = {node: None for node in V}

    visited[source] = True
    queue = [source]
    while queue:
        current_node = queue.pop(0)
        for v in graph.get_neighbors(current_node):
            count_edges += 1
            if not visited[v]:
                queue.append(v)
                predecessor[v] = current_node
                visited[v] = True

    tree_node_root = TreeNode(source)
    build_tree(tree_node_root, predecessor)
    return tree_node_root, predecessor



