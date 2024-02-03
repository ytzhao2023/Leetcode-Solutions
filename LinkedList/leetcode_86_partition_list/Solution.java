package LinkedList.leetcode_86_partition_list;


//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode p = head;
        ListNode dummy_small = new ListNode();
        ListNode dummy_big = new ListNode();
        ListNode p1 = dummy_small;
        ListNode p2 = dummy_big;

        while (p != null){
            if (p.val < x){
                p1.next = p;
                p1 = p1.next;
            }else{
                p2.next = p;
                p2 = p2.next;
            }

            ListNode temp = p.next;
            p.next = null;
            p = temp;
        }

        p1.next = dummy_big.next;
        return dummy_small.next;
        
    }
}