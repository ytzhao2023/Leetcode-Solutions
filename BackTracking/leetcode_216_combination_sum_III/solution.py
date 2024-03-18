class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.backTracking(n, k, 0, 1, [], result)
        return result
    
    def backTracking(self, targetSum, k, currentSum, startIndex, path, result):
        if currentSum > targetSum:
            return
        if len(path) == k:
            if currentSum == targetSum:
                result.append(path[:])
            return
        
        for i in range(startIndex, 9 - (k - len(path)) + 2):
            currentSum += i
            path.append(i)
            self.backTracking(targetSum, k , currentSum, i + 1, path, result)
            currentSum -= i
            path.pop()