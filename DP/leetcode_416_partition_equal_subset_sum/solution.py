class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dp means total sum of the elements in the bag.
        # as the problem descripted, the total sum would equal or less than 200 * 100, so we can define the dp greater than 10001.
        dp = [0] * 10001
        total_sum = 0
        for i in range(nums):
            total_sum += nums[i]

        if total_sum % 2 == 1:
            return False
        target = total_sum // 2

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = max(dp[j], dp[j-num] + num)

        if dp[target] == target:
            return True
        else:
            return False