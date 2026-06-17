# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        p,c,n
        
        """

        if head is None or head.next is None:
            return head

        p = None
        c = head
        n = head.next
        
        while (n is not None):
            c.next = p
            p = c

            c = n
            n = n.next
            c.next = p

        return c
        