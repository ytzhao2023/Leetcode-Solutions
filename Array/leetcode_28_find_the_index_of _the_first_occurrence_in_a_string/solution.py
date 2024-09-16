class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


haystack = "sadbutsad"
needle = "omv"
solution = Solution()
result = solution.strStr(haystack, needle)
print(result)