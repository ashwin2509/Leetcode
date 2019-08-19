guw = {  #graph_unequal_weights
'A': [('B', 5), ('D', 9), ('E', 2)],
'B': [('A', 5), ('C',2)],
'C': [('B', 2), ('D', 3)],
'D': [('C', 3), ('F', 2), ('A', 9)],
'E': [('A', 2), ('F', 3)],
'F': [('D', 2), ('E', 3)],
}

from collections import defaultdict
from heapq import *
import heapq
#
# def dijkstra(graph, f, t):
#     q = [(0, f, [f])]
#     seen = set()
#     mins = {f:0}
#     while q:
#         cost, node, path = heappop(q)
#         if node not in seen:
#             seen.add(node)
#             if node == t: return cost, path
#
#             for nei in graph[node]:
#                 if nei[0] in seen: continue
#                 prev = mins.get(nei[0], None)
#                 next = cost + nei[1]
#                 if prev is None or next < prev:
#                     mins[nei[0]] = next
#                     heappush(q, (next, nei[0], path+[nei[0]]))
#     return float("inf")


# import heapq
# def dijkstras(graph, f, t):
#     q = [(0, f, [f])]
#     seen = set()
#     mins = {f:0}
#     while q:
#         dist, node, path = heapq.heappop(q)
#         if node not in seen:
#             seen.add(node)
#             if node == t: return dist
#             for nei in graph[node]:
#                 if nei[0] in seen: continue
#                 prev = mins.get(nei[0], None)
#                 next = dist + nei[1]
#                 if prev == None or next < prev:
#                     mins[nei[0]] = next
#                     heapq.heappush(q, (next, nei[0], path+[nei[0]]))
#     return float('inf')
#
# def dijkstras(graph, f, t):
#     seen = set()
#     q = [(f, 0, [f])]
#     seen.add(dfsRecursive)
#     mins = {f:0}
#     while q:
#         node, dist, path = heapq.heappop(q)
#         if node not in seen:
#             seen.add(node)
#             if node == t: return dist
#             for nei in graph[node]:
#                 if nei[0] in seen: continue
#                 prev = mins.get(nei[0], None)
#                 next = dist+nei[1]
#                 if prev == None or next < prev:
#                     mins[nei[0]] = next
#                     heapq.heappush(q, (next, nei[0], path+[nei[0]]))
#     return float('inf')

def dijkstra(graph, f, t):
    q = [(0, f, [f])]
    seen = set()
    mins = {f:0}
    while q:
        dist, node, path = heapq.heappop(q)
        if node not in seen:
            seen.add(node)
            if node == t:
                return (dist, node, path)
            for nei in graph[node]:
                if nei in seen: continue
                prev = mins.get(nei[0], None)
                next = dist+nei[1]
                if prev == None or next < prev:
                    mins[nei[0]] = next
                    heapq.heappush(q, (next, nei[0], path+[nei[0]]))
    return float('inf')






print(dijkstra(guw, 'A', 'D'))
