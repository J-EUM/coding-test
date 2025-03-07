import heapq

def solution(operations):
    answer = []
    
    for operation in operations:
        if operation[0] == "I":
            a, b = operation.split()
            answer.append(int(b))
            
        if operation == "D 1":
            if answer:
                v = max(answer)
                idx = answer.index(v)
                answer.pop(idx)
            
        if operation == "D -1":
            if answer:
                v = min(answer)
                idx = answer.index(v)
                answer.pop(idx)
        
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]