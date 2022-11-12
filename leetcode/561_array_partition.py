class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # res = 0
        # i = 0

        # while i < len(nums):
        #     res += min(nums[i], nums[i+1]) # 아 정렬을 했으니까 min(nums[i])가 무조건 작구나..!
        #     i += 2

        # return res
# Runtime: 624 ms, faster than 12.75% of Python online submissions for Array Partition.
# Memory Usage: 15.5 MB, less than 29.76% of Python online submissions for Array Partition.

        # nums.sort()
        # res = 0
        # i = 0

        # while i < len(nums):
        #     res += nums[i] # 이부분만 바꾼거
        #     i += 2

        # return res
# Runtime: 320 ms, faster than 76.11% of Python online submissions for Array Partition.
# Memory Usage: 15.5 MB, less than 29.76% of Python online submissions for Array Partition.

        return sum(sorted(nums)[::2]) # 한줄풀이 리스트 자체를 짝수인덱스만 남겨놓고 다 더했다
# Runtime: 558 ms, faster than 36.84% of Python online submissions for Array Partition.
# Memory Usage: 15.3 MB, less than 90.28% of Python online submissions for Array Partition.

a = Solution()
nums = [6,2,6,5,1,2]
print(a.arrayPairSum(nums))