# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        Iteration: Binary Tree Inorder Traversal
        1. Intialize an empty stack and list to store the result

        2. Start from the root node, push the current node onto the stack and 
        move to the left child. Repeat this step until the current node is None

        3. When the current node is None, it means we have reached th leftmost
        leaf node. Pop the top node from the stack(which is the parent node),
        append its value the result list, and move to its right child

        4. Repeat step2 and step3 until the stack is empty and the current node
        is None, indicating that we have traversed all nodes in the tree.
        """

        if not root:
            return []
        
        stack = []
        result = []
        curNode = root

        while stack or curNode:
            if curNode:
                stack.append(curNode)
                curNode = curNode.left
            
            else:
                curNode = stack.pop()
                result.append(curNode.val)
                curNode = curNode.right
        
        return result


solution = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
result = solution.inorderTraversal(root)
print(result)