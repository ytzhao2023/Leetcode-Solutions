# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tail = 0 
        sum = l1.val + l2.val + tail
        tail = sum // 10
        new_head = ListNode(sum % 10)
        new_body = new_head
        l1 = l1.next
        l2 = l2.next

        while l1 != None and l2 != None:
            sum = l1.val + l2.val + tail
            temp = ListNode(sum % 10)
            tail = sum // 10 
            new_body.next = temp
            new_body = new_body.next
            l1 = l1.next
            l2 = l2.next
        
        if l1 == None:
            new_body, tail = self.processSingleListNode(l2, tail, new_body)
        else:
            new_body, tail = self.processSingleListNode(l1, tail, new_body)


        if tail == 1:
            temp = ListNode(tail)
            new_body.next = temp
            new_body = new_body.next
        
        return new_head
    
    def processSingleListNode(self, single_list, tail, new_body):
        while single_list != None:
            sum = single_list.val + tail
            temp = ListNode(sum % 10)
            tail = sum // 10
            new_body.next = temp
            new_body = new_body.next
            single_list = single_list.next
        return new_body, tail



        


        












