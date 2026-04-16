/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummy := &ListNode{Val: 0,Next: nil}
	curr := dummy
	a := 0
	b := 0
	carry := 0
	sum := 0


	for ; l1 != nil || l2 != nil || carry != 0; {
		a = 0
		b = 0
		sum = 0
		if l1 != nil {
			a = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			b = l2.Val
			l2 = l2.Next
		}

		sum = a + b + carry
		carry = sum/10
		sum = sum%10

		node := &ListNode{Val: sum, Next:nil}
		curr.Next = node
		curr = curr.Next
	}
	return dummy.Next
}
