from collections import Counter

def solution(k, tangerine):
    answer = 0
    c = Counter(tangerine)
    tangerine.sort(key=lambda x: (-c[x], x))
    
    
    
    return len(set(tangerine[:k]))
