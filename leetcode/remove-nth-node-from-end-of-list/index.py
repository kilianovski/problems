# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# To solve it in one path, we will use slow and fast pointers
# When fast pointer reaches the end, we know the size of the list
# when we reach the given point - 1, we reassign it's 'next' value
# 
# 
# Variables we need:
# 1. slow and fast pointers
# 2. list len counter (for fast pointer)
# 3. i for slow pointer
# 4. i of node before node to delete. When we get list len
# 
# 
#  
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow_head = head
        fast_head = head

        list_len = 0 if head is None else 1

        slow_head_i = 0
        i_before_del = None

        while slow_head is not None:

            if i_before_del is None:
                for _ in range(n):
                    if fast_head.next is None:
                        i_before_del = list_len - n - 1

                        if i_before_del == -1:
                            return slow_head.next
                        break

                    list_len += 1
                    fast_head = fast_head.next

            if fast_head.next is None:
                i_before_del = list_len - n - 1

                if i_before_del == -1:
                    return slow_head.next
                    
            if slow_head_i == i_before_del:
                slow_head.next = slow_head.next.next 
                return head

            slow_head = slow_head.next
            slow_head_i += 1
            
# Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
print ( Solution().removeNthFromEnd(ListNode(1, ListNode(2), ), 1) )
