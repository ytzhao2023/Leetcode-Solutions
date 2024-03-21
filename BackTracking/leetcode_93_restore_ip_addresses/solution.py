class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.backtracking(s, 0, 0, "", result)
        return result
    
    def backtracking(self, s, startIndex, pointNum, current, result):
        if pointNum == 3:
            if self.isValid(s, startIndex, len(s)-1):
                current += s[startIndex:]
                result.append(current)
                
            return
        
        for i in range(startIndex, len(s)):
            if self.isValid(s, startIndex, i):
                sub = s[startIndex: i + 1]
                self.backtracking(s, i + 1, pointNum + 1, current + sub + ".", result)
            else:
                break
            
    def isValid(self, s, start, end):
        if start > end:
            return False
        
        if s[start] == "0" and start != end:
            return False
        
        num = 0
        
        for i in range(start, end + 1):
            if not s[i].isdigit():
                return False
            
            num = num * 10 + int(s[i])
            
            if num > 255:
                return False
            
        return True