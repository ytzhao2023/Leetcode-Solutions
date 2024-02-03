class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        l = 0
        r = 0
        max_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                r += 1
                max_length = max(max_length, r-l+1)

            else:
                l = i
                r = i

        return max_length




nums = [1, 3, 5, 4, 7]
solution = Solution()
result = solution.findLengthOfLCIS(nums)
print(result)
