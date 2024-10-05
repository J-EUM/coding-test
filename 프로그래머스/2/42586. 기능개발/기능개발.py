def solution(progresses, speeds):
    answer = []
    days_left = [(99 - progresses[i]) // speeds[i] + 1 for i in range(len(progresses))]
    
    day = days_left[0]
    cnt = 1
    
    for d in days_left[1:]:  # 첫 번째 요소는 이미 처리했으므로 슬라이싱
        if d <= day:
            cnt += 1
        else:
            answer.append(cnt)
            day = d
            cnt = 1
    
    answer.append(cnt)
    return answer
