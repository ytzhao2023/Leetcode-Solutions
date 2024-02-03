class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # if obstacleGrid[0][0] == 1:
        #     return 0

        # if m == 1 and 1 in obstacleGrid[0]:
        #     return 0
        
        # if n == 1 and 1 in [row[0] for row in obstacleGrid]:
        #     return 0

        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
            else:
                dp[i][0] = 1
        
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                break
            else:
                dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print("all the elements in dp list")
        for i in range(m):
            row_values = " ".join(str(dp[i][j]) for j in range(n))
            print(row_values)
        
        return dp[m-1][n-1]
    

        
solution = Solution()
result = solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print(result)