class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # 붙여서 심으면 안되고 사이사이 빈칸이 있어야함
        # 이전값, 현재값, 다음값이 모두 0이면 심을수 있음
        # 그런데 원래 두개연속 심어진 경우는 없으니까 현재위치가 1이면 다음칸은 무조건 0일테니 현재가 1이면 두칸 넘어가서 현재위치, 다음위치만 보면 된다.
        i = 0
        while(i < len(flowerbed)):
            # flowerbed[i]가
            # 1이면 두칸 점프
            # 0인데 다음칸이 1이면 3칸점프(어차피 다음칸 ,다다음칸엔 못심음)
            # 0인데 다음칸이 0이면 심는다 n -= 1 심고나서 2칸점프(이번칸에 심었으니까 다음칸엔 못심음)
            # 0인데 i가 마지막 인덱스면 심는다(앞에서 2칸 3칸씩 점프했으니까 이전칸은 무조건 0)
            if flowerbed[i]:
                i += 2
            else:
                if i == len(flowerbed) - 1 or not flowerbed[i + 1]:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                else:
                    i += 3

        if n > 0:
            return False
        else:
            return True
# Runtime: 342 ms, faster than 24.76% of Python online submissions for Can Place Flowers.
# Memory Usage: 13.6 MB, less than 89.94% of Python online submissions for Can Place Flowers.


a = Solution()

flowerbed = [1,0,0,0,1]
n = 1
# Output: true

# flowerbed = [1,0,0,0,1]
# n = 2
# Output: false

print(a.canPlaceFlowers(flowerbed, n))