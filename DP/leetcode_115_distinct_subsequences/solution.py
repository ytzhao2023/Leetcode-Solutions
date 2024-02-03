class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

    
        m, n = len(s), len(t)
        # dp means the number of distinct subsequences between s ending at 
        # index i and the prefix of t ending at index j.
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if j == 0:
                    dp[i][0] = 1
                elif i == 0:
                    dp[0][j] = 0
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1] # return dp[m][n]
        