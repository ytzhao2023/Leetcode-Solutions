"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        self._postorder(root, result)
        return result
    
    def _postorder(self, node, result):
        if not node:
            return
        for child in node.children:
            self._postorder(child, result)
            
        return result.append(node.val)
        
        