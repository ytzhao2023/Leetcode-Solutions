class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        i = 0
        count = 0
        cover = 0
        while i <= cover:
            for i in range(i, cover+1):
                cover = max(nums[i] + i, cover)
                if cover >= len(nums) - 1:
                    return count + 1
                
            count += 1