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
        
        # balanced conditions: left subtree is balanced and right subtree is 
        # balanced and (left subtree height - right subtree height) <= 1.
        
        if not root:
            return True
        
        left_balance = self.isBalanced(root.left)
        right_balance = self.isBalanced(root.right)
        left_height = self.get_depth(root.left)
        right_height = self.get_depth(root.right)
        
        return left_balance and right_balance and  abs(left_height - right_height) <= 1
        
    def get_depth(self, root):
        if not root:
            return -1
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1