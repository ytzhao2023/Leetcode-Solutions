class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return  0
        
        # Initialize an array to store Fibonacci numbers up to n
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        for element in dp:
            print(element)
        print("all the elements in dp list")
        
        return dp[n]
solution = Solution()
result = solution.fib(5)
print(result)