class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 시작위치 0 에서 점프해서 len(nums)-1까지 가야함
        # [2,3,1,1,4]일때
        # 1번점프해서 갈수있는 인덱스의 최대값: nums[0]->2 (nums[1]=3,nums[2]=1)
        # 2번점프해서 갈수있는 인덱스의 최대값: max(1 + nums[1], 2 + nums[2]) = 4

        # nums=[3,2,1,0,4]면
        # 1번점프해서 nums[0] = 3 까지 갈수있음
        # 2번점프해서 갈수있는곳은 max(1+nums[1]=3, 2+nums[2]=3, 3+nums[3]=3) = 3 똑같음 더이상 못감

        # 점프해서 >= len(nums)-1 면 true
        # 점프했는데 아까최대값보다 크지않으면 false
        # l = 0
        # r = nums[0]

        # while r < len(nums) - 1:
        #     nxt = max(i + nums[i] for i in range(l, r + 1))
        #     if not nxt > r:
        #         return False
        #     l = r
        #     r = nxt

        # return True



        #다른풀이
        if len(nums) <= 1: # 하나짜리면 true
            return True
        j = len(nums) - 2 # 마지막-1인덱스
        i = len(nums) - 1 # 마지막인덱스
        while j > -1:               # j가 0일때까지
            if j + nums[j] >= i:    # i보다 앞에서 점프해서 i까지 올수있으면
                i = j               # 그 앞부분 확인
                j -= 1
                
            else:                   # i까지 못오면 그 전에서 올수있는지 확인
                j -= 1
        #print('i', i, 'j', j)
        if i <= 0:                  # 다 돌았을때 i가 0보다 작으면 = 끝까지 갈수있다는말
            return True
        else:                       # 아니면 중간에 끊겼으면 반대로도 못간다는말
            return False



nums = [2,3,1,1,4] # true
#nums = [3,2,1,0,4] # false
a = Solution()
res = a.canJump(nums)
print(res)