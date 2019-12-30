class TreeNode:

    def __init__(self, name):
        self.name = name
        self.list_of_nodes = []

    def set_name(self, name):
        self.name = name

    def add_node(self, node):
        self.list_of_nodes.append(node)

    def __str__(self):
        children = ''
        for n in self.list_of_nodes:
            children += n.name + ' '
        return self.name + ' ' + ' <' + children + '>'

