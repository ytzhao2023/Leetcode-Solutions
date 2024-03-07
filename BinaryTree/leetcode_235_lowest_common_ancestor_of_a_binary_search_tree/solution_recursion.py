# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.traversal(root, p, q)
    
    def traversal(self, curNode, p, q):
        if curNode is None:
            return None
        
        if curNode.val > p.val and curNode.val > q.val:
            left = self.traversal(curNode.left, p, q)
            if left is not None:
                return left
        
        if curNode.val < p.val and curNode.val < q.val:
            right = self.traversal(curNode.right, p, q)
            if right is not None:
                return right
        
        return curNode
    