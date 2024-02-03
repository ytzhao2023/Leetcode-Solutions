class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0

        for i in range(len(s)):
            left1, right1 = self.expand_around_center(s, i, i)
            left2, right2 = self.expand_around_center(s, i, i+1)

            if right1 - left1 > end - start:
                start, end = left1, right1
            
            if right2 - left2 > end - start:
                start, end = left2, right2
            
        print(start, end)
        
        return s[start : end + 1]


    def expand_around_center(self, s, left, right):
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return left + 1, right - 1


s = Solution()
result = s.longestPalindrome("racecar")
print(result)
