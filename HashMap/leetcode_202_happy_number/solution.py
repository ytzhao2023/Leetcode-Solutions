class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res =[]
        while n != 1:
            sum = 0
            for i in str(n):
                sum += int(i)**2
            n = sum
            if n in res:
                return False
            res.append(n)
        return True

n = 19
s = Solution()
print(s.isHappy(n))
