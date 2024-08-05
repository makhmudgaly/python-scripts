def hasUnvisited(seen, dists):
    return any(not s and dists[idx] < float("inf") for idx, s in enumerate(seen))

def getLowestUnvisited(seen, dists) -> int:
    idx = -1
    lowestDistance = float("inf")

    for i in range(len(seen)):
        if seen[i]: continue

        if lowestDistance > dists[i]:
            lowestDistance = dists[i]
            idx = i
    return idx

def dijkstra(source, sink, arr):
    seen = [False]*len(arr)
    prev = [-1]*len(arr)
    dists = [float("inf")]*len(arr)

    while hasUnvisited(seen, dists):
        curr = getLowestUnvisited(seen, dists)
        seen[curr] = True

        adjs = arr[curr]
        for edge in adjs:
            if seen[edge.to]: continue

            dist = dists[curr] + edge.weight
            if dist < dists[edge.to]:
                dists[edge.to] = dist
                prev[edge.to] = curr
    

    out = []
    curr = sink

    while prev[curr] != -1:
        out.append(curr)
        curr = prev[curr]
    out.append(source)
    
    return out[::-1]
