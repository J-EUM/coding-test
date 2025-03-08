# def solution(operations):
#     answer = []
    
#     for operation in operations:
#         if operation[0] == "I":
#             a, b = operation.split()
#             answer.append(int(b))
            
#         if operation == "D 1":
#             if answer:
#                 v = max(answer)
#                 idx = answer.index(v)
#                 answer.pop(idx)
            
#         if operation == "D -1":
#             if answer:
#                 v = min(answer)
#                 idx = answer.index(v)
#                 answer.pop(idx)
        
#     if answer:
#         return [max(answer), min(answer)]
#     else:
#         return [0, 0]

# import heapq

# def solution(operations):
#     heap = []

#     for operation in operations:
#         operator, operand = operation.split(' ')
#         operand = int(operand)

#         if operator == 'I':
#             heapq.heappush(heap, operand)
#         elif heap:
#             if operand < 0:
#                 heapq.heappop(heap)
#             else:
#                 heap.remove(max(heap))

#     if not heap:
#         return [0, 0]

#     return [max(heap), heap[0]]


import heapq

def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙 (음수 저장)
    valid = {}     # 실제 존재하는 원소를 추적 (동기화 문제 해결)

    for op in operations:
        cmd, num = op.split()
        num = int(num)

        if cmd == "I":  # 삽입 연산
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            valid[num] = valid.get(num, 0) + 1  # 개수 증가

        elif cmd == "D" and valid:  # 삭제 연산 (큐가 비었으면 무시)
            if num == 1:  # 최댓값 삭제
                while max_heap:
                    max_val = -heapq.heappop(max_heap)
                    if valid.get(max_val, 0) > 0:
                        valid[max_val] -= 1
                        break
            else:  # 최솟값 삭제
                while min_heap:
                    min_val = heapq.heappop(min_heap)
                    if valid.get(min_val, 0) > 0:
                        valid[min_val] -= 1
                        break

    # 남은 원소 정리
    while min_heap and valid.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
    while max_heap and valid.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)

    # 결과 반환
    if not valid or all(v == 0 for v in valid.values()):
        return [0, 0]
    return [-max_heap[0], min_heap[0]]  # 최댓값, 최솟값 반환