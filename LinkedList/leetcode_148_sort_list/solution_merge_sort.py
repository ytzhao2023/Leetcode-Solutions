# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        # step1: divide the listnode into 2 halves.
        middle = self.getMiddle(head)
        leftHalf = head
        rightHalf = middle.next
        middle.next = None
        
        # step2: recursively sort both halves.
        left = self.sortList(leftHalf)
        right = self.sortList(rightHalf)
        
        # step3: Merge the sorted halves
        sortedList = self.merge(left, right)
        
        return sortedList
    
    def getMiddle(self, head):
        if head is None:
            return head
        
        left = head
        right = head
        
        while right.next and right.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
    def merge(self, left, right):
        result = ListNode()
        p = result
        while left and right:
            if left.val > right.val:
                p.next = right
                right = right.next
            else:
                p.next = left
                left = left.next
            p = p.next
        
        if left is None:
            p.next = right

        if right is None:
            p.next = left
        return result.next
            