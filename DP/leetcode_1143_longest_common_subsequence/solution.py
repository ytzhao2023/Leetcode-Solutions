class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # The dp[i][j] represents the length of the longest common subsequence ending at i-1 in text1 and j-1 in text2.
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[len(text1)][len(text2)]
    

solution = Solution()
text1 = "abcde"
text2 = "ace"
result = solution.longestCommonSubsequence(text1, text2)
print(result)