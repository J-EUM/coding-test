class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # if sum(gas) < sum(cost):
        #     return -1

        # start = -1

        # for s in range(-len(gas), 0):
        #     tank = 0
        #     cnt = 0
        #     for i in range(s, s+len(gas)):
        #         tank += gas[i]
        #         c = cost[i]
        #         if tank - c < 0:
        #             break
        #         tank -= c
        #         cnt += 1
        #     if cnt == len(gas):
        #         start = s + len(gas)

        # return start
# Time Limit Exceeded

        


a = Solution()

# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]

gas = [2,3,4]
cost = [3,4,3]
res = a.canCompleteCircuit(gas, cost)

print(res)