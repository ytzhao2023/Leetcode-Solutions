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
        :rtype
        """
        if not root:
            return True
        
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        
        while queue:
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            
            if leftNode == None and rightNode == None:
                continue
            
            if leftNode == None or rightNode == None or leftNode.val != rightNode.val:
                return False
            
            # If lefeNode.val == rightNode.val, execute the below code.
            queue.append(leftNode.left)
            queue.append(rightNode.right)
            queue.append(leftNode.right)
            queue.append(rightNode.left)
            
        return True
        