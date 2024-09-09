class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        appearance_count = 0
        candidate = None
        
        for num in nums:
            if appearance_count == 0:
                candidate = num
                appearance_count = 1
            
            elif num == candidate:
                appearance_count += 1
                
            else:
                appearance_count -= 1
        
        return candidate
                