# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode()
        head = dummy

        while len(lists) > 1:
            champion_i = 0
            champion = lists[champion_i]
            for i in range(1, len(lists)):
                candidate = lists[i]
                if candidate.val < champion.val:
                    champion = candidate
                    candidate_i = i
            


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