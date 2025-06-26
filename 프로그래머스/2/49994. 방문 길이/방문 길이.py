def location(r, c, dir):
    if dir == 'U':
        nr, nc = r, c+1
    elif dir == 'D':
        nr, nc = r, c-1
    elif dir == 'R':
        nr, nc = r+1, c
    elif dir == 'L':
        nr, nc = r-1, c
    return nr, nc

def check_range(r, c):
    if 0 <= r <= 10 and 0 <= c <= 10:
        return True
    else:
        return False

def solution(dirs):
    visited = set() # 중복 제거
    answer = 0
    r, c = 5, 5 # 시작 위치
    for dir in dirs:
        nr, nc = location(r, c, dir)
        if check_range(nr, nc) == True:
            # 현재 위치 -> 다음 위치 경로
            path = ((r, c), (nr, nc))
            reverse_path = ((nr, nc), (r, c))   # 양방향
            if path not in visited and reverse_path not in visited:
                visited.add(path)
                visited.add(reverse_path)
                answer += 1
            # 현재 위치 갱신
            r, c = nr, nc
            
        else:
            continue
    return answer