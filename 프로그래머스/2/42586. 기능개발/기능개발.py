from math import ceil

def solution(progresses, speeds):
    answer = []
    max_duration = ceil((100 - progresses[0]) / speeds[0])
    count = 0
    
    for progress, speed in zip(progresses, speeds):
        duration = ceil((100 - progress) / speed)
        # duration = -(-(100 - progress) // speed)
        if max_duration < duration:
            answer.append(count)
            count = 0
            max_duration = duration
        count += 1
    
    if count > 0:
        answer.append(count)
    
    return answer

