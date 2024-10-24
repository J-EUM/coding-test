import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        answer += 1
    
    return answer
# 원소 하나일때, 만들수없을때->1개남았는데 k미만