def solution(n):
    answer = [[0] * n for _ in range(n)]
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c = 0, 0
    dir_idx = 0
    
    for num in range(1, n**2+1):
        answer[r][c] = num
        
        dr, dc = move[dir_idx]
        nr, nc = r + dr, c + dc
        
        # 방향 전환
        if not (0 <= nr < n and 0 <= nc < n) or answer[nr][nc] != 0:
            dir_idx = (dir_idx + 1) % 4
            dr, dc = move[dir_idx]
            nr, nc = r + dr, c + dc
        
        r, c = nr, nc
    return answer