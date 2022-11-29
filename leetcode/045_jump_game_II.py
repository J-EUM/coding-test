class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums[0] 부터 시작
        # 0부터 nums[0]만큼 더한곳까지 갈수있음
        # 1에서 nums[1]만큼 더한곳까지 갈수있음
        # 2에서 nums[2]만큼 더한곳까지 갈수있음
        # i + nums[i] >= len(nums)-1(마지막인덱스)면 점프성공한거임
        # cnt로 몇번 점프했는지 세고
        # res = min(res, cnt)
        # return res

        # 인덱스 범위는 i ~ i+nums[i]

        # def get_res(i, cnt, res):
        #     cnt += 1
        #     if i + nums[i] >= len(nums) - 1 :
        #         res = min(res, cnt)
        #         print(res)
        #         return res

        #     return get_res(i + 1, cnt, res)

        # return get_res(0, 0, 100000)

        #실패...이렇게하면 cnt가 점프할때마다 늘어나는게 아니고 그냥 한칸점프하면서 계속가다가 마지막에만 한방점프함
        # nums = [10,1,1,1,1,1,1,1,1,2,3,0,1,4]면 2가나와야되는데 11이 나옴
        # 모르겠다악

        

#다른사람풀이
# The idea is to maintain two pointers left and right, where left initialy set to be 0 and right set to be nums[0].
# So points between 0 and nums[0] are the ones you can reach by using just 1 jump.
# Next, we want to find points I can reach using 2 jumps, so our new left will be set equal to right, and our new right will be set equal to the farest point we can reach by two jumps. which is:
# right = max(i + nums[i] for i in range(left, right + 1)

# 인덱스 두개 left, right를 둔다 초기값 left: 0, right: nums[0]
# 0, nums[0]사이 left~right 애들이 1번의 점프를 통해 갈 수 있는 곳들.
# nums[0]+1부터는 2번의 점프를 통해 갈 수 있다. 갈수있는 최대 인덱스(right)는 현재 left와 right사이값 i + nums[i]중 가장 큰 숫자
# nums = [2,3,1,1,4]일때
# 1번점프해서는 0,1,2인덱스까지 갈 수 있고
# 2번점프해서는 1+3(1+nums[1])=4, 2+1(2+nums[2])=3까지 갈 수 있다.
# right = max(i + nums[i] for i in range(left, right + 1)
# 이 작업을 right < len(nums) - 1일때까지 점프 횟수(times)를 1씩 늘리면서 반복한다. 
# 모든 경우의 수를 다 계산하려고하지 않고 인덱스 두개로 범위를 지정해서 점프1범위, 점프2범위 이렇게 생각하는게 포인트였다..!ㅠ
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times


a = Solution()
#nums = [2,3,1,1,4] #Output: 2
nums = [10,1,1,1,1,1,1,1,1,2,3,0,1,4] #Output: 2

print(a.jump(nums))