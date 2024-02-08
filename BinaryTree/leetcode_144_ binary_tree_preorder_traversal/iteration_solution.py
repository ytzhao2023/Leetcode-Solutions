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
        if not root:
            return []
        
        # Initialize a stack to store nodes.
        stack = [root]
        # Initialize an empty list to store result.
        result = []

        # while the stack is not empty.
        while stack:
            # pop the top node from the stack
            node = stack.pop()
            # Append the value of the current node to the result list
            result.append(node.val)

            """
            preorderTraversal: root, left child, right child.
            Stack: last in first out.
            So, we iterate the root.right firstly.
            """

            # If the right child of the current node exists, push it onto the stack
            if node.right:
                stack.append(node.right)
            # If the left child of the current node exists, push it onto the stack
            if node.left:
                stack.append(node.left)
        return result
    

solution = Solution() 
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
result = solution.preorderTraversal(root)
print(result)