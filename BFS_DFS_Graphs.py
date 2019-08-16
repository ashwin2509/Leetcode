graph = {
0: [(3, 8), (1, 4), (2, 5)],
1: [(2, -3)],
2: [(4, 4)],
3: [(4, 2)],
4: [(3, 1)]
}

def bfs(graph, src):
    q = [src]
    res = []
    visited = set()
    while q:
        node = q.pop(0)
        res.append(node)
        visited.add(node)
        for nei in graph[node]:
            if nei[0] not in visited:
                visited.add(nei[0])
                q.append(nei[0])
    return res



def dfs(graph, src):
    visited = set()
    res = []
    stack = [src]
    while stack:
        node = stack.pop()
        res.append(node)
        for nei in graph[node]:
            if nei[0] not in visited:
                visited.add(node)

                stack.append(nei[0])
    return res


def dfsRecursive(graph, src):
    visited = set()
    res = []
    dfsUtil(graph, src, visited, res)
    return res


def dfsUtil(graph, node, visited, res):
    visited.add(node)
    res.append(node)

    for nei in graph[node]:
        if nei[0] not in visited:
            dfsUtil(graph, nei[0], visited, res)






print(bfs(graph, 0))
print(dfs(graph, 0))
print(dfsRecursive(graph, 0))
