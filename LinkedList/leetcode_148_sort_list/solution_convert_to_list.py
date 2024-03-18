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
        list = []
        
        current = head
        while current:
            list.append(current.val)
            current = current.next
            
        list.sort()
        
        current = head
        for i in range(len(list)):
            current.val = list[i]
            current = current.next
            
        return head