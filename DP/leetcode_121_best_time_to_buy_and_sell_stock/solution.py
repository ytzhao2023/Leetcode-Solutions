class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # suppose dp[i][0] represents the maximum profits on the 'i'th day you have alreadly sold the stocks.
        # and dp[i][1] represents the maximum profits on the 'i'th day you still hold the stocks.
        dp = [[0 for i in range(2)] for j in range(len(prices))]
        
        for i in range(len(prices)):
            if i-1 == -1:
                # Base case: on the first day, if you have not bought any stock, the profit is 0.
                dp[i][0] = 0
                # On the first day, if you have bought a stock, then the profit is negative of the stock price.
                dp[i][1] = dp[i-1][0]-prices[i]
                continue

            # Calculate the maximum profit for the current day
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1],  - prices[i])

            # Print the result if on the 'i'th day no stocks are held.
            print(f"{i}th day, no stocks:")
            print(dp[i-1][0])

            # Print the result if on the 'i'th day stocks are still held.
            print(f"{i}th day, hold stocks:")
            print(dp[i-1][1])

        # Return the maximum profit on the last day when all stocks are sold.
        return dp[len(prices) - 1][0]


solution = Solution()
prices = [2, 3, 6, 9, 1]
max_profit = solution.maxProfit(prices)
print(max_profit)


