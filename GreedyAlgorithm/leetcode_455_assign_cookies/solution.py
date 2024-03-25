class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        index = len(s)-1
        result = 0
        
        for i in range(len(g)-1, -1, -1):
            if index >= 0 and s[index] >= g[i]:
                result += 1
                index -= 1
                
        return result
            
        