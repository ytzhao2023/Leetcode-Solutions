class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.strip()
        s_list = new_s.split(' ')
        return len(s_list[-1])
    

s = " hello  world"
solution = Solution()
result = solution.lengthOfLastWord(s)
print(result)