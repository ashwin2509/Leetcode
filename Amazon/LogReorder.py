import collections
import heapq

class Solution:
    def logReorder(self, logs):
        nmr, lttr = [], []
        for log in logs:
            if log.split(' ')[1].isdigit():
                nmr.append(log)
            else:
                lttr.append(log)

        lttr.sort(key = lambda x:x.split()[0])
        lttr.sort(key = lambda x:x.split()[1:])

        return [lttr+nmr]




if __name__=="__main__":
    solution = Solution()
    print(solution.logReorder(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
