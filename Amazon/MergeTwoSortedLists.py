import collections
import heapq

class Solution:
    def mergeSortedLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if not l1 and not l2: return None

        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else :
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2 

        return dummy.next






if __name__=="__main__":
    solution = Solution()
    print(solution.logReorder(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
