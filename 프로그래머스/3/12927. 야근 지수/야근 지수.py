import heapq

def solution(n, works):
    answer = 0
    heap = [-w for w in works]
    heapq.heapify(heap)
    for _ in range(n):
        w = -heapq.heappop(heap)
        if w > 0:
            w -= 1
        heapq.heappush(heap, -w)
        
    return sum(w**2 for w in heap)
