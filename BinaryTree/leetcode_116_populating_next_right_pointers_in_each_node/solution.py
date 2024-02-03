
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        connect_nodes(root.left, root.right)
        
        return root
        
        def connect_nodes(node1, node2):
            if node1 == None:
                return
            
            node1.next = node2

            connect_nodes(node1.left, node1.right)
            connect_nodes(node2.left, node2.right)

            connect_nodes(node1.right, node2.left)

        
        

        

