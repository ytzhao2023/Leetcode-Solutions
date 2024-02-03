class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")] * (amount+1)

        dp[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j],dp[j-coins[i]]+1)

        if dp[amount] == float("inf"):
            return -1
        return dp[amount]


solution = Solution()
coins = [1, 2, 5, 10]
amount = 24
result = solution.coinChange(coins, amount)
print(result)
