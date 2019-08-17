# def minimumSize(s, nums):
#     if not nums: return 0
#     summ = 0
#     l = 0
#     for i in range(len(nums)):
#         summ += nums[i]
#         while summ >= s:
#             ans = min(ans, i-l+1)
#             summ -= nums[l]
#             l += 1
#     return ans if ans != math.inf else 0
