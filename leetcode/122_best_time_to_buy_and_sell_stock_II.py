class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 올라가기전에 사야되고 내려가기전에 팔아야함
        # 두개씩 확인하면서 앞<뒤인곳에서 뒤-앞을 결과에 더하면 된다.
        res = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                res += (prices[i+1] - prices[i])
        return res


#다른풀이
        # if prices[i] < prices[i+1]:
        #         res += (prices[i+1] - prices[i])
        # 위 두 줄을 
        # res += max(prices[i+1] - prices[i], 0) 이렇게 바꾸면 속도가 빨라진다 112ms -> 60ms

        # 리스트컴프리헨션
        # 아래 한줄로 가능 시간은 가장 오래걸림
        # return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

#prices = [7,1,5,3,6,4] # Output: 7
#prices = [1,2,3,4,5] # Output: 4
prices = [7,6,4,3,1] # Output: 0

a = Solution()
print(a.maxProfit(prices))