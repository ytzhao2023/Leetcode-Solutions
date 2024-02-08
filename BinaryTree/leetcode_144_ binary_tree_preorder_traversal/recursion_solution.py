# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if the root is None, return an empty list.
        if not root:
            return []
        
        # recursively traverse the left subtree.
        left = self.preorderTraversal(root.left)
        # recursively traverse the right subtree
        right = self.preorderTraversal(root.right)

        return [root.val] + left + right
    

solution = Solution() 
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
result = solution.preorderTraversal(root)
print(result)