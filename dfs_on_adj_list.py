def walk(graph, curr, needle, seen, path):
    

    if seen[curr]:
        return False
    
    seen[curr] = True
    # Pre-
    path.append(curr)
    if curr == needle:
        return True

    adj_list = graph[curr]
    for edge in adj_list:
        if walk(graph, edge.to, needle, seen, path):
            return True

    # Post
    path.pop()
    return False

def dfs(graph, source, needle):
    seen = [False]*len(graph)
    path = []

    walk(graph, source, needle, seen, path)

    if len(path) == 0:
        return None
    
    return path