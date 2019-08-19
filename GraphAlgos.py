# guw = {  #graph_unequal_weights
# 'A': [('B', 5), ('D', 9), ('E', 2)],
# 'B': [('A', 5), ('C',2)],
# 'C': [('B', 2), ('D', 3)],
# 'D': [('C', 3), ('F', 2), ('A', 9)],
# 'E': [('A', 2), ('F', 3)],
# 'F': [('D', 2), ('E', 3)],
# }

# gew = {  #graph_equal_weights
# 'A': ['B', 'G', 'K'],
# 'B': ['A', 'C'],
# 'C': ['B', 'D'],
# 'D': ['C', 'F', 'E'],
# 'E': ['D', 'H'],
# 'F': ['G', 'D'],
# 'G': ['A', 'F'],
# 'H': ['I', 'E'],
# 'I': ['H', 'J'],
# 'J': ['K', 'I'],
# 'K': ['A', 'J']
# }

gew = {  #graph_unequal_weights
'A': [('B', 1), ('D', 1), ('E', 1)],
'B': [('A', 1), ('C',1)],
'C': [('B', 1), ('D', 1)],
'D': [('C', 1), ('F', 1), ('A', 1)],
'E': [('A', 1), ('F', 1)],
'F': [('D', 1), ('E', 1)],
}




from collections import defaultdict
from heapq import *

# def dijkstra(graph, f, t):
#
#     q, seen, mins = [(0,f)], set(), {f: 0}
#     while q:
#         cost, node = heappop(q)
#         if node not in seen:
#             seen.add(node)
#             if node == t: return cost
#
#             for nei in graph[node]:
#                 if nei[0] in seen: continue
#                 prev = mins.get(nei[0], None)
#                 next = cost + nei[1]
#                 if prev is None or next < prev:
#                     mins[nei[0]] = next
#                     heappush(q, (next, nei[0]))
#     return float("inf")

def bfs(graph, src, dest):
    q = [(1, src, [src])]
    seen = set()
    res = None
    seen.add(src)
    minDist = float('inf')
    while q:
        dist, node, path = q.pop(0)
        if node in seen: continue
        if node not in seen:
            seen.add(node)
            if node == t:
                if dist + 1 < minDist:
                    minDist = dist+1
            for nei in graph[node]:
                q.append((dist+1, nei[0], path+[nei[0]]))


    return minDist


# print("Dijktras on unequal", dijkstra(guw, 'A', 'D'))
# print("Dijktras on equal", dijkstra(gew, 'A', 'D' ))
# print("bfs unequal weights", bfs(guw, 'A', 'D'))
print("bfs equal weights", bfs(gew, 'A', 'C'))
