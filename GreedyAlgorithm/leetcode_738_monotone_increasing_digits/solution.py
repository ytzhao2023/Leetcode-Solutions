class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        strNum = list(str(n))
        
        for i in range(len(strNum)-1, 0, -1):
            if strNum[i-1] > strNum[i]:
                strNum[i-1] = str(int(strNum[i-1])-1)
                for j in range(i, len(strNum)):
                    strNum[j] = "9"
                    
        return int("".join(strNum))
        
            
      