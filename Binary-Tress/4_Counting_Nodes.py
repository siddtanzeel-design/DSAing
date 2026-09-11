class node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def counting_nodes(root):
    if root is None:
        return 0

    return 1 + counting_nodes(root.right) + counting_nodes(root.left)

root = node(1)

root.left = node(2)
root.left.left = node(4)
root.left.right = node(5)

root.right = node(3)
root.right.left = node(6)
root.right.right = node(7)

print("Total Nodes:", counting_nodes(root))
