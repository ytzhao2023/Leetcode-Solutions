package LinkedList.leetcode_206_reverse_linked_list;
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }
  
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode currentHead = head;
        ListNode preHead = null;
        ListNode temp = null;

        while(currentHead != null){
            temp = currentHead.next;
            currentHead.next = preHead;
            preHead = currentHead;
            currentHead = temp;
        }
        return preHead;

        
    }
}

 
