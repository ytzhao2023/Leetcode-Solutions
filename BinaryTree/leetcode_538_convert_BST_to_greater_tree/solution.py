# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.pre = 0
        self.traversal(root)
        return root
    
    def traversal(self, curNode):
        if curNode is None:
            return None
        self.traversal(curNode.right)
        curNode.val += self.pre
        self.pre = curNode.val
        
        self.traversal(curNode.left)
