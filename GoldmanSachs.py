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
                    visited.add(nei)
                    q.append((nei, dist+1, path+[nei]))
    return "->".join(res[2])

print(shortestPath(graph, 'A', 'H'))
