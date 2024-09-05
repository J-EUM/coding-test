def solution(n):
    answer = ''
    subak = '수박' * n
    for i in range(n):  
        answer += subak[i]
    return answer