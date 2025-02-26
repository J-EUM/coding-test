def solution(storage, requests):
    answer = 0
    n = len(storage)  # 세로
    m  = len(storage[0])  # 가로
    
    board = [[''] * (m + 2)] + [[''] + list(s) + [''] for s in storage] + [[''] * (m + 2)]
    
    def get_removable():
        q = [(0, 0)]
        visited = [[0] * (m + 2) for _ in range(n + 2)]
        removable = []
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while q:
            x, y = q.pop()
            visited[x][y] = 1
            if board[x][y] != '' and (x, y) not in removable:
                removable.append((x, y))
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if a >= 0 and a < (n + 2) and b >= 0 and b < (m + 2) and visited[a][b] == 0 and board[x][y] == '':
                    q.append((a, b))
                    
        return removable
                    
                    
                    
                    
                
    
    for request in requests:
        # 크레인
        if len(request) == 2:
            for i in range(n):
                for j in range(m):
                    if board[i + 1][j + 1] == request[0]:
                        board[i + 1][j + 1] = ''
                        
        # 지게차
        else:
            removable = get_removable()
            for x, y in removable:
                if board[x][y] == request[0]:
                    board[x][y] = ''
            
                        

    for row in board:
        for ch in row:
            if ch != '':
                answer += 1

    return answer