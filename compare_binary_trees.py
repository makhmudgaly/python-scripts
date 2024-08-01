class BinaryNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right

def compare(a, b):
    if not a and not b:
        return True
    
    if not a or not b:
        return False
    
    if a.val != b.val:
        return False
    
    return compare(a.left, b.left) and compare(a.right, b.right)