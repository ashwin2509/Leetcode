class TreeNode:
    def __init__(self, value):
        self.val = value
        self.parent = []
        self.children = []

class Portfolio:
    def __init__(self):
        self.roots = []
        self.dup = []
        self.dic = {}

    def add(self, parent, child):
        if not self.roots or (parent not in self.dic and child not in self.dic):
            parent = TreeNode(parent)
            child = TreeNode(child)
            parent.children.append(child)
            child.parent.append(parent)
            self.roots.append(parent)
            self.dic[parent.val] = parent
            self.dic[child.val] = child
        else:
            if parent in self.dic and child in self.dic:
                parent = self.parents[parent]
                child = self.all_children[child]
                parent.children.append(child)
                child.parent.append(parent)
                if len(child.parent) >= 2:
                    self.dup.append(child)
            elif child in self.dic and parent not in self.dic:
                child = self.dic[child]
                parent = TreeNode(parent)
                parent.children.append(child)
                child.parent.append(parent)
                if len(child.parent) >= 2:
                    self.dup.append(child)
                self.dic[parent.val] = parent
                self.roots.append(parent)
            elif parent in self.dic and child not in self.dic:
                parent = self.dic[parent]
                child = TreeNode(child)
                parent.children.append(child)
                child.parent.append(parent)
                self.dic[child.val] = child
            if child in self.roots:
                self.roots.remove(child)

    def getRoots(self):
        res = []
        for root in self.roots:
            res.append(root.val)
        return res

    def getDuplicates(self):
        res = []
        for dup in self.dup:
            res.append(dup.val)
        return res

    def getLongestPath(self):
        self.res = None
        for root in self.roots:
            path = []
            self.findPath(root, path+[root.val])
        return self.res

    def findPath(self, root, path):
        if root:
            if not root.children:
                if not self.res or len(self.res) < len(path):
                    self.res = path
                    return
            for c in root.children:
                self.findPath(c, path+[c.val])

    def longestPath(self):
        q = Queue()
        res = []
        md = -float('inf')
        q.put((root, 1, [root]))
        while not q.empty():
            node, dist, path = q.get()
            if not node.children and dist>=md:
                res = [path]
            for c in node.children:
                q.put((c, dist+1, path+[root]))






portfolio = Portfolio()
portfolio.add('shrikant', 'ashwin')
portfolio.add('prajakta', 'ashwin')
portfolio.add('ashwin', 'juniorashwin')
portfolio.add('meena', 'shalika')
portfolio.add('shubhada', 'prajakta')
portfolio.add('shrikant', 'x')
portfolio.add('x', 'y')
portfolio.add('y', 'z')
portfolio.add('z', 'a')
print(portfolio.getRoots())
print("Duplicates are ", portfolio.getDuplicates())
print("Longest path is ", portfolio.getLongestPath())
