def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0]
        j = c[1]
        k = c[2]
        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer