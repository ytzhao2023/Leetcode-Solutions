# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        result = 0
        queue = collections.deque([root])
        
        while queue:
            level_size = len(queue)
        
            for i in range(level_size):
                node = queue.popleft()
                result += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result