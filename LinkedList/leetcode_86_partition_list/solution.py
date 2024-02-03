# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p = head
        dummy_small = ListNode()
        dummy_big = ListNode()
        p1 = dummy_small
        p2 = dummy_big

        while p != None:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next

            temp = p.next
            p.next = None
            p = temp

        p1.next = dummy_big.next
        return dummy_small.next

