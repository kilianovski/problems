# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        head = dummy

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next

            head = head.next

        if l1 is None:
            head.next = l2
        else:
            head.next = l1

        return dummy.next

l1 = ListNode(1, next=ListNode(val=2, next = ListNode(val=4)))
l2 = ListNode(1, next=ListNode(val=3, next = ListNode(val=4)))

Solution().mergeTwoLists(l1, l2)