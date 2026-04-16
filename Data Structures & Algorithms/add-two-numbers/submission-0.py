# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        def helper(A,B,carry, curr):
            if A is None and B is None and carry == 0:
                return dummy.next
            
            a = 0
            b = 0
            sum = 0
            if B is not None:
                b = B.val
                B = B.next
            if A is not None:
                a = A.val
                A = A.next
                
            sum = a+b+carry
            carry = sum//10
            sum = sum%10
            
            node = ListNode(int(sum))
            curr.next = node
            curr = curr.next
            helper(A,B,carry,curr)
                
        helper(A,B,0,curr)
        return dummy.next        