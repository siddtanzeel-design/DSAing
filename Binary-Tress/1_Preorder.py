class node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def preorder(node):
    if node is None:
        return

    print(node.value, end=" ")

    preorder(node.left)
    preorder(node.right)

root = node(1)

root.left = node(2)
root.left.left = node(4)
root.left.right = node(5)

root.right = node(3)
root.right.left = node(6)
root.right.right = node(7)

print("Preoder Traversal:")
preorder(root)
