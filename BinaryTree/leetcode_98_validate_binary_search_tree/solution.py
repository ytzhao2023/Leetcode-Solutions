# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.result = []
        self.traversal(root)
        for i in range (1, len(self.result)):
            if self.result[i] <= self.result[i-1]:
                return False
        return True
    
    def traversal(self, root):
        if root is None:
            return True
        
        self.traversal(root.left)
        self.result.append(root.val)
        self.traversal(root.right)
            