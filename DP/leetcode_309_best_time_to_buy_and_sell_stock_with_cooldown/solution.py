class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) == 0:
            return 0
        
        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0

        # dp[i][0] represents the maximum profit you get in the i th day when you hold stocks.
        # dp[i][1] represents the maximum profit you get in the i th day when you not hold stocks and you are in the cooldown.
        # dp[i][2] represents the maximum profit you get in the i th day when you not hold stocks and you are not in the cooldown.
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
            

        return max(dp[-1][1], dp[-1][2])
