# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a_next = l1
        b_next = l2
        
        digits = []
        
        while a_next != None or b_next != None:
            a_val, a_next = (0, None) if a_next == None else (a_next.val, a_next.next)
            b_val, b_next = (0, None) if b_next == None else (b_next.val, b_next.next)
            digits.append((a_val, b_val))
        
        length = len(digits)
        result = 0
        for i in reversed(range(length)):
            a, b = digits[i]
            result += (a + b) * pow(10, i)
        
        
        result_digits = [int(x) for x in str(result)]
        
        result_node = None
        
        for digit in result_digits:
            
            next_node = ListNode(digit)
            next_node.next = result_node
            result_node = next_node
        
        return result_node
            
