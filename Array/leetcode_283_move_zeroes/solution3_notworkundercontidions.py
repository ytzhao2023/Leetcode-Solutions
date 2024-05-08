class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        new_nums = []
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                new_nums.append(nums[i])
        for i in range(count):
            new_nums.append(0)
        return new_nums
     

new_nums= [1,0,3,4,0,0,0,6]

s = Solution()
print(s.moveZeroes(new_nums))

        
                
