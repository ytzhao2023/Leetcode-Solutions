class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow_index = 0
        fast_index = 0
        for fast_index in range(len(nums)):
            if nums[fast_index] != val:
                nums[slow_index] = nums[fast_index]
                slow_index += 1
        return slow_index        
        


s = Solution()
nums_test = [0, 1, 2, 2, 4, 5]
val_test = 2
print(nums_test)
print(s.removeElement(nums_test, val_test))
print(nums_test)
