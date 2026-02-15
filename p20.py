class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = Node(10)
root.left = Node(5)
root.right = Node(15)
print("Root:", root.data)
print("Left Child:", root.left.data)
print("Right Child:", root.right.data)
