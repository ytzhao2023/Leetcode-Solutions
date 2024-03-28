class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fiveDollars = 0
        tenDollars = 0
        
        for bill in bills:
            if bill == 5:
                fiveDollars += 1
                
            if bill == 10:
                if fiveDollars <= 0:
                    return False
                tenDollars += 1
                fiveDollars -= 1
                
            if bill == 20:
                if fiveDollars > 0 and tenDollars > 0:
                    fiveDollars -= 1
                    tenDollars -= 1
                elif fiveDollars >= 3:
                    fiveDollars -= 3
                else:
                    return False
        return True 

bills = [10, 10]     
solution = Solution()
result = solution.lemonadeChange(bills)
print(result)
      
        