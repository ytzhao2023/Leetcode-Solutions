# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 0
        
        leftValue = self.sumOfLeftLeaves(root.left)
        # if the left subtree is the left leaf.
        if root.left and root.left.left == None and root.left.right == None:
            leftValue = root.left.val
        
        rightValue = self.sumOfLeftLeaves(root.right)
        
        sumValue = leftValue + rightValue
        return sumValue
        