# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        result = []
        queue = collections.deque([root])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                curNode = queue.popleft()
                level.append(curNode.val)
                
                if curNode.left:
                    queue.append(curNode.left)
                    
                if curNode.right:
                    queue.append(curNode.right)
                    
            result.append(level)
        
        return result[::-1]
                
            
                