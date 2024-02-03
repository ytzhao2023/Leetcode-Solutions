class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # suppose there are two sublists of nums which are named postive and negative.
        # we can predict that the sum of positive + negative equal to the sum of nums.
        # and the sum of positive - negative equal to the target.  the sum of positive sublist equal to (target+sum)/2.
        # then we can transfer the problem to how many methods to get the list which sum is equal to (target+sum)/2.

        sum = 0
        for num in nums:
            sum += num

        if (target + sum) % 2 == 1:
            return 0
        if abs(target) > sum:
            return 0
        
        positive_sum = (sum + target)//2

        dp = [[0] * (positive_sum + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums)+1):
            for j in range(positive_sum + 1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        return dp[len(nums)][positive_sum]