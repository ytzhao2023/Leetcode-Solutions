from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        i = 0
        while i < k:
            temp = nums.pop()
            nums.insert(0, temp)
            i += 1
            

nums = [-1,-100,3,99]
solution = Solution()
solution.rotate(nums, 2)
print(nums)