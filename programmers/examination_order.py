# 내풀이
# def solution(emergency):
#     l = len(emergency)
#     answer = [0 for i in range(l)]  # 순서리스트: 환자수랑 같은 길이 리스트를 0으로 초기화해놓고
#     for i in range(l):
#         r = emergency.index(max(emergency)) # 제일 급한 환자 순서대로 1 2 3...넣는다
#         answer[r] = i+1
#         emergency[r] = 0
#     return answer

# 다른풀이: sort한 리스트의 인덱스로 새로운 배열 만들기
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

emergency = [3, 76, 24]
s = sorted(emergency, reverse=True)
print(s)
print(emergency.index(3))

print(s.index(3))
print(s.index(76))
print(s.index(24))
