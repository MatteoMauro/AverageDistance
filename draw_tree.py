from graphviz import Digraph
import copy


def draw_tree(tree_node_root, name_pdf):
    copy_tree_node = copy.deepcopy(tree_node_root)
    g = Digraph()
    g.node(copy_tree_node.name)
    queue = [copy_tree_node]
    while queue:
        node = queue.pop(0)
        for child in node.list_of_nodes:
            queue.append(child)
            g.node(child.name)
            g.edge(node.name, child.name, minlen='2', dir="forward")

    g.view(name_pdf)
