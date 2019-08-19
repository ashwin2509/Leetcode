class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findi(i, j):
            while i <= j:

                m = i + (j-i)//2
                if nums[m] > nums[m+1]:
                    return m + 1
                else:
                    if nums[i] > nums[m]:
                        j = m - 1
                    else:
                        i = m + 1

        def findi(i, j):
            if nums[i] < nums[j]:
                return 0
            while i <= j:
                mid = i + (j-i)//2
                if nums[mid] > nums[mid+1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[i]:
                        j = mid - 1
                    else:
                        i = mid + 1
        def search(l, r):
            while l <= r:
                m = l + (r-l)//2
                if nums[m] == target:
                    return mid
                elif nums[m] < target:
                    r = m+1
                else:
                    l = m-1
            return -1

        ind = findi(0, len(nums)-1)
        print(ind)
        if ind == 0:
            return search(0, len(nums)-1)

        else:
            if target == nums[ind]: return ind

            if target < nums[0]:
                return search(ind, len(nums)-1)
            else:
#                 return search(0, ind)
