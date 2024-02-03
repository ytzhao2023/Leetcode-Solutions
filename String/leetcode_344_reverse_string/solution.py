class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        reverse(s, 0, len(s) - 1)
        

    def reverse(self, s, left, right):
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        self.reverse(s, left + 1, right - 1)
    
    