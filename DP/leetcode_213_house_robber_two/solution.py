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
        
        def circle_rob(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            
            dp = [0] * (len(nums))
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])

            return dp[-1]
        
        return max(circle_rob(nums[1:]), circle_rob(nums[:-1]))
    
solution = Solution()
nums = [2, 3, 2]
max_num = solution.rob(nums)
print(max_num)