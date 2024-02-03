class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]

        # dp[i][0] represents the maximum profit you get when holding the stocks.
        # dp[i][0] represents the maximum profit you get when not holding the stocks.
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
        return max(dp[-1][0], dp[-1][1])
    

solution = Solution()
fee = 1
prices = [0, 3, 5, 8, 10]
max_profit = solution.maxProfit(prices, fee)
print(max_profit)