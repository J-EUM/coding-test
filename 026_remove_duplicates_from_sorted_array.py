class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        return len(nums)
# Runtime: 129 ms, faster than 68.49% of Python online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.3 MB, less than 98.90% of Python online submissions for Remove Duplicates from Sorted Array.
nums = [0,0,4,1,1,1,2,2,3,3]
a = Solution()
res = a.removeDuplicates(nums)
print(res)