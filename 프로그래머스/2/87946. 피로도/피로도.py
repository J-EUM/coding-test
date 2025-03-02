from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for perm in permutations(dungeons):
        cnt = 0
        temp_k = k
        
        for i, j in perm:
            if temp_k >= i:
                cnt += 1
                temp_k -= j
                
        answer = max(answer, cnt)
         
    return answer