class TreeNode:

    def __init__(self, nama):

        self.nama = nama

        self.child1 = None
        self.child2 = None


def tampil_tree(node, level=0):

    if node is not None:

        print("  " * level + node.nama)

        tampil_tree(node.child1, level + 1)

        tampil_tree(node.child2, level + 1)