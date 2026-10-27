class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)

    if root.left is None:
        root.left = Node(value)
    elif root.right is None:
        root.right = Node(value)
    else:
        insert(root.left, value)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = None
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 30)

print("Binary Tree using Linked List:")
inorder(root)
