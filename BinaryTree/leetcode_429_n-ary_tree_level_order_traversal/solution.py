"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        queue = collections.deque([root])
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                curNode = queue.popleft()
                level.append(curNode.val)
                
                for child in curNode.children:
                    queue.append(child)
            
            result.append(level)
            
        return result