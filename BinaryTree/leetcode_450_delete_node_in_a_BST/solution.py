# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # Base case: if the root is None, the key is not found.
        if root is None:
            return None
        
        if root.val == key:
            # Case 2: Node is a leaf, directly remove it by returning None.
            if root.left is None and root.right is None:
                return None
            # Case 3: Node has only one child, replace node with its child.
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Case 4: Node has two children, find the in-order successor (leftmost node in right subtree),
            else:
                cur = root.right
                # Traverse to find the leftmost child of the right subtree.
                while cur.left is not None:
                    cur = cur.left
                # Attach the left subtree of the node to delete to the leftmost position.
                cur.left = root.left
                return root.right
            
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root