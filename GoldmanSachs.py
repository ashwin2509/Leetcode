graph = {
'A': ['B', 'G', 'K'],
'B': ['A', 'C'],
'C': ['B', 'D'],
'D': ['C', 'F', 'E'],
'E': ['D', 'H'],
'F': ['G', 'D'],
'G': ['A', 'F'],
'H': ['I', 'E'],
'I': ['H', 'J'],
'J': ['K', 'I'],
'K': ['A', 'J']
}

def shortestPath(graph, src, dest):
    q = [(src, 1, [src])]
    visited = set()
    visited.add(src)
    minDest = float('inf')
    res = None
    while q:
        node, dist, path = q.pop(0)
        for nei in graph[node]:
            if nei not in visited:
                visited.add(node)
                if nei == dest:
                    if dist+1<=minDest:
                        minDest = dist+1
                        res = (nei, dist+1, path+[nei])
                else:
                    q.append((nei, dist+1, path+[nei]))
    return "->".join(res[2])



def bfs(graph, f, t):
    q = [(f, 0, [f])]
    seen = set()
    minDist = float('inf')
    res = None
    while q:
        node, dist, path = q.pop(0)
        if node not in seen:
            seen.add(node)
            if node == t:
                if dist < minDist:
                    minDist = dist
                    res = path
            for nei in graph[node]:
                if nei[0] in seen: continue
                q.append((nei[0], 1+dist, path+[nei[0]]))
    return minDist, "->".join(res)


print(bfs(graph, 'A', 'H'))
print(shortestPath(graph, 'A', 'H'))
