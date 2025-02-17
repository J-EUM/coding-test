def solution(schedules, timelogs, startday):
    # 1은 월요일, 2는 화요일, 3은 수요일, 4는 목요일, 5는 금요일, 6은 토요일, 7은 일요일
    # 1:0-4(5), 2:-1~3(4), 3:-2~
    def get_time(log):
        return (log // 100) * 60 + (log % 100)
    answer = 0
    for i in range(len(schedules)):
        schedule = get_time(schedules[i])
        cnt = 0
        for j in range(1-startday, 6-startday):
            timelog = get_time(timelogs[i][j])
            if timelog - schedule <= 10:
                cnt += 1
        if cnt >= 5:
            answer += 1
    
    return answer