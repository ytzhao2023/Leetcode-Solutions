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
        
        return self._is_balanced(root)[0]
    
    def _is_balanced(self, root):
        if not root:
            return True, -1
        
        left_balance, left_depth = self._is_balanced(root.left)
        right_balance, right_depth = self._is_balanced(root.right)
        if not (left_balance and right_balance):
            return False
        return (left_balance and right_balance and abs(left_depth - right_depth) <= 1, max(left_depth, right_depth) + 1)