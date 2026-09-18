class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)

    return root

def findMin(root):
    if root.left is None:
        return root.val

    return findMin(root.left)

def findMax(root):
    if root.right is None:
        return root.val

    return findMax(root.right)

arr = list(map(int, input("Enter Values: ").split()))
root = None

for value in arr:
    root = insert(root, value)

print("Maximum: ", findMax(root))
print("Minimum: ", findMin(root))
