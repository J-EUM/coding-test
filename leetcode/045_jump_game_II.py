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


a = Solution()
#nums = [2,3,1,1,4] #Output: 2
nums = [10,1,1,1,1,1,1,1,1,2,3,0,1,4] #Output: 2

print(a.jump(nums))