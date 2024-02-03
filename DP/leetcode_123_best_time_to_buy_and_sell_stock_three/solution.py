class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        # dp[i][0] represents the maximum profit you get on the 'i'th day, 
        # when you have not bought or sold any stocks until the 'i'th day.
        # dp[i][1] represents the maximum profit you get on the 'i'th day, 
        # when holding stocks for the first time.
        # dp[i][2] represents the maximum profit you get on the 'i'th day, 
        # when not holding stocks for the first time.
        # dp[i][3] represents the maximum profit you get on the 'i'th day, 
        # when holding stocks for the second time.
        # dp[i][4] represents the maximum profit you get on the 'i'th day, 
        # when not holding stocks for the second time. 
        dp = [[0 for i in range(5)] for j in range(len(prices))]
        
        # dp[0][1] and dp[0][3] represent the first and second time you choose to spend prices[0] to buy stocks, respectively.
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            print(dp[i][0])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            print(dp[i][1])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            print(dp[i][2])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            print(dp[i][3])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
            print(dp[i][4])

        return dp[-1][4]
    
prices = [4, 9, 20, 1, 3, 10]
solution = Solution()
max_profit = solution.maxProfit(prices)
print(max_profit)