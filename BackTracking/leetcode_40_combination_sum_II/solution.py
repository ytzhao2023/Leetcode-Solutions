class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.backtrack(candidates, target, 0, 0, [], result)
        return result
    
    def backtrack(self, candidates, target, total, startIndex, path, result):
        if total == target:
            result.append(path[:])
            return
        
        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i-1]:
                continue
            
            if total + candidates[i] > target:
                break
            
            total += candidates[i]
            path.append(candidates[i])
            
            self.backtrack(candidates, target, total, i + 1, path, result)
            total -= candidates[i]
            path.pop()
            
            
        