# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode()
        dummy_head.next = head
        current_head = dummy_head
        while current_head.next is not None:
            if current_head.next.val == val:
                current_head.next = current_head.next.next
            else:
                current_head = current_head.next
        
        return dummy_head.next









