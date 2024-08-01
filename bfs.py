class BinaryNode:
    def __init__(self, val, left=None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def bfs(root, needle):
    if not root:
        return False
    queue = [root]

    while queue:
        curr = queue.pop(0)

        if curr.val == needle:
            return False

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    
    return False