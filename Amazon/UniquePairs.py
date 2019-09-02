import collections
import heapq

class Solution:
    def uniquePairs(self, arr, target):
        n = len(arr)
        l = 0
        r = n - 1
        count = 0
        while l <= r:
            if arr[l] + arr[r] == target:
                count += 1
                while l + 1 < r and arr[l] == arr[l+1]: l += 1
                while r - 1 > l and arr[r] == arr[r-1]: r -= 1
                l += 1
            elif arr[l] + arr[r] < target:
                l += 1
            else:
                r -= 1
        return count

if __name__=="__main__":
    solution = Solution()
    print(solution.uniquePairs([1, 1, 2, 45, 46, 46], 47))
