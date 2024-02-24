# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
    
    def traversal(self, node, path, result):
        path.append(node.val)
        if not node.left and not node.right:
            sPath = '->'.join(map(str, path))
            result.append(sPath)
            return
        
        if node.left:
            self.traversal(node.left, path, result)
            path.pop()
            
        if node.right:
            self.traversal(node.right, path, result)
            path.pop()