# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = []
        self.traversal(root)
        
        if len(self.result) < 2:
            return 0
        
        minDifference = float('inf')
        for i in range(1, len(self.result)):
            minDifference = min(minDifference, self.result[i]-self.result[i-1])
        return minDifference
    
    def traversal(self, root):
        if root is None:
            return
        self.traversal(root.left)
        self.result.append(root.val)
        self.traversal(root.right)