class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # nums = [n for n in nums if n != val]
        # return len(nums) 
        # 이게 왜 안되는지 모르겠음ㅠㅠ

        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
        # 이거 정답인데 위에랑 num도, 리턴값도 똑같은데...왜....why....
# Runtime: 24 ms, faster than 83.80% of Python online submissions for Remove Element.
# Memory Usage: 13.5 MB, less than 12.36% of Python online submissions for Remove Element.

# in-place방식으로 풀라는 말이 있는데 in-place알고리즘: 보조 데이터 구조 를 사용하지 않고 입력을 변환하는 알고리즘(transforms input using no auxiliary data structure.) 라고 돼있다.
# len(nums)를 사용하면 안되는건가..?

nums = [3,2,2,3]
val = 3
a = Solution()
res = a.removeElement(nums, val)
print(res)