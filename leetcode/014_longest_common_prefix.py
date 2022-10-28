class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # res = ''
        # strs.sort()

        # s = strs[0]
        # e = strs[-1]

        # l = len(min(s, e, key=len))

        # for i in range(l):
        #     if s[i] != e[i]:
        #         return res
        #     else:
        #         res += s[i]
        # return res
# Runtime: 32 ms, faster than 69.38% of Python online submissions for Longest Common Prefix.
# Memory Usage: 13.4 MB, less than 99.13% of Python online submissions for Longest Common Prefix.
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
# Runtime: 32 ms, faster than 69.38% of Python online submissions for Longest Common Prefix.
# Memory Usage: 13.6 MB, less than 58.27% of Python online submissions for Longest Common Prefix.


