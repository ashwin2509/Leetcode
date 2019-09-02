import collections
import heapq

class Solution:
    def longestPalindromicSubstring(self, string):
        dp = [[0 for _ in range(len(string))] for _ in range(len(string))]
        res = ''
        ml = 0

        for i in range(len(string)):
            dp[i][i] = 1
            ml = 1
            res = string[i]

        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                dp[i][i+1] = 2
                ml = 2
                res = string[i] + string[i+1]


        for i in range(len(string)-3, -1, -1):
            for j in range(i+1, len(string)):
                if string[i] == string[j] and dp[i+1][j-1] != 0:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if dp[i][j] > ml:
                        ml = dp[i][j]
                        res = string[i:j+1]
        return res



if __name__=="__main__":
    solution = Solution()
    print(solution.longestPalindromicSubstring('babad'))
    print(solution.longestPalindromicSubstring('cbbd'))
