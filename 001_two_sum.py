class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)-1):
        #     print(f'i={nums[i]}')
        #     for j in range(i+1, len(nums)):
        #         print(f"j={nums[j]}")
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
# Runtime: 6319 ms, faster than 10.71% of Python online submissions for Two Sum.
# Memory Usage: 14.3 MB, less than 67.72% of Python online submissions for Two Sum.

        for i, value in enumerate(nums):
            print(nums)
            print(f"i={i}, value={value}")
            remaining = target - value
            nums[i] = None
            if remaining in nums:
                return [i, nums.index(remaining)]
# Runtime: 1190 ms, faster than 42.52% of Python online submissions for Two Sum.
# Memory Usage: 14.2 MB, less than 67.72% of Python online submissions for Two Sum.