class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 내가푼거: 모든 경로를 다 계산함
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
# 결과: Time Limit Exceeded


# 다른풀이
# https://leetcode.com/problems/gas-station/discuss/1706142/JavaC%2B%2BPython-An-explanation-that-ever-EXISTS-till-now!!!!

# total_surplus: 한바퀴 돈다고 할때 총 남은 기름
# surplus: 출발지점 start부터 i까지 가며 남은 기름
# i->i+1로가는데 gas[i]이 든다

# 생각해보면 만약에 0에서 출발해서 2까지 가는데 성공했는데 2->3에서 실패했으면 0-2어디서 출발하든 실패임. 2->3으로 갈때 무조건 실패. 그래서 1, 2에서 출발하는 경우는 더이상 따질 필요가 없다. 바로 3부터 시작했을때 경우부터 다시 따지면 된다.
# start=0일때 i(ex 2)에서 surplus<0이면 start가 1일 경우를 따지기 위해 다시 되돌아가서 확인하는 것이 아니고(어차피 같은 구간에서 surplus<0이될것) start를 i+1(3)로 바꾸고, 다음역부터 시작해서(surplus=0) 계속 간다. 그래서 출발지점을 따로 1씩 늘려갈 필요가 없기 때문에 반복문은 하나만 필요하다.
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start
# Runtime: 1496 ms, faster than 26.25% of Python online submissions for Gas Station.
# Memory Usage: 19.7 MB, less than 70.44% of Python online submissions for Gas Station.