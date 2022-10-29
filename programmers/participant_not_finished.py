# 내풀이: 딕셔너리
# def solution(participant, completion):
#     d = {}
#     for p in participant:
#         if p in d.keys():
#             d[p] += 1
#         else:
#             d[p] = 1
#     for c in completion:
#         d[c] -= 1
#     for name, v in d.items():
#         if v:
#             return name

# 다른풀이: hash()
# 키에 문자열 대신 문자열의 해시값을 넣어서 더 빠르게 했다
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer