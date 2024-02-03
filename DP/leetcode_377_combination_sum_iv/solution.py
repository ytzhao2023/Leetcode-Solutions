class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # Suppose dp[j] represents the number of methods to achieve the value equal to target.
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target+1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i-nums[j]]
                    print(dp[i])

        return dp[target]


solution = Solution()
nums = [1, 2, 3]
target = 4
result = solution.combinationSum4(nums, target)

print(result)
