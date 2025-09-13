def solution(board, moves):
    cnt = 0
    st = []
    idx_moves = [i-1 for i in moves]    # 인덱스 맞춰서 -1씩
    # board zip으로 회전
    n_board = [list(col) for col in zip(*board)]
    for m in idx_moves:
        if n_board[m] == [0] * len(n_board[0]):
            continue
        for j in range(len(n_board[0])):
            cur = n_board[m][j]
            if cur == 0:
                continue
            n_board[m][j] = 0
            
            if st and st[-1] == cur:
                st.pop()
                cnt += 2
            else:
                st.append(cur)
            
            break   # 한 번 집었으면 이 move는 끝!
                
    return cnt