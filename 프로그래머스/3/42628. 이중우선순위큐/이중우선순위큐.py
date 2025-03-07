# import heapq

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

import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]