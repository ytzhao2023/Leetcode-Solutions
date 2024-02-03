class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        # dp[i] represents the length of the longest increasing subsequence 
        # that ends at index i in the given array nums.
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # If the current element nums[i] is greater than nums[j],
                    # it can be part of a longer increasing subsequence.
                    # So, update dp[i] with the maximum of its current value and dp[j] + 1.
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)