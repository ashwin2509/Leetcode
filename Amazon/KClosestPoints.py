import collections
import heapq

class Solution:
    def kclosestPoints(self, points, K):
        arr = []
        res = []
        for point in points:
            if len(arr) < K:
                heapq.heappush(arr, (-self.checkDist(point), point))
            else:
                heapq.heappushpop(arr, (-self.checkDist(point), point))

        for ele in arr:
            res.append(ele[1])
        return res

    def checkDist(self, point):
        return point[0] * point[0] + point[1] * point[1]


if __name__=="__main__":
    solution = Solution()
    print(solution.kclosestPoints([[1,3],[-2,2]], 1))
