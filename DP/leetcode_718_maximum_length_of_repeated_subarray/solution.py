class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        """
        # If dp[i][j] ending at nums[i] and nums[j], when we initializt dp list
        # we need discuss dp[i][0] and dp[0][j]. So, dp[i][j] represents the 
        # length of the longest common subarray ending at nums1[i-1] and 
        # nums2[j-1]. Becausr we add one more row and column just equal to 0 to
        # origin 2d lists, and current nums1[i] and nums2[j] are equal to 
        # former nums1[i-1] and nums2[j-1].
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        max_length = 0

        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_length = max(max_length, dp[i][j])

        return max_length
        """
        """
        in the block, we give the code about dp[i][j] represents the maximum 
        length of the longest common subarray ending at nums1[i] and nums2[j].
        """

        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        max_length = 0

        # initilize the first row and column.
        for i in range(len(nums1)):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
        for j in range(len(nums2)):
            if nums2[j] == nums1[0]:
                dp[0][j] = 1

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_length = max(max_length, dp[i][j])

        return max_length
    
solution = Solution()
nums1 = [1,2,3,2,8]
nums2 = [5,6,1,4,7]
result = solution.findLength(nums1, nums2)
print(result)