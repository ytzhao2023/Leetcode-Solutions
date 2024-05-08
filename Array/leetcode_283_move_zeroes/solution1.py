class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                if  nums[j] == 0 and nums[j+1] != 0:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp



a = [1,2,3,4,0,0,0,6]

s = Solution()
s.moveZeroes(a)
print(a)

        