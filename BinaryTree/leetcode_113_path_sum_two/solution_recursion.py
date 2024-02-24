# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        self.traversal(root, targetSum, [], result)
        return result
    
    def traversal(self, node, count, path, result):
        if not node:
            return
        path.append(node.val)
        count -= node.val
        if not node.left and not node.right and count == 0:
            result.append(list(path))
        self.traversal(node.left, count, path, result)
        self.traversal(node.right, count, path, result)
        path.pop()
        
    