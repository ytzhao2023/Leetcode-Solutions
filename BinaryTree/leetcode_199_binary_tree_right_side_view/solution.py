# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        """
        1. Initialization:
        new an empty list store the right node, a queque with root node if exists.
        2. Traversal:
        While the queue is not empty:
            Initialize a variable size to record the length of the current level.
            Loop through all the nodes at the current level:
                Pop the leftmost node from the queue.
                Append the most right value to the right_node list.
                Enqueue its left and right children if they exist.
        
        3. Return: Once the traversal is complete, return the right_node list.

        """
        
        right_node = []
        queque = collections.deque([root])
        
        while queque:
            size = len(queque)
            for i in range(size):
                curNode = queque.popleft()
                
                if i == size - 1:
                    right_node.append(curNode.val)

                if curNode.left:
                    queque.append(curNode.left)
                
                if curNode.right:
                    queque.append(curNode.right)
        
        return right_node