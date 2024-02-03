class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        # dp represents the max length of the continuous increasing list in the list ends with i.
        dp = [1] * len(nums)
        max_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            max_length = max(max_length, dp[i])

        return max_length



nums = [1, 3, 5, 4, 7]
solution = Solution()
result = solution.findLengthOfLCIS(nums)
print(result)
