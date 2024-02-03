class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # as the problem descripted, the largest weight is (10 * 300)//2.
        # initialize the dp * 15001
        dp = [0] * 1501
        total_sum = 0
        for stone in stones:
            total_sum += stone
        
        target = total_sum // 2
        for stone in stones:
            for j in range(target, stone-1, -1):
                dp[j] = max(dp[j], dp[j-stone] + stone)
        
        return total_sum - dp[target] - dp[target]