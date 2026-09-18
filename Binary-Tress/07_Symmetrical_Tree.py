class node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def isSymmetric(root):
    def mirror(p, q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return mirror(p.left, q.right) and mirror(p.right, q.left)

    return mirror(root.left, root.right)

root = node(1)

root.left = node(2)
root.left.left = node(4)
root.left.right = node(5)

root.right = node(2)
root.right.left = node(5)
root.right.right = node(4)

print("Is the Tree Symmetrical:", isSymmetric(root))
