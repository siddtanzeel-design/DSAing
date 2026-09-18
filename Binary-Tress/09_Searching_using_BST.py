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

    if data > root.data:
        root.right = insert(root.right, data)

    return root


def search(root, target):
    if root is None:
        return False

    if target == root.data:
        return True

    if target < root.data:
        return search(root.left, target)
    else:
        return search(root.right, target)


arr = list(map(int, input("Enter values: ").split()))

root = None

for value in arr:
    root = insert(root, value)

target = int(input("Enter Target: "))

if search(root, target):
    print("True")
else:
    print("False")
