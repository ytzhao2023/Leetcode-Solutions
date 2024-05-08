class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_index = 0
        appearance_count = 1
        
        for fast_index in range(1, len(nums)):
            if nums[fast_index] == nums[fast_index - 1]:
                appearance_count += 1
            else:
                appearance_count = 1
                
            if appearance_count <= 2:
                slow_index += 1
                nums[slow_index] = nums[fast_index]
        
        return slow_index + 1
           

