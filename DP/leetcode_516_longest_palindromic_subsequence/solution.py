class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # p.s. means the palindromic subsequence.
        # 2d dp list represents the longest p.s. of the String s from index i 
        # to index j.
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range (len(s)):
            dp[i][i] = 1

        for i in range(len(s)-1, -1, -1):
            # when initializing the dp list, we have already analyze the 
            # situation when i = j. so the range of j start with j + 1.
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][-1]
