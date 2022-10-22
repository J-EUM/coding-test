# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d = cur = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val: # list2가 뒤로
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 or list2
        return d.next
# Runtime: 53 ms, faster than 21.41% of Python online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.4 MB, less than 81.95% of Python online submissions for Merge Two Sorted Lists.


        #return sorted(list1 + list2)

a = Solution()
# list1 = [1,2,4], list2 = [1,3,4]
h1 = ListNode(1)
h1.next = ListNode(2)
h1.next.next = ListNode(4)
h2 = ListNode(1)
h2.next = ListNode(3)
h2.next.next = ListNode(4)

res = a.mergeTwoLists(h1, h2)
#print(res)

print(h1.val)