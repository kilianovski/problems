# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        ids = set()

        while head is not None:
            head_id = id(head)
            if head_id in ids:
                return head
            ids.add(head_id)
            head = head.next
        
        return None