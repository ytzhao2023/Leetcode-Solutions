class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
                
            if counts[num] > len(nums) / 2:
                return num
            

nums = [1, 1, 1, 1, 1, 5, 6, 7]
solution = Solution()
result = solution.majorityElement(nums)
print(result)