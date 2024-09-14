class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numeral = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 
        'V': 5, 'I': 1}
        
        result = 0
        for i in range (len(s) -1 ):
            if roman_numeral[s[i]] < roman_numeral[s[i+1]]:
                result -= roman_numeral[s[i]]
            else:
                result += roman_numeral[s[i]]
        result += roman_numeral[s[-1]]
        
        return result

s = "XI"
solution = Solution()
result = solution.romanToInt(s)
print(result)