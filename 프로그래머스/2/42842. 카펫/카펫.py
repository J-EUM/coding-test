# def solution(brown, yellow):
#     for a in range(yellow, int(yellow ** (1/2) - 1), -1):
#         if yellow % a == 0:
#             b = yellow // a
#             if (a + b + 2) * 2 == brown:
#                 return [a + 2, b + 2]
#     return 0


# def solution(brown, red):
#     width = (brown + red) // 3
#     height = 3
    
#     while (width - 2) * (height - 2) != red:
#         width -= 1
#         height = (brown + red) // width
    
#     return [width, height]


def solution(brown, red):
    answer = []
    brown = (brown - 4)/2
    for i in range(1, red+1):
        if red % i == 0:
            x = red // i
            y = i
            if x + y == brown:
                answer = [x+2, y+2]
                break
    return answer
