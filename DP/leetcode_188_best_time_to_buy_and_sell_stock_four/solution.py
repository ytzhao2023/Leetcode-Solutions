class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        
        # dp[i][j] represents the maximum profit you get on the 'i'th day, 
        # dp[i][j+1] represents the maximum profit you get on the 'i'th day, when holding stocks.
        # dp[i][j+2] represents the maximum profit you get on the 'i'th day, when not holding stocks.
        dp = [[0] * (2 * k + 1) for i in range(len(prices))]

        
        # initialize the dp list, and dp[0][j] represents the first time you hold the stocks.
        for j in range(1, 2*k, 2):
            dp[0][j] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(0, 2 * k - 1, 2):
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i])
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i])
        
        # dp[-1][2*k] represents the maximum profit you get in the last day when stocks are not held.
        return dp[-1][2*k]
    


solution = Solution()
k = 5
prices = [2, 6, 3, 7, 4, 2, 8]
max_profit = solution.maxProfit(k, prices)
print(max_profit)
