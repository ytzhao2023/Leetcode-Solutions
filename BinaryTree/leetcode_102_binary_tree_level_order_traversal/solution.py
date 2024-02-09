# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        """
        1. Initialization: Start with an empty result list to store the 
        traversal levels and initialize a deque (double-ended queue) with the 
        root node if it exists.

        2. Traversal:
        While the queue is not empty:
            Initialize an empty list to store the current level's node values.
            Loop through all the nodes at the current level:
                Pop the leftmost node from the queue.
                Append its value to the current level list.
                Enqueue its left and right children if they exist.
            Append the current level list to the result.
        3. Return: Once the traversal is complete, return the result containing
        the level-order traversal of the binary tree.
        """
        
        queue = collections.deque([root])
        result = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                curNode = queue.popleft()
                level.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                
                if curNode.right:
                    queue.append(curNode.right)
                    
            result.append(level)
            
        return result
        