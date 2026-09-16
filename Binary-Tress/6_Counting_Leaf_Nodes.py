class node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def countLeaf(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return countLeaf(root.left) + countLeaf(root.right)

root = node(1)

root.left = node(2)
root.left.left = node(4)
root.left.right = node(5)

root.right = node(3)
root.right.left = node(6)
root.right.right = node(7)

print("Number of leaf Nodes in this Tree are:",countLeaf(root))
