class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # Suppose dp[j] represents the number of methods to achieve the value equal to target."
        dp = [0] * (amount + 1)

        dp[0] = 1

        # for i in range(len(coins)):
        #     for j in range(coins[i], amount + 1):
        #         dp[j] += dp[j-coins[i]]
    
        # return dp[amount]

        for j in range(amount + 1):
            for i in range(len(coins)):
                if j >= coins[i]:
                    dp[j] += dp[j-coins[i]]
        return dp[amount]



solution = Solution()

amount = 7
coins = [1, 2, 4, 6]

result = solution.change(amount, coins)

print(result)