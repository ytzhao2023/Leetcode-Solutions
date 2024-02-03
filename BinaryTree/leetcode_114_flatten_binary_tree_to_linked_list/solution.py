# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
#        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # use the flatten function, flatten the left and right child.
        self.flatten(root.left)
        self.flatten(root.right)


        # the left and right flatten into a LinkNode.
        left = root.left
        right = root.right

        # change the left child into right child.
        root.left = None
        root.right = left

        # make the former right child to the end of the right child.
        p = root
        while p.right:
            p = p.right
        p.right = right
