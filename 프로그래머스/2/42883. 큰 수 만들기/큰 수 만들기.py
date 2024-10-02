def solution(number, k):
    answer = ''
    for n in number:
        while answer and answer[-1] < n and k > 0:
            answer = answer[:-1]
            k -= 1
        answer += n
    if k > 0:
        answer = answer[:-k]
    return answer