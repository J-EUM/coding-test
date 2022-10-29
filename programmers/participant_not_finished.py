# 내풀이: 딕셔너리
def solution(participant, completion):
    d = {}
    for p in participant:
        if p in d.keys():
            d[p] += 1
        else:
            d[p] = 1
    for c in completion:
        d[c] -= 1
    for name, v in d.items():
        if v:
            return name
