class BinaryNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def walk(node, path:list):
    if not node:
        return
    # pre recursion
    path.append(node.val)
    # recursion
    walk(node.left, path)
    walk(node.right, path)
    # post recursion


def preorder_travelsal(root):
    path = []
    walk(root, path)
    return path