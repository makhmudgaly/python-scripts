class BinaryNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def walk(node, path:list):
    if not node:
        return
    
    walk(node.left, path)
    walk(node.right, path)
    path.append(node.val)

def postorder_travelsal(root):
    path = []
    walk(root, path)
    return path