class BinaryNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search(current:BinaryNode|None, needle):
    if not current:
        return False
    
    if current.val == needle:
        return True
    
    if current.val < needle:
        return search(current.right, needle)
    else:
        return search(current.left, needle)

def dfs(head:BinaryNode, needle):
    return search(head, needle)
