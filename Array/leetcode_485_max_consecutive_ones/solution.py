class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) >= 1:
            count = 0
            result = count
            for i in range(len(nums)):
                if nums[i] == 1:
                    count += 1
                else:
                    count = 0
                result = max(result, count)
            return result


