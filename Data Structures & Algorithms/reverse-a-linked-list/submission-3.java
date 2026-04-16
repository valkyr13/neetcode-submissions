/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode curr, ListNode prev, ListNode nxt){
            if(nxt == null){
                curr.next = prev;
                return curr;
            }

            curr.next = prev;
            prev = curr;
            curr = nxt;
            nxt = nxt.next;

            return reverseList( curr,  prev,  nxt);


        }


    public ListNode reverseList(ListNode head) {
        if(head == null ){
            return head;
        }
        ListNode curr = head;
        ListNode prev = null;
        ListNode nxt = head.next;

        return reverseList(curr,  prev,  nxt);
    }
}
