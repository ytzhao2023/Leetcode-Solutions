# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        
        while stack:
            rightNode = stack.pop()
            leftNode = stack.pop()
            
            if rightNode == None and leftNode == None:
                continue
            
            if rightNode == None or leftNode == None or rightNode.val != leftNode.val:
                return False
            
            stack.append(leftNode.left)
            stack.append(rightNode.right)
            stack.append(leftNode.right)
            stack.append(rightNode.left)
            
        return True
        