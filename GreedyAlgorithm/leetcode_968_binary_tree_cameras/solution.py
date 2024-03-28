# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        if self.traversal(root, result) == 0:
            result[0] += 1
    
        return result[0]
    
    def traversal(self, curNode, result):
        if not curNode:
            return 2
        
        left = self.traversal(curNode.left, result)
        right = self.traversal(curNode.right, result)
        
        if left == 2 and right == 2:
            return 0
        
        if left == 0 or right == 0:
            result[0] += 1
            return 1
        
        if left == 1 or right == 1:
            return 2
    