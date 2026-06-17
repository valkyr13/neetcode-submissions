# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        edges cases
        n = N
        head is None
        """

        if head is None:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        l = dummy
        r = head
        i = 0

        while (i < n):
            i += 1
            r = r.next
        
        while (r is not None):
            r = r.next
            l = l.next
        
        l.next = l.next.next

        return dummy.next

        