class Solution:
    def solution(self, arr):

        visited = set(arr)
        output = set()
        def findCyclicNumbers(num):
            leng = len(str(num))
            string = str(num) + str(num)
            res = []
            for i in range(1, leng):
                res.append(int(string[i: i + leng]))
            return res

        for ele in arr:
            cyclicNumbers = findCyclicNumbers(ele)
            for cyclic_number in cyclicNumbers:

                if cyclic_number in visited:
                    s = sorted([ele, cyclic_number])
                    s = tuple(s)
                    if s not in output:
                        output.add(s)
        print(output)
        return len(output)



solution = Solution()
print(solution.solution([567, 675, 456, 987, 980, 890, 809]))


