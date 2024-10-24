from collections import Counter

def solution(k, tangerine):
    answer = 0
    c = Counter(tangerine)
    tangerine.sort()
    tangerine.sort(key=lambda x: (-c[x]))
    
    
    
    return len(set(tangerine[:k]))
