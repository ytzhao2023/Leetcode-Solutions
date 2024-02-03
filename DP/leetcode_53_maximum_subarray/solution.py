class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp represents the max sum of the subarray which belongs to the array ending with i.
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])
        
        return max_sum
    

solution = Solution()
nums = [1, 2, 3, 4, -10, 11]
result = solution.maxSubArray(nums)
print(result)
