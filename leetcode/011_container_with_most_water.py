class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # max = 0
        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         w = j - i
        #         h = min(height[i], height[j])
        #         area = w * h
        #         if max < area:
        #             max = area
        # return max
# 시간제한 걸림
        
        i, j = 0, len(height) - 1
        water = 0
        while i < j: # 반복문을 한번만 사용하면서 인덱스 두개 조작..
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]: # 높이가 더 높은쪽은 그대로 두고 낮은쪽을 한칸씩 움직이면서 면적계산
                i += 1
            else:
                j -= 1
        return water
# Runtime: 1499 ms, faster than 36.21% of Python online submissions for Container With Most Water.
# Memory Usage: 24 MB, less than 22.18% of Python online submissions for Container With Most Water.

a = Solution()
height = [1,8,6,2,5,4,8,3,7]

res = a.maxArea(height)
print(res)