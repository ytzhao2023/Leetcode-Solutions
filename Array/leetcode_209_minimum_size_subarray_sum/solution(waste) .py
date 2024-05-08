class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = float("inf")
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                sum_subarray = 0
                subarray = nums[i:j]                
                sum_subarray = sum(subarray)
                if sum_subarray >= target:
                    min_length = min(min_length, len(subarray))
        return min_length if min_length != float('inf') else 0