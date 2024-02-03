class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n = 1, 1 method exists;
        n = 2, 2 methods exist;
        n = 3, 3 methods exist;
        n = 4, 5 methods exist;
        n = 5, 8 methods exist;
        """

        if n <= 1:
            return n
        
        """
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range (3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

        """
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        
        return b