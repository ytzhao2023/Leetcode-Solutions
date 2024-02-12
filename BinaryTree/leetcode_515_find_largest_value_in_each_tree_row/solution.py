# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        queue = collections.deque([root])
        
        while queue:
            level_size = len(queue)
            max_val = float('-inf')
            
            for _ in range(level_size):
                curNode = queue.popleft()
                max_val = max(max_val, curNode.val)
                
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            
            result.append(max_val)
            
        return result