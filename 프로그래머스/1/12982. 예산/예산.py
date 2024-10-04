def solution(d, budget):
    # d.sort() 
    # while sum(d) > budget:
    #     d.pop()      
    # return len(d)
    
    d.sort()
    count = 0
    
    for cost in d:
        if budget - cost >= 0:
            budget -= cost
            count += 1
        else:
            break
            
    return count