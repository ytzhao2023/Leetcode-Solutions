# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.count = 0
        self.maxCount = 0
        # This is to keep track of the previous node during the inorder traversal
        self.pre = None
        self.result = []
        
        self.searchBST(root)
        return self.result
    
    def searchBST(self, curNode):
        if curNode is None:
            return
        self.searchBST(curNode.left)
        
        # If this is the first node or the value is different from the previous one, reset count to 1
        if self.pre is None or self.pre.val != curNode.val:
            self.count = 1
        # If the value is the same as the previous one, increment the count
        else:
            self.count += 1
        
        # Update the result list based on the count
        if self.count == self.maxCount:
            self.result.append(curNode.val)
        
        if self.count > self.maxCount:
            self.maxCount = self.count
            # Reset the result list as we found a new mode
            self.result = [curNode.val]
        
        self.pre = curNode
        
        self.searchBST(curNode.right)