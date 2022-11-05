class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums = [n for n in nums if n != val]
        print(nums)
        return len(nums)

nums = [3,2,2,3]
val = 3
a = Solution()
res = a.removeElement(nums, val)
print(res)