class BinaryNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def walk(node, path:list):
    if not node:
        return
    walk(node.left, path)
    path.append(node.val)
    walk(node.right, path)

def inorder_travelsal(root):
    path = []
    walk(root, path)
    return path