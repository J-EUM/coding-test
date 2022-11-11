class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # g.sort()
        # s.sort()

        # cnt = 0

        # while len(g) and len(s):
        #     child = g.pop(0)
        #     for i, cookie in enumerate(s):
        #         print(child, cookie)
        #         if child <= cookie:
        #             s.pop(i)
        #             cnt += 1
        #             break
        # return cnt
# Runtime: 762 ms, faster than 12.03% of Python online submissions for Assign Cookies.
# Memory Usage: 15 MB, less than 23.80% of Python online submissions for Assign Cookies.
        g.sort()
        s.sort()
        
        childi = 0
        cookiei = 0
        
        while cookiei < len(s) and childi < len(g): # 인덱스 두개를 활용해서 반복문을 한번만 돌린다
            if s[cookiei] >= g[childi]:
                childi += 1
            cookiei += 1
        
        return childi
# Runtime: 195 ms, faster than 82.09% of Python online submissions for Assign Cookies.
# Memory Usage: 14.3 MB, less than 99.47% of Python online submissions for Assign Cookies.

g = [1,2]
s = [1,2,3]

a = Solution()
res = a.findContentChildren(g, s)
print(res)