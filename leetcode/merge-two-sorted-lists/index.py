# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# idea:

# pointers:
# 1. new list 'res'
# 2, 3 - heads h1, h2
# we go on until we have nodes:
#   pick smallest node and attack to res


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = None
        r = res
        h1, h2 = l1, l2

        while h1 is not None or h2 is not None:


            if h1 is None:
                head_to_pick = h2
                h2 = h2.next
            elif h2 is None:
                head_to_pick = h1
                h1 = h1.next
            elif h1.val < h2.val:
                head_to_pick = h1
                h1 = h1.next
            else:
                head_to_pick = h2
                h2 = h2.next

            val = head_to_pick.val

            if r is None:
                res = ListNode(val)
                r = res
            else:
                r.next = ListNode(val=val)
                r = r.next
            head_to_pick = head_to_pick.next

        return res
l1 = ListNode(1, next=ListNode(val=2, next = ListNode(val=4)))
l2 = ListNode(1, next=ListNode(val=3, next = ListNode(val=4)))

Solution().mergeTwoLists(l1, l2)