import collections
import heapq

class Solution:
    def minCost(self, ropes):
        cost = 0
        while ropes:
            ropes.sort()
            if len(ropes) >= 2:
                rope1 = ropes.pop(0)
                rope2 = ropes.pop(0)
                cost += rope1 + rope2
                ropes.append(rope1 + rope2)
            else:
                break
        return cost


if __name__=="__main__":
    solution = Solution()
    print(solution.minCost([8, 4, 6, 12]))
    print(solution.minCost([20, 4, 8, 2]))
    print(solution.minCost([1, 2, 5, 10, 35, 89]))
    print(solution.minCost([2, 2, 3, 3]))
