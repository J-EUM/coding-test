def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        t = min(i + 1, citations[i])
        answer = max(answer, t)
    
    return answer

# 3 0 6 1 5
# 0 2 3 5 6 번 이상 인용
# 5 4 3 2 1 개 (여기가 위에꺼보다 같거나크)

# 6 5 4 2 0
# 1 2 3 4 5
#     3 2아니고
# 2아니고 3이답