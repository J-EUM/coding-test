class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i, j in zip(nums[:], nums[1:]):
            if target == i:
                return nums.index(i)
            if target == j:
                return nums.index(j)
            if target > i and target <= j:
                return nums.index(j)
# Runtime: 65 ms, faster than 57.99% of Python online submissions for Search Insert Position.
# Memory Usage: 14.5 MB, less than 7.78% of Python online submissions for Search Insert Position.

        if not nums:
            return 0
        
        for i, num in enumerate(nums):
            if num >= target:
                return i
        
        return len(nums)
# Runtime: 74 ms, faster than 36.10% of Python online submissions for Search Insert Position.
# Memory Usage: 14.1 MB, less than 78.36% of Python online submissions for Search Insert Position.


a = Solution()

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 7
# Output: 4

nums = [1,3,5,6]
target = 5

res = a.searchInsert(nums, target)
print(res)