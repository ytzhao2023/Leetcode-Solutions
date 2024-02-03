class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # dp[i][j] represents the length of the common subsequence for the 
        # substring of string s ending at index i-1 and the substring of 
        # string t ending at index j-1.
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        if dp[-1][-1] == len(s):
            return True
        
solution = Solution()
s = "ab"
t = "ahb"
result = solution.isSubsequence(s, t)
print(result)