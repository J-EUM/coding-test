class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # opening=['(', '[', '{']
        # closing=[')', ']', '}']
        # res=''
        # for ch in s:
        #     if ch in opening:
        #         res += ch
        #     elif ch in closing:
        #         if res == '':
        #             return False
        #         elif res[-1] in opening:
        #             if opening.index(res[-1]) == closing.index(ch):
        #                 res = res[:-1]
        #             else:
        #                 res += ch
        # if res == '':
        #     return True
        # else:
        #     return False
# Runtime: 49 ms, faster than 9.11% of Python online submissions for Valid Parentheses.
# Memory Usage: 13.7 MB, less than 29.90% of Python online submissions for Valid Parentheses.
        # res = ''   
        # for ch in s:
        #     res += ch
        #     res = res.replace('()','').replace('[]','').replace('{}','')
        # if not len(res):
        #     return True
        # else:
        #     return False
# Runtime: 143 ms, faster than 5.02% of Python online submissions for Valid Parentheses.
# Memory Usage: 13.5 MB, less than 55.79% of Python online submissions for Valid Parentheses.
        stack = [0]
        mapping = {0: None, '(':')', '[':']', '{':'}'}
        for c in s:
            if c in mapping: 
                stack.append(c)
            else:
                if mapping[stack.pop()] != c: return False
        return stack == [0]
# Runtime: 39 ms, faster than 28.22% of Python online submissions for Valid Parentheses.
# Memory Usage: 13.4 MB, less than 94.89% of Python online submissions for Valid Parentheses.