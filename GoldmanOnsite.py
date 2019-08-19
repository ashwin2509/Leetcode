class Version:
    def __init__(self):
        self.arr = []
        self.l = 0
        self.r = 0
        self.version = 0
        self.target_version = 8
        self.dic = {}


    def push(self, x):
        self.dic[self.r] = x
        self.r += 1
        self.version += 1

        if self.version == self.target_version:
            for i in range(self.l, self.r)
                self.arr.append(self.dic[i])
            return self.arr
        return "Added"

    def pop(self):
        self.r -= 1
        self.version += 1

        if self.version == self.target_version:
            for i in range(self.l, self.r):
                self.arr.append(self.dic[i])
            return self.arr
        return "Popped"



solution = Version()
print(solution.push(1))
print(solution.push(2))
print(solution.push(3))
print(solution.push(4))
print(solution.pop())
print(solution.pop())
print(solution.push(5))
print(solution.push(6))
