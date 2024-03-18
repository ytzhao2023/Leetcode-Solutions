class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone_mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                result.append(combination)
                
            else:
                for letter in phone_mapping[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
                    
        result = []
        backtrack("", digits)
        return result