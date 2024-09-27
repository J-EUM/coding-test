def solution(common):
    answer = 0
    a = common[0]
    b = common[1]
    c = common[2]
    
    if b-a == c-b:
        return common[-1] + (b - a)
    else:
        return common[-1] * (b // a)
    