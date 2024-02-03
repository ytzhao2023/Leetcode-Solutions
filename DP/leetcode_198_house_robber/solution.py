class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        # suppose dp[i] represents the maximum amount of money can be robbed.
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[-1]
    

solution = Solution()
list = [4, 7, 9, 20, 1, 3, 1]
max_money = solution.rob(list)
print(max_money)