class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min = 0
        max = len(nums)-1
        while min <= max:
            middle = (min + max) // 2
            if nums[middle] < target:
                min = middle + 1
            elif nums[middle] > target:
                max = middle -1
            elif nums[middle] == target:
                return middle
        return -1

