# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        queue = collections.deque([(root, 1)])
        
        while queue:
            node, level = queue.popleft()
            
            left_depth = self.get_depth(node.left)
            right_depth = self.get_depth(node.right)
            
            if abs(left_depth - right_depth) > 1:
                return False
            
            if node.left:
                queue.append(node.left, level + 1)
                    
            if node.right:
                queue.append(node.right, level + 1)
                    
        return True
    
    def get_depth(self, node):
        if not node:
            return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1