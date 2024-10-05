# def solution(progresses, speeds):
#     answer = []
#     days_left = [(99 - progresses[i]) // speeds[i] + 1 for i in range(len(progresses))]
    
#     day = days_left[0]
#     cnt = 1
    
#     for d in days_left[1:]:  # 첫 번째 요소는 이미 처리했으므로 슬라이싱
#         if d <= day:
#             cnt += 1
#         else:
#             answer.append(cnt)
#             day = d
#             cnt = 1
    
#     answer.append(cnt)
#     return answer

def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        days_left = (100 - p + s - 1) // s  # 남은 일수 계산 (올림 효과)
        if not Q or Q[-1][0] < days_left:
            Q.append([days_left, 1])  # 새로운 배포 그룹 시작
        else:
            Q[-1][1] += 1  # 같은 배포 그룹에 포함
    return [q[1] for q in Q]

