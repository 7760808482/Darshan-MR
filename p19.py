class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
root = Node(10)
root.left = Node(20)
root.right = Node(30)
print("Inorder Traversal:")
inorder(root)
