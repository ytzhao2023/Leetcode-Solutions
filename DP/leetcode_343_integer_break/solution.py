class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        # suppose the first broken positive integer is j, then we have 2 possibilities.
        # firstly, integer i is broken into j and i-j, and i-j cannot be broken again, then dp = j * (i-j).
        # seconly, integer i is broken into j and i-j, and i-j can be broken into other positive integers, then dp = j * dp[i-j].

        # initialize the dp list.
        dp = [0] * (n+1)
        dp[2] = 1

        for i in range(3, n+1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], (i-j)*j, dp[i-j] * j)
                print(dp[i])

        return dp[n]
    

solution = Solution()
result = solution.integerBreak(20)
print(result)


        
    
    