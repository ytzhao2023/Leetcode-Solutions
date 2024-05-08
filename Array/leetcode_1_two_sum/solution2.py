class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            rest_value = target - num
            if rest_value in nums_dict:
                return [nums_dict[rest_value], i]
            nums_dict[num] = i
        return []

nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))