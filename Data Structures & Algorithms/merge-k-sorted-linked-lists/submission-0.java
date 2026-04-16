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

    public ListNode mergeKLists(ListNode l1, ListNode l2) {

        if(l1 == null){
            return l2;
        }
        if(l2 == null){
            return l1;
        }


        ListNode mergeHead = new ListNode();
        ListNode curr;
        ListNode c1 = l1;
        ListNode c2;

        curr = mergeHead;    

        c2 = l2;

        while(c1 != null && c2 != null){
            if(c1.val > c2.val){
                curr.next = c2;
                c2 = c2.next;
            }
            else{
                curr.next = c1;
                c1 = c1.next;
            }
            curr = curr.next;
        }

        if(c1 == null){
            curr.next = c2;
        }

        if(c2 == null){
            curr.next = c1;
        }

        return mergeHead.next;

    }


    public ListNode mergeKLists(ListNode[] lists) {
        ListNode l1;
        ListNode l2;
        int len = lists.length;
        int interval = 1;

        while(interval < len){
            for(int i = 0; i<len - interval;i += 2*interval){
            l1 = lists[i];
            if(lists[i+interval] == null){
                l2 = null;
            }else{
                l2 = lists[i+interval];
            }
            lists[i] = mergeKLists(l1,l2);
        }
            interval *= 2;
        }

        return lists.length > 0 ? lists[0] : null;

    }
}
