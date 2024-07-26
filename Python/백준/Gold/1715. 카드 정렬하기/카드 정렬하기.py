import sys
import heapq
def input(): return sys.stdin.readline()

n = int(input())
l = []
res = 0
for _ in range(n):
    heapq.heappush(l, int(input()))

while len(l) > 1:
    a = heapq.heappop(l)
    b = heapq.heappop(l)
    heapq.heappush(l, a + b)
    res += a + b
print(res)