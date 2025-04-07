from collections import deque
import heapq

def solution(users, emoticons):
    # 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됩니다.
    rate = [10, 20, 30, 40]
    discount = []
    
    def dfs(path, n):
        if len(path) == n:
            discount.append(path)
            return
        for r in rate:
            dfs(path + [r], n)
        
    dfs([], len(emoticons))
        
    
    heap = []
    heapq.heapify(heap)
    for rates in discount:
        cnt = 0
        sales = 0
        for user_rate, user_price in users:
            user_spent = 0
            for rate, price in zip(rates, emoticons):
                discounted_price = price * (100 - rate) / 100
                if rate >= user_rate:
                    user_spent += discounted_price
            if user_spent >= user_price:
                cnt += 1
            else:
                sales += user_spent
        heapq.heappush(heap, [-cnt, -sales])
    cnt, sales = heapq.heappop(heap)
    return [-cnt, -sales]
