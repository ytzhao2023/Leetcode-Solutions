class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(candidates, target, 0, 0, [], result)
        return result

    def backtracking(self, candidates, target, total, startIndex, path, result):
        if total > target:
            return
        
        if total == target:
            result.append(path[:])
            
        for i in range(startIndex, len(candidates)):
            total += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, total, i, path, result)
            total -= candidates[i]
            path.pop()
        