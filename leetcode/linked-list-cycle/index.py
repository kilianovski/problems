# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ids = set()

        while head is not None:
            head_id = id(head)
            if head_id in ids:
                return True
            ids.add(head_id)
            head = head.next
        
        return False