'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 6 and 8 have a common ancestor of 4.

         14  13
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parentChildPairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

hasCommonAncestor(parentChildPairs1, 3, 8) => false
hasCommonAncestor(parentChildPairs1, 5, 8) => true
hasCommonAncestor(parentChildPairs1, 6, 8) => true
hasCommonAncestor(parentChildPairs1, 6, 9) => true
hasCommonAncestor(parentChildPairs1, 1, 3) => false
hasCommonAncestor(parentChildPairs1, 7, 11) => true
hasCommonAncestor(parentChildPairs1, 6, 5) => true
hasCommonAncestor(parentChildPairs1, 5, 6) => true

Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

        11
       /  \
      10   12
     /  \
1   2    5
 \ /    / \
  3    6   7
   \        \
    4        8

parentChildPairs2 = [
    (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
    (2, 3), (3, 4), (5, 6), (5, 7), (7, 8),
]

hasCommonAncestor(parentChildPairs2, 4, 12) => true
hasCommonAncestor(parentChildPairs2, 1, 6) => false
hasCommonAncestor(parentChildPairs2, 1, 12) => false
'''



'''

         14  13
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parentChildPairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

hasCommonAncestor(parentChildPairs1, 3, 8) => false
hasCommonAncestor(parentChildPairs1, 5, 8) => true
hasCommonAncestor(parentChildPairs1, 6, 8) => true
hasCommonAncestor(parentChildPairs1, 6, 9) => true
hasCommonAncestor(parentChildPairs1, 1, 3) => false
hasCommonAncestor(parentChildPairs1, 7, 11) => true
hasCommonAncestor(parentChildPairs1, 6, 5) => true
hasCommonAncestor(parentChildPairs1, 5, 6) => true
'''

import collections


def hasCommonAncestor(parent_child_pairs, node1, node2):
    dic = collections.defaultdict(list)
    parents = set()
    for pair in parent_child_pairs:
        dic[pair[1]].append(pair[0])

    if node1 not in dic or node2 not in dic: return False

    for parent in dic[node1]:
        check(parent, node1, parents, dic)

    for parent in dic[node2]:
        if check2(parent, node2, parents, dic):
            return True
    return False


def check2(parent, node, parents, dic):
    if parent in parents:
        return True

    while parent in dic:
        for ele in dic[parent]:
            child = parent
            parent = ele
            if check2(parent, child, parents, dic):
                return True
    return False

def check(parent, node, parents, dic):
    if parent not in dic:
        parents.add(parent)
        return

    while parent in dic:
        for ele in dic[parent]:
            child = parent
            parent = ele
            check(parent, child, parents, dic)



def check(parent, child, parents, dic):
    if parent not in dic:
        parents.add(parent)
        return
    while parent in dic:
        for ele in dic[parent]:
            child = parent
            parent = ele
            check(parent, child, parents, dic)



def check2(parent, child, parents, dic):
    if parent in parents:
        return True
    while parent in dic:
        for ele in dic[parent]:
            child = parent
            parent = ele
            if check2(parent, child, parents, dic):
                return True
    return False



parentChildPairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

parentChildPairs2 = [
    (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
    (2, 3), (3, 4), (5, 6), (5, 7), (7, 8),
]

print(hasCommonAncestor(parentChildPairs1, 3, 8), False)
print(hasCommonAncestor(parentChildPairs1, 5, 8), True)
print(hasCommonAncestor(parentChildPairs1, 6, 8), True)
print(hasCommonAncestor(parentChildPairs1, 6, 9), True)
print(hasCommonAncestor(parentChildPairs1, 1, 3), False)
print(hasCommonAncestor(parentChildPairs1, 7, 11), True)
print(hasCommonAncestor(parentChildPairs1, 6, 5), True)
print(hasCommonAncestor(parentChildPairs1, 5, 6), True)

print("------------")
print(hasCommonAncestor(parentChildPairs2, 4, 12), True)
print(hasCommonAncestor(parentChildPairs2, 1, 6), False)
print(hasCommonAncestor(parentChildPairs2, 1, 12), False)
