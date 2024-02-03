class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = float("inf")
        left = 0 # the beginning point
        right = 0 # the ending point
        sum_subarray = 0
        for right in range(len(nums)):
            sum_subarray += nums[right]

            while sum_subarray >= target:
                min_length = min(min_length, right - left +1)
                sum_subarray -= nums[left]
                left += 1
        return (min_length) if min_length != float('inf') else 0