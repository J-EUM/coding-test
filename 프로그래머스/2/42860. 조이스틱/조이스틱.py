def solution(name):
    answer = 0
    
    # A-J: 9, 26-9
    # A-N: 13, 26-13
    # JEROEN
    # 9 4 ...
    # JAN
    # 9 0 13
    
    # "BBAAAAABBB" : 10
    
    steps = []
    
    for ch in name:
        diff = ord(ch) - ord("A")
        steps.append(min(diff, 26-diff))
        
    if sum(steps) == 0:
        return 0
    
    # AAA  BB  A
    # 000110
    # ->: 00011 4칸
    # <-: 0011  3칸
    
    left_count = 0
    right_count = 0
    
    for i in steps[1:]:
        if i == 0:
            left_count += 1
        else:
            break
    
    for i in steps[::-1]:
        if i == 0:
            right_count += 1
        else:
            break
    
    return sum(steps) + len(steps) - max(left_count, right_count) - 1