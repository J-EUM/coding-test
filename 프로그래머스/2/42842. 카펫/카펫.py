def solution(brown, yellow):
    for a in range(yellow, int(yellow ** (1/2) - 1), -1):
        if yellow % a == 0:
            b = yellow // a
            if (a + b + 2) * 2 == brown:
                return [a + 2, b + 2]
    return 0
