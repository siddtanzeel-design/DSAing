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

def inorder(root, result):
    if root is None:
        return

    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)

def kthSmallest(root, k):
    result = []

    inorder(root, result)
    return result[k-1]

arr = list(map(int, input("Enter values: ").split()))
root = None

for i in arr:
    root = insert(root, i)

k = int(input("Enter target element: "))

print("Kth smallest element: ", kthSmallest(root, k))
