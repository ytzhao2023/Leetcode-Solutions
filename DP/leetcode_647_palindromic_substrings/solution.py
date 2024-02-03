class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # p.s. means palindromic substrings.
        # If we define the dp list represents the number of p.s. of string s, 
        # it's hard to find the recurrence relation. So we define 2d dp list 
        # to store the number of p.s.. dp[i][j] represents whether the 
        # substring from index i to index j is p.s..
        dp = [[False] * len(s) for _ in range(len(s))]

        result = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    # if len(s) is 1 or 2, the string must be p.s.
                    if j-i<=1:
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        result += 1
                        dp[i][j] = True
        return result