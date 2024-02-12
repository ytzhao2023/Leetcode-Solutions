# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        average_value = []
        queque = collections.deque([root])
        
        while queque:
            size = len(queque)
            level_sum = 0
    
            for i in range(size):
                curNode = queque.popleft()
                
                level_sum += curNode.val
                
                if curNode.left:
                    queque.append(curNode.left)
                    
                if curNode.right:
                    queque.append(curNode.right)
            
            average_value.append(float(level_sum)/size)    
            
        return average_value
            
                
            
        