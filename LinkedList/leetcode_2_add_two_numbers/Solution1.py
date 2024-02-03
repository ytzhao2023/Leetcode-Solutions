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
        l1_str = ""
        while l1 != None:
            l1_str += str(l1.val)
            l1 = l1.next
        l1_val = int(l1_str[::-1])

        l2_str = ""
        while l2 != None:
            l2_str += str(l2.val)
            l2 = l2.next
        l2_val = int(l2_str[::-1])

        result = l1_val + l2_val
        result_str = str(result)[::-1]

        answer = ListNode(int(result_str[0]))
        body = answer
        for i in range(1, len(result_str)):
            temp = ListNode(int(result_str[i]))
            # if i < len(result_str) - 1:
            #     temp.next = ListNode(int(result_str[i+1]))
            body.next = temp
            body = body.next

        return answer


    