class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = sorted(nums)
        # for i in range (0, nums[-1]+2):
        #     if i not in nums:
        #         return i
# Runtime: 1780 ms, faster than 19.73% of Python online submissions for Missing Number.
# Memory Usage: 14.9 MB, less than 26.18% of Python online submissions for Missing Number.
        for i in range(0, len(nums)+1):
            if i not in nums:
                return i
# Runtime: 2798 ms, faster than 13.28% of Python online submissions for Missing Number.
# Memory Usage: 14.6 MB, less than 85.88% of Python online submissions for Missing Number.
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)
# Runtime: 104 ms, faster than 95.45% of Python online submissions for Missing Number.
# Memory Usage: 14.6 MB, less than 67.69% of Python online submissions for Missing Number.
