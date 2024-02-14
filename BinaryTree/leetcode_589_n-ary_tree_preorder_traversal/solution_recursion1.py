"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        self._preorder(root, result)
        return result
    
    def _preorder(self, node, result):
        if not node:
            return
        result.append(node.val)
            
        for child in node.children:
            self._preorder(child, result)