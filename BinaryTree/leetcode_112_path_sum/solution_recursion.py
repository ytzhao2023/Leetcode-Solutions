# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self.traversal(root, targetSum - root.val)
    
    def traversal(self, cur, count):
        if not cur.left and not cur.right and count == 0:
            return True
        
        if not cur.left and not cur.right:
            return False
        
        if cur.left:
            count -= cur.left.val
            if self.traversal(cur.left, count):
                return True
            count += cur.left.val
            
        if cur.right:
            count -= cur.right.val
            if self.traversal(cur.right, count):
                return True
            count += cur.right.val
            
        return False
            
        