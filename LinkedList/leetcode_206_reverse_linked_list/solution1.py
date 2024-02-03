# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_head = head
        pre_head = None
        while current_head is not None:
            temp = current_head.next
            current_head.next = pre_head
            pre_head = current_head
            current_head = temp
            
        return pre_head

node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

solution = Solution()

new_head = solution.reverseList(node1)

current_node = new_head
while current_node is not None:
    print(current_node.val, end = "-->")
    current_node = current_node.next
