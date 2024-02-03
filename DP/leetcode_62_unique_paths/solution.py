class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        #  initialize the dp list.
        dp = [[0 for j in range(n)] for i in range(m)]

        # initialize the first row and first column with 1.
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1

        # calculate the number of unique paths.
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        

       

solution = Solution()
result = solution.uniquePaths(3,4)
print(result)