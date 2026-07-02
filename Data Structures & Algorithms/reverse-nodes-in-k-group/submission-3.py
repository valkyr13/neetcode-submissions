# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        i know how to reverse in place
        first traverse and check if length is divisible by k
        need to reverse n//k times

        """

        l = 0
        start = head

        while (start is not None):
            start = start.next
            l += 1

        grp = l//k

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        nxt = head.next
        nodes = k
        prev_tail = dummy


        while(grp > 0):
            start = curr
            while (nodes > 0):
                # in place reversal
                curr.next = prev
                prev = curr

                curr = nxt
                if nxt is not None:
                    nxt = nxt.next
                
                nodes -= 1
            #set tail and start again
            start.next = curr
            prev_tail.next = prev
            prev_tail = start

            grp -= 1
            nodes = k

        return dummy.next
        
        
        