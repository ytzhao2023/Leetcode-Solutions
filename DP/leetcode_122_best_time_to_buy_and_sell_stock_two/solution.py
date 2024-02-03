class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # suppose dp represents the maximum profit you get in the 'i'th day.
        # dp[i][0] represents the day you sold the stock, and dp[i][1] represents the day you buy the stock.
        dp = [[0 for j in range(2)] for i in range(len(prices))]

        # dp[0][0] represents in the first day, you do not buy the stock, so your profit is 0.
        dp[0][0] = 0
        # dp[0][1] represents in the first day, you spend prices[0] to buy the stock, so your profit is the minus prices[0]
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            # in the current day, dp[i][0] can be demonstrated by the status of 'i-1'th day.
            # if in the 'i-1'th day you do not hold the stock, dp[i][0] = dp[i-1][0],
            # if in the 'i-1'th day you hold the stock, dp[i][0] = dp[i-1][1] + prices[i], that means you sell the stock in 'i'th day.
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # in the current day, dp[i][1] also can be demonstrated by the status of 'i-1'th day.
            # if in the 'i-1'th day you hold the stock, dp[i][1] = dp[i-1][1],
            # if in the 'i-1'th day you do not hold the stock, dp[i][1] = dp[i-1][0] - prices[i], that means you buy the stock in 'i'th day.
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

            print(f"{i} th day, no stocks")
            print(dp[i-1][0])
            print(f"{i}th day, hold stocks")
            print(dp[i-1][1])

        return dp[len(prices)-1][0]
    

prices = [1, 3, 5, 9, 10]
solution = Solution()
max_profit = solution.maxProfit(prices)
print(max_profit)

