from collections import deque
# returns path to needle
def bfs(graph, source, needle):
    prev = [-1]*len(graph)
    seen = [False]*len(graph)

    seen[source] = True
    q = deque([source])

    while q:
        curr = q.popleft()
        if curr == needle:
            break
        
        adjs = graph[curr]
        for i in range(len(adjs)):
            if adjs[i] == 0:
                continue
            if seen[i]:
                continue

            seen[i] = True
            prev[i] = curr
            q.append(i)
        
        seen[curr] = True
    
    curr = needle
    path = []

    if prev[needle] == -1:
        return None

    while prev[curr] != -1:
        path.append(curr)
        curr = prev[curr]
    if path:
        return [source] + path[::-1]