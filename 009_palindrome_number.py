class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #return list(reversed(str(x))) == list(str(x))
# Runtime: 104 ms, faster than 43.79% of Python online submissions for Palindrome Number.
# Memory Usage: 13.3 MB, less than 85.23% of Python online submissions for Palindrome Number.   
        #return str(x) == str(x)[::-1]
# Runtime: 66 ms, faster than 84.25% of Python online submissions for Palindrome Number.
# Memory Usage: 13.5 MB, less than 35.99% of Python online submissions for Palindrome Number.
        # if x<0:
        #     return False

        # inputNum = x
        # newNum = 0
        # while x>0:
        #     newNum = newNum * 10 + x%10
        #     x = x//10
        #     print(f'newNum:{newNum}, x:{x}')
        # return newNum == inputNum
# Runtime: 129 ms, faster than 20.48% of Python online submissions for Palindrome Number.
# Memory Usage: 13.2 MB, less than 85.27% of Python online submissions for Palindrome Number.
        if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
            return False
	
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10
            print(f'x: {x}, result: {result}')

        return True if (x == result or x == result // 10) else False        
# Runtime: 106 ms, faster than 41.91% of Python online submissions for Palindrome Number.
# Memory Usage: 13.1 MB, less than 96.99% of Python online submissions for Palindrome Number.
a = Solution()
x=123454321
print(reversed(str(x)))
print(list(reversed(str(x))))
print(a.isPalindrome(x))