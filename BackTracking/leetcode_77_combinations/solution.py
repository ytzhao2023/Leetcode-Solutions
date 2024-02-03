class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = [] 
        self.backtracking(n, k, 1, [], result)
        return result
    
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n+1):
            path.append(i)
            self.backtracking(n, k, i+1, path, result)
            path.pop()
    
solution = Solution()
n = [2, 5, 9, 8, 7]
k = 3
result = solution.combine(n, k)
print(result)

        