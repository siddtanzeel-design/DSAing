class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    return root

def inorder(root, result):
    if root is None:
        return

    inorder(root.left, result)
    result.append(root.data)
    inorder(root.right, result)

arr = list(map(int, input("Enter values: ").split()))
root = None

for value in arr:
    root = insert(root, value)

result = []
inorder(root, result)
print(result)
