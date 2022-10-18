class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # r_dict = {
        #     'I': 1,
        #     'V': 5,
        #     'X': 10,
        #     'L': 50,
        #     'C': 100,
        #     'D': 500,
        #     'M': 1000
        # }
        # res = 0
        # for c in s:
        #     res += r_dict[c]
        
        # if 'IV' in s or 'IX' in s: res -= 2
        # if 'XL' in s or 'XC' in s: res -= 20
        # if 'CD' in s or 'CM' in s: res -= 200

        # return res

#Runtime: 71 ms, faster than 55.76% of Python online submissions for Roman to Integer.
#Memory Usage: 13.4 MB, less than 80.61% of Python online submissions for Roman to Integer.

        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
# Runtime: 41 ms, faster than 91.17% of Python online submissions for Roman to Integer.
# Memory Usage: 13.7 MB, less than 8.55% of Python online submissions for Roman to Integer.

a = Solution()

s = "MCDLXXVI" #1476
print(list(s))
print(a.romanToInt(s))
